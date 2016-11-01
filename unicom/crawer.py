from urllib import request as Request
import ssl
import re
import time

def crawe_webpage(id):
    url = "https://10.0.10.66:8080/user/base/view?user_name="+str(id)
    header = ['Host', '10.0.10.66:8080'
        , 'User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
        , 'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        , 'Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        , 'Accept-Encoding', 'gzip, deflate, br'
        , 'Referer', 'https://10.0.10.66:8080/user/base/index'
        , 'Cookie',
            'double_stack_login=bQ0pOyR6IX%252Fu0akbf5QES0glql2rcKzXGlxUSZa4Y%252Fu1zT5qwKNz7okdEQ4Er6aphZzda08PWPHWJNQ%252BBEv3fz3ibZgIcSO85Or%252FRf6IyaoKIXQnagfvnQqt3oyFWu%252BHsekPMfog0PyfeM%252BOsfWLf%252FEvugw85TZPoSgpOT62HE%252BNLuHOcHZ0tZFdOlNizPI%253D; login=bQ0o5ZADI11BgO3HLndd%252Bxt3LbV4WDOtcUYR49j7qmFl9li9lbBbzLPhh9W1LAzvLV%252FsnjEBBd9BefmbMSxy5ub%252FZYNTRIUbGwIsBcm2s8r4%252B39C6AcateWt9KpeEDFys4FUwWuOBPGWy0Q9aUT9kqwccyzdZA51r%252F77JXR4; srun_login=u33315S051052%7C17153X%7C%7C%7C%7C3; PHPSESSID=rm1is7liac96nsjufqhc07soo6; _csrf=4ca575ddf37ef63a0a40b91c1613c1c7af6040a8cf88f237c789a4f6d4c62aada%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22ueVNZD9Dg-Y9VN3gehPp9ETyk6TMtZuG%22%3B%7D'
        , 'DNT', '1'
        , 'Connection', 'keep-alive'
        , 'Upgrade-Insecure-Requests', '1']
    request = Request.Request(url)
    for i in range(header.__len__()-1):
        if i%2 == 0:
            # print(header[i],header[i+1])
            # input()
            request.add_header(header[i],header[i+1])
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    response = Request.urlopen(request,context=gcontext)
    html = response.read()
    html = html.decode('utf-8')
    if html.find("<th>产品ID</th>")<0:
        return ["not unicom"]
    tmp_html = html[html.index("<th>产品ID</th>"):]
    tmp_html = tmp_html[:tmp_html.index("<a class")]
    tmp = tmp_html.split("<td>")
    tmp_html1 = html
    name1 = tmp_html1[tmp_html1.index("/h3>"):]
    name1 = name1[:name1.index("</p>")]
    name1 = name1[name1.index("p>") + 2:]
    tmp_result =[id,name1]
    for t in tmp:
        string  =t.strip()
        if string != "":
            if string.find("td")>0 :
            # tmp_result.append()
                tmp_result.append(re.sub("</td>","",string))
    return tmp_result

def writeIntofile(file,content):
    file_object = open(file, 'w')
    file_object.write(content)
    file_object.close()


