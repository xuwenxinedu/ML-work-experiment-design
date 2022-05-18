import pandas as pd
import numpy as np


class Util:
    def __init__(self, data, label_name) -> None:
        self.data = data
        self.label_name = label_name
    
    staticmethod
    def infor(data) -> float:
        a = pd.value_counts(data) / len(data)
        return sum(np.log2(a) * a * (-1))
    
    def col_infor(self, col) -> float:
        col_dict = {}
        for i, item in enumerate(self.data[col]):
            if item in col_dict.keys():
                col_dict[item].append(self.data[self.label_name][i])
            else:
                col_dict[item] = [self.data[self.label_name][i]]
        ans = 0.0
        for key in col_dict.keys():
            ans += len(col_dict[key]) / len(self.data[col]) * Util.infor(col_dict[key])
        return ans
    
    def max_info(self) -> str:
        all_info = Util.infor(self.data[self.label_name])
        maxn = 0
        max_col = ''
        for col in self.data.columns:
            if col == self.label_name:
                continue
            col_info = self.col_infor(col)
            sub = all_info - col_info
            max_col = max_col if sub < maxn else col
            maxn = maxn if sub < maxn else sub
        return max_col

