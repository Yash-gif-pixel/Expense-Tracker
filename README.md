# Expense Tracker

A web-based Expense Tracker built using **Python**, **Streamlit**, and **SQLite**. The application enables users to efficiently record, manage, and analyze their daily expenses through an intuitive interface while demonstrating CRUD (Create, Read, Update, Delete) operations using a relational database.

---

## Features

* Add new expenses
* View all recorded expenses
* Update existing expenses
* Delete expenses
* View total expenditure
* View category-wise expense summary
* Persistent data storage using SQLite
* Simple and interactive Streamlit interface

---

## Technologies Used

* Python 3
* Streamlit
* SQLite3

---

## Project Structure

```text
Expense-Tracker/
│
├── app.py              # Streamlit application
├── database.py         # SQLite database operations
├── requirements.txt    # Project dependencies
├── README.md
└── .gitignore
```

> **Note:** `expenses.db` is created automatically when the application is run for the first time.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Yash-gif-pixel/Expense-Tracker.git
```

### Navigate to the project

```bash
cd Expense-Tracker
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Database

The application uses **SQLite** for persistent data storage.

The database is automatically created on the first run and currently stores:

* Expense ID
* Category
* Amount

---

## Skills Demonstrated

* Python Programming
* CRUD Operations
* SQLite Database Integration
* Streamlit Application Development
* Modular Project Structure
* Git & GitHub

---

## Future Improvements

* Interactive charts and visualizations
* Monthly expense reports
* Budget planning
* Export expenses to CSV/PDF
* User authentication
* Expense filtering and search

---

## Author

**Yash Malik**

GitHub: https://github.com/Yash-gif-pixel
