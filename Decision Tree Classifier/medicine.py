import tkinter as tk
from tkinter import messagebox
import joblib
from sklearn.preprocessing import LabelEncoder

# Load your trained model
model = joblib.load(r'C:\Users\LENOVO\Desktop\Machine-Learning\Decision Tree Classifier\DecisionTree.joblib')

# Initialize LabelEncoder for categorical columns
le_sex = LabelEncoder()
le_bp = LabelEncoder()
le_cholesterol = LabelEncoder()
le_medicine = LabelEncoder()  # LabelEncoder for the target variable

# Example fitting the encoders with possible categories (adjust based on your training data)
le_sex.fit(['M', 'F'])  # Fit with training data values
le_bp.fit(['HIGH', 'LOW','NORMAL'])
le_cholesterol.fit(['HIGH', 'NORMAL'])
# Fit the encoder for the target variable 'Medicine'
le_medicine.fit(['drugY', 'drugC', 'drugX', 'drugA', 'drugB'])  # List your medicines here

def predict_medicine():
    try:
        # Get input data from the user
        age = float(entry_age.get())  # Convert to float for numerical values
        sex = entry_sex.get()
        bp = entry_bp.get()
        cholesterol = entry_cholesterol.get()
        na_to_k = float(entry_na_to_k.get())  # Convert to float for numerical values

        # Encode categorical features
        sex_encoded = le_sex.transform([sex])[0]  # Encode input 'Male'/'Female'
        bp_encoded = le_bp.transform([bp])[0]  # Encode input 'High'/'Low'
        cholesterol_encoded = le_cholesterol.transform([cholesterol])[0]  # Encode input 'High'/'Normal'
        
        # Prepare input data for prediction
        input_data = [[age, sex_encoded, bp_encoded, cholesterol_encoded, na_to_k]]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Decode the prediction (the target variable 'Medicine')
        decoded_prediction = le_medicine.inverse_transform([prediction])[0]  # Decode to original medicine name
        
        # Display the result
        result_label.config(text=f"Prediction: {decoded_prediction}")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Pharmacy")

# Create labels and entry fields for input
label_age = tk.Label(root, text="Age:")
label_age.grid(row=0, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=0, column=1)

label_sex = tk.Label(root, text="Sex (M/F):")
label_sex.grid(row=1, column=0)
entry_sex = tk.Entry(root)
entry_sex.grid(row=1, column=1)

label_bp = tk.Label(root, text="Blood Pressure (HIGH/LOW/NORMAL):")
label_bp.grid(row=2, column=0)
entry_bp = tk.Entry(root)
entry_bp.grid(row=2, column=1)

label_cholesterol = tk.Label(root, text="Cholesterol (HIGH/NORMAL):")
label_cholesterol.grid(row=3, column=0)
entry_cholesterol = tk.Entry(root)
entry_cholesterol.grid(row=3, column=1)

label_na_to_k = tk.Label(root, text="Na_to_K Ratio:")
label_na_to_k.grid(row=4, column=0)
entry_na_to_k = tk.Entry(root)
entry_na_to_k.grid(row=4, column=1)

# Prediction button
predict_button = tk.Button(root, text="Predict", command=predict_medicine)
predict_button.grid(row=5, column=0, columnspan=2)

# Label to display prediction result
result_label = tk.Label(root, text="Prediction: None")
result_label.grid(row=6, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
