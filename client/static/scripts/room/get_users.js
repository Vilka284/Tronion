// get users in current room
function get_users() {

    var code = window.location.href.split('#')[0].split('/');
    code = code[code.length - 1];
    $.ajax({
            method: "POST",
            url: '/get_users',
            contentType: 'application/json; charset=UTF-8',
            data: JSON.stringify({
                'id_user': localStorage.getItem('id_user'),
                'code': code,
            }),
            dataType: "json",
            headers: {"auth_token": localStorage.getItem('auth_token')},
            success: function (data) {
                console.log(data);
            },
            statusCode: {
                400: function (data) {
                    console.log(data);
                }
            },
            error: function (err) {
                console.log(err);
            }
    });
}

document.onload = get_users();