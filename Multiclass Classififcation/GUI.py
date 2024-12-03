import tkinter as tk
from tkinter import messagebox, filedialog as fd
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load your trained model
model = joblib.load(r'C:\Users\LENOVO\Desktop\Machine-Learning\Multiclass Classififcation\multi_class_model.joblib')
scaler = joblib.load(r'C:\Users\LENOVO\Desktop\Machine-Learning\Multiclass Classififcation\ss.joblib')

# Function to browse and load a file
def browse_file():
    try:
        filename = fd.askopenfile()
        if filename:
            filepath.config(text=f"Loaded file: {filename.name}")
            data = pd.read_csv(filename.name)
            
            # Use Standard Scaler
            input_data = data.iloc[:100, 1:]
            input_data = scaler.transform(input_data)

            # Predict outcomes
            global y_pred
            y_pred = model.predict(input_data)
            messagebox.showinfo("Success", f"Dataset loaded with {len(input_data)} rows.")
        else:
            messagebox.showwarning("No File", "Please select a file to proceed.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading the file: {e}")

# Function to predict obesity levels
def predict_obesity():
    try:
        if 'y_pred' not in globals():
            messagebox.showerror("Error", "Please load a dataset first.")
            return

        print("Prediction started...")

        # Clear previous results
        output_text.delete('1.0', tk.END)

        # Store patients' predictions in a dictionary (Levels 0-6)
        obesity_levels = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        valid_classes = {0, 1, 2, 3, 4, 5, 6}

        for i, prediction in enumerate(y_pred):
            result_text = f"Patient {i + 1}"
            print(f"Prediction for Patient {i + 1}: {prediction}")
            if prediction in valid_classes:
                obesity_levels[prediction].append(result_text)
            else:
                print(f"Warning: Unexpected prediction value {prediction} for Patient {i + 1}")

        # Display the predictions as bullet points in a single text box
        for level, patients in obesity_levels.items():
            output_text.insert(tk.END, f"Obesity Level {level}: {', '.join(patients)}\n\n")

        print("Prediction completed.")
        messagebox.showinfo("Prediction Completed", "Predictions have been added to the output.")
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Set up the Tkinter GUI
root = tk.Tk()
root.title("Obesity Level Prediction")
root.geometry("800x650+20+10")  
root.config(bg='#1A3D2A')  # Dark Green Background

# Centering all components
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Styling options
label_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Title label
title_label = tk.Label(root, text="Obesity Level Prediction System", font=("Arial", 16, "bold"), bg='#1A3D2A', fg="white")
title_label.grid(row=0, column=0, columnspan=3, pady=20)

# File browsing section
browse_button = tk.Button(root, text='Browse CSV/Dataset', font=button_font, bg="#2A6340", fg="white", command=browse_file)
browse_button.grid(row=1, column=0, columnspan=3, pady=10)

filepath = tk.Label(root, text='', font=label_font, bg='#1A3D2A', fg="white")
filepath.grid(row=2, column=0, columnspan=3, pady=5)

# Prediction button
predict_button = tk.Button(root, text="Predict", font=button_font, bg="#2A6340", fg="white", command=predict_obesity)
predict_button.grid(row=3, column=0, columnspan=3, pady=10)

# Output section
result_label = tk.Label(root, text="Prediction Results:", font=("Arial", 14, "bold"), bg='#1A3D2A', fg="white")
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Scrollable Text widget for results
output_text = tk.Text(root, height=15, width=50, font=("Arial", 12), bg="#4C8063", fg="white")
output_text.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

# Scrollbar for the output text widget
output_scrollbar = tk.Scrollbar(root, command=output_text.yview)
output_scrollbar.grid(row=5, column=2, sticky="ns", padx=5)
output_text.config(yscrollcommand=output_scrollbar.set)

root.mainloop()
