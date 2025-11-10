// 값 받아오기
const input = document.getElementById("search")
const button = document.getElementById("button")
const table = document.getElementById("product_data_Table")
const select = document.getElementById("inlineFormSelectPref")

// 제품 데이터
const product_data = [
    { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
    { category: "상의", brand: 'adidas', product: '아디다스 박스로고 후드티', price: '390,000' },
    { category: "하의", brand: 'New Balance', product: '뉴발란스 트랙 팬츠', price: '188,000' },
    { category: "신발", brand: 'Jordan Brand', product: '에어조던 1', price: '137,000' },
    { category: "패션잡화", brand: 'Uniqlo', product: '빵빵이 가방', price: '29,000' },
    { category: "신발", brand: 'Birkenstock', product: '여름 샌들', price: '390,000' },
    { category: "하의", brand: 'Salomon', product: '숏 팬츠', price: '188,000' },
    { category: "신발", brand: 'HumanMade', product: '운동화', price: '137,000' },
    { category: "패션잡화", brand: 'PUMA', product: '크로스백', price: '29,000' },
    { category: "상의", brand: 'Supreme', product: '슈프림 라운드티', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 라운드티', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 2', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '마시멜로 키링', price: '29,000' },
    { category: "상의", brand: 'Supreme', product: '로고 후드티', price: '390,000' },
    { category: "하의", brand: 'DIESEL', product: '디젤 팬츠', price: '188,000' },
    { category: "신발", brand: 'Nike', product: '에어포스 3', price: '137,000' },
    { category: "패션잡화", brand: 'Music&Goods', product: '머리띠', price: '29,000' },
    // ...
];

// 제품 테이블에 데이터 추가
const product_data_Table = document.getElementById('product_data_Table');

// 초기 데이터 로딩
displayTable(product_data)
////////////////////////////////////////////////

// 테이블 표시 함수
function displayTable(data) {
    product_data_Table.innerHTML = "";
    data.forEach((item) => {
        const row = product_data_Table.insertRow()
        row.insertCell(0).innerHTML = item.category
        row.insertCell(1).innerHTML = item.brand
        row.insertCell(2).innerHTML = item.product
        row.insertCell(3).innerHTML = item.price
    })
}

// 조회 버튼 클릭 이벤트
button.addEventListener("click", function(e){
    e.preventDefault()
    const keyword = input.value.trim();
    const filtered = product_data.filter(item =>
        item.product.includes(keyword)
    );
    displayTable(filtered)
    input.value = ""
})

// 셀렉트시 셀렉트된 정보만 표시하기
select.addEventListener("change", function(e){
    e.preventDefault()
    const filtered = product_data.filter(item =>
        item.category.includes(select.value)
    )
    displayTable(filtered)
})