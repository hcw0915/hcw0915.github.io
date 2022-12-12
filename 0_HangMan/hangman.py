import random

hangman = { 
1:  "\-—┌———————┐——\n\  ┃       ┃\n\  ┃     \n\  ┃     \n\  ┃    \n\  ┃     \n\  ┃      \n\  ┃ \n━━━━━━━━━━━━━━",
2:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     \n\  ┃      \n\  ┃ \n━━━━━━━━━━━━━━",
3:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃       ┃ \n\  ┃      \n\  ┃ \n━━━━━━━━━━━━━━",
4:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     ╱ ┃ \n\  ┃      \n\  ┃ \n━━━━━━━━━━━━━━",
5:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     ╱ ┃ ╲\n\  ┃     \n\  ┃ \n━━━━━━━━━━━━━━",
6:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     ╱ ┃ ╲\n\  ┃      ╱ \n\  ┃ \n━━━━━━━━━━━━━━",
7:  " —┌———————┐——\n\  ┃       ┃\n\  ┃     ◺  ◿\n\  ┃     ◯  ◯\n\  ┃    ╰- X -╯\n\  ┃     ╱ ┃ ╲\n\  ┃      ╱ ╲\n\  ┃ \n━━━━━━━━━━━━━━"
} # 這個是 hangman 圖示

# 題目設計，隨機出題(後面可自由新增難易度選項跟題海)
dict = ["apple","banana","cat","doodle","elephant","fragile","bedroom",
        "enough","computer","giant","interesting","grape","noodle",
        "sister","taiwan","watermelon","wonderful"] 
question = random.sample(dict,1)  # 隨機從字典裡挑1個 (路徑,樣本數)

# 題目分割成各單元
list_question = []
for i in range(len(question)):
  list_question += question[i]

question_copy = list_question.copy()  # 複製一個copy 主要是為了要跟 while迴圈裡跟answer比對
anwser = ["_"]*(len(list_question)) # 製造與題目相同長度的 ["_","_","_","_","_"]
print("★★★★  隱藏遊戲-HangMan ★★★★")
print("猜猜題目的英文單字是甚麼吧!!!")
print("===============================")
print("題目: ",' '.join(anwser))    # 題目:  _ _ _ _ _ _

list_guess = []                   # 預設猜過的字母放裡面
count_wrong = 0                   # 預設猜錯數從0開始
while anwser != question_copy:    # 兩個不相等代表還沒有猜中
  any_key()
  alphbet = input("請輸入字母(a~z):")
  print("===============")
  list_guess.append(alphbet)                      # 把答案放進猜的空list裡面  確認猜過的字母
  set_guess = set(list_guess)                     # 用set轉換list 因為set裡有不重複性，所以會把重複的刪掉
  list_guess = list(set_guess)                    # 再把set轉回list列表
  if alphbet in list_question:
    count_right = list_question.count(alphbet)    # 數 list_qusetion 裡面有多少個alphbet
    for i in range(1,count_right+1):              # for 執行 count +1次的迴圈 
      guess_right = list_question.index(alphbet)  # 用index回查答案在題目中的位置
      anwser[guess_right] = alphbet               # 將anwser對應的位置插入答案
      list_question[guess_right] = "_"            # 在list_qusetion裡將猜對的字母，用"底線"替換
    if anwser == question_copy:
      print("恭喜答對了,答案就是:",' '.join(anwser))
    elif anwser != question_copy:
      print("你已猜過的字母: ",' '.join(list_guess))
      print("---------------")
      print("答案: ",' '.join(anwser))
      print("---------------")
  elif alphbet not in list_question:
    count_wrong += 1
    print("你已猜過的字母: ",' '.join(list_guess))
    print("---------------")
    print("Oh,NO!!  你已猜錯 %d 次!! 剩餘 %d 次機會。" %(count_wrong,7-count_wrong))
    print("---------------")
    print(hangman[count_wrong])
    if count_wrong == 7:
      print("~GaMe oVeR~")
      break