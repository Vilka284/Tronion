function isLogged() {


        $.ajax({
            method: "GET",
            url: '/is_logged',
            dataType: "json",
            headers: {"auth_token": localStorage.getItem('auth_token')},
            success: function (data) {
                //Set token to current user
                localStorage.setItem('auth_token', data.token);
                localStorage.setItem('id_user', data.id_user);
                localStorage.setItem('loggedin', 1);
            },
            statusCode: {
                400: function () {
                    localStorage.setItem('auth_token', 0);
                    localStorage.setItem('id_user', 0);
                    localStorage.setItem('loggedin', 0);
                }
            },
            error: function (err) {
                console.log(err);
            }
        });
    }

    document.onload = isLogged();