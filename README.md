# Smart Contact Manager

A command-line Contact Manager built with **Python 3.13.7**. This project was created for learning purposes to practice Python fundamentals, modular programming, file handling, JSON data storage, and CRUD operations.

**Project Status:** Completed (Version 1.0)

---

## About the Project

Smart Contact Manager is a terminal-based application that allows users to manage contacts efficiently. It stores contact information in a JSON file, allowing data to persist even after the program is closed.

The primary objective of this project was to apply fundamental Python concepts by building a complete command-line application from scratch.

---

## Features

* Add new contacts
* View all saved contacts
* Search contacts by name
* Update existing contacts
* Delete a specific contact
* Delete all contacts (with confirmation)
* Input validation for names and phone numbers
* Persistent data storage using JSON

---

## Technologies Used

* Python 3.13.7
* JSON
* Python Standard Library

---

## Concepts Practiced

This project helped me practice and understand:

* Functions
* Modular Programming
* Python Modules
* File Handling
* JSON (`json.load()` and `json.dump()`)
* Dictionaries
* Exception Handling
* Input Validation
* Loops
* Conditional Statements
* CRUD (Create, Read, Update, Delete) Operations
* Basic Project Structure

---

## Project Structure

```text
Smart-Contact-Manager/
│
├── SCM.py
├── Add_Contacts.py
├── view_contacts.py
├── search_contacts.py
├── update_contact.py
├── delete_contact.py
├── contacts_book.json
└── README.md
```

---

## Getting Started

### Prerequisites

* Python 3.13.7 or any compatible Python 3 version

### Installation

Clone the repository:

```bash
git clone https://github.com/im-sarwar/Smart-Contact-Manager.git
```

Navigate to the project directory:

```bash
cd Smart-Contact-Manager
```

Run the application:

```bash
python SCM.py
```

---

## Example Menu

```text
-----------------
Do you want to

1. Add Contacts
2. View Contacts
3. Search Contacts
4. Edit/Update Contacts
5. Delete Contacts
6. Exit Now
```

---

## Data Storage

All contacts are stored locally in:

```text
contacts_book.json
```

The application uses JSON format to store contact information, ensuring that data remains available between program executions.

---

## Compatibility

This project was developed on **Windows** using **Python 3.13.7**.

Since it only uses Python's standard library, it is compatible with:

* Windows
* Linux
* macOS

---

## Learning Objective

This project was built for learning purposes. It helped me strengthen my understanding of Python fundamentals by applying them in a complete command-line application, with a focus on writing modular code, handling files, validating user input, and implementing CRUD functionality.

---

## Author

**Sarwar Baqi**

GitHub: https://github.com/im-sarwar

---

## License

This project is licensed under the MIT License.
