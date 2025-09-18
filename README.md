# DAY_5_LIBRARY_MANAGEMENT_SYSTEM


📚 Library Management System

A simple command-line based Library Management System built using Python and Supabase as the backend database.
This project allows you to manage library members, books, and perform CRUD operations efficiently.
<img width="777" height="487" alt="image" src="https://github.com/user-attachments/assets/0f867975-82f6-4320-bcab-7e1ad17aef92" />


🚀 Features

👤 Member Management

Register a new member

Update member email

Delete a member

Search member by ID

📖 Book Management

Add a new book

List all available books

Search books by author

Delete a book

🛠️ Database

Uses Supabase as the backend

Secure connection with .env variables

🏗️ Project Structure
├── library_management.py   # Main Python script
├── .env                    # Environment variables (Supabase URL & Key)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/library-management-system.git
cd library-management-system

2️⃣ Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


requirements.txt should include:

supabase
python-dotenv

4️⃣ Configure Environment Variables

Create a .env file in the root directory:

SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_api_key

5️⃣ Run the Application
python library_management.py

📌 Menu Options

When you run the program, you’ll see:

1. REGISTER A MEMBER
2. ADD A NEW BOOK
3. LIST ALL AVAILABLE BOOKS
4. SEARCH BOOKS BY AUTHOR
5. SHOW DETAILS OF A MEMBER
6. UPDATE USER EMAIL
7. DELETE A BOOK
8. DELETE A USER
9. EXIT

🗄️ Database Schema
Members Table (members)
Column	Type	Description
member_id	int (PK)	Unique member ID
name	text	Member’s name
email	text	Member’s email
join_date	date	Auto-generated date
Books Table (books)
Column	Type	Description
book_id	int (PK)	Unique book ID
title	text	Book title
author	text	Author’s name
category	text	Book category/genre
stock	int	Number of copies
🔮 Future Enhancements

✅ Borrow/Return functionality for books

✅ Track issued/returned dates

✅ Late fee calculation

✅ Member activity reports

✅ GUI/Web dashboard using Flask/Django

🤝 Contribution

Fork this repository

Create a new branch (feature-branch)

Commit your changes

Push the branch and create a Pull Request

📜 License

This project is licensed under the MIT License.
