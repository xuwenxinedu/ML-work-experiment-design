from util import *
import pandas as pd
import numpy as np
import easydict

config = easydict.EasyDict({
    "fileName": "disease.csv"
})

class Tree:
    def __init__(self, label_name) -> None:
        self.label = label_name
    
    def create_tree(self, data):
        if self.all_same(data):
            return data[self.label][0]
        

    def all_same(self, data) ->bool:
        s = set()
        for item in data:
            s.add(item)
            if len(s) > 1:
                return False
        return True

def main():
    df = pd.read_csv(config.fileName)
    df = df.drop("order", axis = 1)
    t = Util(df, "disease")
    one = t.max_info()
    print(one)

if __name__ == "__main__":
    main()