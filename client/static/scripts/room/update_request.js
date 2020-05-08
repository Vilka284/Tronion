function update() {

    $.ajax({
        method: "POST",
        url: '/update_manage',
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({'id_user': localStorage.getItem('id_user')}),
        dataType: "json",
        headers: {"auth_token": localStorage.getItem('auth_token')},
        success: function (data) {
            $('#message').remove();
            var rooms = data.rooms;
            var iDiv = document.createElement('div');
            iDiv.id = 'message';
            iDiv.className = 'message';
            document.getElementsByTagName('body')[0].appendChild(iDiv);
            iDiv.innerHTML = `${data.message}`;

            for (var i = 0; i < rooms.length; i++) {
                var innerDiv = document.createElement('div');
                innerDiv.id = 'room-data';
                innerDiv.className = `room-data-${i}`;
                iDiv.appendChild(innerDiv);
                innerDiv.innerHTML = `${rooms[i]}`;
            }

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


}

$(document).on('submit', '#update-form', function(a){
    a.preventDefault();
    update();
});

document.onload = update();