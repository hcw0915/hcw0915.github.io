// Selectors
const todoInput = document.querySelector('.todo-input')
const todoButton = document.querySelector('.todo-button')
const todoList = document.querySelector('.todo-list')


// Event Listeners
todoButton.addEventListener('click',addTodo)
todoList.addEventListener('click',deleteCheck)

// Functions
function addTodo(e){
  e.preventDefault()
  console.log("hello");
  // 製作todo的<div>、<li>、<button>
  const todoDiv = document.createElement('div')
  // 為todo div標籤加上 class="todo"
  todoDiv.classList.add("todo")

  const newTodo = document.createElement('li')
  newTodo.innerText = todoInput.value
  newTodo.classList.add("todo-item")
  // 把newTodo加到tododiv後面 (也就是<li> 加進 <div>)
  todoDiv.appendChild(newTodo)


  // 完成按鈕
  const completedButoon = document.createElement('button')
  completedButoon.innerHTML = '<i class="fa-solid fa-check"></i>'
  completedButoon.classList.add("complete-btn")
  todoDiv.appendChild(completedButoon)
  // 刪除按鈕
  const deletedButton = document.createElement('button')
  deletedButton.innerHTML = '<i class="fa-solid fa-trash"></i>'
  deletedButton.classList.add("delete-btn")
  todoDiv.appendChild(deletedButton)

  // APPEND TODO LIST
  todoList.appendChild(todoDiv)
  
  // CLEAR TODO INPUT VALUE
  todoInput.value = ""
  return todoDiv
}

function deleteCheck(e,){
  const item = e.target
  // DELETE TODO
  if (item.classList[0] === 'delete-btn'){
    const todo = item.parentElement
    // Animation
    todo.classList.add('fall')
    // 監聽在transition 結束的時候 才做remove的行為
    todo.addEventListener('transitionend',( ) => 
    todo.remove() )
  }

  // CHECK MARK
  if (item.classList[0] === 'complete-btn'){
    // document.getElementById('todo-item').style.textDecoration = 'underline'

    const todo = item.parentElement
    todo.classList.toggle("completed")
  }
}



//




// 1.創建變數 = 創造標籤
// 2.給予變數(標籤)內容渲染HTML
// 3.給予變數(標籤)class名字
// 4.把此變數(標籤)加入母層<div></div>









// ＊先建立 Selectors, Event Listener, Function 三個區塊
// ＊先監聽 todobutton 當按下按鈕時，要做加入新todo進去
//   因為還沒有加入功能，所以在function 做一個 addTodo()