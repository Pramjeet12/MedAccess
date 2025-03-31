import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="Compare Hospitals Across India", page_icon="🏥", layout="wide")
st.title("Find Hospitals in India Based on Your Requirements 🏥")

# Database of hospitals with specialties, cost, rating, and services
HOSPITALS_DB = {
    "Delhi": {
        "Government": [
            {"name": "AIIMS", "website": "https://www.aiims.edu", "specialties": ["Cardiology", "Oncology"], "rating": 4.8, "cost": "Affordable", "services": ["Emergency", "OPD", "24/7"]},
            {"name": "Safdarjung Hospital", "website": "https://www.vmmc-sjh.nic.in", "specialties": ["Neurology", "Orthopedics"], "rating": 4.5, "cost": "Low", "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Medanta Hospital", "website": "https://www.medanta.org", "specialties": ["Cardiology", "Neurology"], "rating": 4.7, "cost": "Expensive", "services": ["Emergency", "OPD", "24/7"]},
            {"name": "Fortis Escorts Hospital", "website": "https://www.fortisescorts.in", "specialties": ["Oncology", "Orthopedics"], "rating": 4.6, "cost": "High", "services": ["Emergency", "24/7"]},
        ]
    },
    "Mumbai": {
        "Government": [
            {"name": "KEM Hospital", "website": "https://www.kem.edu", "specialties": ["Cardiology", "Neurology"], "rating": 4.7, "cost": "Low", "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Bombay Hospital", "website": "https://www.bombayhospital.com", "specialties": ["Cardiology", "Oncology"], "rating": 4.8, "cost": "Expensive", "services": ["Emergency", "24/7"]},
        ]
    },
    "Bangalore": {
        "Government": [
            {"name": "NIMHANS", "website": "https://www.nimhans.ac.in", "specialties": ["Neurology", "Psychiatry"], "rating": 4.6, "cost": "Affordable", "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Bangalore Baptist Hospital", "website": "https://www.bbh.org.in", "specialties": ["Cardiology", "Endocrinology"], "rating": 4.7, "cost": "Moderate", "services": ["Emergency", "24/7"]},
            {"name": "Manipal Hospital", "website": "https://www.manipalhospitals.com", "specialties": ["Orthopedics", "Gastroenterology"], "rating": 4.8, "cost": "High", "services": ["Emergency", "OPD", "24/7"]},
        ]
    },
    "Chennai": {
        "Government": [
            {"name": "Govt. Stanley Medical College", "website": "https://www.stanleymedicalcollege.com", "specialties": ["Cardiology", "Pulmonology"], "rating": 4.5, "cost": "Low", "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Apollo Hospital", "website": "https://www.apollohospitals.com", "specialties": ["Oncology", "Neurology"], "rating": 4.9, "cost": "Expensive", "services": ["Emergency", "OPD", "24/7"]},
            {"name": "Fortis Malar Hospital", "website": "https://www.fortismalar.com", "specialties": ["Orthopedics", "Cardiology"], "rating": 4.7, "cost": "Moderate", "services": ["Emergency", "OPD"]},
        ]
    },
    # Add more cities and hospitals as needed
}

# User filters
st.subheader("Filter Hospitals by Your Preferences")

# Specialization filter
specialty = st.selectbox("Select Specialty🩺", ["Any"] + ["Cardiology", "Neurology", "Oncology", "Orthopedics", "Gastroenterology", "Pulmonology", "Urology", "Nephrology", "Endocrinology"])

# Cost filter
cost = st.selectbox("Select Cost Range💰", ["Any", "Affordable", "Moderate", "High", "Expensive"])

# Rating filter
rating = st.slider("Select Minimum Rating⭐", 1, 5, 4)

# Button to display results
if st.button("Search Hospitals🔍"):
    st.subheader("Hospitals Based on Your Search")

    # Filter hospitals based on user's selection
    filtered_hospitals = []
    for city, types in HOSPITALS_DB.items():
        for hospital_type, hospitals in types.items():
            for hospital in hospitals:
                # Apply filters
                if (specialty == "Any" or specialty in hospital["specialties"]) and \
                   (cost == "Any" or cost == hospital["cost"]) and \
                   hospital["rating"] >= rating:
                    hospital_info = hospital.copy()
                    hospital_info["city"] = city
                    filtered_hospitals.append(hospital_info)

    # Display the filtered hospitals
    if filtered_hospitals:
        for hospital in filtered_hospitals:
            st.markdown(f"### **{hospital['name']}** ({hospital['city']})")
            st.markdown(f"🌐 [Visit Website]({hospital['website']})")
            st.write(f"⭐ Rating: {hospital['rating']}/5")
            st.write(f"💰 Cost: {hospital['cost']}")
            st.write(f"🩺 Specialties: {', '.join(hospital['specialties'])}")
            st.write(f"🛑 Services: {', '.join(hospital['services'])}")
            st.markdown("---")
    else:
        st.warning("No hospitals found for the selected criteria.")

# Footer
st.markdown(
    "⚠️ **Disclaimer:** This app provides information on hospitals but does not endorse any particular hospital. Please visit the websites for more details."
)
