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

## Installation

Install questionbox-donkey-team-questionbox-backend with the package manager [pip](https://pip.pypa.io/en/stable/):

```bash
  pip install questionbox-donkey-team-questionbox-backend
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

Start your server with:

```bash
 python manage.py runserver
```

## API Reference

#### API Root

```http
GET https://team-question-box.herokuapp.com
```

| Parameter  | Type     | Description                    |
| :--------- | :------- | :----------------------------- |
| `api_root` | `string` | The root entrypoint to the API |

#### Get All Questions

```http
GET https://team-question-box.herokuapp.com/questions/
```

| Parameter        | Type     | Description                            |
| :--------------- | :------- | :------------------------------------- |
| `pk`             | `int`    | The question pk                        |
| `user`           | `string` | Username                               |
| `question_title` | `string` | Title to the question                  |
| `question_field` | `string` | The question text                      |
| `date_created`   | `int`    | Date and time the question was created |

#### Submit A Question

```http
POST https://team-question-box.herokuapp.com/questions/
```

| Parameter        | Type     | Description              |
| :--------------- | :------- | :----------------------- |
| `question_title` | `string` | **Required**: User Login |
| `question_field` | `string` | The question text        |

#### Get All Answers By User - **Required**. User Login

```http
GET https://team-question-box.herokuapp.com/answers/
```

| Parameter       | Type     | Description                        |
| :-------------- | :------- | :--------------------------------- |
| `pk`            | `int`    | Answer PK                          |
| `user`          | `string` | Username who answered the question |
| ` question`     | `int`    | Question PK                        |
| `answer_field`  | `string` | Answer text                        |
| `date_answered` | `int`    | Date the answer was submitted      |

#### Submit An Answer - **Required**: User Login

```http
POST https://team-question-box.herokuapp.com/answers/
```

| Parameter      | Type     | Description                       |
| :------------- | :------- | :-------------------------------- |
| `question`     | `int`    | Question PK that will be answered |
| `answer_field` | `string` | The answer text                   |
