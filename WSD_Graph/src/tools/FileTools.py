import codecs
import os
import Dir
import re

def read(filename,encoding="utf-8"):
    file = codecs.open(filename,encoding=encoding)
    content = file.read()
    file.close()
    return content

def read_lines(filename,encoding ="utf-8"):
    file = codecs.open(filename, encoding=encoding)
    lines = file.readlines()
    content=[]
    for line in lines:
        line = line.strip()
        line = line.replace("\r\n","")
        content.append(line)
    file.close()
    return content

def write(filename,content,encoding="utf-8"):
    check_filename(filename)
    file = codecs.open(filename=filename,mode='w',encoding=encoding)
    file.write(content)
    file.close()

def write_list(filename,list_content,encoding = "utf-8"):
    content  =""
    for line in list_content:
        content+= line+"\n"
    write(filename,content,encoding)


def write_dict(filename,dict_content,encoding = "utf-8"):
    content  =""
    for key in dict_content.keys():
        content+= key+"\t"+str(dict_content[key])+"\n"
    write(filename,content,encoding)


def nothing(s):
    return


def seperate_sentence(essay):
    result = {}
    i = 0
    regex = "。|\?|\!|？|！"
    tmp = re.split(regex, essay)
    for sentence in tmp:
        result[i] = sentence
        i += 1
    return result

def get_filelist(dir, fileList,filter=nothing):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            if filter(s):
                continue
            newDir=os.path.join(dir,s)
            get_filelist(newDir, fileList)
    return fileList

def check_filename(filename):
    if not os.path.exists(filename):

        path = filename[:filename.rfind("/")]
        if not os.path.exists(path):
            print(path)
            os.makedirs(path)

def read_dir_content(file_dir,filter = nothing):
    filelist=[]
    get_filelist(file_dir,filelist,filter)
    # print(filelist)
    result =[]
    for file in filelist:
        result.append(read(file))
    return result

def read_dir_lines(file_dir,filter = nothing):
    filelist=[]
    get_filelist(file_dir,filelist,filter)
    # print(filelist)
    result =[]
    for file in filelist:
        result.append(read_lines(file))
    return result

def get_name(filepath):
    start = filepath.rfind("\\")
    end = filepath.rfind(".")
    name = filepath[start+1:end]
    return name

def replace_nothing(s):
    return s

def read_dir_lines_dict(file_dir,filter = nothing,replace_fun = replace_nothing):
    filelist = []
    get_filelist(file_dir,filelist,filter)
    result = {}
    for file in filelist:
        name = get_name(file)
        name = replace_fun(name)
        if name not in result.keys():
            result[name]=""
        data = read_lines(file)
        result[name] = data
    return result

