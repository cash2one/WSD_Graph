import codecs
import os
import Dir

def read(filename,encoding="utf-8"):
    file = codecs.open(filename,encoding=encoding)
    content = file.read()
    file.close()
    return content

def write(filename,content,encoding="utf-8"):
    check_filename(filename)
    file = codecs.open(filename=filename,mode='w',encoding=encoding)
    file.write(content)
    file.close()

def nothing():
    return

def get_filelist(dir, fileList,filter=nothing):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            filter()
            newDir=os.path.join(dir,s)
            get_filelist(newDir, fileList)
    return fileList

def check_filename(filename):
    if not os.path.exists(filename):
        path = filename[:filename.rfind("\\")]
        if not os.path.exists(path):
            os.makedirs(path)
