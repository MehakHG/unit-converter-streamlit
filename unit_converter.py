import streamlit as st

st.title("Unit Converter")

# Unit categories and units
unit_categories = {
    "Length": {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
}
# Choose category
category = st.selectbox("Choose a category", list(unit_categories.keys()))

# Choose units within the category
units = unit_categories[category]
from_unit = st.selectbox("From Unit", list(units.keys()))
to_unit = st.selectbox("To Unit", list(units.keys()))

# Input number
value = st.number_input("Enter the value to convert", min_value=0.0, format="%.6f")

# Conversion logic
converted_value = value * units[from_unit] / units[to_unit]

# Show result
st.write(f"**{value} {from_unit} = {converted_value:.6f} {to_unit}**")
