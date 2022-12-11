// 驗證碼
var code;

// 驗證碼產生
function createCode() {
  code = "";
  var codeLength = 6; //驗證碼的長度
  var checkCode = document.getElementById("checkCode");
  var codeChars = new Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z');
  for (var index = 0; index < codeLength; index++) {
    var charNum = Math.floor(Math.random() * 52);
    code += codeChars[charNum];
  }
  if (checkCode) {
    checkCode.className = "code";
    checkCode.innerHTML = code;
  }
}
// 驗證碼驗證流程
function validateCode() {
  var inputCode = document.getElementById("inputCode").value;
  var textShow = document.getElementById("text_show")
  if (inputCode.length <= 0) {
    textShow.innerHTML = "請輸入驗證碼";
    textShow.style.color = "red";
  } else if (inputCode.toUpperCase() != code.toUpperCase()) {
    textShow.innerHTML = "您輸入的驗證碼有誤";
    textShow.style.color = "red";
    createCode();
  } else {
    textShow.innerHTML = "驗證碼正確";
    textShow.style.color = "green";
  }
}
// 確定按鍵
function checkCode(){
  var btn = document.getElementById("Button1");
  btn.onclick=function(){
    validateCode();
  }
}
window.onload = function () {
  checkCode();
  createCode();
  document.getElementById("checkCode").onclick = function () { createCode() }
  linkbt.onclick = function () { createCode() }
  inputCode.onclick = function () { validateCode(); }
}