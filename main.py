import requests
from bs4 import BeautifulSoup
import cx_Oracle
import time
import traceback
import sys
import io

def get_html_text(keyword):
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Encoding":"gzip, deflate",
               "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
               "Connection":"keep-alive",
               "Host":"www.zou114.com",
               "Upgrade-Insecure-Request":"1",
               "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"}
    #keyword = 'zm=a&page=2'
    get_html = 0
    while(get_html == 0):
        try:
            res = requests.get('http://www.zou114.com/sanzidaima/index.asp', params=keyword, headers = headers, timeout=3)
            get_html = 1
        except:
            print("----------------------------------------------请求超时:"+keyword)

    res.encoding = 'gb2312'
    #print(res.text)
    return res.text

def get_airpot_list(html_text):
    soup = BeautifulSoup(html_text,'lxml')
    #对soup.p的子节点进行循环输出
    airports = []
    for child in soup.find_all(height="25"):
        airport = []
        #print(child)
        for c1 in child.children:
            if str(type(c1)) == "<class 'bs4.element.Tag'>":
                if c1.string is None:
                    #print(c1.contents[0].string)
                    #print(str(c1.contents[1].string))
                    #print(str(c1.contents[0].string.encode('unicode_escape')).find("u30fb"))
                    airport.append(c1.contents[0].string.replace("�C","-"))
                    airport.append(c1.contents[1].string.strip().replace("・","·").replace("�",""))
                else:
                    #print(c1.string)
                    airport.append(c1.string)
        airports.append(airport)
    #print(airports)
    return airports

def clear_tmp_data():
    conn = cx_Oracle.connect('la_dw/oracle123@ladw_41')
    c = conn.cursor()

    print("清空临时表数据")
    r = c.execute("truncate table tmp_webget_airport")

    c.close()
    conn.close()

def insert_data(airports):
    conn = cx_Oracle.connect('la_dw/oracle123@ladw_41')
    c = conn.cursor()

    r = c.execute("SELECT COUNT(*) FROM tmp_webget_airport")
    print("插入前",c.fetchone())

    try:
        c.executemany('insert into tmp_webget_airport(iata,airport_en,airport_cn, country) values(:iata,:airport_en,:airport_cn, :country)',airports);
        conn.commit()
    except:
        traceback.print_exc()
        return -1

    r = c.execute("SELECT COUNT(*) FROM tmp_webget_airport")
    print("插入后",c.fetchone())

    c.close()
    conn.close()

par_zms = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#par_zms = ['a']
start_parm = ''
fail_page = []
#清空临时表数据
clear_tmp_data()
#开始抓取数据
for par_zm in par_zms:
    for i in range(1,100):
        keyword = 'zm='+par_zm+'&page='+str(i)
        if keyword > start_parm :
            print("开始抓取：",keyword,"------")
            page_text = get_html_text(keyword)
            airports = get_airpot_list(page_text)
            #print(airports)
            if airports.__len__() == 0 :
                print("par_zm ",par_zm," finish: ",keyword)
                break
            r = insert_data(airports)
            if r == -1:
                fail_page.append(keyword)
                print("------------------------------------------------抓取失败：",keyword)
            else:
                print("抓取成功：",keyword)
            time.sleep(10)

print("抓取失败结果：",fail_page)
