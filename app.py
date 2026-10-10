
import streamlit as st

# -----------------------------------------
# 1. Page configuration
# -----------------------------------------

st.set_page_config(
    page_title="Kerala Property Price Estimator",
    page_icon="🏡",
    layout="wide"
)

# -----------------------------------------
# 2. Kerala districts
# -----------------------------------------

districts = [
    "Thiruvananthapuram",
    "Kollam",
    "Pathanamthitta",
    "Alappuzha",
    "Kottayam",
    "Idukki",
    "Ernakulam",
    "Thrissur",
    "Palakkad",
    "Malappuram",
    "Kozhikode",
    "Wayanad",
    "Kannur",
    "Kasaragod"
]

# -----------------------------------------
# 3. Page heading
# -----------------------------------------

st.title("🏡 Kerala House & Land Price Estimator")

st.write(
    "Estimate property value using location, square-foot "
    "area and local property rates."
)

st.info(
    "Important: The default rates in this demo are illustrative "
    "examples, NOT verified market rates. Enter a suitable local "
    "rate for a meaningful estimate. This version is a calculator, "
    "not a trained machine-learning prediction model."
)

# -----------------------------------------
# 4. Location details
# -----------------------------------------

st.header("📍 Location Details")

col1, col2, col3 = st.columns(3)

with col1:
    district = st.selectbox(
        "Select district",
        districts
    )

with col2:
    locality_type = st.selectbox(
        "Area type",
        ["City", "Town", "Village"]
    )

with col3:
    locality_name = st.text_input(
        "City / town / village name",
        placeholder="e.g. Kozhikode"
    )

# -----------------------------------------
# 5. Property details
# -----------------------------------------

st.header("🏠 Property Details")

property_type = st.radio(
    "What do you want to estimate?",
    ["House / Villa", "Land / Plot"],
    horizontal=True
)

# These are demonstration defaults only.
# Replace them with locally researched rates.
if locality_type == "City":
    demo_land_rate = 4000.0
    demo_building_rate = 2500.0
elif locality_type == "Town":
    demo_land_rate = 2000.0
    demo_building_rate = 2200.0
else:
    demo_land_rate = 800.0
    demo_building_rate = 2000.0

st.caption(
    "Rates below are editable demonstration values in rupees "
    "per square foot. They are not verified rates for your district."
)

col1, col2 = st.columns(2)

with col1:
    land_area = st.number_input(
        "Land area (sq ft)",
        min_value=0.0,
        value=2000.0,
        step=100.0
    )

    land_rate = st.number_input(
        "Land rate (₹ per sq ft)",
        min_value=0.0,
        value=demo_land_rate,
        step=100.0
    )

with col2:
    if property_type == "House / Villa":
        builtup_area = st.number_input(
            "Built-up area (sq ft)",
            min_value=0.0,
            value=1200.0,
            step=100.0
        )

        building_rate = st.number_input(
            "Building value rate (₹ per sq ft)",
            min_value=0.0,
            value=demo_building_rate,
            step=100.0
        )
    else:
        builtup_area = 0.0
        building_rate = 0.0
        st.write("Land-only property selected.")
        st.write("Building value is not included.")

# -----------------------------------------
# 6. House age and condition
# -----------------------------------------

if property_type == "House / Villa":
    st.subheader("🔧 House Condition")

    col1, col2 = st.columns(2)

    with col1:
        house_age = st.number_input(
            "House age (years)",
            min_value=0,
            max_value=150,
            value=5,
            step=1
        )

    with col2:
        condition = st.selectbox(
            "Current condition",
            ["Excellent", "Good", "Average", "Needs renovation"]
        )

    condition_factors = {
        "Excellent": 1.00,
        "Good": 0.90,
        "Average": 0.75,
        "Needs renovation": 0.55
    }

    # Simple illustrative depreciation rule.
    # Replace this rule with a locally validated method.
    age_factor = max(0.40, 1 - (house_age * 0.01))
    condition_factor = condition_factors[condition]

else:
    house_age = 0
    age_factor = 1.0
    condition_factor = 1.0

# -----------------------------------------
# 7. Estimate property price
# -----------------------------------------

st.divider()

if st.button("💰 Calculate Estimated Price", type="primary"):

    if land_area <= 0:
        st.error("Please enter a land area greater than zero.")

    elif property_type == "House / Villa" and builtup_area <= 0:
        st.error("Please enter a built-up area greater than zero.")

    elif land_rate <= 0:
        st.error("Please enter a land rate greater than zero.")

    elif property_type == "House / Villa" and building_rate <= 0:
        st.error("Please enter a building value rate greater than zero.")

    else:
        # Land value
        land_value = land_area * land_rate

        # Building value, adjusted for age and condition
        if property_type == "House / Villa":
            building_value = (
                builtup_area
                * building_rate
                * age_factor
                * condition_factor
            )
        else:
            building_value = 0.0

        total_price = land_value + building_value

        # ---------------------------------
        # 8. Display results
        # ---------------------------------

        st.header("📊 Estimated Property Value")

        st.caption(
            f"Location: {locality_name.strip() or 'Not specified'}, "
            f"{district} | {locality_type}"
        )

        st.metric(
            label="Estimated Total Price",
            value=f"₹{total_price:,.0f}"
        )

        st.write("### Price Breakdown")

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric(
                "Land Value",
                f"₹{land_value:,.0f}"
            )

        with result_col2:
            st.metric(
                "Building Value",
                f"₹{building_value:,.0f}"
            )

        st.write("### Calculation Details")

        st.write(
            f"- Land: {land_area:,.0f} sq ft × "
            f"₹{land_rate:,.0f} = ₹{land_value:,.0f}"
        )

        if property_type == "House / Villa":
            st.write(
                f"- Building: {builtup_area:,.0f} sq ft × "
                f"₹{building_rate:,.0f} × "
                f"{age_factor:.2f} age factor × "
                f"{condition_factor:.2f} condition factor "
                f"= ₹{building_value:,.0f}"
            )

        st.success(
            f"Total estimated value: ₹{total_price:,.0f}"
        )

        st.warning(
            "This is a basic estimate based on the rates and "
            "adjustments you entered. It is not a verified "
            "market valuation. Actual prices vary by road access, "
            "exact location, zoning, title, amenities, building "
            "quality and current market demand."
        )

# -----------------------------------------
# 9. Footer
# -----------------------------------------

st.divider()

st.caption(
    "Kerala Property Price Estimator | Streamlit + Python"
)
