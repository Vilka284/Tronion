$(document).on('submit', '#join-form', function (e) {
    e.preventDefault();

    var code = $('#join').val();

    if (code != "" && code.length == 5) {

        $.ajax({
            method: "POST",
            url: '/join_room',
            contentType: 'application/json; charset=UTF-8',
            data: JSON.stringify({'code': code}),
            dataType: "json",
            headers: {"auth_token": localStorage.getItem('auth_token')},
            success: function (data) {
                var room_code = data.room_data[0];
                var room_name = data.room_data[1];
                $('#msg').html(`<span style="color: green;">Success! Room exists</br>In a few seconds you will be ` +
                    `conected to the room <b>${room_name}</b></span>`);
                //Redirect to room
                var timeout = 100;
                setTimeout(function redirect() {
                    location.replace(`/room/${room_code}`)
                }, timeout);
                //Set user state
                localStorage.setItem('user_in_room', room_code);
            },
            statusCode: {
                400: function (data) {
                    $('#msg').html('<span style="color: red;">Bad request</span>');
                    if (data.message == 'token expired' || 'Invalid token, please try again'){
                        localStorage.setItem('auth_token', 0);
                        location.replace('/login');
                    }
                },
                404: function () {
                    $('#msg').html('<span style="color: red;">There is no room with this code</span>');
                }
            },
            error: function (err) {
                console.log(err);
            }
        });

    } else {
        $('#msg').html('<span style="color: red;">Input room code!</span>');
    }
});