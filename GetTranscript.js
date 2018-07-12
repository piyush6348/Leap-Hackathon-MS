const express = require('express')
const path = require('path')
const pythonShell = require('python-shell');
var app = express()
var bodyParser = require('body-parser')

const scriptOne = "C:\\Users\\Administrator\\Desktop\\Hackathon project\\scriptByRishabh.py"
var arg1 = "Piyush"
var arg2 = "Gupta"

app.use('/',express.static(path.join(__dirname,'public_static')))

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
    extended: true
}));

app.post('/abc',function (req,res) {
    console.log("Server hit")

    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('C:\\Python\\python',[scriptOne, arg1, arg2]);

    pythonProcess.stdout.on('data',(data)=>{
        console.log("Data from python file "+ data)
        res.send(data)
    })
})


app.listen(8000,function () {
    console.log("Server started at port http://localhost:8000");
});