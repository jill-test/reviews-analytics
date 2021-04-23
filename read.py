data = []
n = 0
str_num = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        str_num += len(data[n])
        n += 1
num = len(data)
avg_num = str_num / num 
print('檔案讀取完了，留言總共有', num, '筆')
print('所有留言總長度：', str_num)
print('平均留言長度:', avg_num)

#篩選小於100個字的留言
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])
