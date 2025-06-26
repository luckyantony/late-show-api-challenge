# SA-02: Phase 4 Code Challenge: Late Show API

A Flask RESTful API for managing a Late Night Show system with PostgreSQL and JWT-based authentication.

---

##  Learning Goals

* Build a Flask API backend
* Use PostgreSQL as the database
* Implement JWT-based authentication
* Provide route-based access control
* Work with 3+ models: `User`, `Episode`, `Guest`, `Appearance`

---

##  Requirements

* Python 3.8+
* PostgreSQL (installed and running)
* pipenv
* Postman account (optional for testing)

---

##  Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install Dependencies

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary python-dotenv
pipenv shell
```

### 3. Create Database

```sql
CREATE DATABASE late_show_db;
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```ini
DATABASE_URI=postgresql://postgres:luckyantony@localhost:5432/late_show_db
JWT_SECRET_KEY=supersecretkey
```

### 5. Run Migrations and Seed

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py
```

### 6. Start the Server

```bash
flask run
```

Visit: `http://127.0.0.1:5000/`

---

##  Auth Flow

### Register

```http
POST /register
Content-Type: application/json

{
  "username": "testuser",
  "password": "1234"
}
```

### Login

```http
POST /login
Content-Type: application/json

{
  "username": "testuser",
  "password": "1234"
}
```

Response:

```json
{
  "access_token": "your_jwt_token"
}
```

### Protected Routes

Use the JWT token returned from login:

```http
Authorization: Bearer your.jwt.token
```

---

## API Endpoints

| Endpoint         | Method | Auth Required | Description              |
| ---------------- | ------ | ------------- | ------------------------ |
| `/register`      | POST   | No            | Register user            |
| `/login`         | POST   | No            | Login user and get token |
| `/episodes`      | GET    | No            | Get all episodes         |
| `/episodes/<id>` | GET    | No            | Get episode with guests  |
| `/episodes/<id>` | DELETE | Yes           | Delete episode           |
| `/guests`        | GET    | No            | List all guests          |
| `/appearances`   | POST   | Yes           | Add appearance           |

---

## Data Models

* A `User` can register and log in.
* An `Episode` can have many `Guests` via `Appearances`.
* A `Guest` can appear in many `Episodes` via `Appearances`.
* An `Appearance` belongs to a `Guest` and an `Episode`.

### Validations

* `rating` must be between 1-10 in `Appearance`
* `username` and `password` required for `User`

---

##  Postman Testing

1. Open Postman.
2. Import the collection file `challenge-4-lateshow.postman_collection.json`.
3. Run:

   * `POST /register` to create user
   * `POST /login` to retrieve JWT token
   * Use token in header for:

     * `POST /appearances`
     * `DELETE /episodes/<id>`

---

##  Tech Stack

* Python
* Flask
* PostgreSQL
* SQLAlchemy
* Flask-Migrate
* Flask-JWT-Extended

---

##  Author

Built with 💻, ❤️ and ☕ by Luckyantony Leshan

---

##  License

ISC License
