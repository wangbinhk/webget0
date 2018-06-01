#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import chardet

#123
html = """
<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AJY</td>
		<td align="center"><a target=_blank href=ajy.html>Mano Dayak International Airport</a> 阿加德兹机场</td>
		<td align="center"><a href=index2.asp?gj=尼日尔>尼日尔</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AGA</td>
		<td align="center"><a target=_blank href=aga.html>Agadir�CAl Massira Airport</a> 阿尔马希拉机场<span class=hg>海关</span></td>
		<td align="center"><a href=index2.asp?gj=摩洛哥>摩洛哥</a></td>
	</tr>

"""
soup = BeautifulSoup(html,'lxml')
#对soup.p的子节点进行循环输出
airports = []
for child in soup.find_all(height="25"):
    airport = []
    for c1 in child.children:
        if str(type(c1)) == "<class 'bs4.element.Tag'>":
            if c1.string is None:
                #print(c1.contents[0].string)
                # #print(c1.contents[1].string.strip())
                print(c1.contents[0].string)
                #print(c1.contents[0].string.encode('unicode_escape'))
                #print(str(c1.contents[0].string.encode('unicode_escape')).replace(r'\\ufffd',"-"))
                print(c1.contents[0].string.replace("�C","-"))
                airport.append(c1.contents[0].string.replace("�C","-"))
                #airport.append(c1.contents[0].string)
                airport.append(c1.contents[1].string.strip())
            else:
                #print(c1.string)
                airport.append(c1.string)
    airports.append(airport)
print(airports)
