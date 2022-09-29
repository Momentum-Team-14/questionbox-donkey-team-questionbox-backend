# The Question Box

The question box is the backend code for a question and answer app.

## Features

- An authenticated user can create a question.
- An authenticated user can create an answer to a question
- Unauthenticated users can view all questions and answers.
- Question Box uses a registration and token-based authentication.
- A user can get a list of all the questions they have posted.
- A user can get a list of all the answers they have posted.
- The original author of the question can mark an answer as accepted.
- Authenticated users can favorite questions or answers they like and unfavorite as well.
- A question can be deleted by its author, whether answered or unanswered.
- Users can search the text of a question.

## Run Locally

Clone the project

```bash
  git clone https://github.com/Momentum-Team-14/questionbox-donkey-team-questionbox-backend
```

Go to the project directory

```bash
  cd questionbox-donkey-team-questionbox-backend
```

Run your virtual enviroment with:

```bash
   pipenv shell
```

(If running for the first time) migrate with:

```bash
   python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```

## API Reference

#### API Root

```http
GET https://team-question-box.herokuapp.com
```

| Body       | Type     | Description                    |
| :--------- | :------- | :----------------------------- |
| `api_root` | `string` | The root entrypoint to the API |

---

#### New User Create

```http
POST - https://team-question-box.herokuapp.com/auth/users/
```

| Body       | Type     | Description             |
| :--------- | :------- | :---------------------- |
| `username` | `string` | New Username            |
| `password` | `string` | User generated password |
| `email`    | `string` | User generated email    |

Request Sample:

```
POST /auth/users/
Content-Type: json
Authorization: N/A
Host: team-question-box.herokuapp.com

{
	"username": "TestUserLogin" ,
	"password": "TestUserPassword",
	"email": "testemail@fake.com"
}
```

Response Example (201 Created)

```
{
	"email": "testemail@fake.com",
	"username": "TestUserLogin",
	"id": 4
}
```

---

#### Token Authentication

```http
POST - https://team-question-box.herokuapp.com/auth/token/login/
```

| Body       | Type     | Description             |
| :--------- | :------- | :---------------------- |
| `username` | `string` | New Username            |
| `password` | `string` | User generated password |

Request Sample:

```
POST /auth/token/login/
Content-Type: json
Authorization: N/A
Host: team-question-box.herokuapp.com

{
	"username": "TestUserLogin" ,
	"password": "TestUserPassword",
}
```

Response Example (200 OK)

```
{
	"auth_token": "****************************************"
}

```

---

#### User Login

```http
POST - https://team-question-box.herokuapp.com/auth/token/login/
```

| Body       | Type     | Description             |
| :--------- | :------- | :---------------------- |
| `username` | `string` | New Username            |
| `password` | `string` | User generated password |

Request Sample:

```
POST /auth/token/login/
Content-Type: json
Authorization:
Host: team-question-box.herokuapp.com

{
	"username": "TestUserLogin" ,
	"password": "TestUserPassword",
}
```

Response Example (200 OK)

```
{
	"auth_token": "****************************************"
}

```

---

#### User Logout **Required**

```http
POST - https://team-question-box.herokuapp.com/auth/token/logout/
```

| Body       | Type     | Description             |
| :--------- | :------- | :---------------------- |
| `username` | `string` | New Username            |
| `password` | `string` | User generated password |

Request Sample:

```
POST /auth/token/logout/
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	"username": "TestUserLogin" ,
	"password": "TestUserPassword",
}
```

Response Example (204 No Content)

```
No body returned for response

```

#### Get All Questions

```http
GET - https://team-question-box.herokuapp.com/questions/
```

| Body             | Type     | Description                            |
| :--------------- | :------- | :------------------------------------- |
| `pk`             | `int`    | The question pk                        |
| `user`           | `string` | Username                               |
| `question_title` | `string` | Title to the question                  |
| `question_field` | `string` | The question text                      |
| `date_created`   | `int`    | Date and time the question was created |

Answer [
| Body | Type | Description |
| :-------- | :------- | :-------------------------------- |
| `pk` | `int` | The answer pk |
| `user` | `string` | Username |
| `question` | `int` | Question pk |
| `answer_field` | `string` | The answer text |
| `date_answered` | `int` | Date and time the answer was submitted |
| `accepted` | `Boolean` | Accepted answer boolean field |

]

