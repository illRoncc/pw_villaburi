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
    res.sendFile('C:/Users/ronca/Desktop/pw_villaburi/mappa_interattiva/mappa_open_street_map.html')
});

router.get("/lm", function (req, res) {
   res.sendFile('C:/Users/ronca/Desktop/pw_villaburi/mappa_interattiva/mappa_light_mode.html')
});

router.get("/dm", function (req, res) {
    res.sendFile('C:/Users/ronca/Desktop/pw_villaburi/mappa_interattiva/mappa_dark_mode.html')
});

router.get("/mm", function (req, res) {
    res.send('Mappa per manutenzione!')
});

app.listen(port, () => {
  console.log(`Connesso sulla porta ${port}`)
 });
