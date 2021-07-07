$(document).ready(function (){

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

    $(".btn_auto_gen_stat").click(function(){
        window.open('stat','_blank')
    });
});