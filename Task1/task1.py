import itertools
import string
import tkinter as tk
from tkinter import scrolledtext


def dictionary_attack(username, dictionary, correct_password):
    result_text.insert(tk.END, f"\nAttempting Dictionary Attack for user: {username}...\n")
    for word in dictionary:
        word = word.strip()  # Remove any trailing newlines or spaces
        if word == correct_password:
            result_text.insert(tk.END, f"Password cracked using Dictionary Attack! Password: {word}\n")
            return True
    result_text.insert(tk.END, "Dictionary Attack failed.\n")
    return False


def brute_force_attack(correct_password):
    """Attempts brute-force attack and displays results in the GUI."""
    result_text.insert(tk.END, "\nAttempting Brute Force Attack...\n")

    chars = string.ascii_letters  # A-Z, a-z
    for guess in itertools.product(chars, repeat=5):
        guess = ''.join(guess)
        if guess == correct_password:
            result_text.insert(tk.END, f"Password cracked using Brute Force Attack! Password: {guess}\n")
            return True

    result_text.insert(tk.END, "Brute Force Attack failed.\n")
    return False


def start_attack():
    """Handles the attack process by running dictionary attack first, then brute force if needed."""
    username = username_entry.get()
    correct_password = "Zeyad"  # Hardcoded password
    dictionary_list = ["hEllo", "worLd", "Zeyad", "adMin", "apple"]  # Sample List

    result_text.delete(1.0, tk.END)  # Clear previous results

    if not dictionary_attack(username, dictionary_list, correct_password):  # First, try dictionary attack
        brute_force_attack(correct_password)  # If it fails, start brute force


def main():
    """Main function to initialize the GUI."""
    global root, username_entry, result_text  # Declare global variables for GUI elements

    # GUI Setup
    root = tk.Tk()
    root.title("Password Cracker")

    # Labels & Inputs
    tk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5)
    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    # Buttons
    attack_button = tk.Button(root, text="Start Attack", command=start_attack)
    attack_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    # Result Box
    result_text = scrolledtext.ScrolledText(root, width=50, height=10)
    result_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Run GUI
    root.mainloop()


# Run the program
if __name__ == "__main__":
    main()
