import time #計數時間
import progressbar #載入第三方套件

data = []
count = 0
bar = progressbar.ProgressBar(man_value = 1000000) #第三方套件的語言
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print('檔案讀取完了，總共有' , len(data), '筆資料')

#print(data[0])

# 找出每一個字出現的次數

#文字記數
start_time = time.time() #計算這個程式要執行多久
wc = {} #word_count
for d in data:
	words = d.split() #用空格分割每個字
	for word in words:
		if word in wc: #檢查這個字有沒有出現在字典裡
			wc[word] += 1
		else:
			wc[word] = 1 #新增key進字典

for word in wc: #把字典中的每一個key叫出來
	if wc[word] > 1000000: #出現次數大於100
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds') #結束時間減到開始時間就是執行需要的時間
print(len(wc))
print(wc['Allen']) #查詢特定的字出現的次數

while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	else: #若沒使用這個功能，當出現字典沒有的字時程式會當掉
		print('這個字沒有出現過喔!')
	print(word, '出現過的次數為: ', wc[word])
	print('感謝使用此查詢功能')
