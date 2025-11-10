'''
    zigzag 크롤링
'''
# category, brand, product, price

import time
import pymysql
# import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# HTML 요청 및 파싱
url = 'https://zigzag.kr'
options_ = Options()
options_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options_)
driver.get(url)
time.sleep(0.5)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# 상품 정보 가져오기
result = soup.select(".zds4_798wu00.medium.medium.padding-on.product-card-metadata.css-1jciu1s")
products = []

# 카테고리 자동 분류 함수
def get_category(name):
    name = product.lower()
    if any(k in name for k in ["후드", "맨투맨", "니트", "티셔츠", "셔츠", "자켓", "코트", "탑", "가디건"]):
        return "상의"
    elif any(k in name for k in ["팬츠", "바지", "슬랙스", "청바지", "스커트", "치마", "트레이닝", "조거"]):
        return "하의"
    elif any(k in name for k in ["운동화", "스니커즈", "샌들", "구두", "부츠", "슬리퍼"]):
        return "신발"
    elif any(k in name for k in ["가방", "모자", "벨트", "시계", "목걸이", "키링", "악세서리", "귀걸이"]):
        return "패션잡화"
    else:
        return "기타"

# 데이터 수집
for i in result:
    brand = i.select_one(".zds4_1kdomr8").text.strip()
    product = i.select_one(".zds4_1kdomrc.zds4_1kdomra").text.strip()
    price = i.select_one(".zds4_s96ru86.zds4_s96ru81n.zds4_1jsf80i3.zds4_1jsf80i5").text.strip()
    category = get_category(product)

    # products.append({
    #     "category": category,
    #     "brand": brand.text if brand else "",
    #     "product": product_name,
    #     "price": price.text if price else "",
    # })

    product_info = [category, brand, product, price]
    products.append(product_info)

# json에 저장
# with open("/Users/admin/StudyClass/oz7class/task/admin-project/crawlling/zigzag_data.json", "w", encoding="utf-8") as f:
#     json.dump(products, f, ensure_ascii=False, indent=2)

driver.quit()

# db에 저장
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="20241013",
    db="admin",
    charset="utf8mb4"
)

def execute_query(conn, query, args=None):
    with conn.cursor() as cursor:
        cursor.execute(query, args or ()) # select * from kream3
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            conn.commit()

for i in products:
    execute_query(connection,"INSERT INTO `admin` (category, brand, product, price) VALUES (%s, %s, %s, %s)",(i[0],i[1],i[2],i[3]))
