$(document).on('submit', '#room-form', function (e) {
    e.preventDefault();

    var name = $('#name').val();
    var description = $('#description').val();

    if (name != "" && description != "") {

        $.ajax({
            method: "POST",
            url: '/create_room',
            contentType: 'application/json; charset=UTF-8',
            data: JSON.stringify({
                'name': name,
                'description': description,
                'id_user': localStorage.getItem('id_user')
            }),
            dataType: "json",
            headers: {"auth_token": localStorage.getItem('auth_token')},
            success: function (data) {
                $('#msg').html('<span style="color: green;">Room created successfully</span>');
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

    } else {
        $('#msg').html('<span style="color: red;">All fields are required</span>');
    }

});