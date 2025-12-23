import streamlit as st

# Setup der Seite
st.set_page_config(page_title="AI-Matchmaker MVP", page_icon="🚀")

st.title("AI-Matchmaker: Der Vibe-Check")
st.subheader("Finde heraus, ob die Chemie mathematisch stimmt.")

# Input-Bereich
st.write("### Erzähl uns von dir")
user_input = st.text_area("Was sind deine Core-Values und was bedeutet Musik für dich?", 
                         placeholder="Z.B. Gerechtigkeit ist mir wichtig, ich liebe Techno...")

# Button für die Logik
if st.button("Profil-Vektor erstellen"):
    if user_input:
        st.success("Daten empfangen!")
        st.write("**Dein vorläufiges Profil-Paket:**")
        # Hier simulieren wir erst mal nur die Datenstruktur
        st.json({
            "status": "Vektorisierung bereit",
            "input_length": len(user_input),
            "note": "Morgen verknüpfen wir das mit der KI-Logik."
        })
    else:
        st.warning("Bitte gib erst etwas über dich ein.")

st.sidebar.info("Projekt: Holiday-Hack | Status: v0.1")