Request Sample:

```
GET /questions/
Content-Type: json
Authorization: N/A
Host: team-question-box.herokuapp.com

{
    ""
}
```

Response Example (200 OK)

```
{
		"pk": 3,
		"user": "Groot",
		"question_title": "Test Question 3",
		"question_field": "Test 3",
		"date_created": "2022-09-22T19:00:39.014337Z",
		"answers": [
			{
				"pk": 1,
				"user": "Groot",
				"question": 3,
				"answer_field": "Test",
				"date_answered": "2022-09-22T21:57:19.267262Z",
				"accepted": false
			}
		]
	},
```

---

#### Search All Questions

```http
GET - https://team-question-box.herokuapp.com/questions/?search=
```

| Body             | Type     | Description                            |
| :--------------- | :------- | :------------------------------------- |
| `pk`             | `int`    | The question pk                        |
| `user`           | `string` | Username                               |
| `question_title` | `string` | Title to the question                  |
| `question_field` | `string` | The question text                      |
| `date_created`   | `int`    | Date and time the question was created |

Answer [
| Body | Type | Description |
| :-------- | :------- | :-------------------------------- |
| `pk` | `int` | The answer pk |
| `user` | `string` | Username |
| `question` | `int` | Question pk |
| `answer_field` | `string` | The answer text |
| `date_answered` | `int` | Date and time the answer was submitted |
| `accepted` | `Boolean` | Accepted answer boolean field |

]

Request Sample:

```
GET /questions/?search=
Content-Type: json
Authorization: N/A
Host: team-question-box.herokuapp.com

{
    ""
}
```

Response Example (200 OK)

```
{
		"pk": 3,
		"user": "Groot",
		"question_title": "Test Question 3",
		"question_field": "Test 3",
		"date_created": "2022-09-22T19:00:39.014337Z",
		"answers": [
			{
				"pk": 1,
				"user": "Groot",
				"question": 3,
				"answer_field": "Test",
				"date_answered": "2022-09-22T21:57:19.267262Z",
				"accepted": false
			}
		]
	},
```

---

#### Submit A Question - User Authentication **Required**

```http
POST - https://team-question-box.herokuapp.com/questions/
```

| Body             | Type     | Description        |
| :--------------- | :------- | :----------------- |
| `question_title` | `string` | The question title |
| `question_field` | `string` | The question text  |

Request Sample:

```
POST /questions/
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	"question_title": "Test 1",
	"question_field": "Test"
}
```

Response Example (201 Created)

```
{
	"pk": 16,
	"user": "TestUser2",
	"question_title": "Test Question 1",
	"question_field": "Test ",
	"date_created": "1991-1-20T02:02:11.587060Z",
	"answers": []
}
```

---

#### Delete Question - User Authentication **Required**

Note: Will delete all associated answers

```http
DELETE - https://team-question-box.herokuapp.com/questions/{question_pk}
```

| Body | Type | Description |
| :--- | :--- | :---------- |
| ""   | ""   | ""          |

Request Sample:

```
DELETE /questions/{question_pk}
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	""
}
```

Response Example (204 No Content)

```
{
	"No body returned for response"
}
```

---

#### Submit An Answer - User Authentication **Required**

```http
POST https://team-question-box.herokuapp.com/answers/
```

| Body           | Type     | Description                       |
| :------------- | :------- | :-------------------------------- |
| `question`     | `int`    | Question PK that will be answered |
| `answer_field` | `string` | The answer text                   |

Request Sample:

```
POST /answers/
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	"question": 1,
	"answer_field": "Answer text"
}
```

Response Example (201 Created)

```
{
	"pk": 5,
	"user": "TestUser",
	"question": 1,
	"answer_field": "Answer text",
	"date_answered": "1991-1-20T02:02:11.587060Z",
	"accepted": false
}
```

---

#### Submit An Answer - User Authentication **Required**

```http
POST https://team-question-box.herokuapp.com/user/answers/
```

| Body           | Type     | Description                       |
| :------------- | :------- | :-------------------------------- |
| `question`     | `int`    | Question PK that will be answered |
| `answer_field` | `string` | The answer text                   |

