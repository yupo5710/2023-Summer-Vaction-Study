const loginButton = document.getElementById("login-btn");

loginButton.addEventListener("click", () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // 아이디 혹은 비번이 공란일 경우
    if (username === "" || password === "") {
        alert("Please fill in both username and password.");
        return;
    }

    // 비밀번호 맞으면
    if (password === "summervacation") { // 비밀번호
        alert("Login successful! You can proceed to the next step.");
        // 다음페이지로 넘기기(빈페이지)
        window.location.href = "success.html";
    } else {
        alert("Incorrect password. Please try again.");
    }
});
