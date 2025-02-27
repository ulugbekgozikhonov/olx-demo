function showLogin() {
    document.getElementById("loginForm").classList.remove("hidden");
    document.getElementById("registerForm").classList.add("hidden");
    document.getElementById("loginTab").classList.add("active");
    document.getElementById("registerTab").classList.remove("active");
}

function showRegister() {
    document.getElementById("registerForm").classList.remove("hidden");
    document.getElementById("loginForm").classList.add("hidden");
    document.getElementById("registerTab").classList.add("active");
    document.getElementById("loginTab").classList.remove("active");
}

function togglePassword(inputId) {
    let input = document.getElementById(inputId);
    if (input.type === "password") {
        input.type = "text";
    } else {
        input.type = "password";
    }
}





document.querySelectorAll(".setting-title").forEach(button => {
    button.addEventListener("click", () => {
        const content = button.nextElementSibling;
        const icon = button.querySelector("span");

        // Agar ochilgan bo'lsa, yopish
        if (content.classList.contains("active-content")) {
            content.classList.remove("active-content");
            icon.textContent = "▼";
        } else {
            // Barcha ochilgan bo‘limlarni yopish
            document.querySelectorAll(".setting-content").forEach(item => {
                item.classList.remove("active-content");
            });

            document.querySelectorAll(".setting-title span").forEach(icon => {
                icon.textContent = "▼";
            });

            // Yangi bo‘limni ochish
            content.classList.add("active-content");
            icon.textContent = "▲";
        }
    });
});


