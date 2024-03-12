import streamlit as st

def calculate_body_measurements(height):
    # Constants for body proportions (can be adjusted based on standard ratios)
    shoulder_width_ratio = 0.2
    waist_ratio = 0.45
    hip_ratio = 0.45
    inseam_ratio = 0.45
    
    # Calculate body measurements based on height
    shoulder_width = height * shoulder_width_ratio
    waist = height * waist_ratio
    hip = height * hip_ratio
    inseam = height * inseam_ratio
    
    return shoulder_width, waist, hip, inseam

def main():
    st.title("Body Measurements Calculator")
    st.write("Enter your height (in inches) to calculate body measurements.")
    
    height = st.number_input("Height (in inches)", min_value=56, max_value=87, value=65, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    
    if st.button("Calculate Measurements"):
        shoulder_width, waist, hip, inseam = calculate_body_measurements(height)
        st.write(f"**Shoulder Width:** {shoulder_width:.2f} inches")
        st.write(f"**Waist:** {waist:.2f} inches")
        st.write(f"**Hip:** {hip:.2f} inches")
        st.write(f"**Inseam:** {inseam:.2f} inches")

if __name__ == "__main__":
    main()
