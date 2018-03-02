import pyperclip,re

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # 아이디
    @                      # @ 골뱅이
    [a-zA-Z0-9.-]+         # 네이버,네이트 같은 도메인 이름
    (\.[a-zA-Z]{2,4}){1,2} # .com/.co.kr/,.net 기타 등등
    )''', re.VERBOSE)

#pyperclip.copy('hihihi')
cb_text = str(pyperclip.paste())
#print(cb_text)
cb_list = cb_text.split(' ')
text = ''
for i in cb_list:
    text = i + '\n'

matches = []
for i in emailRegex.findall(text):
    matches.append(i[0])

if len(matches) > 0:
    print(matches)
else:
    print('no email')
    print(pyperclip.paste())