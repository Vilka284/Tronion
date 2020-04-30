$(document).on('submit', '#reg-form', function (e) {
        e.preventDefault();
        csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
        //формуємо js обєкт info витягуючи з полів значення
        info = {
            //username: 'danylo567222222',
            //email: 'danylo51202@gmail.com',
            //password: '123',
            //repeated_password: '123',
            //username: $('#username').val(),
            first_name: $('#first_name').val(),
            last_name: $('#last_name').val(),
            email: $('#email').val(),
            password: $('#password').val(),

        }
        // if any errors, it can be here because я скопіпастив той код єбу як працює але то то шо треба(ajaxSetup).
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken",
                        csrfmiddlewaretoken)
                }
            }
        });

        $.ajax({
            type: 'POST',
            url: '/register',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            data: JSON.stringify(info),

            success: function () {
                //Redirect to main page
                var timeout = 100;
                setTimeout(function redirect() {location.replace('/login')}, timeout);
            }

        });
    });