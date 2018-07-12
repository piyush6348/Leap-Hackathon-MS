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
            //console.log(response);
            response = JSON.parse(response)
            let captions = response['captions']
            let translation = response['translation']
            let meaning = response['meaning']
            let keywords = response['keywords']
            console.log("captions "+ captions)
            console.log("translation "+ translation)
            console.log("meaning "+ meaning)
            console.log("keywords "+ keywords)
        })
    })
    console.log("Loaded")

})