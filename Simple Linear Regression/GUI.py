import tkinter as tk
import pandas as pd
import numpy as np
import joblib

# Load your model
model = joblib.load(r"C:\Users\LENOVO\Desktop\Machine-Learning\Simple Linear Regression\SLReg.joblib")

# Initialize the root window
root = tk.Tk()
root.title("Salary Predictor")
root.geometry("600x300")
root.config(bg="#e8f1f5") 

def prediction():
    try:
        year = int(entry.get())
        new = np.array([[year]])  # Ensure a 2D array
        result = model.predict(new)
        value.config(
            text=f'Approximately {str(result[0])[0:7]} US Dollars.',
            bg="#c3dce9", 
        )
    except Exception as e:
        entry.delete(0, tk.END)
        value.config(text="Invalid Value.", bg="#f5d3d3")
        print(f"Error: {e}")  # Debugging

# Title Label
head = tk.Label(
    root,
    text="Know Your Salary",
    font=("Roboto", 20, "bold"),
    fg="#173753", 
    bg="#e8f1f5",
)
head.pack(ipady=10, pady=10, fill='both')

# Input Frame
frame = tk.Frame(root, bg="#e8f1f5")
frame.pack()

# Entry Box
entry = tk.Entry(frame, bg="white", fg="black", font=("Roboto", 14), width=10)
entry.grid(row=0, column=0, padx=5, pady=10)

# Label next to Entry Box
label = tk.Label(frame, text="Years", font=("Roboto", 14), bg="#e8f1f5", fg="#173753")
label.grid(row=0, column=1, padx=5, pady=10)

# Submit Button
button = tk.Button(
    frame,
    text="Submit",
    font=("Roboto", 14),
    bg="#c3dce9",
    fg="#173753",
    command=prediction,
)
button.grid(row=1, column=0, pady=10, columnspan=2)

# Output Label
value = tk.Label(root, font=("Roboto", 14), bg="#e8f1f5", fg="#173753")
value.pack()

# Start the application
root.mainloop()
