const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");
let todos = [];

todoForm.addEventListener("submit", submitAddTodo);

function paintTodoList() {
  todoList.innerHTML = ""; // 기존의 할 일 목록을 초기화

  todos.forEach((todo) => {
    const li = document.createElement('li');
    li.id = todo.id;
    const span = document.createElement('span');
    const button = document.createElement('button');
    span.innerText = todo.text;
    button.innerText = '끝!';
    button.addEventListener("click", () => deleteTodo(todo.id));

    li.appendChild(span);
    li.appendChild(button);
    todoList.appendChild(li);
  });
}

function submitAddTodo() {
  event.preventDefault();
  const content = document.getElementById("content");
  const newTodo = { text: content.value, id: Date.now() };
  todos.push(newTodo);
  window.localStorage.setItem('todo', JSON.stringify(todos));
  content.value = "";
  paintTodoList();
}

function deleteTodo(todoId) {
  todos = todos.filter((todo) => todo.id !== todoId);
  window.localStorage.setItem('todo', JSON.stringify(todos));
  paintTodoList();
}

function loadTodoList() {
  const storedTodos = JSON.parse(localStorage.getItem('todo'));
  if (storedTodos !== null) {
    todos = storedTodos;
    paintTodoList();
  }
}

loadTodoList();
