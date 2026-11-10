OURLY 홈페이지 GitHub Pages 배포 방법

1. GitHub에서 새 Public 저장소를 만듭니다. 예: ourly-shop
2. 이 ZIP 파일의 압축을 풉니다.
3. 저장소의 Add file > Upload files를 선택하고 index.html 및 .nojekyll 파일을 저장소 최상위 폴더에 업로드한 뒤 Commit changes를 누릅니다.
4. 저장소 Settings > Pages > Build and deployment에서 Source: Deploy from a branch, Branch: main, Folder: /(root)를 선택하고 Save합니다.
5. 생성되는 기본 웹주소는 https://깃허브사용자명.github.io/ourly-shop/ 형식입니다.
   저장소를 '깃허브사용자명.github.io'로 만들었다면 https://깃허브사용자명.github.io/ 입니다.

참고
- index.html에는 현재 OURLY 홈페이지 디자인, 상품 정보, 사진이 포함되어 있습니다. 이미지 ZIP을 따로 업로드할 필요는 없습니다.
- 이 버전은 프런트엔드 데모입니다. 브라우저에 저장하는 상품/장바구니 자료는 방문자끼리 공유되지 않습니다.
- 실제 회원가입, 결제, 중앙 상품관리, 주문 처리 기능은 별도 백엔드와 결제 연동이 필요합니다.
- 개인 도메인(예: ourly.kr)은 별도 구매 후 DNS와 GitHub Pages에서 연결해야 합니다.
