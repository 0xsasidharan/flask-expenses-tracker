
# ✅ Expense Tracker Flask API

A simple and extendable RESTful API for managing personal expenses, built with **Python Flask**.
This API allows users to create, update, delete, and view expenses with basic field validation.
It uses **pure Flask**, in-memory data storage (`expenses` dict), and standard RESTful patterns.

---

## 📝 Features

* Full CRUD for Expenses
* Track expenses with amount, category, and description
* Validation for required fields and allowed keys
* RESTful structure using route parameters
* Easy to extend with Flask-Smorest, Marshmallow, or SQLAlchemy later

---

## 🚧 Project Progress Checklist

| Day | Feature                                | Status    |
| --- | -------------------------------------- | --------- |
| 1   | Basic Flask App with GET, POST, DELETE | ✅ Done    |
| 2   | Add PUT for updating expenses          | ✅ Done    |
| 3   | Ensure required fields in POST         | ✅ Done    |
| 4   | Validate allowed keys                  | ✅ Done    |
| 5   | Add proper error handling              | ✅ Done    |
| 6   | Consistent response formatting         | ✅ Done    |
| 7   | Convert to Blueprints & MethodView     | ✅ Done |
| 8   | Add Marshmallow Schemas                | ✅ Done |
| 9   | Database Integration                   | ⬜ Pending |
| 10  | JWT Authentication                     | ⬜ Pending |

---

## 📘 API Endpoints

### `GET /expenses`

**Description:** Retrieve all expenses.

**Responses:**

* `200 OK`: List of all expenses.

---

### `POST /expenses`

**Description:** Create a new expense.

**Request Body (JSON):**

```json
{
  "amount": 500,
  "category": "Food",
  "description": "Lunch at cafe"
}
```

**Responses:**

* `201 Created`: Created expense with `expenses_id`.
* `400 Bad Request`: If required fields are missing or invalid keys are provided.

---

### `GET /expenses/<expenses_id>`

**Description:** Retrieve a specific expense by ID.

**URL Parameters:**

* `expenses_id`: Expense UUID

**Responses:**

* `200 OK`: Expense object.
* `400 Bad Request`: If expense ID not found.

---

### `PUT /expenses/<expenses_id>`

**Description:** Update an existing expense.

**Request Body (JSON):**

```json
{
  "amount": 600,
  "category": "Travel",
  "description": "Taxi fare"
}
```

**Responses:**

* `200 OK`: Updated expense.
* `400 Bad Request`: If expense ID not found or invalid key provided.

---

### `DELETE /expenses/<expenses_id>`

**Description:** Delete an expense by ID.

**Responses:**

* `200 OK`: Success message.
* `400 Bad Request`: If expense ID not found.

---

# 🔧 Local Installation

## 📦 Using Python (venv)

### Create virtual environment & activate

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

### Install dependencies

```bash
pip install flask
```

### Run the app

```bash
flask run
```


