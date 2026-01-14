from dataclasses import dataclass,field
from shopping_cart.random_number_utils import RandomUtils

@dataclass(frozen=True,order=True,slots=True)  
#自动将Item类转为数据类，自动生成特殊方法
#frozen=true    使实例不可变，防止属性被修改
#order=true     自动生成比较方法，基于字段定义顺序
#slots=true     使用_slots_属性减少内存访问，提高访问速度
class Item:
    """
    name、type、_price、id
    """
    name:str
    type:str
    #下划线表示私有变量
    _price:float=0.0
    #default_factory延迟生成唯一ID，避免所有实例共享相同值
    id:str=field(default_factory=RandomUtils.generate_random_id)

    @property
    #将方法转为只读属性
    def price(self):
        return round(self._price,2)
    
    @property
    def search_string(self):
        return f"{self.name} {self.type}"
    

