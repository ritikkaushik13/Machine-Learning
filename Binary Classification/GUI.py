import tkinter as tk
from tkinter import messagebox, filedialog as fd
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load your trained model
model = joblib.load(r'C:\Users\LENOVO\Desktop\Machine-Learning\Binary Classification\binary_classification_model.joblib')

# Initialize LabelEncoder for categorical columns
label = LabelEncoder()

# Function to browse and load a file
def browse_file():
    try:
        filename = fd.askopenfile()
        if filename:
            filepath.config(text=f"Loaded file: {filename.name}")
            data = pd.read_csv(filename.name)
            
            # Select and encode the input features
            input_data = data.iloc[:, 1:13]
            input_data[['gender', 'ssc_b', 'hsc_b', 'hsc_s', 'degree_t', 'workex', 'specialisation']] = input_data[
                ['gender', 'ssc_b', 'hsc_b', 'hsc_s', 'degree_t', 'workex', 'specialisation']].apply(label.fit_transform)

            # Predict outcomes
            global y_pred
            y_pred = model.predict(input_data)
            messagebox.showinfo("Success", f"Dataset loaded with {len(input_data)} rows.")
        else:
            messagebox.showwarning("No File", "Please select a file to proceed.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading the file: {e}")

# Function to predict placement
def predict_placement():
    try:
        if 'y_pred' not in globals():
            messagebox.showerror("Error", "Please load a dataset first.")
            return

        # Clear previous results
        placed_text.delete('1.0', tk.END)
        rejected_text.delete('1.0', tk.END)

        # Display predictions in two columns
        for i, prediction in enumerate(y_pred):
            result_text = f"Student {i + 1}\n"
            if prediction == 1:
                placed_text.insert(tk.END, result_text)
            else:
                rejected_text.insert(tk.END, result_text)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Placement Prediction")
root.geometry("720x600+20+40")  
root.config(bg='lightblue')

# Styling options
label_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Title label
title_label = tk.Label(root, text="Placement Prediction System", font=("Arial", 16, "bold"), bg='lightblue', fg="darkblue")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# File browsing section
browse_button = tk.Button(root, text='Browse CSV/Dataset', font=button_font, bg="white", fg="black", command=browse_file)
browse_button.grid(row=1, column=0, columnspan=3, pady=10)

filepath = tk.Label(root, text='', font=label_font, bg='lightblue')
filepath.grid(row=2, column=0, columnspan=3, pady=5)

# Prediction button
predict_button = tk.Button(root, text="Predict", font=button_font, bg="green", fg="white", command=predict_placement)
predict_button.grid(row=3, column=0, columnspan=3, pady=10)

# Output section
result_label = tk.Label(root, text="Prediction Results:", font=("Arial", 14, "bold"), bg='lightblue', fg="darkblue")
result_label.grid(row=4, column=0, columnspan=3, pady=10)

# Headers for columns
placed_label = tk.Label(root, text="Placed", font=("Arial", 12, "bold"), bg="lightgreen")
placed_label.grid(row=5, column=0, padx=10, pady=5)

rejected_label = tk.Label(root, text="Rejected", font=("Arial", 12, "bold"), bg="lightcoral")
rejected_label.grid(row=5, column=2, padx=10, pady=5)

# Scrollable Text widgets for results
placed_text = tk.Text(root, height=20, width=30, font=("Arial", 12), bg="lightyellow")
placed_text.grid(row=6, column=0, padx=10, pady=5)

rejected_text = tk.Text(root, height=20, width=30, font=("Arial", 12), bg="lightgray")
rejected_text.grid(row=6, column=2, padx=10, pady=5)

# Scrollbars for each Text widget
placed_scrollbar = tk.Scrollbar(root, command=placed_text.yview)
placed_scrollbar.grid(row=6, column=1, sticky="ns")
placed_text.config(yscrollcommand=placed_scrollbar.set)

rejected_scrollbar = tk.Scrollbar(root, command=rejected_text.yview)
rejected_scrollbar.grid(row=6, column=3, sticky="ns")
rejected_text.config(yscrollcommand=rejected_scrollbar.set)

# Start the Tkinter event loop
root.mainloop()
