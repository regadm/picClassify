from typing import List
import os


def print_list(biglist: List[str]):
    for listitem in biglist:
        print(listitem)


def printlistinline(printlist):
    for anyitemsinlist in printlist:
        print(str(anyitemsinlist))


def get_filelist(file_dir):
    try:
        filelist = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                filelist.append(os.path.join(root, file))
        return filelist
    except Exception as e:
        print(str(e))


def rename_file(file_dir, listcategory: str) -> None:
    try:
        for root, dirs, files in os.walk(file_dir):
            counter_i = 10001
            for file in files:
                path_and_name = os.path.join(root, file)
                os.rename(path_and_name, os.path.join(root, "{0}{1}{2}".format(listcategory, str(counter_i),
                                                                               os.path.splitext(file)[1])))
                counter_i += 1
    except Exception as e:
        print(str(e))
