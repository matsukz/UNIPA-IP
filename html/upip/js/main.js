$(document).ready(function(){

    var url = new URL(window.location.href);
    var host = url.hostname;

    document.getElementById("gettime").innerText = new Date().toLocaleString({ timeZone: 'Asia/Tokyo' });

    start_button = document.getElementById("btn_start");

    $.ajax({
        type: "GET",
        url: "http://" + host + "/upip/api/classroom",
        contentType: "application/json",
        cache: false
    }).done(function(response){
        change_status("ip",response.client_ip);
        change_status("classroom",response.classroom);
    }).fail(function(response_status){
    })

    function change_status(id,msg){
        document.getElementById(id).innerText = msg;
    }

})