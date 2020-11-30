import os
import re
from PIL import Image

# 自己改，原图目录
path = r'D:\Programs\MyResearch\HOG_SVM\INRIAPerson'
pat = r'INRIAPerson'
repl = r'INRIAPerson2'

ctr = 0

file_list = []

# 限制为只处理png，可以改
pattern = 'png'

for root, dirs, files in os.walk(path):
    for f in files:
        searcher = re.search(pattern, f)
        if searcher:
            origin_file = os.path.join(root, f)
            # 替换成存储的目录
            save_path = re.sub(pat, repl, root)
            save_file = save_path + '\\' + f
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            img = Image.open(origin_file)
            img.save(save_file)