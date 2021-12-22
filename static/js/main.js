$(document).ready(function () {
    // jQuery.Event.prototype.preventDefault = (function () {
    //     var origin = jQuery.Event.prototype.preventDefault;
    //     return function () {
    //         if ($(this.target).hasClass('txt_area_result')) { return; }
    //         origin.call(this)
    //     }
    // }())
    if (window.location.pathname == "/") {
        const link = document.createElement('div');
        link.innerHTML = "Before start using this apps please read <a class='link' href='help'>Help</a>, if you already know what you doing just go ahead"
        swal({
            title: "Info",
            content: link,
            icon: "info",
            buttons: false,
            closeOnClickOutside: true,
            closeOnEsc: true,
            timer: 2000
        });
    }

    $(".btn_generate").click(function (e) {
        // e.preventDefault()
        // jQuery.Event.prototype.preventDefault = (function () {
        //     var origin = jQuery.Event.prototype.preventDefault;
        //     return function () {
        //         if ($(this.target).hasClass('txt_area_result')) { return; }
        //         origin.call(this)
        //     }
        // }())
        $.ajax({
            type: "POST",
            url: "/",
            async: true,
            timeout: 70000,
            data: $('form').serialize(),
            success: function () {
                console.log("OK");
            },
            error: function () {
                console.log("NOT OK! [err_btn_generate]");
            }
        });
    });

    $(".btn_clear").click(function () {
        $("#txt_result").val("");
        $("#iteration").val("5");
        $("#shots").val("1024");
        $("#qubit").val("2");
        $("#auto_iter").val("100");
        $("#radio_all").prop("checked", true).trigger("click");
        $("#radio_bar").prop("checked", true).trigger("click");
        swal({
            title: "Clear",
            icon: "info",
            buttons: false,
            closeOnClickOutside: true,
            closeOnEsc: true,
            timer: 1000
        });
    });

    $(".btn_auto_gen_stat").click(function () {
        $.ajax({
            type: "POST",
            url: "/stat",
            async: true,
            timeout: 70000,
            data: $('form').serialize(),
            success: function () {
                console.log("OK");
            },
            error: function () {
                console.log("NOT OK! [err_btn_auto_gen_stat]");
            }
        });
        window.open('stat', '_blank');
    });

    $(".btn_auto_gen").click(function () {
        const contents = document.createElement('div');
        contents.innerHTML = "Succesfully to generate data"
        $.ajax({
            type: "POST",
            url: "/auto_gen",
            async: true,
            timeout: 70000,
            data: $('form').serialize(),
            success: function () {
                console.log("OK");
                swal({
                    title: "Success",
                    content: contents,
                    icon: "info",
                    buttons: false,
                    closeOnClickOutside: true,
                    closeOnEsc: true,
                    timer: 1500
                });
            },
            error: function () {
                console.log("NOT OK! [err_btn_auto_gen]");
            }
        });
    });
});