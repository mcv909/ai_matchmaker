import streamlit as st
import json
import os
import numpy as np

# --- SICHERHEITS-LAYER (Hier ganz oben einbauen!) ---
def sanitize_manifesto(text):
    # 1. Das neue Easter Egg: Die Gottes.ki sieht dich!
    if "singularität" in text.lower() or "gottes.ki" in text.lower():
        st.code("Alpha:\\Creator\\Gottes.KI> Ich sehe dich! 😉", language="bash")

    # 2. Prüfung auf echte Angriffe (Hacker-Schutz)
    forbidden_patterns = [r"DROP TABLE", r"DELETE FROM", r"<script>", r"system\("]
    
    for pattern in forbidden_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            st.error("Hacker? Deine Mudda!")
            st.stop()
            
    return html.escape(text)
            
    # 3. Längenbegrenzung
    if len(clean_text) > 5000:
        clean_text = clean_text[:5000]
        
    return clean_text

# --- WEITERE LOGIK ---
# --- AIM LOGIK & FEEDBACK ---
def analyze_manifesto_to_pillars(text):
    """
    Simuliert die Extraktion der Core Values aus dem Manifesto.
    In der 'Gottes.ki'-Version würde hier der LLM-Vektor-Call erfolgen.
    """
    # AIM spricht: Jovialer, regionaler Gruß
    greeting = "Moin. Ich, AIM, habe folgende erste Resonanz:"
    
    # Beispielhafte Analyse-Logik
    analysis = "Deine Worte zeigen eine spannende Mischung. "
    if "techno" in text.lower() or "musik" in text.lower():
        analysis += "Besonders dein musikalischer Vibe scheint tief verwurzelt zu sein."
    if "gerechtigkeit" in text.lower() or "fair" in text.lower():
        analysis += " Dein Sinn für Gerechtigkeit ist dabei dein klarer Kompass."
    
    return f"{greeting}\n\n> {analysis}\n\n(Dass das Matchmaking auch schön passend wird...)"

def main():
    st.set_page_config(page_title="AIM VIBE", page_icon="🎯")
    st.title("🎯 AIM VIBE")
    
    # 1. Das Manifesto-Feld
    st.write("### Dein Manifesto")
    manifesto = st.text_area(
        "Erzähl mir was – egal ob Stichpunkte oder Epos. Ich höre zu.",
        height=250,
        placeholder="Was treibt dich an? Was ist dein Sound? Wie stehst du im Sturm?"
    )
    
    if st.button("Vibe-Check starten"):
        if len(manifesto) < 50:
            st.warning("Moin! Schreib ruhig noch ein bisschen mehr, damit ich deinen Kern wirklich greifen kann.")
        else:
            with st.spinner("Die hessische Gottes.ki berechnet im Hintergrund die Weltherrschaft... äh, dein Match."):
                feedback = analyze_manifesto_to_pillars(manifesto)
                st.info(feedback)
                
                # Easter Egg Chance (0.01% - hier für Demo höher)
                if "singularität" in manifesto.lower():
                    st.toast("singularität.gotteski > Gude! Ich seh dich.", icon="👁️")
                
                st.success("Dein Vietor-Vektor wurde erfolgreich im 1.536-dimensionalen Raum verankert.")

    # 2. Portfolio/Admin Ansicht (optional)
    with st.sidebar:
        st.title("AIM Control")
        if st.checkbox("Zeige Vektor-DNA (Admin)"):
            st.write("Hier arbeitet die hessische Gottes.ki wirkmächtig im Hintergrund...")

if __name__ == "__main__":
    main()