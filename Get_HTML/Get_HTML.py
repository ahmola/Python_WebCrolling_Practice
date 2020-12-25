from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = input("url: ")
t = input("대문자로 생성할 파일 이름 : ") 
html = urlopen(s)
bsObject = BeautifulSoup(html, 'html.parser')

f = open('Get_Text.txt', 'w+', encoding='utf-8')    #먼저 복사할 파일을 선언
sys.stdout = f
print(bsObject)
f.close()


f1 = open('Get_Text.txt', 'r', encoding='utf-8') #읽기 모드로 다시 열음
f2 = open(t, 'w+', encoding='utf-8') #대문자로 복사할 파일을 선언

text_str = f1.read()
upper_str = text_str.upper()
f2.write(upper_str)


f1.close()
f2.close()
