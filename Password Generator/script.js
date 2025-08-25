document.getElementById("generate").addEventListener("click", () => {
    const length = parseInt(document.getElementById("length").value);

    if (isNaN(length) || length < 4 || length > 20) {
        document.getElementById("password").textContent = "Enter a valid length (4-20).";
        return;
    }

    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?";
    let password = "";

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters[randomIndex];
    }

    document.getElementById("password").textContent = password;
});
