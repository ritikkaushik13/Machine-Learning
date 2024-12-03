import tkinter as tk
from tkinter import messagebox
import joblib
from sklearn.preprocessing import LabelEncoder

# Load your trained model
model = joblib.load(r'C:\Users\LENOVO\Desktop\Machine-Learning\Decision Tree Classifier\DecisionTree.joblib')

# Initialize separate LabelEncoders for each column
encoders = {
    'Sex': LabelEncoder(),
    'BP': LabelEncoder(),
    'Cholesterol': LabelEncoder(),
    'Medicine': LabelEncoder()  # For decoding the prediction
}

# Example fitting the encoders with possible categories (adjust based on your training data)
# You should train your encoders with the same categories used in your training data
# For example:
encoders['Sex'].fit(['M', 'F'])
encoders['BP'].fit(['HIGH', 'LOW', 'NORMAL'])
encoders['Cholesterol'].fit(['HIGH', 'NORMAL'])
encoders['Medicine'].fit(['drugY', 'drugC', 'drugX', 'drugA', 'drugB'])

def predict_medicine():
    try:
        # Get input data from the user
        age = float(entry_age.get())
        sex = sex_var.get()
        bp = bp_var.get()
        cholesterol = cholesterol_var.get()
        na_to_k = float(entry_na_to_k.get())

        # Encode categorical features
        sex_encoded = encoders['Sex'].transform([sex])[0]
        bp_encoded = encoders['BP'].transform([bp])[0]
        cholesterol_encoded = encoders['Cholesterol'].transform([cholesterol])[0]
        
        # Prepare input data for prediction - ensure it's in 2D format
        input_data = [[age, sex_encoded, bp_encoded, cholesterol_encoded, na_to_k]]
        
        # Debugging: Print input data shape
        print(f"Input data shape: {len(input_data)}, {len(input_data[0])}")
        
        # Make prediction and flatten the prediction array to avoid shape issues
        prediction = model.predict(input_data)
        
        # Debugging: Print the prediction shape
        print(f"Prediction shape: {prediction.shape}")
        
        # Decode the prediction (the target variable 'Medicine')
        decoded_prediction = encoders['Medicine'].inverse_transform(prediction)[0]
        
        # Display the result
        result_label.config(text=f"Prediction: {decoded_prediction}")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Set up the Tkinter GUI
root = tk.Tk()
root.title("Pharmacy")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

# Create labels and entry fields for input
label_age = tk.Label(root, text="Age:", bg="#f0f8ff", fg="#000")
label_age.grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_age = tk.Entry(root, width=20)
entry_age.grid(row=0, column=1, padx=10, pady=5)

# Radio buttons for Sex
sex_var = tk.StringVar(value="M")
label_sex = tk.Label(root, text="Sex:", bg="#f0f8ff", fg="#000")
label_sex.grid(row=1, column=0, sticky="e", padx=10, pady=5)
sex_frame = tk.Frame(root, bg="#f0f8ff")
sex_frame.grid(row=1, column=1, padx=10, pady=5)
tk.Radiobutton(sex_frame, text="Male", variable=sex_var, value="M", bg="#f0f8ff").pack(side="left", padx=5)
tk.Radiobutton(sex_frame, text="Female", variable=sex_var, value="F", bg="#f0f8ff").pack(side="left", padx=5)

# Radio buttons for Blood Pressure
bp_var = tk.StringVar(value="NORMAL")
label_bp = tk.Label(root, text="Blood Pressure:", bg="#f0f8ff", fg="#000")
label_bp.grid(row=2, column=0, sticky="e", padx=10, pady=5)
bp_frame = tk.Frame(root, bg="#f0f8ff")
bp_frame.grid(row=2, column=1, padx=10, pady=5)
tk.Radiobutton(bp_frame, text="HIGH", variable=bp_var, value="HIGH", bg="#f0f8ff").pack(side="left", padx=5)
tk.Radiobutton(bp_frame, text="LOW", variable=bp_var, value="LOW", bg="#f0f8ff").pack(side="left", padx=5)
tk.Radiobutton(bp_frame, text="NORMAL", variable=bp_var, value="NORMAL", bg="#f0f8ff").pack(side="left", padx=5)

# Radio buttons for Cholesterol
cholesterol_var = tk.StringVar(value="NORMAL")
label_cholesterol = tk.Label(root, text="Cholesterol:", bg="#f0f8ff", fg="#000")
label_cholesterol.grid(row=3, column=0, sticky="e", padx=10, pady=5)
cholesterol_frame = tk.Frame(root, bg="#f0f8ff")
cholesterol_frame.grid(row=3, column=1, padx=10, pady=5)
tk.Radiobutton(cholesterol_frame, text="HIGH", variable=cholesterol_var, value="HIGH", bg="#f0f8ff").pack(side="left", padx=5)
tk.Radiobutton(cholesterol_frame, text="NORMAL", variable=cholesterol_var, value="NORMAL", bg="#f0f8ff").pack(side="left", padx=5)

# Entry for Na_to_K
label_na_to_k = tk.Label(root, text="Na_to_K Ratio:", bg="#f0f8ff", fg="#000")
label_na_to_k.grid(row=4, column=0, sticky="e", padx=10, pady=5)
entry_na_to_k = tk.Entry(root, width=20)
entry_na_to_k.grid(row=4, column=1, padx=10, pady=5)

# Prediction button
predict_button = tk.Button(root, text="Predict", command=predict_medicine, bg="#4682b4", fg="#fff")
predict_button.grid(row=5, column=0, columnspan=2, pady=10)

# Label to display prediction result
result_label = tk.Label(root, text="Prediction: None", bg="#f0f8ff", fg="#000")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Center the whole layout by adding padding
for widget in root.grid_slaves():
    widget.grid_configure(padx=15, pady=5)

# Start the Tkinter event loop
root.mainloop()
