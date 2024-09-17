# PRODIGY_CY_03
Password Complexity Checker with GUI using Python
## Task Description:
This repository contains my third task for Prodigy InfoTech as part of my Cyber Security internship. The task was to build a **Password Complexity Checker** tool that evaluates the strength of a password based on criteria such as:
- Length (at least 8 characters),
- Presence of both **uppercase** and **lowercase** letters,
- **Numbers**,
- **Special characters** (e.g., @, #, $, %, etc.).

Additionally, the tool provides **feedback** to users, suggesting ways to improve their password strength.

### Features:
- **Password Strength Evaluation**:
    - Categorizes passwords as **Weak**, **Moderate**, or **Strong** based on the presence of the above criteria.

- **Personalized Suggestions**:
    - Provides feedback to help users strengthen their passwords, such as adding more characters, uppercase letters, numbers, or special characters.

- **Graphical User Interface (GUI)**:
    - A user-friendly GUI built with **Tkinter** allows users to input their password and receive immediate feedback.

### Password Strength Criteria:
1. **Length**: Minimum 8 characters.
2. **Uppercase Letters**: At least one uppercase letter.
3. **Lowercase Letters**: At least one lowercase letter.
4. **Numbers**: At least one digit.
5. **Special Characters**: At least one special character (e.g., @, #, $, %, etc.).

### Example Feedback:
- For the password `hello123`:

Password Strength: Moderate Suggestions:

Add at least one uppercase letter.
Add a special character (e.g., @, #, $, %).

- For the password `Hello@123`:
## How to Run:

1. **Clone the Repository**:
 ```bash
 git clone https://github.com/KarimSIM2024/PRODIGY_CY_03.git

2. Navigate to the Project Directory:
cd PRODIGY_CY_03

3. Install the Required Libraries: The project uses the built-in tkinter module, so no external libraries are required for the GUI. However, if you're using a virtual environment, activate it first:

source .venv/bin/activate  # (on Mac/Linux)
.\.venv\Scripts\activate  # (on Windows)
 
4. Run the Python File:

python password_checker_gui.py
Files Included:
password_checker_gui.py: The Python script containing the GUI and password complexity checking logic.
README.md: This file, which provides an overview of the project, how it works, and how to run it.
Learning Outcomes:
Gained a deeper understanding of password complexity evaluation.
Worked with regular expressions (regex) to validate different types of characters (uppercase, lowercase, digits, and special characters).
Enhanced skills in building a Graphical User Interface (GUI) using the Tkinter library in Python.
Learned how to provide real-time feedback and suggestions to users based on password strength.
Future Enhancements:
Implement password strength scoring to provide more granular feedback (e.g., a score from 0 to 100).
Add options for generating strong passwords automatically.
Display a visual strength meter (e.g., a progress bar) to give a better user experience.
