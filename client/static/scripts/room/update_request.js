$(document).on('update', '#room-form', function (a) {
    a.preventDefault();


    $.ajax({
        method: "GET",
        url: '/create_room',
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({'id_user': localStorage.getItem('id_user')}),
        dataType: "json",
        headers: {"auth_token": localStorage.getItem('auth_token')},
        success: function (data) {
            alert(data);
        },
        statusCode: {
            400: function () {
                $('#msg').html('<span style="color: red;">Bad request parameters</span>');
            }
        },
        error: function (err) {
            console.log(err);
        }
    });


});