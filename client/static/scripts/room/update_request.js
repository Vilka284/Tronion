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
            $('#header1').remove();
            var rooms = data.rooms;
            var Header = document.createElement('h1');
            var text = document.createTextNode(data.message);
            // add text to header
            Header.appendChild(text);
            Header.id = 'header1';
            Header.className = 'header1';
            var iDiv = document.createElement('div');
            iDiv.id = 'message';
            iDiv.className = 'message';
            iDiv.style = 'display: grid;\n' +
                '  font-family: Coda;\n' +
                '  grid-column-gap: 30px;\n' +
                '  grid-template-columns: auto auto auto;\n' +
                '  background-color: #dfe3f3;\n' +
                '  padding: 10px;';
            //Add main div and header
            document.getElementsByTagName('body')[0].appendChild(Header);
            document.getElementsByTagName('body')[0].appendChild(iDiv);


            //Dynamic create room data elements
            for (let room = 0; room < rooms.length; room++) {
                for (let element = 0; element < 3; element++) {
                    var innerDiv = document.createElement('div');
                    var info = null;
                    var code = rooms[room][0];
                    switch (element) {
                        case 0:
                            info = `<a href="/room/${code}"> ${code} </a>`;
                            break;
                        case 1:
                            info = rooms[room][element] + ' : ' + rooms[room][element + 1];
                            break;
                        case 2:
                            info = `<a href="/manage/${code}">Manage this room </a>`;
                            break;
                        default:
                            break;
                    }
                    innerDiv.id = `room-data-${room}-${element}`;
                    innerDiv.className = 'room-data';
                    innerDiv.style = 'background-color: rgba(255, 255, 255, 0.8);\n' +
                        '  border: 1px solid rgba(0, 0, 0, 0.8);\n' +
                        '  font-family: Coda;\n' +
                        '  padding: 15px;\n' +
                        '  font-size: 20px;\n' +
                        '  text-align: center;';
                    iDiv.appendChild(innerDiv);
                    innerDiv.innerHTML = info;
                }
            }

        },
        statusCode: {
            400: function (data) {
                $('#msg').html('<span style="color: red;">Bad request parameters</span>');
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

$(document).on('submit', '#room-form', function(a){
    a.preventDefault();
    update();
});

document.onload = update();