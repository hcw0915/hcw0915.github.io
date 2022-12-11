

// DOM & Variables section
const lengthElement = document.getElementById('length')
const symbolElement = document.getElementById('includeSymbols')
const numberElement = document.getElementById('includeNumbers')
const lowerElement = document.getElementById('includeLowercaseCharacters')
const upperElement = document.getElementById('includeUppercaseCharacters')
const form = document.getElementById('passwordGeneratorForm')


// ascii 用 轉換位數
const symbolCharCode = 
  asciiCode(33,47)
  .concat(asciiCode(58,64))
  .concat(asciiCode(91,96))
  .concat(asciiCode(123, 126))
const numberCharCode = asciiCode(48, 57)
const upperCharCode = asciiCode(65, 90)
const lowerCharCode = asciiCode(97, 122)


// 監聽事件 追蹤選項checked的狀況，
form.addEventListener('submit', e => {
  // cancel DOM's default movement
  e.preventDefault()
  const length = lengthElement.value
  const symbol = symbolElement.checked
  const number = numberElement.checked
  const upper = upperElement.checked

  // 將監聽狀況傳入 generatPassword() 函數裡，並回傳生產密碼
  const password = generatePassword(length,symbol,number,upper)
  // 產出的密碼送回 result 裡
  document.getElementById('result').value = password
})

// 密碼產生函式
function generatePassword(length,symbol,number,upper){
  // 預設密碼產生在不勾選(unchecked => false)的情況下為小寫
  let charCodes = lowerCharCode
  // 將ASCII的位數與lowercharcode合併
  if (symbol) charCodes = charCodes.concat(symbolCharCode)
  if (number) charCodes = charCodes.concat(numberCharCode)
  if (upper) charCodes = charCodes.concat(upperCharCode)

  // 預設passwordChar 是空值
  const passwordChar = []
  /* for 迴圈導入 
    每次迴圈都會產生一個數 charCodes是一數列，
    每次亂數產生1個數放入 characterCodes 裡
    再由String.fromCharCode()轉換，再push 進 passwordChar
  */
  for (let i = 0; i < length; i++ ){
    const characterCodes = charCodes[Math.floor(Math.random() * charCodes.length)]
    passwordChar.push(String.fromCharCode(characterCodes))
  }
  // 把陣列用join('')整理出來
  return passwordChar.join('')
}

// 產生ASCII代碼用
function asciiCode(numStart,numEnd){
  const charCodeNumber = []
  for (let i = numStart; i <= numEnd; i++ ){
    charCodeNumber.push(i)
  }
  return charCodeNumber
}


// 複製鍵 / Copy Function 
function copyFn(){
  document.querySelector('#result').select()
  document.execCommand ("Copy");
  alert("Copy Successfully")
}




//  走錯的彎路總是多



// // 主程式執行
// function Generate () {
//   const passwordLengthValue = passwordLength.value
//   let result = []

//   for (let i = 0; i < passwordLengthValue; i++ ){
//   const num = Math.floor(Math.random() * 25) // 0~25數字
//   const char = String.fromCharCode(65 + num) // A~Z的ASCII碼 (65~90)
//   result.push(Math.random() >= 0.5 ? char.toLowerCase() : char);
//   }
//   document.getElementById('result').value = result.join("")

// }


// const checkbox = document.getElementById('includeSymbols')

// // 確認框事件監聽 checkbox EventListener
// checkbox.addEventListener('change', (e) => {
//   if (e.currentTarget.checked) {
//     alert('checked');
//   } else {
//     alert('not checked');
//   }
// })


/* 
  使用者勾選完之後按下產生鍵需要先判斷 checkbox 的執行情況
  要建立 function 去判斷 每一個打勾狀況
  確認狀況後 return 回主程式執行
  主程式要判斷條件執行。
*/

