import streamlit as st

def main():
    st.title("Custom Suit Fitting App")
    st.write("Enter individual measurements for customers.")

    measurements = {
        "Out Seam": "",
        "Chest": "",
        "Coat Sleeve": "",
        "Pant Waist": "",
        "Coat Length": "",
        "Wrist": "",
        "Calf": "",
        "Bicep": "",
        "Armpit": "",
        "Pant Seat": "",
        "Incline": ""
    }

    # Image URLs for each measurement entry
    measurement_images = {
        "Out Seam": "https://example.com/out_seam_image.png",
        "Chest": "https://example.com/chest_image.png",
        "Coat Sleeve": "https://example.com/coat_sleeve_image.png",
        "Pant Waist": "https://example.com/pant_waist_image.png",
        "Coat Length": "https://example.com/coat_length_image.png",
        "Wrist": "https://example.com/wrist_image.png",
        "Calf": "https://example.com/calf_image.png",
        "Bicep": "https://example.com/bicep_image.png",
        "Armpit": "https://example.com/armpit_image.png",
        "Pant Seat": "https://example.com/pant_seat_image.png",
        "Incline": "https://example.com/incline_image.png"
    }

    # Input fields for each measurement
    for measurement, image_url in measurement_images.items():
        st.subheader(measurement)
        st.image(image_url, use_column_width=True)
        measurements[measurement] = st.number_input(f"Enter {measurement} measurement (in inches):", step=0.1)

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
