const express = require('express')
// body-parser: nodejs body parsing middleware
// https://github.com/expressjs/body-parser
const bodyParser = require("body-parser")

// Create express application
// http://expressjs.com/ko/api.html#express
const app = express()
const port = 3000

// Dummy Data
var userList = [
    {id: 1, name: "user1"},
    {id: 2, name: "user2"},
    {id: 3, name: "user3"},
]

// expressjs docs recommend using it to use req.body
// http://expressjs.com/ko/api.html#req.body
app.use(bodyParser.json());  // for parsing application/json
app.use(express.urlencoded({ extended: true }))  // for parsing application/x-www-form-urlencoded

// GET -> Root
app.get('/', (req, res) => {
        // res.set(): set the response content-type at header
        res.set('Content-Type', 'text/html')
        // res.send(): response with body
        //http://expressjs.com/ko/api.html#res.send
        res.send("This is ROOT\n");
})

// GET -> users : Get user list
app.get('/users/', (req, res) => {
        // req.query parameter: parse the query string from url
        // query string example(set req.query.limit as 1)
        // -> $ curl -X GET "localhost:3000/users?limit=1"
        // http://expressjs.com/en/5x/api.html#req.query
        req.query.limit = req.query.limit || 10;

        const limit = parseInt(req.query.limit, 10);

        if (Number.isNaN(limit)) {
                // res.end(): quickly end the response without any data
                // http://expressjs.com/ko/api.html#res.end
                return res.status(400).end();
        }
        // res.json(): response with json data
        // http://expressjs.com/ko/api.html#res.json
        // - setting Content-Type as 'application/json'
        // - call res.send(body)
        res.json(userList.slice(0, limit));
})

// GET -> users/:id : Get user information with certain id
app.get("/users/:id", (req, res)=> {
        const id = parseInt(req.params.id, 10);
        
        if (Number.isNaN(id)){
            return res.status(400).end();
        }

        const user = userList.filter((usr)=>{
            return usr.id === id
        })[0];
        
        if (!user){
            return res.status(404).end()
        }

        res.json(user);
})

// DELETE -> users/:id : Delete user information from userList with certain id
app.delete("/users/:id", (req, res) => {
        const id = parseInt(req.params.id, 10);
        
        if (Number.isNaN(id)) {
            return res.status(400).end()
        }

        // Create new users array and replace it as users
        userList = userList.filter(user => user.id !== id);
        res.status(204).end()
})

// POST -> users : Create new user information
app.post("/users", (req, res) => {
        const name = req.body.name;  //with middleware body-parser
        
        if (!name) return res.status(400).end();

        if (userList.filter(user => user.name == name).length) {
                return res.status(409).end()
        }
        
        const id = Date.now();
        const user = {id, name};
        userList.push(user);
        res.status(201).json(user);
})

// PUT -> users/:id : Update certain user information(name)
app.put("/users/:id", (req, res)=>{
        const id = parseInt(req.params.id, 10);
        const name = req.body.name;
        const user = userList.filter(usr => { 
                return usr.id === id
        })[0];
        user.name = name

        res.json(user)
})

// app.listen(): Start a UNIX socket and listens from connections.
// http://expressjs.com/ko/api.html#app.listen_path_callback
app.listen(port, () => {
          console.log(`Example app listening at http://localhost:${port}`)
})

module.exports = app;
