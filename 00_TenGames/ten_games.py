import random
from sys import exit

"""
登入程式後 輸入 hangman 可以玩隱藏遊戲
"""
class Gaming_Programs:
	# 0.離開程式-大小寫還沒處理
	def out(self):
		while True:
			print("=====================")
			check = (input("請問是否確認離開程式(Y/N)"))
			if check == "Y":
				print("你已離開程式，歡迎下次使用！")
				exit()
			elif check == "N":
				any_key()
				main_catalog()
				break
			else:
				print("輸入錯誤請重新輸入")
				any_key()

	# 1.BMI計算
	def bmi(self):
		print("=====================")
		print("歡迎來到PY健康中心")
		weight = eval(input("請輸入體重(kg):"))
		height = eval(input("請輸入身高(cm):"))
		bmi = weight / ((height/100) ** 2)
		print("=====================")
		print("你的BMI為%.2f(kg/cm2)" % (bmi))	
		# 計算「標準體重」的功能並給予建議
		rcmd_up = 24*(height/100)**2
		rcmd_low = 18.5*(height/100)**2
		if bmi >= 24 or bmi < 18.5:
			print("=====================")
			print("目前體重不在理想範圍喔~~\n\
身高%.1fcm，標準體重介於%.2f~%.2fkg" % (height, rcmd_low, rcmd_up))
			any_key()

	# 2.溫度轉換-用try_exception解決輸入問題
	def temp_trans(self):
		while True:
			print("=====================")
			print("歡迎來到PY溫度計")
			print("請輸入你要傳換的溫度單位(1/2):\n1.華式\n2.攝氏")
			option = input()
			try:
				option = int(option)
				if  option == 1:
					cel = input("請輸入攝氏溫度:")
					fah = (float(cel) * 9 / 5) + 32  # C → F
					print("現在溫度為華氏%.2f度。" % (fah))
					any_key()
					break
				elif option == 2:
					fah = input("請輸入華氏溫度:")
					cel = (float(fah) - 32) * 5 / 9  # F → C
					print("現在溫度為攝氏%.2f度。" % (cel))
					any_key()
					break
				else:
					mistake()
			except Exception: 
					mistake()

	# 3.公/英里換算
	def distance(self):
		while True:
			print("=====================")
			print("歡迎來到PY公/英哩傳換器")
			print("請輸入你要兌換的長度單位(1/2):\n1.公里\n2.英哩")
			print("(公里/英哩 = 1 km:0.6 miles)")
			option = input()
			try:
				option = int(option)
				if option == 1:
					km = eval(input("請輸入公里數:"))
					miles = km * 0.62
					print("%.2f公里為%.2f英哩。" % (km, miles))
					any_key()
					break
				elif option == 2:
					miles = eval(input("請輸入英哩數:"))
					km = miles / 0.6
					print("%.2f英哩為%.2f公里。" % (miles, km))
					any_key()
					break
				else:		# else 是為了輸入非選項數字出現的問題
					mistake()
			except Exception:	
					mistake()

	# 4.飲料店-註解已整理-list
	def drinks(self):
		drinks = [		
			["可樂(Coka Cola)", 25],
			["奶茶(Milk Tea)", 35],
			["綠茶(Green Tea)", 20]
		]  # 1x3 可新增擴充 
		"""
		似乎不適合以 json/dict 儲存 (如果真的要的話應該把 key值 要指定為 品項、價錢去匯入每筆資料)
		{
			{	"product":"可樂",
				"price":25	},
			{	"product":"奶茶",
				"price":35	}
			{	"product":"綠茶",
				"price":20	}
		} 
		"""
		print("=======歡迎光臨 PY 飲料店========")
		print("可樂%d元、奶茶%d元、綠茶%d元"
			  % (drinks[0][1], drinks[1][1], drinks[2][1]))  # 檢索陣列裡的資料

		total = 0
		for i in range(len(drinks)):
			num = eval(input("請輸入%s數量:" % drinks[i][0]))  # drink[i][0] 找品名
			cost = drinks[i][1] * num                         # drink[i][1] 找價格
			total += cost
			print("=======================")
			print("此品項已購買 %d 杯，小計：%d 元，總金額：%d 元" % (num, cost, total))
			print("=======================")
			any_key()

	# 5.99乘法表
	def charts(self):
		print("=====================")
		print("歡迎使用乘法表系統")
		a = input("請輸入第一個數字:")
		b = input("請輸入第一個數字:")
		try:
			a = int(a)
			b = int(b)
			for i in range(1, a+1):
				for j in range(1, b+1):
					print("%-2dx %-2d= %-2d  " % (i, j, i*j), end="")
				print("")
				any_key()
		except Exception:
			mistake()


	# 6.終極密碼-註解已整理
	def code(self):
		code = random.randint(1, 100)
		ceil = 100  # 設定初始上限
		floor = 1  # 設定初始下限
		print(code)
		while ans != code:
			print("---------------------")
			print("請輸入密碼:(密碼介於%d~%d之間)" % (floor, ceil))
			ans = eval(input())
			if ans == code:
				print("恭喜答對了!")
				any_key()
			elif code <= ans <= ceil:
				print("密碼介於%d~%d" % (floor, ans))
				ceil = ans   # 此輪定義答案為範圍上限
			elif floor <= ans <= code:
				print("密碼介於%d~%d" % (ans, ceil))
				floor = ans  # 此輪定義答案為範圍下限
			else:
				mistake()

	# 7.PY升職記-註解已整理-dict-用isdigit解決輸入問題
	def promote(self):
		# 作答、得分流程
		def promote_choice(score_default, i):  # !!!!已排除輸入不同字串、符號、數字的情況!!!!
			while True:
				answer = input("請作答(大小寫皆可):")					# 使用可輸入大小寫
				if answer.isdigit() == True:  								# 判定輸入的answer是否為數字
					mistake()
					continue
				elif answer.isdigit() == False:  							# 若不是數字則~~~
					upper = answer.upper() 											# 指定upper = 輸入答案轉為大寫字母
					if upper in Answer_list[i]:  								# 判定字母有沒有在Answer[i]的答案列表裡不同的字典
						score_default += Answer_list[i][upper]		# 變數 i 用下面for迴圈的 i 去代入 (讓列表可自動切到不同字典)
						print("此題得分為%d分，目前分數為%d分\n" %(Answer_list[i][upper], score_default))
						break
					else:
						mistake()
						continue
			return score_default
		
		#---Content---
		print("=============歡迎來到PY升職記=============\n")
		print("你好，你是一位公司業務，需要透過提升與老闆的好感度，晉升主管的位置。\n以下將有「3」個問題，每個問題都有對應分數，並請試著達到高分。\n")
		any_key()

		#---MAIN---
		Question_list = [  # 第一題~第三題的題目列表
			"早晨，你剛進公司電梯就看到老闆，請問應該怎麼辦呢?(A~C)\n\nA.見面尷尬，微笑以待。\nB.精神飽滿，噓寒問暖。\nC.繼續低頭滑手機。",
			"工作中，老闆請你幫他買一杯咖啡，請問應該怎麼辦呢?(A~C)\n\nA.不要找我，我很忙。\nB.好的老闆，要甚麼口味的?。\nC.老闆，我也想點一杯嗎?。",
			"下班時間到了，老闆問你今天可不可以加班，請問應該怎麼辦呢?(A~C)\n\nA.老闆，我晚一點還有事。\nB.好的老闆，衝衝衝!\nC.老闆，下班時間，絕不加班!"
		]  # 1x3
		Answer_list = [
			{"A": 1, "B": 2, "C": 0},  # 第一題得分分配
			{"A": 0, "B": 2, "C": 1},  # 第二題得分分配
			{"A": 1, "B": 2, "C": 0}   # 第三題得分分配
		]  # 1x3x3

		score = 0                                  # 初始分數
		for i in range(3):                         # 用 list 跟 dict 制定題目跟的分數(變於管理題目、答案更新)
			print("========第%d題========" % (i+1))
			print(Question_list[i])									 # 分數由Promote_choice()函式裡面去累加，每次迴圈都return新的score
			score = promote_choice(score, i)
			any_key()                                # i主要是賦予函式內 用Answer_list找列表裡的字典 !!!!
			print("")                                # 純粹換行用
		# ===================================================================

		# 成績單
		print("============成績單=============\n")
		print("本試卷總分6分，你得分為%d分" % (score))
		if score == 6:		print("恭喜你，獲取老闆的歡心! 晉升主管指日可待!!!\n")
		elif score >= 3:	print("再努力一點，奉獻你的肝、拍老闆馬屁，遲早升主管!!\n")
		else:							print("只能說，有骨氣，是個狠人!!\n")
		print("===============================")
		any_key()

	# 8.AB遊戲-註解已整理
	def ab_game(self):
		"""
		＊用Random取題目變數
		＊使用list填入比對做迴圈判斷
		"""
		ans = list(random.sample(range(1, 10), 4))  # 取 4位變數1~10
		print(ans)
		a = b = n = 0  												# 賦予初始值 a=A符合數 b=B符合數 n=取陣列n數 皆從0開始 做for迴圈。
		while a != 4:
			a = b = n = 0  											# 每次迴圈都回到初始0
			nums = list(input("輸入四個數字：")) # 讓使用者輸入數字，並透過 list 轉換成串列
			for i in nums:                      # 使用 for 迴圈，將使用者輸入的數字一一取出
				if int(nums[n]) == ans[n]:        # 因為使用者輸入的是「字串」，透過 int 轉換成數字，和答案陣列互相比較
					a += 1                          # 如果位置和內容都相同，就將 a 增加 1
				else:
					if int(i) in ans:               # 如果位置不同，但答案裡有包含使用者輸入的數字
						b += 1                        # 就將 b 增加 1
				n += 1														# 因為輸入的每個數字(列表內的每個數字)都要判斷，將 n 增加 1
			# answer = ",".join(nums).replace(",","")     # 可用可不用 可與下面user替換
			nums = [int(x) for x in nums]       # 四個數字都判斷後，使用 join 將串列合併成字串
			print(nums, ":{:d}A{:d}B".format(a, b))
		print("答對了!")
		any_key()

	# 9.21點-註解已整理-list
	def blackjack(self):
		"""
		＊基本所需 一副撲克牌 4個花色、13張牌(但是只有[1,2,3,4,5,6,7,8,9,10,10,10,10])
		＊角色:banker、player
		＊莊、玩 各發兩張牌 莊家(一開一關)、玩家(雙開)
		＊詢問閒家是否補牌(要設計A在牌內的行為)
		＊補牌後加總分數 並且判定是否 > 21點  未超過就要繼續詢問補牌
		＊莊家 < 17點 自動補牌
		＊最後比較點數
		"""
		# 隨機補牌(單張)
		def random_choice():
			card = random.choice(pokercards)
			pokercards.remove(card)
			return card

		# 玩家判斷+補牌
		def judge_player_draw():
			if sum(player_cards) > 21:
				print("超過21點，蹦蹦蹦!!")
			elif sum(player_cards) < 21:
				while sum(player_cards) < 21:
					print("===============")
					any = input("請問是否要補牌 ( Y / N ) ? ")
					if any == "Y":
						a = input("(抽牌中...)\n(請輸入任意鍵進入下一步...)")
						card = random_choice()
						print("===============")
						print("抽到的點數為 %d 點" %(card))
						player_cards.append(card)
						print("玩家的牌為 %d 點 %s " %(sum(player_cards), player_cards))
					else:
						print("不補牌")
						break
			return player_cards

		# 莊家判斷+補牌
		def judge_banker_draw():
			if sum(banker_cards) > 21:
				print("超過21點，蹦蹦蹦!!")
			elif sum(banker_cards) > 17:
				print("莊家的牌為 %d 點 %s" % (sum(banker_cards), banker_cards))
			elif True:
				print("莊家的牌為 %d 點 %s" % (sum(banker_cards), banker_cards))
				while sum(banker_cards) < 17:
					print("===============")
					a = input("(莊家小於17點，自動補牌中...)\n(請輸入任意鍵進入下一步...)")
					card = random_choice()
					print("===============")
					print("抽到的點數為 %d 點" % (card))
					banker_cards.append(card)
					print("莊家的牌為 %d 點 %s " % (sum(banker_cards), banker_cards))
			return banker_cards

		# 比牌值
		def high_low():
			banker_point = sum(banker_cards)
			player_point = sum(player_cards)
			if banker_point > player_point and banker_point <= 21:
				print("莊家%d點，玩家%d點，莊家贏!!" % (banker_point, player_point))
			elif banker_point == player_point:
				print("莊家%d點，玩家%d點，和局!!" % (banker_point, player_point))
			elif banker_point < player_point and player_point <= 21:
				print("莊家%d點，玩家%d點，玩家贏!!" % (banker_point, player_point))

		# 初始牌組======================================================
		pokercards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
		banker_cards = random.sample(pokercards, 2)  # 莊家預設牌x2
		player_cards = random.sample(pokercards, 2)  # 玩家預設牌x2

		for i in range(len(banker_cards)):  							# 把預設牌的值 從牌組內排除
			# 莊家
			num_banker = banker_cards[i]  									# 預設牌給予變數num
			Position_banker = pokercards.index(num_banker)  # 依順序找num在Pokercards的位置
			del pokercards[Position_banker]  								# 找到位置後刪除P裡面的num_banker
			# 玩家
			num_player = player_cards[i]  									# 預設牌給予變數num
			Position_player = pokercards.index(num_player)  # 依順序找num在Pokercards的位置
			del pokercards[Position_player]  								# 找到位置後刪除P裡面的num_banker
		# print(pokercards) #這時的P就是 扣掉莊家、玩家共4張牌的列表

		# 遊戲步驟
		print("===== Welcome To PY_21點 =====")
		print("提示:本遊戲不適用「1點(A) = 11點規則」")
		any_key()
		print("==============================")
		print("莊家的牌為 %d + ? 點 " % (banker_cards[0]))
		print("玩家的牌為 %d 點 %s " % (sum(player_cards), player_cards))
		any_key()
		judge_player_draw()
		print("==============================")
		judge_banker_draw()
		print("==============================")
		high_low()
		any_key()

	# 隱藏遊戲-hangman猜單詞-註解已整理
	def hangman(self):
		hangman = {
			1:  "\-—┌———————┐——\n\  ┃       ┃\n\  ┃     \n\  ┃     \n\  ┃    \n\  ┃     \n\  ┃      \n\  ┃ \n━━━━━━━━━━━━━━",
			2:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     \n\  ┃      \n\  ┃ \n━━━━━━━━━━━━━━",
			3:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃       ┃ \n\  ┃      \n\  ┃ \n━━━━━━━━━━━━━━",
			4:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     ╱ ┃ \n\  ┃      \n\  ┃ \n━━━━━━━━━━━━━━",
			5:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     ╱ ┃ ╲\n\  ┃     \n\  ┃ \n━━━━━━━━━━━━━━",
			6:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     ╱ ┃ ╲\n\  ┃      ╱ \n\  ┃ \n━━━━━━━━━━━━━━",
			7:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     ╱ ┃ ╲\n\  ┃      ╱ ╲\n\  ┃ \n━━━━━━━━━━━━━━"
		}  # 這個是 hangman 圖示

		# 題目設計，隨機出題(後面可自由新增難易度選項跟題海，欄位設定為難易度/分類)
		dict = ["apple", "banana", "cat", "watermelon", "elephant", "cheery", "bedroom",
				"enough", "computer", "giant", "kiwi", "grape", "noodle",
				"sister", "taiwan", "watermelon", "wonderful"]
		question = random.sample(dict, 1)  # 隨機從字典裡挑1個 (路徑,樣本數)

		list_question = list(question[0])  # question 是list型態 先取出[0]，對字串list就會分割字母	
		# 直接分割 不用再土炮用for迴圈 填入
		# list_question = []		
		# for i in range(len(question)):
		# 	list_question += question[i]

		question_copy = list_question.copy()  # 複製一個copy 主要是為了要跟 while迴圈裡跟answer比對
		anwser = ["_"]*(len(list_question)) 	# 製造與題目相同長度的 ["_","_","_","_","_"]
		print("★★★★  隱藏遊戲-HangMan ★★★★")
		print("猜猜題目的英文單字是甚麼吧!!!")
		print("===============================")
		print("題目: ", ' '.join(anwser))    # 題目: _ _ _ _ _ _  空白連接每個字元
		# print(list_question)
		# print(anwser)
		list_guess = []                   # 預設猜過的字母放裡面
		count_wrong = 0                   # 預設猜錯數從0開始
		while anwser != question_copy:    # 兩個不相等代表還沒有猜中，沒猜中就不停止迴圈
			alphbet = input("請輸入字母(a~z):")
			print("===============")
			list_guess.append(alphbet)											# 把答案放進猜的空list裡面  確認猜過的字母								
			list_guess = list(set(list_guess))              # 用set轉換list 把重複的刪掉，再把set轉回list列表
			if alphbet in list_question:
				count_right = list_question.count(alphbet)		# 數 list_qusetion 裡面有多少個alphbet
				for i in range(1, count_right+1):             # for 執行 count +1次的迴圈
					guess_right = list_question.index(alphbet)  # 用index回查答案在題目中的位置
					anwser[guess_right] = alphbet								# 將anwser對應的位置插入答案
					list_question[guess_right] = "_"					  # 在list_qusetion裡將猜對的字母，用"底線"替換
				if anwser == question_copy:
					print("恭喜答對了,答案就是:", ' '.join(anwser))
					any_key()
				elif anwser != question_copy:
					print("你已猜過的字母: ", ' '.join(list_guess))
					print("---------------")
					print("答案: ", ' '.join(anwser))
					print("---------------")
			elif alphbet not in list_question:
				count_wrong += 1
				print("---------------")
				print("你已猜過的字母: ", ' '.join(list_guess))
				print("答案: ", ' '.join(anwser))
				print("---------------")
				print("Oh,NO!!  你已猜錯 %d 次!! 剩餘 %d 次機會。" %(count_wrong, 7-count_wrong))
				print("---------------")
				print(hangman[count_wrong])
				if count_wrong == 7:
					print("~GaMe oVeR~")
					any_key()
					break

