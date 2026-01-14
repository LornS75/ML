import sys
import os

# 获取 shopping_cart 模块所在的父目录
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# 现在可以正常导入模块
from shopping_cart.item import Item

def test_item_price()->None:
    item = Item("Car","vehicle",1200.02)
    assert item.price >=0.0 or item.price == 1200.02

def test_item_name()->None:
    item = Item("a","b",16.00)
    assert len(item.name) > 0