$(document).ready(function (){

    $(".btn_generate").click(function(j){
        var n = parseInt($("#iteration").val());
        var shots = parseInt($("#shots").val());
        var q = parseInt($("#qubit").val());
        var auto_iter = parseInt($("#auto_iter").val());
        var selected = $("input[name='radio_select']:checked").val();

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
});