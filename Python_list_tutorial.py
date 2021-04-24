# a = ['현금','현금과 예금','보통예금','외상매충금','외상매입금','미수금']
# b = ['현금', '예금']

# for i in a:
#     if all(j in i for j in b):
#         print(i)
# print()

# for i in a:
#     if not all(j in i for j in b):
#         print(i)
# print()

# for i in a:
#     if any(j in i for j in b):
#         print(i)
# print()

# for i in a:
#     if not any(j in i for j in b):
#         print(i)

# a = 'Hello World'
# b = [1,2,[5,['4째',9,0],6,7],'4번째']

# print(b[2][1])

a = ['동', '호', '동호명', '가구수', '계약\n종별', '요금적용\n전력', '사용량', '기본요금', '전력량\n요금',
       '기후환경\n요금', '연료비조정\n요금', '필수사용\n공제', '할인\n구분', '복지할인', '요금개편\n차액',
       '절전할인', '자동이체\n/인터넷', '단수', '전기요금', '부가세', '전력\n기금', '전기\n바우처', '정산',
       '출산가구소급', '당월소계', 'TV수신료', '청구금액']
b = ['동','호','공제','할인']      
c = []
for i in a:
    if any(j in i for j in b):
        c.append(i)
print(c)

