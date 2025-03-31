import streamlit as st

# App title
st.set_page_config(page_title="Hair Care Assistant", page_icon="💇", layout="wide")
st.title("Hair Care Assistant – Find the Best Products for Your Hair!💇")

# Hair issues database with product recommendations
HAIR_CARE_DB = {
    "Hair Fall": [
        {"name": "Biotin Shampoo", "brand": "WOW", "link": "https://www.amazon.in/dp/B07B4ZB4S9"},
        {"name": "Onion Hair Oil", "brand": "Mamaearth", "link": "https://www.amazon.in/dp/B07QFW5QYH"},
        {"name": "Hair Growth Serum", "brand": "Minimalist", "link": "https://www.amazon.in/dp/B08XWCN1B9"}
    ],
    "Dandruff": [
        {"name": "Anti-Dandruff Shampoo", "brand": "Head & Shoulders", "link": "https://www.amazon.in/dp/B08CVT7W8P"},
        {"name": "Tea Tree Oil", "brand": "Soulflower", "link": "https://www.amazon.in/dp/B07KXT3ZVD"}
    ],
    "Dry & Frizzy Hair": [
        {"name": "Argan Oil Shampoo", "brand": "St. Botanica", "link": "https://www.amazon.in/dp/B07DGPPGGY"},
        {"name": "Deep Conditioner", "brand": "L'Oreal", "link": "https://www.amazon.in/dp/B07J5MVRBG"}
    ],
    "Oily Scalp": [
        {"name": "Oil Control Shampoo", "brand": "Neutrogena", "link": "https://www.amazon.in/dp/B00OJFK9IK"},
        {"name": "Apple Cider Vinegar Rinse", "brand": "WOW", "link": "https://www.amazon.in/dp/B07GZY9SP7"}
    ]
}

# Select Hair Problem
st.subheader("Select Your Hair Problem🧐")
hair_issue = st.selectbox("Choose a hair concern:", ["Select an Issue"] + list(HAIR_CARE_DB.keys()))

# Show Product Recommendations
if st.button("Get Recommendations🔍"):
    if hair_issue != "Select an Issue":
        st.subheader(f"✨ Recommended Products for {hair_issue}")
        for product in HAIR_CARE_DB[hair_issue]:
            st.markdown(f"**{product['name']}** – {product['brand']}")
            st.markdown(f"[🛒 Buy Now]({product['link']})")
            st.markdown("---")

        # Hair Care Tips (Now appearing after product recommendations)
        st.subheader("💡 Hair Care Tips")
        st.write("✔ Use sulfate-free shampoos for gentle cleansing.")
        st.write("✔ Massage scalp regularly to improve blood circulation.")
        st.write("✔ Maintain a healthy diet rich in vitamins and proteins.")
        st.write("✔ Avoid excessive heat styling to prevent damage.")

    else:
        st.warning("Please select a hair issue to get product recommendations.")

# Footer
st.markdown("⚠️ **Disclaimer:** This app provides hair care product recommendations based on common hair problems. Always check ingredient compatibility before use.")

