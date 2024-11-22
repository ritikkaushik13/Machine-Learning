#importing libraries
import tkinter as tk
import pandas as pd
import numpy as np
import joblib

# Load your multi-linear regression model
model = joblib.load(r"C:\Users\LENOVO\Desktop\Machine-Learning\Multiple Linear Regression\multi_linear_model.joblib")

# Initialize the root window
root = tk.Tk()
root.title("Advertising Budget Predictor")
root.geometry("600x400")
root.config(bg="#f9f9f9") 

def prediction():
    try:
        youtube = float(entry_youtube.get())
        facebook = float(entry_facebook.get())
        newspaper = float(entry_newspaper.get())
        
        # Create input array for prediction
        new = np.array([[youtube, facebook, newspaper]])
        result = model.predict(new)
        
        # Update output label
        value.config(
            text=f'Predicted Sales: {str(result[0])[0:7]} USD.',
            bg="#daf7dc",  
            fg="#2e7031",  
        )
    except Exception as e:
        # Handle invalid input
        entry_youtube.delete(0, tk.END)
        entry_facebook.delete(0, tk.END)
        entry_newspaper.delete(0, tk.END)
        value.config(
            text="Invalid Values. Please enter numeric values.",
            bg="#f8d7da", 
            fg="#a94442", 
        )
        print(f"Error: {e}")  # Debugging

# Title Label
head = tk.Label(
    root,
    text="Advertising Budget Predictor",
    font=("Roboto", 20, "bold"),
    fg="#ffffff", 
    bg="#00796b",  
)
head.pack(ipady=10, pady=10, fill='both')

# Input Frame
frame = tk.Frame(root, bg="#f9f9f9") 
frame.pack(pady=10)

# Input for YouTube
label_youtube = tk.Label(frame, text="YouTube ($):", font=("Roboto", 14), bg="#f9f9f9", fg="#37474f")
label_youtube.grid(row=0, column=0, padx=5, pady=5)
entry_youtube = tk.Entry(frame, bg="#ffffff", fg="#37474f", font=("Roboto", 14), width=10, relief="solid")
entry_youtube.grid(row=0, column=1, padx=5, pady=5)

# Input for Facebook
label_facebook = tk.Label(frame, text="Facebook ($):", font=("Roboto", 14), bg="#f9f9f9", fg="#37474f")
label_facebook.grid(row=1, column=0, padx=5, pady=5)
entry_facebook = tk.Entry(frame, bg="#ffffff", fg="#37474f", font=("Roboto", 14), width=10, relief="solid")
entry_facebook.grid(row=1, column=1, padx=5, pady=5)

# Input for Newspaper
label_newspaper = tk.Label(frame, text="Newspaper ($):", font=("Roboto", 14), bg="#f9f9f9", fg="#37474f")
label_newspaper.grid(row=2, column=0, padx=5, pady=5)
entry_newspaper = tk.Entry(frame, bg="#ffffff", fg="#37474f", font=("Roboto", 14), width=10, relief="solid")
entry_newspaper.grid(row=2, column=1, padx=5, pady=5)

# Submit Button
button = tk.Button(
    frame,
    text="Predict Sales",
    font=("Roboto", 14, "bold"),
    bg="#ff7043", 
    fg="#ffffff", 
    relief="flat",
    command=prediction,
)
button.grid(row=3, column=0, columnspan=2, pady=10)

# Output Label
value = tk.Label(root, font=("Roboto", 14), bg="#f9f9f9", fg="#37474f")
value.pack(pady=10)

# Start the application
root.mainloop()
