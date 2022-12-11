// ClassElement
const computerElement = document.querySelector('.computer');
const playerElement = document.querySelector('.player');
const resultElement = document.querySelector('.result');

// choice
let computerChoice;
let playerChoice;
// Buttons
const scissorsElement = document.querySelector('.scissors');
const rockElement = document.querySelector('.rock');
const paperElement = document.querySelector('.paper');
const buttonElement = document.querySelectorAll('button');
// IMG
const newImgPlayer = document.createElement('img');
const newImgComputer = document.createElement('img');
// 用數值比較大小
function computerShuffle() {
  const array = ['剪刀', '石頭', '布'];
  let randomNumber = Math.floor(Math.random() * 3);
  computerChoice = array[randomNumber];
  return computerChoice;
}

function display(computerChoice) {
  if (computerChoice === '剪刀') {
    newImgComputer.src = '/picture/scissors-removebg-reverse.png';
    newImgComputer.style = 'width:200px;height:250px';
    computerElement.appendChild(newImgComputer);
  }
  if (computerChoice === '石頭') {
    newImgComputer.src = '/picture/rock-removebg-reverse.png';
    newImgComputer.style = 'width:200px;height:250px';
    computerElement.appendChild(newImgComputer);
  }
  if (computerChoice === '布') {
    newImgComputer.src = '/picture/paper-removebg-reverse.png';
    newImgComputer.style = 'width:200px;height:250px';
    computerElement.appendChild(newImgComputer);
  }
}

function getResult(computerChoice, playerChoice) {
  if (computerChoice === playerChoice) {
    resultElement.innerText = '===';
  }
  if (computerChoice === '石頭' && playerChoice === '剪刀') {
    resultElement.innerHTML = 'COM WIN!';
  }
  if (computerChoice === '石頭' && playerChoice === '布') {
    resultElement.innerText = 'PLAYER WIN';
  }
  if (computerChoice === '剪刀' && playerChoice === '布') {
    resultElement.innerText = 'COM WIN!';
  }
  if (computerChoice === '剪刀' && playerChoice === '石頭') {
    resultElement.innerText = 'PLAYER WIN';
  }
  if (computerChoice === '布' && playerChoice === '石頭') {
    resultElement.innerText = 'COM WIN!';
  }
  if (computerChoice === '布' && playerChoice === '剪刀') {
    resultElement.innerText = 'PLAYER WIN';
  }
  return resultElement;
}

// function winnerPic(resultElement) {
//   if ((resultElement.innerText = '電腦 勝利')) {
//     newImgComputer.src = '/picture/winner-removebg-preview.png';
//     newImgComputer.style = 'width:200px;height:250px';
//     computerElement.appendChild(newImgComputer);
//   } else if ((resultElement.innerText = '玩家 勝利')) {
//     newImgPlayer.src = '/picture/winner-removebg-preview.png';
//     newImgPlayer.style = 'width:200px;height:250px';
//     PnewImgPlayerElement.appendChild(newImgPlayer);
//   }
// } else if ((resultElement.innerText = '平手')) {
//   return;
// }
// }

// // 流程
buttonElement.forEach((button) => {
  button.addEventListener('click', (e) => {
    playerChoice = button.innerText;
    newImgPlayer.src = `/picture/${button.className}-removebg-preview.png`;
    newImgPlayer.style = 'width:200px;height:250px';
    playerElement.appendChild(newImgPlayer);

    computerShuffle();
    display(computerChoice);
    getResult(computerChoice, playerChoice);
  });
});

// 流程

// buttonArray.forEach((button) => {
//   button.addEventListener('click', (e) => {
//     playerChoice = button.innerText;
//     playerElement.innerText = `Player : ${playerChoice}`;
//     computerShuffle();
//     display(computerChoice);
//     getResult(computerChoice, playerChoice);
// })

// scissorsElement.addEventListener('click', (e) => {
//   playerChoice = scissorsElement.innerText;
//   playerElement.innerText = `Player : ${playerChoice}`;

//   newImgPlayer.src = '/picture/scissors-removebg-preview.png';
//   newImgPlayer.style = 'width:200px;height:250px';
//   playerElement.appendChild(newImgPlayer);

//   computerShuffle();
//   display(computerChoice);
//   getResult(computerChoice, playerChoice);
//   // winnerPic(resultElement);
// });

// rockElement.addEventListener('click', (e) => {
//   playerChoice = rockElement.innerText;
//   playerElement.innerText = `Player : ${playerChoice}`;

//   newImgPlayer.src = '/picture/rock-removebg-preview.png';
//   newImgPlayer.style = 'width:200px;height:250px';
//   playerElement.appendChild(newImgPlayer);

//   computerShuffle();
//   display(computerChoice);
//   getResult(computerChoice, playerChoice);
//   // winnerPic(resultElement);
// });

// paperElement.addEventListener('click', (e) => {
//   playerChoice = paperElement.innerText;
//   playerElement.innerText = `Player : ${playerChoice}`;

//   newImgPlayer.src = '/picture/paper-removebg-preview.png';
//   newImgPlayer.style = 'width:200px;height:250px';
//   playerElement.appendChild(newImgPlayer);

//   computerShuffle();
//   display(computerChoice);
//   getResult(computerChoice, playerChoice);
//   // winnerPic(resultElement);
// });
