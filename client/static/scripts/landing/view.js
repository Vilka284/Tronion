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


function isLogged() {


    $.ajax({
        method: "GET",
        url: '/is_logged',
        dataType: "json",
        headers: {"auth_token": localStorage.getItem('auth_token')},
        success: function (data) {
            console.log(data);
            view();
        },
        statusCode: {
            400: function () {
                localStorage.setItem('auth_token', 0);
                localStorage.setItem('id_user', 0);
                localStorage.setItem('loggedin', 0);
                view();
            }
        },
        error: function (err) {
            console.log(err);
        }
    });
}

document.onload = isLogged();