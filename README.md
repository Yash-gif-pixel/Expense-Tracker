# Expense Tracker

A simple Expense Tracker application built using **Python**, **Streamlit**, and **SQLite**. The application allows users to record, manage, and analyze their daily expenses through an interactive web interface.

---

## Features

- Add new expenses
- View all recorded expenses
- Update existing expenses
- Delete expenses
- View total expenditure
- Category-wise expense summary
- Persistent data storage using SQLite

---

## Technologies Used

- Python
- Streamlit
- SQLite3

---

## Project Structure

```
expense_tracker/
│
├── app.py                 # Streamlit user interface
├── database.py            # Database operations
├── expenses.db            # SQLite database (generated automatically)
├── requirements.txt
├── README.md
└── .gitignore
```

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

Activate it

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

The application uses **SQLite** for persistent storage.

If the database does not exist, it is automatically created when the application starts.

The database stores:

- Expense ID
- Category
- Amount

---

## Future Improvements

- Expense analytics dashboard
- Charts and visualizations
- Monthly expense reports
- Export to CSV/PDF
- Budget tracking
- User authentication

---

## Author

**Yash Malik**

GitHub: https://github.com/Yash-gif-pixel
