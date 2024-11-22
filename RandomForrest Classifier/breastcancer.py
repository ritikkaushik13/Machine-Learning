import tkinter as tk
from tkinter import messagebox
import joblib
from sklearn.preprocessing import LabelEncoder

# Load your trained model
model = joblib.load(r'C:\Users\LENOVO\Desktop\Machine-Learning\RandomForrest Classifier\RFClassifier.joblib')

# Initialize LabelEncoder for categorical columns
le_diagnosis = LabelEncoder()
le_diagnosis.fit(['M', 'B'])  # 'M' for Malignant, 'B' for Benign

def predict_cancer():
    try:
        # Get input data from the user and convert to float for numerical features
        radius_mean = float(entry_radius_mean.get())
        texture_mean = float(entry_texture_mean.get())
        perimeter_mean = float(entry_perimeter_mean.get())
        area_mean = float(entry_area_mean.get())
        smoothness_mean = float(entry_smoothness_mean.get())
        compactness_mean = float(entry_compactness_mean.get())
        concavity_mean = float(entry_concavity_mean.get())
        concave_points_mean = float(entry_concave_points_mean.get())
        symmetry_mean = float(entry_symmetry_mean.get())
        # Add additional features as needed for 'mean' and 'worst'
        
        # Add worst values similarly, for example:
        radius_worst = float(entry_radius_worst.get())
        texture_worst = float(entry_texture_worst.get())
        perimeter_worst = float(entry_perimeter_worst.get())
        area_worst = float(entry_area_worst.get())
        smoothness_worst = float(entry_smoothness_worst.get())
        compactness_worst = float(entry_compactness_worst.get())
        concavity_worst = float(entry_concavity_worst.get())
        concave_points_worst = float(entry_concave_points_worst.get())
        symmetry_worst = float(entry_symmetry_worst.get())
        fractal_dimension_worst = float(entry_fractal_dimension_worst.get())
        
        # Prepare input data for prediction
        input_data = [[
            radius_mean, texture_mean, perimeter_mean, area_mean,
            smoothness_mean, compactness_mean, concavity_mean, concave_points_mean,
            symmetry_mean, radius_worst, texture_worst, perimeter_worst, area_worst,
            smoothness_worst, compactness_worst, concavity_worst, concave_points_worst,
            symmetry_worst, fractal_dimension_worst
        ]]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Decode the prediction result
        decoded_prediction = le_diagnosis.inverse_transform([prediction])[0]
        
        # Display the result
        result_label.config(text=f"Prediction: {'Malignant' if decoded_prediction == 'M' else 'Benign'}", fg="white", bg="red" if decoded_prediction == 'M' else "green")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Breast Cancer Diagnosis Prediction")
root.config(bg="lightblue")

# Create labels and entry fields for input
label_radius_mean = tk.Label(root, text="Radius Mean:", bg="lightblue")
label_radius_mean.grid(row=0, column=0)
entry_radius_mean = tk.Entry(root)
entry_radius_mean.grid(row=0, column=1)

label_texture_mean = tk.Label(root, text="Texture Mean:", bg="lightblue")
label_texture_mean.grid(row=1, column=0)
entry_texture_mean = tk.Entry(root)
entry_texture_mean.grid(row=1, column=1)

label_perimeter_mean = tk.Label(root, text="Perimeter Mean:", bg="lightblue")
label_perimeter_mean.grid(row=2, column=0)
entry_perimeter_mean = tk.Entry(root)
entry_perimeter_mean.grid(row=2, column=1)

label_area_mean = tk.Label(root, text="Area Mean:", bg="lightblue")
label_area_mean.grid(row=3, column=0)
entry_area_mean = tk.Entry(root)
entry_area_mean.grid(row=3, column=1)

label_smoothness_mean = tk.Label(root, text="Smoothness Mean:", bg="lightblue")
label_smoothness_mean.grid(row=4, column=0)
entry_smoothness_mean = tk.Entry(root)
entry_smoothness_mean.grid(row=4, column=1)

label_compactness_mean = tk.Label(root, text="Compactness Mean:", bg="lightblue")
label_compactness_mean.grid(row=5, column=0)
entry_compactness_mean = tk.Entry(root)
entry_compactness_mean.grid(row=5, column=1)

label_concavity_mean = tk.Label(root, text="Concavity Mean:", bg="lightblue")
label_concavity_mean.grid(row=6, column=0)
entry_concavity_mean = tk.Entry(root)
entry_concavity_mean.grid(row=6, column=1)

label_concave_points_mean = tk.Label(root, text="Concave Points Mean:", bg="lightblue")
label_concave_points_mean.grid(row=7, column=0)
entry_concave_points_mean = tk.Entry(root)
entry_concave_points_mean.grid(row=7, column=1)

label_symmetry_mean = tk.Label(root, text="Symmetry Mean:", bg="lightblue")
label_symmetry_mean.grid(row=8, column=0)
entry_symmetry_mean = tk.Entry(root)
entry_symmetry_mean.grid(row=8, column=1)

# You can continue adding entry fields for other features like radius_worst, texture_worst, etc.

# Entry fields for worst values should be added similarly
label_radius_worst = tk.Label(root, text="Radius Worst:", bg="lightblue")
label_radius_worst.grid(row=9, column=0)
entry_radius_worst = tk.Entry(root)
entry_radius_worst.grid(row=9, column=1)

# Prediction button
predict_button = tk.Button(root, text="Predict", command=predict_cancer, bg="yellow", fg="black")
predict_button.grid(row=10, column=0, columnspan=2)

# Label to display prediction result
result_label = tk.Label(root, text="Prediction: None", bg="lightblue", font=("Arial", 14))
result_label.grid(row=11, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
