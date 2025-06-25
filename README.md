# Late Show API

A Flask REST API for managing a Late Night Show system.

---

##  Setup Instructions

### 1. Install Dependencies

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary python-dotenv
pipenv shell
```

---

### 2. Set Up PostgreSQL Database

Create your database:

```sql
CREATE DATABASE late_show_db;
```

---

### 3. Create `.env` File

Create a `.env` file at the root (same level as `server/`) and add:

```ini
DATABASE_URI=postgresql://postgres:yourpassword@localhost:5432/late_show_db
JWT_SECRET_KEY=your_jwt_secret_key
```

Replace `yourpassword` and `your_jwt_secret_key` with actual values.

---

### 4. Initialize and Migrate DB

```bash
export FLASK_APP=server/app.py

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

python server/seed.py
```

---

##  Auth Flow

### 1. Register

```http
POST /register
Content-Type: application/json

{
  "username": "admin",
  "password": "password123"
}
```

---

### 2. Login

```http
POST /login
Content-Type: application/json

{
  "username": "admin",
  "password": "password123"
}
```

Response:

```json
{
  "access_token": "your_jwt_token"
}
```

---

### 3. Using the Token

Add this header to **protected routes**:

```http
Authorization: Bearer <your_token_here>
```

---

## 📡 API Endpoints

| Endpoint               | Method | Auth Required | Description                 |
|------------------------|--------|----------------|-----------------------------|
| `/register`            | POST   |     No        | Register new user           |
| `/login`               | POST   |     No          | Login + get token           |
| `/episodes`            | GET    |     No         | List all episodes           |
| `/episodes/<id>`       | GET    |     No         | Get one episode with guests |
| `/episodes/<id>`       | DELETE |     Yes         | Delete episode              |
| `/guests`              | GET    |     No         | List all guests             |
| `/appearances`         | POST   |     Yes         | Add new appearance          |

---

##  Postman Testing

1. Open Postman.
2. Import the `challenge-4-lateshow.postman_collection.json` file.
3. Test all routes:
   - `/register` → Create user
   - `/login` → Get token
   - Use `Bearer <token>` for:
     - `POST /appearances`
     - `DELETE /episodes/<id>`

---

##  Tech Stack

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended

---

Built with 💻, ❤️ and ☕ by Luckyantony Leshan
