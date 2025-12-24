import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Umgebung laden
load_dotenv()
client = OpenAI()

# 2. Dein Statement (Die Basis für den Vibe-Check)
text_input = "Musik ist für mich kein Konsumgut, sondern ein essentielles Ordnungssystem (Fokus auf Techno/Klangästhetik)."

print("Starte Vektorisierung...")

# 3. Den Vektor erzeugen (1536 Dimensionen pure Mathematik)
response = client.embeddings.create(
    input=text_input,
    model="text-embedding-3-small"
)

# Den eigentlichen Vektor (eine Liste von Zahlen) extrahieren
vector = response.data[0].embedding

print(f"\nErfolgreich! Dein Statement wurde in einen Vektor mit {len(vector)} Dimensionen verwandelt.")
print(f"Hier sind die ersten 10 Dimensionen deines Profils:\n{vector[:10]}")