function isLogged() {


    $.ajax({
        method: "GET",
        url: '/is_logged',
        dataType: "json",
        headers: {"auth_token": localStorage.getItem('auth_token')},
        success: function (data) {
            console.log(data);
        },
        statusCode: {
            400: function (data) {
                localStorage.setItem('auth_token', 0);
                localStorage.setItem('id_user', 0);
                localStorage.setItem('loggedin', 0);
                if (data.message == 'token expired' || 'Invalid token, please try again'){
                        localStorage.setItem('auth_token', 0);
                        location.replace('/login');
                }
            }
        },
        error: function (err) {
            console.log(err);
        }
    });
}

document.onload = isLogged();