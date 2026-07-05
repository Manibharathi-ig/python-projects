#  Password Manager

A command-line Password Manager built using Python that securely stores and retrieves account passwords using **Fernet encryption** from the `cryptography` library. The application is protected with a master password, ensuring that only authorized users can access stored credentials.

##  Features

- Master password authentication
- Secure password encryption
- Password decryption for authorized users
- Add new account credentials
- View saved account passwords
- Store encrypted passwords in a text file
- Encryption key management using a separate key file

##  Technologies Used

- Python 3
- Cryptography (Fernet)
- File Handling

##  Concepts Practiced

- Functions
- Variables
- User Input (`input()`)
- Conditional Statements (`if`, `else`)
- While Loops
- File Handling
- Reading and Writing Files
- Encryption & Decryption
- Encoding & Decoding
- Authentication
- Program Flow Control

## ▶ How to Run

1. Clone this repository.
2. Install the required package:

```bash
pip install cryptography
```

3. Ensure the `key.key` file exists in the project directory.
4. Run the following command:

```bash
python main.py
```

##  Project Structure

```text
password-manager/
│── main.py
│── key.key
│── password.txt
└── README.md
```

##  Sample Output

```text
What is your master password:
bharathi2003

Login success!

Would you like to 'add' a new password or 'view' an existing password or 'q' to quit?

> add

Account name: GitHub
Password: MyPassword123

Password saved successfully.

> view

User: GitHub | Password: MyPassword123
```

##  Author

**Mani Bharathi**

Learning Python by building real-world projects.