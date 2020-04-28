 $(document).on('submit', '#login-form', function (e) {
        e.preventDefault();

        var email = $('#email').val();
        var pswd = $('#password').val();

        if (email != "" && pswd != "") {
            $.ajax({
                method: "POST",
                url: '/login_user',
                contentType: 'application/json; charset=UTF-8',
                data: JSON.stringify({'email': email, 'password': pswd}),
                dataType: "json",
                success: function (data) {
                    //Set token to current user
                    localStorage.setItem('auth_token', data.token);
                    localStorage.setItem('loggedin', 1);
                    //Say hi!
                    var user_name = data.user.first_name;

                    $('#msg').html(`<span style="color: green;">Hello, ${user_name} </br> In a few seconds you
                                    will be redirected to the main page</span> `);
                    //Redirect to main page
                    var timeout = 100;
                    setTimeout(function redirect() {location.replace('/')}, timeout);
                },
                statusCode: {
                    400: function () {
                        $('#msg').html('<span style="color: red;">Bad request - invalid credentials</span>');
                    }
                },
                error: function (err) {
                    console.log(err);
                }
            });

        } else {
            $('#msg').html('<span style="color: red;">All fields are required</span>');
        }
    });