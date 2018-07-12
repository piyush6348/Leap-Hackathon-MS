$(function () {

    $("#playBtn").click(function () {
        console.log("Button Click")
        $.post('/abc', {
            url: "Some Url"
        },function (response) {
            console.log("Response got "+ response);
        })
    })
    console.log("Loaded")

})