def get_all_info():
    ids = ['3SZ160310202', '221601213507', '33316S153556', '3SZ160110228', '3SZ160310232', '33316S151539',
           '3SZ160310133', '33316S151509', '33316S053205', '3SZ160410220', '33316S057431', '33316S053156',
           '33316S053155', '33316S058507', '3SZ160510113', '33316S057432', '3SZ160110102', '33316S054226',
           '33316S151541', '33316S153642', '33316S153575', '33316S051044', '221601214018', '3SZ160410125',
           '3SZ160410122', '33316S054235', '33316S153607', '33316S055320', '3SZ160610224', '33316S051026',
           '33316S051033', '3SZ160610113', '33316S153558', '33316S058501', '33316S057406', '33316S057405',
           '3SZ160110210', '3SZ160610104', '3SZ160210132', '3SZ160410120', '33316S058483', '33316S053179',
           '3SZ160610106', '3SZ160410103', '3SZ160410115', '33316S057433', '33316S053122', '33316S054232',
           '33316S054233', '33316S153599', '33316S154658', '33316S053188', '33316S057423', '33316S154666',
           '33316S156751', '33316S156747', '33316S153604', '33316S055321', '33316S055306', '33316S055249',
           '33316S155734', '33316S153598', '33316S057425', '33316S053162', '33316S051035', '33316S153597',
           '33316S053098', '33316S051048', '33316S058441', '33316S053146', '33316S053142', '33316S151527',
           '33316S053192', '33316S158798', '33316S053177', '33316S153602', '33316S055272', '112016211787',
           '33316B953040', '33316S058487', '33316S056386', '33316S053099', '33316S053088', '33316S154675',
           '33316S057427', '221601213936', '221601214071', '221601214061', '221601213846', '221601213988',
           '221601214058', '221601213890', '221601213535', '221501213342', '221601213783', '221601213573',
           '221601213513', '221601213799', '221601213667', '221601213905', '221601213441', '221601213992',
           '221601213843', '3sz160510132', '3sz160110219', '3sz160110207', '3sz160210129', '3sz160410126',
           '3sz160310210', '3sz160610216', '3sz160210203', '3sz160110225', 'u33315S056382', '3sz160110124',
           '3sz160110105', '3sz160610108', '3sz160410213', '3sz160110110', '3sz160310117', '3sz160210111',
           '3sz160510130', '3sz160410212', '3sz160410226', '3sz160610220', '3sz160310134', '3sz160210105',
           '3sz160310126', '33315S053188', '33315S053187']

    contact = ['18895433437','18811464056','13155140990','13267019830','13243878030','18139285196','13113001734','15602318775','15280085625','none','13612834394','15602968407','15602906779','13612893940','13392352816','15602981765','13267083426','15602904696','13102029562','15602432642','18646238887','15606978994','15940910582','13145833147','13267027780','15602953290','13115319890','13450445619','13243884820','15602900719','15602982612','13267031718','18844124083','18504510154','15602953536','15046104805','18927243458','13145893829','18161125667','13243854009','15602957416','18576728205','13243869715','13145890220','18077889094','18345172961','17190306579','13247804906','13580355133','15602958769','17770705790','15602900405','13613034493','17190418622','15078349820','18200273259','15602981245','18881570561','18502337530','18345053770','18715128267','15635321967','18647093569','15602978216','15602432517','18645559556','18638074458','18345174087','15602983073','15602959091','18646081923','18689597523','18710505109','15145063688','18745149361','13212776107','18671296026','15071059185','15602909307','18646086877','15602958794/13163677803','15602968352/15662174493','15615043786','15602900650','15602904968','13173166235','18710350191','13260190119','18910682371','18811445658','15521040344','13202258874','18565858868','18665916760','18810370525','18811322428','13617675955','18811597504','13043454280','18670013916','15611229520','13243833192','18811476934','13735712952','15898586521','15360429318','13202267028','13267098761','15517002170','15948544399','13145801690','18870744558','15387336793','13145826020','13267055808','15132180965/13612954757','13202298384','15917922696','15532010806','13267088645','15217732305','13652481158','13202258137','13243836858','13145832251','18620987640','13113016006','13751051554','13751060539']
    string,count ="",0
    for i  in range(ids.__len__()):
        id = ids[i]
        result = crawe_webpage(id)
        result.append(contact[i])
        tmp =""
        for res in result:
            tmp += res+"\t"
        string += tmp+"\n"
        print(count,ids.__len__(),id)
        count+=1
    tiemstr = time.strftime("%Y-%m-%d %H %M %S", time.localtime())
    filename = "E:/PythonWorkSpace/unicom/data/"+tiemstr+".txt"
    # filename = re.sub("\\\\","\\")
    # print(filename)
    writeIntofile(filename,string)
# tiemstr = time.strftime("%Y-%m-%d %H %M %S", time.localtime())
# writeIntofile("E:/PythonWorkSpace/unicom/data/"+tiemstr+".txt","ddd")
get_all_info()

# result = crawe_webpage("15S051052")
# print(result)