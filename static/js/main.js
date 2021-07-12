$(document).ready(function (){

    swal({
        title: "Info",
        text: "Before start using this apps please read Help, if you already know what you doing just go ahead",
        icon: "info",
        buttons: false,
        closeOnClickOutside: true,
        closeOnEsc: true,
        timer: 2500
    });
    
    $(".btn_generate").click(function(j){
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
        //j.preventDefault();
    });

    $(".btn_clear").click(function(e){
        $("#txt_result").val("");
        $("#iteration").val("1");
        $("#shots").val("1024");
        $("#qubit").val("2");
        $("#auto_iter").val("100");
    });

    $(".btn_auto_gen_stat").click(function(j){
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

    $(".btn_auto_gen").click(function(j){
        $.ajax({
            type: "POST",
            url:"/auto_gen",
            data: $('form').serialize(),
            success: function(){
                console.log("OK");
            },
            error: function(){
                console.log("OK");
            }
        });
        //j.preventDefault();
    });
});