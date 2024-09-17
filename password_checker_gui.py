import tkinter as tk
import re

# Function to check password strength and provide suggestions
def check_password_strength_and_suggestions(password):
    # Initialize strength criteria
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digit": bool(re.search(r'[0-9]', password)),
        "special": bool(re.search(r'[@#$%^&+=]', password))
    }

    # Count the number of criteria met
    criteria_met = sum(strength_criteria.values())

    # Determine password strength based on the criteria met
    if criteria_met == 5:
        strength = "Strong"
    elif 3 <= criteria_met < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide suggestions based on missing criteria
    suggestions = []
    if not strength_criteria["length"]:
        suggestions.append("Increase length to at least 8 characters.")
    if not strength_criteria["uppercase"]:
        suggestions.append("Add at least one uppercase letter.")
    if not strength_criteria["lowercase"]:
        suggestions.append("Add at least one lowercase letter.")
    if not strength_criteria["digit"]:
        suggestions.append("Include at least one number.")
    if not strength_criteria["special"]:
        suggestions.append("Add a special character (e.g., @, #, $, %).")

    # Join suggestions into a single string for feedback
    if suggestions:
        suggestions_text = "Suggestions:\n- " + "\n- ".join(suggestions)
    else:
        suggestions_text = "Your password meets all requirements."

    return strength, suggestions_text

# Function to update the feedback label
def update_feedback():
    password = entry_password.get()
    strength, suggestions = check_password_strength_and_suggestions(password)
    label_result.config(text=f"Password Strength: {strength}\n\n{suggestions}")

# Main function to create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Password Complexity Checker")

    # Label for password input
    label_password = tk.Label(root, text="Enter Password:")
    label_password.pack()

    # Entry field for password input
    global entry_password
    entry_password = tk.Entry(root, width=30, show="*")
    entry_password.pack()

    # Button to check password strength
    btn_check = tk.Button(root, text="Check Strength", command=update_feedback)
    btn_check.pack()

    # Label to display the result
    global label_result
    label_result = tk.Label(root, text="", justify="left")
    label_result.pack()

    # Run the application
    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
