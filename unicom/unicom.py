import xlrd
import xlwt
import datetime

## kaihu
## 9 yufen
## 11 riqi
##
## xufei
## 7 yuefen
## 8 riqi
def readExcel(filename):
    book = xlrd.open_workbook(filename)
    sheetName = book.sheet_names()[0]
    sheet = book.sheet_by_name(sheetName)
    row_data=[]
    row_title = []
    row_title.append(list(sheet.row_values(0)))
    for row in range(1,sheet.nrows):
        row_data.append(list(sheet.row_values(row))[1:])
        # print(list(sheet.row_values(row))[1:])
    return row_data

## huode daoqi shijian
def process(data_kh,data_xf):
    data_k = {}
    data_x = {}
    standard_time = datetime.datetime.strptime("2016-09-01", "%Y-%m-%d").date()
    index_month, index_date = 7,8
    index_contact =5
    for data in data_xf:
        data[0]=data[0].lower()
        if data[0] not in data_x.keys():
            data_x[data[0]] = []
        time = datetime.datetime.strptime(data[index_date], "%Y-%m-%d").date()
        time = datetime.date(time.year, time.month, 1)
        dead_time = datetime_offset_by_month(time, int(data[index_month]))
        data_x[data[0]] = [data[index_month], data[index_date], str(dead_time)]

    index_month, index_date = 9, 11
    dead = datetime.datetime.strptime("2016-11-01", "%Y-%m-%d").date()
    for data in data_kh:
        data[1] = data[1].lower()
        if data[1] not in data_k.keys():
            data_k[data[1]] = []
        if data[index_date] == "":
            continue
        time = datetime.datetime.strptime(data[index_date], "%Y-%m-%d").date()
        if time < standard_time:
            time = standard_time
            # if data[1] in data_x.keys():
                # print(data[0],data[1],time,data_x[data[1]][0])
        time = datetime.date(time.year, time.month, 1)
        index_set =0
        if data[1] in data_x.keys():
            index_set = data_x[data[1]][0]
        dead_time = datetime_offset_by_month(time, int(data[index_month]+index_set))
        data_k[data[1]] = [int(data[index_month]+index_set), data[index_date], str(dead_time)]
        string = str(data[1])+"\t"+str(data[0])+"\t"+str(data[index_contact])+"\t"+str(data_k[data[1]][0])+"\t"+str(data_k[data[1]][1])+"\t"+str(data_k[data[1]][2])
        if dead_time.date() <=dead:
            string+= "\t欠费"
        else:
            string+="\t正常"
        print(string)

def datetime_offset_by_month(datetime1, n=1):
    # create a shortcut object for one day
    one_day = datetime.timedelta(days=1)

    # first use div and mod to determine year cycle
    q, r = divmod(datetime1.month + n, 12)

    # create a datetime2
    # to be the last day of the target month
    datetime2 = datetime.datetime(
        datetime1.year + q, r + 1, 1) - one_day

    if datetime1.month != (datetime1 + one_day).month:
        return datetime2

    '''
        if datetime1 day is bigger than last day of
        target month, then, use datetime2
        for example:
        datetime1 = 10.31
        datetime2 = 11.30
    '''

    if datetime1.day >= datetime2.day:
        return datetime2

    '''
     then, here, we just replace datetime2's day
     with the same of datetime1, that's ok.
    '''

    return datetime2.replace(day=datetime1.day)

filename = "data/kh.xlsx"
data_k = readExcel(filename)
fielname = "data/xf.xlsx"
data_x = readExcel(fielname)
process(data_k,data_x)