var button = document.getElementById("myButton");

button.addEventListener("click", function () {
  if (button.textContent === "확인") {
    button.textContent = "취소";
    button.style.backgroundColor = "red";
  } else {
    button.textContent = "확인";
    button.style.backgroundColor = "blue";
  }
});
