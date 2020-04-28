$('#logout').on('submit', function e() {
        e.preventDefault();

        $ajax({
            url: '/logout',
            dataType: 'json',
            success: function (data) {
                localStorage.setItem('loggedin', 0);

                document.getElementById("signin").style.visibility = "visible";
                document.getElementById("signup").style.visibility = "visible";
                document.getElementById("or").style.visibility = "visible";
                document.getElementById("profile").style.display = "none";
                document.getElementById("manage").style.display = "none";
                document.getElementById("join").style.display = "none";
            }

        })
    });