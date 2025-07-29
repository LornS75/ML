import json
import os
from dataclasses import dataclass,field

'''
"Items":{
    "sdfsdas":{"name":"apple","type":"fruit","price":"0.2"},
    "fdjsioj":{"name":"banana","type":"fruit","price":"0.4"}
},
"metadate":{"version":"1.0"}
'''

@dataclass
class Fstream:
    name:str
    path:str
    extension:str
    data_file:str = field(init=False)

    @classmethod
    def load_json_files(cls,path) -> dict: 
        """
        Read json files from a directory.
        Args:
            path: the path for the json file to read
        Returns:
            dict: A hash map with the json structure.
        """
        with open(path,"rb") as data_file:
            # 读取全部内容
            cls.data_file=json.load(data_file)
        return cls.data_file
    

    @staticmethod
    def print_json_structure(data_file):
        '''
        print xxxxxx {'name':'a','type':'b','price':c}
        '''
        for id,item in data_file["Items"].items():
            print(id,item)  

      
