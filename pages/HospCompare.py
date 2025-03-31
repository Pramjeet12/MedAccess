import streamlit as st

# App title with an improved UI
st.set_page_config(page_title="Compare Hospitals in India", page_icon="🏥", layout="wide")
st.title("Compare Hospitals in Your City🏥")

# Database of hospitals with additional details
HOSPITALS_DB = {
    "Delhi": {
        "Government": [
            {"name": "AIIMS", "website": "https://www.aiims.edu", "specialties": ["Cardiology", "Oncology"],
             "rating": 4.8, "cost": "Affordable", "services": ["Emergency", "OPD", "24/7"]},
            {"name": "Safdarjung Hospital", "website": "https://www.vmmc-sjh.nic.in",
             "specialties": ["Neurology", "Orthopedics"], "rating": 4.5, "cost": "Low",
             "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Medanta Hospital", "website": "https://www.medanta.org", "specialties": ["Cardiology", "Neurology"],
             "rating": 4.7, "cost": "Expensive", "services": ["Emergency", "OPD", "24/7"]},
            {"name": "Fortis Escorts Hospital", "website": "https://www.fortisescorts.in",
             "specialties": ["Oncology", "Orthopedics"], "rating": 4.6, "cost": "High",
             "services": ["Emergency", "24/7"]},
        ]
    },
    "Mumbai": {
        "Government": [
            {"name": "KEM Hospital", "website": "https://www.kem.edu", "specialties": ["Cardiology", "Neurology"],
             "rating": 4.7, "cost": "Low", "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Bombay Hospital", "website": "https://www.bombayhospital.com",
             "specialties": ["Cardiology", "Oncology"], "rating": 4.8, "cost": "Expensive",
             "services": ["Emergency", "24/7"]},
        ]
    },
    "Bangalore": {
        "Government": [
            {"name": "NIMHANS", "website": "https://www.nimhans.ac.in", "specialties": ["Neurology", "Psychiatry"],
             "rating": 4.6, "cost": "Affordable", "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Bangalore Baptist Hospital", "website": "https://www.bbh.org.in",
             "specialties": ["Cardiology", "Endocrinology"], "rating": 4.7, "cost": "Moderate",
             "services": ["Emergency", "24/7"]},
            {"name": "Manipal Hospital", "website": "https://www.manipalhospitals.com",
             "specialties": ["Orthopedics", "Gastroenterology"], "rating": 4.8, "cost": "High",
             "services": ["Emergency", "OPD", "24/7"]},
        ]
    },
    "Chennai": {
        "Government": [
            {"name": "Govt. Stanley Medical College", "website": "https://www.stanleymedicalcollege.com",
             "specialties": ["Cardiology", "Pulmonology"], "rating": 4.5, "cost": "Low",
             "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Apollo Hospital", "website": "https://www.apollohospitals.com",
             "specialties": ["Oncology", "Neurology"], "rating": 4.9, "cost": "Expensive",
             "services": ["Emergency", "OPD", "24/7"]},
            {"name": "Fortis Malar Hospital", "website": "https://www.fortismalar.com",
             "specialties": ["Orthopedics", "Cardiology"], "rating": 4.7, "cost": "Moderate",
             "services": ["Emergency", "OPD"]},
        ]
    },
    "Hyderabad": {
        "Government": [
            {"name": "Osmania General Hospital", "website": "https://www.osmaniahospital.com",
             "specialties": ["General Surgery", "Orthopedics"], "rating": 4.4, "cost": "Affordable",
             "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Care Hospitals", "website": "https://www.carehospitals.com",
             "specialties": ["Cardiology", "Gastroenterology"], "rating": 4.6, "cost": "Expensive",
             "services": ["Emergency", "OPD", "24/7"]},
            {"name": "Yashoda Hospitals", "website": "https://www.yashodahospitals.com",
             "specialties": ["Neurology", "Orthopedics"], "rating": 4.7, "cost": "High",
             "services": ["Emergency", "OPD"]},
        ]
    },
    "Kolkata": {
        "Government": [
            {"name": "R.G. Kar Medical College", "website": "https://www.rgkar.edu.in",
             "specialties": ["Cardiology", "Nephrology"], "rating": 4.5, "cost": "Low",
             "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "AMRI Hospitals", "website": "https://www.amrihospitals.in",
             "specialties": ["Oncology", "Cardiology"], "rating": 4.8, "cost": "Expensive",
             "services": ["Emergency", "24/7"]},
            {"name": "Fortis Hospital", "website": "https://www.fortishealthcare.com",
             "specialties": ["Nephrology", "Urology"], "rating": 4.7, "cost": "High", "services": ["Emergency", "OPD"]},
        ]
    },
    "Patna": {
        "Government": [
            {"name": "Patna Medical College", "website": "https://www.pmch.ac.in",
             "specialties": ["Cardiology", "Orthopedics"], "rating": 4.4, "cost": "Low",
             "services": ["Emergency", "OPD"]},
        ],
        "Private": [
            {"name": "Indira Gandhi Institute of Medical Sciences", "website": "https://www.igims.org",
             "specialties": ["Oncology", "Nephrology"], "rating": 4.5, "cost": "Moderate",
             "services": ["Emergency", "24/7"]},
            {"name": "Shree Harsha Hospital", "website": "https://www.shreeharshahospital.com",
             "specialties": ["Neurology", "Gastroenterology"], "rating": 4.6, "cost": "Expensive",
             "services": ["Emergency", "OPD", "24/7"]},
        ]
    },
}

# User selection
st.subheader("Select Your City📍")
city = st.selectbox("Select City:", ["Select a City"] + list(HOSPITALS_DB.keys()))

st.subheader("Select Hospital Type🏥")
hospital_type = st.selectbox("Select Type:", ["Select a Type"] + ["Government", "Private"])

st.subheader("Select Specialty🩺")
specialty = st.selectbox("Select Specialty:",
                         ["Any"] + ["Cardiology", "Neurology", "Oncology", "Orthopedics", "Gastroenterology",
                                    "Pulmonology", "Urology", "Nephrology", "Endocrinology"])

# Button to display results
if st.button("Compare Hospitals🔍"):
    if city != "Select a City" and hospital_type != "Select a Type":
        st.subheader(f"🏥 {hospital_type} Hospitals in {city}")
        hospitals = HOSPITALS_DB[city].get(hospital_type, [])
        filtered_hospitals = [h for h in hospitals if specialty == "Any" or specialty in h["specialties"]]

        if filtered_hospitals:
            for hospital in filtered_hospitals:
                st.markdown(f"### **{hospital['name']}**")
                st.markdown(f"🌐 [Visit Website]({hospital['website']})")
                st.write(f"⭐ Rating: {hospital['rating']}/5")
                st.write(f"💰 Estimated Cost: {hospital['cost']}")
                st.write(f"🛑 Services: {', '.join(hospital['services'])}")
                st.markdown("---")
        else:
            st.warning("No hospitals found for the selected criteria.")
    else:
        st.warning("Please select a city and hospital type to view hospitals.")

# Footer
st.markdown(
    "⚠️ **Disclaimer:** This app provides information on hospitals but does not endorse any particular hospital. Please visit the websites for more details.")
