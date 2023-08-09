
var clickCount = 0;
var clickTextElement = document.getElementById("clickText");
  
function updateClickCount() {
    clickCount++; //clickCount라는 변수에 +1씩 더함
    clickTextElement.textContent = "click: " + clickCount;
}
  
clickTextElement.addEventListener("click", updateClickCount);
; //click이벤트 발생시 updateClickCount 함수 작동
  