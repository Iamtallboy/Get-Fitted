import streamlit as st

def main():
    st.title("Custom Suit Fitting App")

    st.write(
        """
        Welcome to the Ultimate Custom Suit Fitting Adventure!

        Are you ready to embark on a journey that will transform your wardrobe and elevate your style to new heights? 
        Picture this: You, stepping into a room with confidence, your custom-tailored suit fitting you like a glove, 
        turning heads and making a lasting impression wherever you go. But wait! Before you can achieve this sartorial nirvana, 
        there's one crucial step you can't afford to overlook: getting the right measurements.

        Think of your custom suit as a work of art, and the measurements as the blueprint. 
        Just as a master sculptor meticulously crafts every detail of their masterpiece, 
        so too must your tailor ensure that every inch of fabric drapes perfectly over your frame.

        But fear not, dear fashion aficionado! Our Custom Suit Fitting App is here to guide you through the process with ease and flair. 
        From the elegant sweep of your outseam to the snug embrace of your bicep, 
        we'll help you capture every measurement with precision and panache.

        But that's not all! We understand that looking good is only half the battle. 
        Feeling good is equally important. That's why we invite you to personalize your profile with your first and last name, 
        along with your contact details. After all, when you look this good, the compliments will come pouring in, 
        and you'll want to share your style secrets with the world!

        And now, we want to hear from you! How easy was the process? 
        Rate your experience on a scale of 1 to 5 in our customer satisfaction survey. 
        Your feedback is invaluable and will help us continue to provide exceptional service to customers like you.

        So, what are you waiting for? Let's dive in, upload those images, and start crafting the custom suit of your dreams. 
        Your journey to sartorial greatness begins now!
        """
    )

    # Customer information
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    phone_number = st.text_input("Phone Number")
    email_address = st.text_input("Email Address")
    social_media_handle = st.text_input("Social Media Handle")

    # Measurements
    st.header("Measurements")
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

    for measurement, _ in measurements.items():
        st.subheader(measurement)
        measurements[measurement] = st.number_input(f"Enter {measurement} measurement (in inches):", step=0.1)
        uploaded_image = st.file_uploader(f"Upload image for {measurement}:", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            st.image(uploaded_image, caption=f"Uploaded image for {measurement}", use_column_width=True)

    # Customer satisfaction survey
    st.header("Customer Satisfaction Survey")
    satisfaction_level = st.slider("How easy was the process? (1 - Very Difficult, 5 - Very Easy)", min_value=1, max_value=5)

    if st.button("Save Measurements and Survey"):
        save_data(first_name, last_name, phone_number, email_address, social_media_handle, measurements, satisfaction_level)
        st.success("Measurements and survey saved successfully!")

def save_data(first_name, last_name, phone_number, email_address, social_media_handle, measurements, satisfaction_level):
    # Logic to save data (e.g., to a database or file)
    with open("customer_data.txt", "a") as file:
        file.write(f"Name: {first_name} {last_name}\n")
        file.write(f"Phone Number: {phone_number}\n")
        file.write(f"Email Address: {email_address}\n")
        file.write(f"Social Media Handle: {social_media_handle}\n")
        file.write("Measurements:\n")
        for measurement, value in measurements.items():
            file.write(f"{measurement}: {value} inches\n")
        file.write(f"Customer Satisfaction: {satisfaction_level}\n")

if __name__ == "__main__":
    main()
