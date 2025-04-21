import streamlit as st

def length_converter(value, from_unit, to_unit):
    to_metre = {
        "Metre": 1,
        "Centimetre": 0.01,
        "Kilometre": 1000,
        "Millimetre": 0.001,
        "Inch": 0.0254,
        "Foot": 0.3048
    }

    from_metre = {
        "Metre": 1,
        "Centimetre": 100,
        "Kilometre": 0.001,
        "Millimetre": 1000,
        "Inch": 39.3701,
        "Foot": 3.28084
    }

    value_in_metres = value * to_metre[from_unit]
    return value_in_metres * from_metre[to_unit]

def main():
    st.title("📏 Unit Converter (Length)")

    units = ["Metre", "Centimetre", "Kilometre", "Millimetre", "Inch", "Foot"]

    value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)
    from_unit = st.selectbox("Convert from:", units)
    to_unit = st.selectbox("Convert to:", units)

    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()
