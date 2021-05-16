# express.js tutorials

## Usage

```
$ npm install 
```

## Contents

- user_list.js: Basic API Server example with express.js

## user_list.js

### Run server

```
$ node user_list.js
```

### Request examples

- GET Root

```
$ curl -X GET "localhost:3000/"
```

- GET /users/ : Get user list

```
$ curl -X GET "localhost:3000/users"
```

- GET /users/ : Get user list (maximum 1)

```
$ curl -X GET "localhost:3000/users?limit=1"
```

- GET /users/:id : Get user information with certain id

```
$ curl -X GET "localhost:3000/users/1"
```

- DELETE users/:id : Delete user information from userList with certain id

```
$ curl -X DELETE "localhost:3000/users/1"
```

- POST users/:id : Create new user

```
$ curl -d "name=new_user" http://localhost:3000/users
(Result) [{"id":1,"name":"user1"},{"id":2,"name":"user2"},{"id":3,"name":"user3"},{"id":1620444233798,"name":"new_user"}]
```

- PUT users/:id : Update certain user information(name)

```
$ curl -d "name=update_user" -X PUT http://localhost:3000/users/1
(Result) [{"id":1,"name":"update_user"},{"id":2,"name":"user2"},{"id":3,"name":"user3"}]
```

