from os import walk

def subfolders_count(path):
    count = 0
    for root, dirs, files in walk(path):
        count += len(dirs)

    return count

def files_count(path):
    count = 0
    for root, dirs, files in walk(path):
        count += len(files)

    return count
