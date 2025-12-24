import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Lade die Schlüssel aus dem Geheimversteck (.env)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 2. Den Client initialisieren
client = OpenAI(api_key=api_key)

print("Sende Test-Signal an OpenAI...")

try:
    # 3. Ein winziger Call an das Modell gpt-4o-mini
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Sag kurz 'Leitung steht!'"}],
        max_tokens=10
    )
    print(f"\nKI-Antwort: {response.choices[0].message.content}")
    print("\n--- STATUS: Verbindung perfekt! Das Gehirn ist online. ---")
except Exception as e:
    print(f"\nFehler: Da klemmt noch was. Details: {e}")