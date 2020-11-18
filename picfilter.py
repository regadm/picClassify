import os
import shutil
from typing import List
from PIL import Image

path_test1: str = 'C:\\Users\\2002251505\\Desktop\\xxx\\new'


def get_files1(file_dir) -> List[str]:
    filepathnames: List[str] = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            filepathnames.append(os.path.join(root, file))
    return filepathnames


# 以下函数带有文件夹信息返回，暂时不能用。
"""def get_files2(file_dir) -> List[str]:
    filepathnames: List[str] = []
    for file in os.listdir(file_dir):
        filepathnames.append(os.path.join(file_dir, file))
    return filepathnames"""


def movesiglefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % srcfile)
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.move(srcfile, dstfile)  # 移动文件
        print("move %s -> %s" % (srcfile, dstfile))


def copysiglefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % srcfile)
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstfile))


def filter_files(filepathnames: List[str]):
    for file_path_name in filepathnames:
        fileextendnames: str = os.path.splitext(file_path_name)[1]
        if fileextendnames != '.jpg':
            if fileextendnames == '.gif':
                movesiglefile(file_path_name, path_test1 + 'GIF\\' + os.path.basename(file_path_name))
            else:
                movesiglefile(file_path_name, path_test1 + 'Other\\' + os.path.basename(file_path_name))
        elif get_file_size(file_path_name) <= 50.0:
            movesiglefile(file_path_name, path_test1 + 'Small\\' + os.path.basename(file_path_name))
        elif get_file_size(file_path_name) >= 10000.0:
            movesiglefile(file_path_name, path_test1 + 'Big\\' + os.path.basename(file_path_name))
        elif get_image_scale(file_path_name) > 1.777:
            movesiglefile(file_path_name, path_test1 + 'WrongProportion\\' + os.path.basename(file_path_name))
        else:
            pass

    return


def get_file_size(file_path_name: str) -> float:
    fsize = os.path.getsize(file_path_name)
    fsize = fsize / float(1024)
    return fsize


def get_image_scale(file_path_name: str) -> float:
    img = Image.open(file_path_name)
    img_size = img.size  # 图片的长和宽
    max_size = max(img_size)  # 图片的长边
    min_size = min(img_size)  # 图片的短边
    img.close()
    return round(max_size / min_size, 3)


def print_list(biglist: List[str]):
    for listitem in biglist:
        print(listitem)


filter_files(get_files1(path_test1))
