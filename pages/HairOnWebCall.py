import streamlit as st
import urllib.parse

# App title with an improved UI
st.set_page_config(page_title="Find Top Haircare Specialists", page_icon="\U0001F487", layout="wide")
st.title("Find Top Haircare Doctors & Hospitals \U0001F468‍⚕️")

# Database of top haircare doctors and hospitals
HAIRCARE_DB = {
    "Delhi": {
        "Trichology": [("Dr. Apoorva Shah", "RichFeel", "https://www.richfeel.com", "+919876543210"),
                       ("Dr. Nivedita Dadu", "Dadu Medical Centre", "https://www.dadumedicalcentre.com",
                        "+919812345678")],
        "Dermatology": [("Dr. Rohit Batra", "DermaWorld Skin Clinic", "https://www.drrohitbatra.com", "+919845678321"),
                        ("Dr. Niti Khunger", "AIIMS", "https://www.aiims.edu", "+919874563210")]
    },
    "Mumbai": {
        "Trichology": [("Dr. Rajesh Rajput", "HairRestore", "https://www.hairrestore.com", "+919823456789"),
                       ("Dr. Viral Desai", "DHI India", "https://www.dhiindia.com", "+919877654321")],
        "Dermatology": [
            ("Dr. Jaishree Sharad", "Skinfiniti Aesthetic Clinic", "https://www.skinfiniti.in", "+919898765432"),
            ("Dr. Rinky Kapoor", "The Esthetic Clinics", "https://www.theestheticclinic.com", "+919865432178")]
    },
    "Bangalore": {
        "Trichology": [("Dr. Pradeep Sethi", "Eugenix Hair Sciences", "https://www.eugenix.in", "+919878765432"),
                       ("Dr. Madan Kumar", "Hairline International", "https://www.hairline.in", "+919864321789")],
        "Dermatology": [
            ("Dr. Rashmi Shetty", "Ra Skin & Aesthetics", "https://www.drrashmishetty.com", "+919854678921"),
            ("Dr. Swetha Reddy", "Oliva Skin & Hair Clinic", "https://www.olivaclinic.com", "+919899876543")]
    },
    "Kolkata": {
        "Trichology": [("Dr. Biplab Deb", "Kaayakalp Clinic", "https://www.kaayakalp.com", "+919876543217"),
                       (
                       "Dr. Sudipto Pakrasi", "Apollo Gleneagles", "https://www.apollohospitals.com", "+919843217654")],
        "Dermatology": [("Dr. Arindam Das", "AMRI Hospitals", "https://www.amrihospitals.in", "+919899999999"),
                        ("Dr. Sandeep Ghosh", "Tata Medical Center", "https://tmckolkata.com", "+919888888888")]
    }
}

# User selections
st.subheader("Select Your City\U0001F4CD")
city = st.selectbox("Select City:", ["Select a City"] + list(HAIRCARE_DB.keys()))

st.subheader("Select Hair Concern\U0001F9B7")
specialty = st.selectbox("Select Concern:",
                         ["Select a Concern"] + sorted(set(spec for city in HAIRCARE_DB.values() for spec in city)))

# Button to display results
if st.button("Find Specialists \U0001F50D"):
    if city != "Select a City" and specialty != "Select a Concern":
        if specialty in HAIRCARE_DB.get(city, {}):
            st.subheader(f"\U0001F468‍⚕️ Top {specialty} Specialists in {city}")
            for doctor in HAIRCARE_DB[city][specialty]:
                name, hospital, website, phone = doctor
                st.markdown(f"### **{name}**")
                st.write(f"\U0001F3E5 {hospital}")
                st.markdown(f"\U0001F310 [Visit Website]({website})")

                # WhatsApp Booking Link
                msg = f"Hello {name}, I would like to book an appointment for {specialty} consultation."
                encoded_msg = urllib.parse.quote(msg)
                whatsapp_url = f"https://api.whatsapp.com/send?phone={phone}&text={encoded_msg}"
                st.markdown(f"[📩 Book Appointment on WhatsApp]({whatsapp_url})")
                st.markdown("---")
        else:
            st.warning("No specialists available for the selected concern in this city.")

# Footer
st.markdown(
    "⚠️ **Disclaimer:** This app provides information on haircare specialists but is not a replacement for professional medical advice. Always consult a doctor directly.")