# 系統登入頁面
def log_in_sys():
	user_acc = "123"
	user_pwd = "123"
	key_acc = input("請輸入帳號：")
	key_pwd = input("請輸入密碼：")
	i = 1
	while i < 4:
		if key_acc == user_acc and key_pwd == user_pwd:
			print("帳號密碼正確，歡迎進入本系統。")
			break
		elif i == 3:
			print("錯誤已達3次，請重新執行本程式。")
			exit()
		elif key_acc != user_acc or key_pwd != user_pwd:
			print("輸入錯誤達%d次，剩餘%d次機會，請重新輸入!!" % (i, 3-i))
		i += 1

# 節奏控制用
def any_key():
	a = input("(請輸入任意鍵進入下一步...)")
def mistake():
	a = input("(輸入錯誤!!請重新輸入...)")


# 主畫面
def main_catalog():
	print("=====================")
	print("本程式目錄如下:\n1.BMI計算\n2.溫度換算\n3.公里/英哩轉換\n4.結帳系統\
		\n5.乘法表\n6.終極密碼\n7.小遊戲-PY升職記\n8.數字AB遊戲\n9.PY_21點\n0.離開")
	print("=====================")
	choose = input("請選擇你需要執行的程式:\n")
	choose = choose.lower()	# 這是為了hangman確保執行
	if choose == "0":		games.out()
	elif choose == "1":	games.bmi()
	elif choose == "2":	games.temp_trans()
	elif choose == "3":	games.distance()
	elif choose == "4":	games.drinks()
	elif choose == "5":	games.charts()
	elif choose == "6":	games.code()
	elif choose == "7":	games.promote()
	elif choose == "8":	games.ab_game()
	elif choose == "9":	games.blackjack()
	elif choose == "hangman":	games.hangman()
	else:	mistake()
	main_catalog()

games = Gaming_Programs()  # 物件指定結合class Gaming_Programs，便於主程式呼叫

# 程式登入  log_in_sys()
print("=====================")
print("---歡迎來到py小程式---")
print("=====================")
any_key()
log_in_sys()

# 進入程式主頁面 main_catalog()
print("=====================")
print("---歡迎登入py小程式---")
print("=====================")
main_catalog()
