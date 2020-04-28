document.getElementById("join_button").onclick = function e() {
        e.preventDefault();
        var isLoggedIn = localStorage.getItem('loggedin');

        if (isLoggedIn == 1) {
            location.replace('/join');
        } else {
            location.replace('/login')
        }
    };