Request Sample:

```
POST user/answers/
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	"question": 1,
	"answer_field": "Answer text"
}
```

Response Example (201 Created)

```
{
	"pk": 5,
	"user": "TestUser",
	"question": 1,
	"answer_field": "Answer text",
	"date_answered": "1991-1-20T02:02:11.587060Z",
	"accepted": false
}
```

---

#### Favorite a Quesiton - User Authentication **Required**

```http
POST https://team-question-box.herokuapp.com/favorites/
```

| Body       | Type  | Description                        |
| :--------- | :---- | :--------------------------------- |
| `question` | `int` | Question PK that will be favorited |

Request Sample:

```
POST /favorites/
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	"question": 1
}
```

Response Example (201 Created)

```
{
	"pk": 5,
	"user": "TestUser",
	"question": 1
}
```

---

#### List of Questions by User - User Authentication **Required**

```http
GET https://team-question-box.herokuapp.com/user/questions/
```

| Body | Type | Description |
| :--- | :--- | :---------- |
| `""` | `""` | ""          |

Request Sample:

```
GET /user/questions/
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	""
}
```

Response Example (200 OK)

```
{
    "pk": 1,
	"user": "TestUser",
	"question_title": "Test Question 1",
	"question_field": "Test Question Field 1",
	"date_created": "1999-12-31T23:59:59.430665Z",
	"answers": []
},
{
	"pk": 2,
	"user": "TestUser",
	"question_title": "Test Question 2",
	"question_field": "Test Question Field 2",
	"date_created": "1999-12-31T23:59:59.430665Z",
	"answers": []
},
{
	"pk": 3,
	"user": "TestUser",
	"question_title": "Test Question 3",
	"question_field": "Test Question Field 3",
	"date_created": "1999-12-31T23:59:59.430665Z",
	"answers": []
},
```

---

#### List of Answers by User - User Authentication **Required**

```http
GET https://team-question-box.herokuapp.com/user/answers/
```

| Body | Type | Description |
| :--- | :--- | :---------- |
| `""` | `""` | ""          |

Request Sample:

```
GET /user/answers/
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	""
}
```

Response Example (200 OK)

```
{
	"pk": 6,
	"user": "TestUser",
	"question": 1,
	"answer_field": "Testing question 1 with JSON",
	"date_answered": "1999-12-31T23:59:59.430665Z",
	"accepted": false
}
{
	"pk": 7,
	"user": "TestUser",
	"question": 2,
	"answer_field": "Testing question 2 with JSON",
	"date_answered": "1999-12-31T23:59:59.430665Z",
	"accepted": true
},
{
	"pk": 8,
	"user": "TestUser",
	"question": 3,
	"answer_field": "Testing question 3 with JSON",
	"date_answered": "1999-12-31T23:59:59.430665Z",
	"accepted": false
},
```

---

#### List of Favorite Questions by User - User Authentication **Required**

```http
GET https://team-question-box.herokuapp.com/user/favorites/
```

| Body | Type | Description |
| :--- | :--- | :---------- |
| `""` | `""` | ""          |

Request Sample:

```
GET user/favorites/
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	""
}
```

Response Example (200 OK)

```
[
	{
		"pk": 1,
		"user": "TestUser",
		"question": 4
	},
	{
		"pk": 2,
		"user": "TestUser",
		"question": 7
	},
	{
		"pk": 3,
		"user": "TestUser",
		"question": 8
	}
]
```

---

#### Accept an Answer - User Authentication **Required**

```http
PATCH https://team-question-box.herokuapp.com/answers/{answer_pk}/accept
```

| Body | Type | Description |
| :--- | :--- | :---------- |
| `""` | `""` | ""          |

Request Sample:

```
PATCH /answers/{answer_pk}/accept
Content-Type: json
Authorization: Required
Host: team-question-box.herokuapp.com

{
	""
}
```

Response Example (200 OK)

```
{
	"pk": 8,
	"user": "TestUser",
	"question": 10,
	"answer_field": "Testing question 10",
	"date_answered": "1999-12-31T23:59:59.430665Z",
	"accepted": true
}
```
