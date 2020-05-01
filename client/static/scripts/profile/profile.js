function build_profile() {
    var isLoggedIn = localStorage.getItem('loggedin');

    if (isLoggedIn == 1) {
        $.ajax({
            method: "POST",
            url: '/build_profile',
            contentType: 'application/json; charset=UTF-8',
            data: JSON.stringify({'id_user': localStorage.getItem('id_user')}),
            dataType: "json",
            headers: {"auth_token": localStorage.getItem('auth_token')},
            success: function (data) {
                console.log(data);
            },
            statusCode: {
                400: function () {

                }
            },
            error: function (err) {
                console.log(err);
            }
        });

    } else {
        location.replace('/login');
    }

}

document.onload = build_profile();