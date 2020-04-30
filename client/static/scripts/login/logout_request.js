 $(document).on('submit', '#logout-form', function (e) {
        e.preventDefault();

        $.ajax({
            method: "GET",
            url: '/logout_user',
            dataType: 'json',
            success: function (data) {
                localStorage.setItem('loggedin', 0);
                localStorage.setItem('auth_token', 0);

                //Redirect to main page
                var timeout = 100;
                setTimeout(function redirect() {location.replace('/')}, timeout);
            },
            error: function (err) {
                    console.log(err);
            }

        })
    });