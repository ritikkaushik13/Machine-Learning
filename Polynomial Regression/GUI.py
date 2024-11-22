import tkinter as tk
import pandas as pd
import numpy as np
import joblib

# Load your polynomial regression model
model = joblib.load(r"C:\Users\LENOVO\Desktop\Machine-Learning\Polynomial Regression\polynomial_model.joblib")
poly = joblib.load(r"C:\Users\LENOVO\Desktop\Machine-Learning\Polynomial Regression\polytransform.joblib")

# Initialize the root window
root = tk.Tk()
root.title("Height Predictor")
root.geometry("600x400")
root.config(bg="#ffe6e1")

def prediction():
    try:
        weight = float(entry_weight.get())
        
        # Create input array for prediction
        old = np.array([[weight]])
        new = poly.fit_transform(old)
        result = model.predict(new)
        
        # Update output label
        value.config(
            text=f'Predicted Height: {str(result[0])[0:7]} cm.',
            bg="#e8f6d8", 
            fg="#3b6e23", 
        )
    except Exception as e:
        # Handle invalid input
        entry_weight.delete(0, tk.END)
        value.config(
            text="Invalid Value. Please enter a number.",
            bg="#ffe5e5", 
            fg="#aa3d3d",  
        )
        print(f"Error: {e}")  # Debugging

# Title Label
head = tk.Label(
    root,
    text="Height Predictor",
    font=("Comic Sans MS", 20, "bold"),
    fg="#4d5bf9", 
    bg="#ffe6e1", 
)
head.pack(ipady=10, pady=10, fill='both')

# Input Frame
frame = tk.Frame(root, bg="#ffe6e1") 
frame.pack(pady=10)

# Input for Weight
label_weight = tk.Label(frame, text="Weight (kg):", font=("Comic Sans MS", 14), bg="#ffe6e1", fg="#a3476b")
label_weight.grid(row=0, column=0, padx=5, pady=5)
entry_weight = tk.Entry(frame, bg="#ffffff", fg="#4b4b4b", font=("Comic Sans MS", 14), width=10, relief="solid")
entry_weight.grid(row=0, column=1, padx=5, pady=5)

# Submit Button
button = tk.Button(
    frame,
    text="Predict Height",
    font=("Comic Sans MS", 14, "bold"),
    bg="#fcba03", 
    fg="#ffffff", 
    relief="flat",
    command=prediction,
)
button.grid(row=1, column=0, columnspan=2, pady=10)

# Output Label
value = tk.Label(root, font=("Comic Sans MS", 14), bg="#ffe6e1", fg="#4b4b4b")
value.pack(pady=10)

# Start the application
root.mainloop()
