s = input("path: ") #경로를 받음

src_file = open(s, 'r', encoding='utf-8')    # 경로의 파일을 열음

a = input("입력 단어: ")    # 단어를 입력받음
count = 0

text = src_file.read() #파일을 읽음

#파일을 읽어서 있다면 해당 단어를 셈
if a in text :
    data = text.split()
    for i in data:
        if a in i :
            count += 1
else :
    count = 0


print("결과 : ", count)