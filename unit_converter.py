import streamlit as st

# Define categories and their units
categories = {
    "Length": ["meters", "kilometers", "inches", "centimeters"],
    "Weight": ["grams", "kilograms", "pounds"],
    "Temperature": ["celsius", "fahrenheit"],
    "Volume": ["gallons", "liters"]
}

# Conversion logic
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  
        "kilometers_meters": 1000,   
        "grams_kilograms": 0.001,    
        "kilograms_grams": 1000,     
        "inches_centimeters": 2.54,  
        "centimeters_inches": 1 / 2.54,  
        "gallons_liters": 3.78541,  
        "liters_gallons": 1 / 3.78541,  
        "kilograms_pounds": 2.20462,  
        "pounds_kilograms": 1 / 2.20462  
    }

    # Temperature conversion separately handled
    if unit_from == "fahrenheit" and unit_to == "celsius":
        return (value - 32) * 5/9
    elif unit_from == "celsius" and unit_to == "fahrenheit":
        return (value * 9/5) + 32
    elif f"{unit_from}_{unit_to}" in conversions:
        return value * conversions[f"{unit_from}_{unit_to}"]
    else:
        return "Conversion Not Supported"

# Streamlit UI
st.title("ConvertEase - Universal Unit Converter")

# Step 1: Choose category
category = st.selectbox("Choose a category:", list(categories.keys()))

# Step 2: Based on category, show available units
if category:
    units = categories[category]
    unit_from = st.selectbox("Convert from:", units)
    unit_to = st.selectbox("Convert to:", units)

    # Step 3: Take user input and perform conversion
    value = st.number_input("Enter the value:", value=1.0, step=1.0, format="%.2f")

    if st.button("Convert"):
        if unit_from == unit_to:
            st.warning("Please select different units for conversion!")
        else:
            result = convert_units(value, unit_from, unit_to)
            st.success(f"Converted Value: {result:.4f}")

# Footer
st.markdown("---")  
st.markdown("<p style='text-align: center; font-size: 16px;'>🚀 Created by Jawad Nasir</p>", unsafe_allow_html=True)
