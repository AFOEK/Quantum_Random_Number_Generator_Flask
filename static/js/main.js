$(document).ready(function (){
    if(window.location.pathname == "/"){
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
    
    $(".btn_generate").click(function(){
        $.ajax({
            type: "POST",
            url:"/",
            data: $('form').serialize(),
            success: function(){
                console.log("OK");
            },
            error: function(){
                console.log("OK");
            }
        });
    });

    $(".btn_clear").click(function(){
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

    $(".btn_auto_gen_stat").click(function(){
        $.ajax({
            type: "POST",
            url:"/stat",
            data: $('form').serialize(),
            success: function(){
                console.log("OK");
            },
            error: function(){
                console.log("OK");
            }
        });
        window.open('stat','_blank');
    });

    $(".btn_auto_gen").click(function(){
        const contents = document.createElement('div');
        contents.innerHTML = "Succesfully to generate date"
        $.ajax({
            type: "POST",
            url:"/auto_gen",
            data: $('form').serialize(),
            success: function(){
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
            error: function(){
                console.log("OK");
            }
        });
    });
});