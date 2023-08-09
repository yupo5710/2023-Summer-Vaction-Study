var clickCount = 0;
var clickTextElement = document.getElementById("clickText");

function updateClickCount() {
  clickCount++;
  clickTextElement.textContent = "click: " + clickCount;
}

clickTextElement.addEventListener("click", updateClickCount);
