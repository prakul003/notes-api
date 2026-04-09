#📝 Notes API with Search

A simple backend API built using Flask that allows users to create, read, delete, and search notes.

🚀 Features

* Create notes
* Get all notes
* Delete notes
* Search notes by title or content
* Handles edge cases:
  * Empty search query
  * No matching results

🛠️ Tech Stack

* Python
* Flask
* SQLite

📂 Project Structure

notes-api/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore

⚙️ Setup Instructions

1. Clone the repository:
   git clone https://github.com/prakul003/notes-api.git

2. Navigate to the folder:
   cd notes-api

3. Install dependencies:
   pip install -r requirements.txt

4. Run the server:
   python app.py

📌 API Endpoints:--

➕ Create Note

POST /notes

📖 Get All Notes

GET /notes

❌ Delete Note

DELETE /notes/{id}

🔍 Search Notes

GET /search?q=keyword

🧪 Example Request (Postman)

### Create Note

POST /notes

Body:
{
"title": "Exam",
"content": "Study Data Structures"
}

📸Screenshort:

<img width="1907" height="1015" alt="image" src="https://github.com/user-attachments/assets/ea6b2cf2-d98d-489e-a0db-5add1cc5b260" />


⚠️ Edge Cases Handled

* Returns error when search query is empty
* Returns message when no results are found


🎯 Approach

* Designed a simple database schema using SQLite
* Implemented REST APIs using Flask
* Used SQL LIKE queries for keyword search
* Ensured proper handling of edge cases
* Tested APIs using Postman

👨‍💻 Author

Raj Binayak

📌 Note

This project was built as part of an internship assignment to demonstrate backend development skills and problem-solving approach.
