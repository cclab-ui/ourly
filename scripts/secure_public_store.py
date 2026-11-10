from pathlib import Path
import re
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'function openAdmin(' not in s:
    print('Already secured or unexpected source; no changes')
    raise SystemExit(0)
if s.count('function openAdmin(')!=1 or s.count('function showBanner(')!=1:
    raise SystemExit('Unexpected storefront version; aborting without changes')
s=re.sub(r"let adminEditingId='';\s*function openAdmin\(.*?(?=function showBanner\()",'',s,flags=re.S)
s=re.sub(r'<button[^>]*onclick="openAdmin\(\)"[^>]*>DEMO PRODUCT MANAGER ↗</button>','',s)
s=re.sub(r'<button[^>]*onclick="openAdmin\(\'\$\{p\.id\}\'\)"[^>]*>.*?</button>','',s)
s=s.replace("products=read('ourly_photo_products_v5',initialProducts)","products=initialProducts")
s=s.replace('개별 상품 판매형 데모입니다. 상품명·카테고리·가격·사진은 상품 관리에서 변경할 수 있습니다. 실제 결제는 연결되지 않았습니다.','OURLY 상품 컬렉션입니다. 표시 가격은 예시이며 실제 결제는 연결되지 않았습니다.')
if any(term in s for term in ['openAdmin(', 'openProductList(', 'saveCuratedProduct(', 'DEMO PRODUCT MANAGER']):
    raise SystemExit('Admin links still present; abort')
p.write_text(s,encoding='utf-8')
print('Secured public storefront; product images retained')
