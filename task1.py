import os
import re
import sys
import argparse
from create_file import create_file

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', help='insert path floder')
parser.add_argument('-cls_l', '--class_list', nargs='+', type=str, help='inser list class')

args = parser.parse_args()


path = args.path
list_cls = args.class_list


# создание тестовых файлов
# os.mkdir(path)
# for i in list_cls:
#     create_file(i, 5, path)

os.mkdir('sort_data')
for i in list_cls:
    os.mkdir(f"sort_data//{i}")
    
list_dir = os.listdir(path)   
patern = r'\d+'
repl = r''

for i in list_dir:
    dir = re.sub(patern, repl, i.split('.')[0]).strip()
    if dir in list_cls:
        os.replace(f"{path}//{i}", f"sort_data//{dir}//{i}")