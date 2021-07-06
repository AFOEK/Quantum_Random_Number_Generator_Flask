$(document).ready(function (){

    $(".btn_generate").click(function(j){
        j.preventDefault();
        var n = parseInt($("#iteration").val());
        var shots = parseInt($("#shots").val());
        var q = parseInt($("#qubit").val());
        var auto_iter = parseInt($("#auto_iter").val());
        var selected = $("input[name='radio_select']:checked").val();
        var datas = [
            {"iteration": n},
            {"shot": shots},
            {"qubit": q},
            {"auto_iter": auto_iter},
            {"option": selected}
        ];

        $.ajax({
            type: "POST",
            url:"/",
            data: JSON.stringify(datas),
            contentType: "application/json",
            dataType: 'json'
        });
    });

    $(".btn_clear").click(function(e){
        $("#txt_result").val("");
        $("#iteration").val("1");
        $("#shots").val("1024");
        $("#qubit").val("2");
        $("#auto_iter").val("100");
    });
});