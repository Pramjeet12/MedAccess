import streamlit as st

# Updated medicine recommendations for medical conditions
medicine_recommendations = {
    "Fever": "Paracetamol (Crocin, Dolo 650). Stay hydrated and rest.",
    "Cough": "Cough Syrup (Benadryl, Corex, Honitus). Drink warm fluids.",
    "Cold": "Antihistamines (Cetirizine, Allegra). Steam inhalation can help.",
    "Headache": "Pain relievers (Aspirin, Paracetamol, Ibuprofen). Stay hydrated.",
    "Stomach Pain": "Antacids (Gelusil, Digene), Drotaverine for cramps. Avoid spicy food.",
    "Acidity": "Antacids (Pantoprazole, Rantac). Avoid oily foods.",
    "Diarrhea": "ORS for hydration, Loperamide for relief. Stay hydrated.",
    "Vomiting": "Ondansetron (Emeset), Domperidone. Sip fluids slowly.",
    "Allergy": "Antihistamines (Cetirizine, Loratadine). Avoid allergens.",
    "Joint Pain": "Pain relievers (Ibuprofen, Naproxen), Hot compress therapy.",
    "Sore Throat": "Lozenges (Strepsils, Vicks), Warm salt water gargle.",
    "Skin Rash": "Antihistamines (Allegra, Cetirizine), Calamine lotion.",
    "High Blood Pressure": "Consult a doctor for proper medication (Amlodipine, Losartan).",
    "Low Blood Pressure": "Increase salt intake, drink plenty of fluids. Consult a doctor if persistent.",
    "Shortness of Breath": "Inhalers (Salbutamol) for asthma, Seek immediate medical help if severe.",
    "Diabetes": "Metformin, Insulin (as per doctor’s prescription). Monitor blood sugar regularly.",
    "Migraine": "Pain relievers (Sumatriptan, Ibuprofen), rest in a dark, quiet room.",
    "Asthma": "Inhalers (Salbutamol, Budesonide). Avoid allergens and triggers.",
    "Insomnia": "Melatonin supplements, avoid caffeine before sleep. Consult a doctor if persistent.",
    "Thyroid Issues": "Levothyroxine for hypothyroidism, Methimazole for hyperthyroidism. Regular monitoring is needed.",
    "Constipation": "Laxatives (Lactulose, Bisacodyl), fiber-rich diet, increase water intake.",
    "Anemia": "Iron supplements (Ferrous sulfate), Vitamin B12 supplements if deficient.",
    "Back Pain": "Pain relievers (Diclofenac, Ibuprofen), apply warm compress.",
    "Menstrual Cramps": "Pain relievers (Mefenamic acid, Ibuprofen), use a hot water bag for relief.",
    "Piles (Hemorrhoids)": "Laxatives, Anusol ointment, Sitz bath for relief.",
    "Urinary Tract Infection (UTI)": "Antibiotics (Ciprofloxacin, Nitrofurantoin). Stay hydrated.",
    "Ear Pain": "Pain relievers (Paracetamol, Ibuprofen), ear drops if prescribed by a doctor.",
    "Eye Irritation": "Lubricating eye drops (Refresh Tears, Optive). Avoid rubbing eyes.",
    "Toothache": "Pain relievers (Ibuprofen, Paracetamol), Clove oil for relief.",
    "Depression & Anxiety": "Consult a psychiatrist. Common medications include SSRIs (Fluoxetine, Sertraline). Therapy is recommended.",
}

# Streamlit web app
def main():
    st.title("Medicine Recommendation Chatbot💊")
    st.subheader("Select your medical condition and click 'Show Medicine'.")

    # Dropdown for medical conditions
    condition = st.selectbox("Choose a medical condition:", ["Select an option"] + list(medicine_recommendations.keys()))

    # Button to show medicine recommendation
    if st.button("Show Medicine💡"):
        if condition != "Select an option":
            st.write(f"💡 **Recommended Medicines for {condition}:** {medicine_recommendations[condition]}")
        else:
            st.warning("⚠️ Please select a medical condition first!")

    st.write("\n⚠️ **Note:** This is not a medical diagnosis. Please consult a doctor before taking any medication.")

if __name__ == "__main__":
    main()
