from RunAll import Runall

Runall().run()


'''
def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files


import os


def traverse(f):
    fs = os.listdir(f)
    print(fs[-1])
    for f1 in fs:
        tmp_path = os.path.join(f,f1)
        if not os.path.isdir(tmp_path):
            print('文件: %s'%tmp_path)
        else:
            print('文件夹：%s'%tmp_path)
            traverse(tmp_path)

path = 'C:/Users/Administrator/PycharmProjects/untitled10/result'



traverse(path)
'''