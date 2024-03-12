import streamlit as st

def main():
    st.title("Custom Suit Fitting App")
    st.write("Enter individual measurements for customers.")

    measurements = {
        "Out Seam": None,
        "Chest": None,
        "Coat Sleeve": None,
        "Pant Waist": None,
        "Coat Length": None,
        "Wrist": None,
        "Calf": None,
        "Bicep": None,
        "Armpit": None,
        "Pant Seat": None,
        "Incline": None
    }

    # Input fields for each measurement and upload image
    for measurement, _ in measurements.items():
        st.subheader(measurement)
        measurements[measurement] = st.number_input(f"Enter {measurement} measurement (in inches):", step=0.1)
        uploaded_image = st.file_uploader(f"Upload image for {measurement}:", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            st.image(uploaded_image, caption=f"Uploaded image for {measurement}", use_column_width=True)

    st.subheader("Customer Satisfaction Survey")
    satisfaction_level = st.slider("How easy was the process for the customer? (1 - Very Difficult, 5 - Very Easy)", min_value=1, max_value=5)

    if st.button("Save Measurements and Survey"):
        save_measurements_and_survey(measurements, satisfaction_level)
        st.success("Measurements and survey saved successfully!")

def save_measurements_and_survey(measurements, satisfaction_level):
    # Logic to save measurements and survey responses
    with open("customer_measurements.txt", "a") as file:
        for measurement, value in measurements.items():
            file.write(f"{measurement}: {value} inches\n")
        file.write(f"Customer Satisfaction: {satisfaction_level}\n")

if __name__ == "__main__":
    main()
