var express = require('express')
var app = express()

app.get('/', function (req, res) {
  res.send('hello world!!!')
})

var host = "0.0.0.0"
var port = 3000

app.listen(3000)
console.log(`Running on http://${host}:${port}`)
