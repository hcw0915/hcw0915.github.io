class Calculator {
  constructor(previousOperandTextElement, currentOperandTextElement) {
    this.previousOperandTextElement = previousOperandTextElement;
    this.currentOperandTextElement = currentOperandTextElement;
    this.clear();
  }
  //  清除(AC)把顯示板(current跟previous的值設定為空)、操作符(operation設定為未定義)
  clear() {
    this.currentOperand = '';
    this.previousOperand = '';
    this.operation = undefined; // 不是很理解
  }

  delete() {
    // 把current數字轉字串，並從最後一位開始刪除
    this.currentOperand = this.currentOperand.toString().slice(0, -1);
  }

  // 這裡的number = 下面的button.innerText
  appendNumber(number) {
    // 如果number裡面有"."，而且current裡已經含"."，則用return打斷，不執行再下一行(也就是不會顯示)
    // 要沒有 才會執行下一行(顯示)
    if (number === '.' && this.currentOperand.includes('.')) return;
    // 定義this.currentOperand這個變數為number // 改成這樣是因為要顯示在current上(先確保是字串)再用加號合併
    this.currentOperand = this.currentOperand.toString() + number.toString();
  }

  choosrOperation(operation) {
    // 如果current沒數字 就中斷
    if (this.currentOperand === '') return;
    // 如果previous欄有數字就要做計算
    if (this.previousOperand !== '') {
      this.compute();
    }

    this.operation = operation;
    this.previousOperand =
      this.currentOperand.toString() + ' ' + operation.toString();
    this.currentOperand = '';
  }

  compute() {
    let computation;
    const prev = parseFloat(this.previousOperand) || 0;
    const curr = parseFloat(this.currentOperand) || 0;
    if (isNaN(prev) || isNaN(curr)) return;
    switch (this.operation) {
      case '+':
        computation = prev + curr;
        break;
      case '-':
        computation = prev - curr;
        break;
      case '*':
        if (curr == '') {
          computation = prev;
        } else {
          computation = prev * curr;
        }
        break;
      case '/':
        if (curr == '') {
          computation = prev;
        } else {
          computation = prev / curr;
        }
        break;
      default:
        return;
    }
    this.currentOperand = computation;
    this.operation = undefined;
    this.previousOperand = '';
  }

  // 把要呈現數字的欄位裡的數字(用.innerText呈現) 指定為appendNumber裡定義的this.currentOperand(也就是number也就是button.innerText)
  updateDisplay() {
    this.currentOperandTextElement.innerText = this.currentOperand;
    this.previousOperandTextElement.innerText = this.previousOperand;
  }

  //
  // equalResult() {
  //   if (this.currentOperand != '' && this.operation == undefined)
  //     this.previousOperandTextElement.innerText = this.currentOperand;
  //   if (this.operationButtons)
  //   // 按下等於後 current要被清空(等於要重新開始下一輪的計算)   此欄位清空的是current內部的值
  //   this.currentOperand = '';
  //   // 此欄位清空的是current外部顯示的值
  //   this.currentOperandTextElement.innerText = '';
  // }
}

// create the variable which contains their [data-] selector
const numberButtons = document.querySelectorAll('[data-number]');
const operationButtons = document.querySelectorAll('[data-operation]');
const equalsButton = document.querySelector('[data-equals]');
const deleteButton = document.querySelector('[data-delete]');
const allClearButton = document.querySelector('[data-all-clear]');
const previousOperandTextElement = document.querySelector(
  '[data-previous-operand]'
);
const currentOperandTextElement = document.querySelector(
  '[data-current-operand]'
);

// create a new object of Calculator.
const calculator = new Calculator(
  previousOperandTextElement,
  currentOperandTextElement
);

//  每個(foreach)按鈕都加入事件(addeventlistener) (目的為了把鍵盤上的數字「加入(appendNumber)」並「呈現updatedisplay」)
numberButtons.forEach((button) => {
  button.addEventListener('click', () => {
    // 把按鈕上的文字加入 calculator 這個物件裡面
    calculator.appendNumber(button.innerText);
    // 加入完之後用函數呈現出來
    calculator.updateDisplay();
  });
});

operationButtons.forEach((button) => {
  button.addEventListener('click', () => {
    calculator.choosrOperation(button.innerText);
    calculator.updateDisplay();
  });
});

equalsButton.addEventListener('click', () => {
  calculator.compute();
  calculator.updateDisplay();
  // calculator.equalResult();
});

allClearButton.addEventListener('click', () => {
  calculator.clear();
  calculator.updateDisplay();
});

deleteButton.addEventListener('click', () => {
  calculator.delete();
  calculator.updateDisplay();
});
