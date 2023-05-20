from pathlib import Path
from urllib.request import urlretrieve

base_url = "https://raw.githubusercontent.com/codingalzi/pybook/master/jupyter-book/data/"

data_path = Path() / "data"
data_path.mkdir(parents=True, exist_ok=True)

def shopping(shop_file):
    shop_dict = {}  # 생성할 사전 객체

    # data_path 변수 정의 확인
    if 'data_path' not in locals():
        data_path = Path() / "data"

    with open(data_path / shop_file, mode='r', encoding='utf-8') as f:
        for line in f:
            price_of_goods = line.strip().split()
            if price_of_goods != []:
                goods, price = price_of_goods
            if price != shop_file[4]:
                shop_dict[goods] = int(price.rstrip('원'))

    return shop_dict


    return shop_dict

def item_price(shop_file, item):
    return shopping(shop_file)[item]
