
   /*
   Need to check if token has expired
    */
    function view() {
        var isLoggedIn = localStorage.getItem('loggedin');

        if (isLoggedIn == 1) {
            document.getElementById("signin").style.display = "none";
            document.getElementById("signup").style.display = "none";
            document.getElementById("or").style.display = "none";
            document.getElementById("profile").style.visibility = "visible";
            document.getElementById("manage").style.visibility = "visible";
            document.getElementById("join").style.visibility = "visible";
        } else {
            document.getElementById("signin").style.visibility = "visible";
            document.getElementById("signup").style.visibility = "visible";
            document.getElementById("or").style.visibility = "visible";
            document.getElementById("profile").style.display = "none";
            document.getElementById("manage").style.display = "none";
            document.getElementById("join").style.display = "none";
        }
    };

    window.onload = view();