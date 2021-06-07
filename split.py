def split(text,splitter):
    splited = text.split(splitter)
    return splited

splitter = '.'
text = 'commercial.naver.com'
y = split(text, splitter)
print(y[-2])
