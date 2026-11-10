from pathlib import Path
import json, re, base64, mimetypes
root=Path(".")
page=root/"index.html"
s=page.read_text(encoding="utf-8")
if "const initialProducts=" not in s:
    raise SystemExit("Source format changed; stopping")
start=s.index("const initialProducts=")+len("const initialProducts=")
products,end=json.JSONDecoder().raw_decode(s[start:])
dest=root/"assets"/"products"; dest.mkdir(parents=True,exist_ok=True)
for p in products:
    data=p.get("image","")
    if data.startswith("data:image/"):
        head, encoded=data.split(",",1)
        ext=".jpg" if ("jpeg" in head or "jpg" in head) else ".png" if "png" in head else ".webp"
        fp=dest/(p["id"]+ext)
        fp.write_bytes(base64.b64decode(encoded))
        p["image"]=str(fp).replace("\\","/")
    p.setdefault("visible",True)
(root/"products.json").write_text(json.dumps(products,ensure_ascii=False,indent=2),encoding="utf-8")
replacement="const initialProducts="+json.dumps(products,ensure_ascii=False,separators=(",",":"))
s=s[:start]+replacement+s[start+end:]
# Public storefront always reads the published catalog; failed loads keep original defaults
sync_js="""\nasync function syncPublishedCatalog(){try{const response=await fetch('./products.json?ts='+Date.now(),{cache:'no-store'});if(!response.ok)throw new Error('Catalog unavailable');const data=await response.json();if(!Array.isArray(data))throw new Error('Invalid catalog');products=data.filter(p=>p.visible!==false);renderProducts();updateCount()}catch(err){console.warn('Published catalog fallback',err)}}\n"""
if "async function syncPublishedCatalog()" not in s:
    needle="startBannerRotation();\nrenderProducts();updateCount();"
    if needle not in s: raise SystemExit("Startup hook not found")
    s=s.replace(needle, sync_js+"\n"+needle+"\nsyncPublishedCatalog();",1)
page.write_text(s,encoding="utf-8")
print(f"Prepared {len(products)} products, images and storefront sync")