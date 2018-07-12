$(function () {

    $("#playBtn").click(function () {
        console.log("Button Click")

        let url = $("#urlVal").val()
        let lang = $("#select_box").val()

        console.log("url is "+ url)
        console.log("lang is "+ lang)
        $.post('/abc', {
            url: url,
            lang: lang
        },function (response) {
            console.log(response);
        })
    })
    console.log("Loaded")

})