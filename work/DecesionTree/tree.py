from util import *
import pandas as pd
import easydict

config = easydict.EasyDict({
    "fileName": "disease_str.csv",
    "label": "disease"
})

class Tree:
    def __init__(self, label_name) -> None:
        self.label = label_name
    
    def create_tree(self, data):
        if self.all_same(data[self.label]):
            return data[self.label][0]
        else:
            t = Util(data, self.label)
            # root是用来分类的字段
            root = t.max_info()
            subtree_root = self.get_dict_by_root(data, root)
            for roots in subtree_root.keys():
                # 将index重置为从0开始
                subtree_root[roots] = subtree_root[roots].drop(root, axis = 1)
                subtree_root[roots] = subtree_root[roots].reset_index(drop = True)
                # 然后建子树
                temp = subtree_root[roots]
                tree = Tree(self.label)
                subtree_root[roots] = tree.create_tree(temp)
            return subtree_root
                

    def get_dict_by_root(self, data, root) -> dict:
        ans = {}
        for i, item in enumerate(data[root]):
            key = str(root + '_' + str(item))
            if key not in ans.keys():
                ans[key] = pd.DataFrame(columns = data.columns)
                ans[key] = ans[key].append(data.loc[i])
            else:
                ans[key] = ans[key].append(data.loc[i])
        return ans


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

    tree = Tree(config.label)
    t = tree.create_tree(df)
    print(t)
    

if __name__ == "__main__":
    main()