const express = require('express')
//const mysql = require('mysql2'); 
const app = express()
const router = express.Router();
const bodyParser = require('body-parser');
const port = 3000

app.use(bodyParser.urlencoded({ extended: true }));
app.use(router);
app.use(bodyParser.json());

router.get("/", function (req, res) {
    res.sendFile('D:/ITS/ITS/PWconNodejs/file2.html')
});

router.get("/lm", function (req, res) {
   res.sendFile('D:/ITS/ITS/PWconNodejs/file3.html')
});

router.get("/dm", function (req, res) {
    res.sendFile('D:/ITS/ITS/PWconNodejs/file.html')
});

router.get("/mm", function (req, res) {
    res.send('Mappa per manutenzione!')
});

app.listen(port, () => {
  console.log(`Connesso sulla porta ${port}`)
 });
