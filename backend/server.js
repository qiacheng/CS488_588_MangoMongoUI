const mongo = require('mongodb');
const express = require('express');
let {PythonShell} = require('python-shell');
var cors = require('cors');
const API_PORT = 3001;
const router = express.Router();
const app = express();
app.use(cors());
const MongoClient = mongo.MongoClient;
const url = 'mongodb://34.69.61.31:27017';
var q1 = "Loading";
var result = "";
console.log(__dirname);
MongoClient.connect(url, { useNewUrlParser: true }, (err, client) => {
    if (err) throw err;
    const db = client.db("project").collection("detectors");
    db.findOne({}, function(err, res){
        console.log(res);
        result = res;
        client.close();
    })
});

app.get('/', (req, res) => {
    res.setHeader('Content-Type', 'text/plain')
    res.send('Welcome To Our Mango Mong DB');
    //res.end(JSON.stringify(result));
})

router.get('/getData', function(req,res){
    data = result;
    return res.json({success: true, data: data});
})


router.get('/Query/:id', function(req,res){
    var id = req.params.id;
    var pyshell = new PythonShell(`./queries/query${id}.py`);
    var answer = "";
    pyshell.on('message', function(message){
        console.log(message);
        answer += message + "\n"
    })
    pyshell.end(function(err){
        if(err) throw (err)
        var jsdata =
        {
            scriptPrints: ""
        }
        jsdata.scriptPrints = answer;
        return res.json({success: true, data: jsdata});
    })
})




app.use('/api', router);

app.listen(API_PORT, () => console.log(`listening to port ${API_PORT}`));