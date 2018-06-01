from bs4 import BeautifulSoup
import re
#123
html = """
<table class="tablea">
	<tr>
		<td bgcolor="#09589F" height="27" width="114" align="center">
		<font color="#FFFFFF"><b>三字代码</b></font></td>
		<td bgcolor="#09589F" height="27" width="400" align="center">
		<font color="#FFFFFF"><b>机场名称</b></font></td>
		<td bgcolor="#09589F" height="27" width="141" align="center">
		<font color="#FFFFFF"><b>所属国家　</b></font></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ACR</td>
		<td align="center"><a target=_blank href=acr.html>Araracuara Airport</a> 阿拉拉库拉机场</td>
		<td align="center"><a href=index2.asp?gj=哥伦比亚>哥伦比亚</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABK</td>
		<td align="center"><a target=_blank href=abk.html>Kabri Dar Airport</a> 卡布里达机场</td>
		<td align="center"><a href=index2.asp?gj=埃塞俄比亚>埃塞俄比亚</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AHJ</td>
		<td align="center"><a target=_blank href=jcn.asp?szm=AHJ>Hongyuan Airport</a> 红原机场</td>
		<td align="center"><a href=index2.asp?gj=中国>中国</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AAH</td>
		<td align="center"><a target=_blank href=aah.html>Merzbrück Airport</a> 亚琛机场</td>
		<td align="center"><a href=index2.asp?gj=德国>德国</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AAL</td>
		<td align="center"><a target=_blank href=aal.html>Aalborg Airport</a> 奥尔堡机场<span class=hg>海关</span></td>
		<td align="center"><a href=index2.asp?gj=丹麦>丹麦</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AAR</td>
		<td align="center"><a target=_blank href=aar.html>Aarhus Airport</a> 提尔斯特卢普机场<span class=hg>海关</span></td>
		<td align="center"><a href=index2.asp?gj=丹麦>丹麦</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABD</td>
		<td align="center"><a target=_blank href=abd.html>Abadan International Airport</a> 阿巴丹机场<span class=hg>海关</span></td>
		<td align="center"><a href=index2.asp?gj=伊朗>伊朗</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABF</td>
		<td align="center"><a target=_blank href=abf.html>Abaiang Atoll Airport</a> 阿拜昂环礁机场</td>
		<td align="center"><a href=index2.asp?gj=基里巴斯>基里巴斯</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABA</td>
		<td align="center"><a target=_blank href=aba.html>Abakan International Airport</a> 阿巴坎机场<span class=hg>海关</span></td>
		<td align="center"><a href=index2.asp?gj=俄罗斯>俄罗斯</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABW</td>
		<td align="center"><a target=_blank href=abw.html>Abau Airport</a> 阿包机场</td>
		<td align="center"><a href=index2.asp?gj=巴布亚新几内亚>巴布亚新几内亚</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AEH</td>
		<td align="center"><a target=_blank href=aeh.html>Abeche Airport</a> 阿贝歇机场</td>
		<td align="center"><a href=index2.asp?gj=乍得>乍得</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AEA</td>
		<td align="center"><a target=_blank href=aea.html>Abemama Atoll Airport</a> 阿贝马马环礁机场</td>
		<td align="center"><a href=index2.asp?gj=基里巴斯>基里巴斯</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABZ</td>
		<td align="center"><a target=_blank href=abz.html>Aberdeen Airport</a> 阿伯丁机场<span class=hg>海关</span></td>
		<td align="center"><a href=index2.asp?gj=英国>英国</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABR</td>
		<td align="center"><a target=_blank href=abr.html>Aberdeen Regional Airport</a> 阿伯丁地方机场</td>
		<td align="center"><a href=index2.asp?gj=美国>美国</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">APG</td>
		<td align="center"><a target=_blank href=apg.html>Phillips Army Air Field Airport</a> </td>
		<td align="center"><a href=index2.asp?gj=美国>美国</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABJ</td>
		<td align="center"><a target=_blank href=abj.html>Port Bouet Airport</a> 费里克斯霍佛特博伊戈尼机场<span class=hg>海关</span></td>
		<td align="center"><a href=index2.asp?gj=科特迪瓦>科特迪瓦</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABI</td>
		<td align="center"><a target=_blank href=abi.html>Abilene Regional Airport</a> 阿比林地方机场</td>
		<td align="center"><a href=index2.asp?gj=美国>美国</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABG</td>
		<td align="center"><a target=_blank href=abg.html>Abingdon Airport</a> 阿宾登机场</td>
		<td align="center"><a href=index2.asp?gj=澳大利亚>澳大利亚</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">ABO</td>
		<td align="center"><a target=_blank href=abo.html>Aboisso Airport</a> 阿博伊索机场</td>
		<td align="center"><a href=index2.asp?gj=科特迪瓦>科特迪瓦</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AOD</td>
		<td align="center"><a target=_blank href=aod.html>Abou-Dea Airport</a> 阿布 - 德亚机场</td>
		<td align="center"><a href=index2.asp?gj=乍得>乍得</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AUH</td>
		<td align="center"><a target=_blank href=auh.html>Abu Dhabi International Airport</a> 阿布扎比国际机场<span class=hg>海关</span></td>
		<td align="center"><a href=index2.asp?gj=阿联酋>阿联酋</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AYM</td>
		<td align="center"><a target=_blank href=aym.html>Yas Island Seaplane Base</a> 亚斯岛水上飞机基地</td>
		<td align="center"><a href=index2.asp?gj=阿联酋>阿联酋</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AZI</td>
		<td align="center"><a target=_blank href=azi.html>Al Bateen Executive Airport</a> 艾尔巴滕行政机场</td>
		<td align="center"><a href=index2.asp?gj=阿联酋>阿联酋</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AEU</td>
		<td align="center"><a target=_blank href=aeu.html>Abu Musa Iran Airport</a> 阿布穆萨岛机场</td>
		<td align="center"><a href=index2.asp?gj=伊朗>伊朗</a></td>
	</tr>

	<tr height="25" onmouseover="bgColor='#F0FFF9';" onmouseout="this.bgColor='#FFFFFF'">
		<td align="center">AUE</td>
		<td align="center"><a target=_blank href=aue.html>Abu Rudeis Airport</a> 阿布努德斯机场</td>
		<td align="center"><a href=index2.asp?gj=埃及>埃及</a></td>
	</tr>
</table>
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
                airport.append(c1.contents[0].string)
                airport.append(c1.contents[1].string.strip())
            else:
                #print(c1.string)
                airport.append(c1.string)
    airports.append(airport)
print(airports)