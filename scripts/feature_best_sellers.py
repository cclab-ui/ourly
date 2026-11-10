from pathlib import Path
p=Path('index.html')
s=p.read_text(encoding='utf-8')
if 'id="best-sellers"' in s:
 print('Best sellers section already exists')
 raise SystemExit(0)
required=['<div class="search-category-bar">','function renderProducts(){','startBannerRotation();','<div class="banner-slide active"','</style>']
if any(token not in s for token in required):
 raise SystemExit('Unexpected HTML layout, aborting safely')
section='''<section class="section best-sellers-section" id="best-sellers" aria-label="OURLY 베스트 상품">
<div class="section-head"><div><div class="eyebrow">OURLY MOST LOVED</div><h2>BEST SELLERS</h2><p class="sub">지금 가장 먼저 만나볼 OURLY 베스트 아이템</p></div><button class="text-link" onclick="setCategory('BEST');go('shop')">VIEW ALL BEST →</button></div>
<div class="product-grid" id="best-products"></div></section>
'''
s=s.replace('<div class="search-category-bar">',section+'<div class="search-category-bar">',1)
css='''.best-sellers-section{background:#f8f3ec;padding-top:45px;padding-bottom:52px}.best-sellers-section .product-grid{margin-top:23px}.best-sellers-section article{min-width:0}.best-sellers-section .product-image{background:#f0e8df}.best-sellers-section .prod-info{padding-top:12px}.best-sellers-section .sub{color:#816e61}
@media(max-width:640px){.best-sellers-section{padding-top:28px;padding-bottom:33px}.best-sellers-section .section-head{align-items:flex-start}.best-sellers-section .product-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.best-sellers-section .prod-info h3{font-size:13px}.best-sellers-section .prod-desc{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}.best-sellers-section .section-head h2{font-size:25px}}
'''
s=s.replace('</style>',css+'</style>',1)
function='''function renderBestSellers(){
 const target=document.getElementById('best-products');if(!target)return;
 const best=products.filter(p=>p.tag==='BEST'&&p.visible!==false).slice(0,4);
 target.innerHTML=best.length?best.map(p=>`<article><div class="product-image" style="background:#f2ebe5;cursor:pointer" onclick="openProductDetail('${p.id}')">${productVisual(p)}<span class="pill">BEST</span><button class="heart" onclick="event.stopPropagation();toggleFavorite('${p.id}')" aria-label="찜하기">${favorites.includes(p.id)?'♥':'♡'}</button></div><div class="prod-info"><span class="kind">${escapeHtml(p.category)}</span><button class="add" onclick="addProduct('${p.id}')" aria-label="장바구니 담기">＋</button><h3>${escapeHtml(p.name)}</h3><p class="prod-desc">${escapeHtml(p.description||'')}</p><span class="price">${money(p.price)}</span><span class="demo-price"> · 테스트용 예시가</span></div></article>`).join(''):'<p class="empty">베스트 상품을 준비하고 있습니다.</p>';
}
'''
s=s.replace('function renderProducts(){',function+'function renderProducts(){renderBestSellers();',1)
# On initial homepage load, first banner emphasizes bestseller discovery while keeping photo and layout
s=s.replace('OUR EVERYDAY STYLE · 01','OUR EVERYDAY STYLE · BEST',1)
s=s.replace('Everyday,<br/><em>with OURLY.</em>','Meet Your<br/><em>Best Picks.</em>',1)
s=s.replace('당신의 일상에 자연스럽게 스며드는 스타일','OURLY에서 사랑받는 베스트 아이템을 먼저 만나보세요',1)
s=s.replace('onclick="go(\'shop\')">EXPLORE OURLY ↗','onclick="go(\'best-sellers\')">SHOP BEST SELLERS ↗',1)
p.write_text(s,encoding='utf-8')
print('Added best sellers feature without changing product data')
