// Recreate the game in Js and console it 
// Link every function & onclick & onchange 

let guesses;
let answer;


window.onload = function() {
  InitGame()
  document.getElementById("number-submit").addEventListener("click", PlayGame);
  document.getElementById("restart-game").addEventListener("click", InitGame)
}


// 遊戲執行過程需要獲取(id="number-guess")裡面的值 再執行 儲存、歷史展示、結果展示
// while the game is in progress, we can get the value via id="number-guess".
function PlayGame () {
  let guess = document.getElementById("number-guess").value 
  SaveGuessHistory(guess)
  DisplayInHistory()
  DisplayResult(guess)
} 

// 遊戲初始化 / Initialize a new game by resetting all values and content on the page 
function InitGame () {
  answer = GetRandomNumber()
  guesses = []
  DisplayInHistory()
  ResetResultContent()
}

// 清除結果欄  / clean up the Result
function ResetResultContent () {
  document.getElementById('result').innerHTML=''
}

// 建立隨機數(1~100) / Generate the random number(answer)
function GetRandomNumber () {
  return Math.floor(Math.random()*100+1);
}
// 以陣列型態儲存歷史紀錄 / Use object to store the value you guess 
function SaveGuessHistory (guess) {
  guesses.push(guess)
}

// 展示歷史紀錄(id="history") // display the history
function DisplayInHistory () {
  // 索引長度 index 表示陣列裡的最後一個位置  // rewrite the ul & li everytime.
  let index = guesses.length-1
  let list = "<ul class='list-group'>"
  while (index >= 0) {
    list += "<li class='list-group-item'>" + "You guessed " + guesses[index] +  "</li>"
    index -= 1
    // 不是保留舊的，直接新增一條li 而是每次有新的參數進入guesses 重新渲染心得ul清單
  }
  list += '</ul>'
  document.getElementById("history").innerHTML = list;
}

// 展示結果 / Use if else statment to compare the value between answer and guess
function DisplayResult(guess) {
  if (guess > answer) {
    HigherThan()
  } else if (guess < answer) {
    LowerThan()
  } else {
    GuessEqualsAnswer()
  }
}

// 可輸入比較後的結果文字並產出div標籤 
function GetDialog(dialogType, text){
  let dialog;
  switch(dialogType){
    case "warning":
      dialog = "<div class='alert alert-warning'>"
      break;
    case "won":
      dialog = "<div class='alert alert-success'>"
      break;
  }
  dialog += text; // <div class='alert alert-warning'> Your guess is too high! 
  dialog += "</div>" // <div class='alert alert-warning'> Your guess is too high! </div>
  return dialog; 
  // 
}

// 產出div標籤後回傳，並渲染id="result"的位置 
// After get the dialog, we can render the HTML via id="result".
function HigherThan () {
  const text = "Your guess is too high!"
  let dialog = GetDialog('warning', text)
  document.getElementById("result").innerHTML = dialog;
}
function GuessEqualsAnswer () {
  const text = "Congraulation. You got it!"
  let dialog = GetDialog('won', text)
  document.getElementById("result").innerHTML = dialog;
}
function LowerThan () {
  const text = "Your guess is too low!"  
  let dialog = GetDialog('warning', text)
  document.getElementById("result").innerHTML = dialog;
}



// const history = "You guessed " + guess
// console.log(history);

