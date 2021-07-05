$(document).ready(function (){
    $("#shots").change(function(){
        var temp = parseInt($("#shots").val());
        var result = temp*2-1;
        $("#shots").attr("step", result);
    });
    
    $(".btn_generate").click(function(){
        
    });
});