# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 23:03:52 2025

@author: PC
"""

import json
import os

# Archivo donde se guardará la base de conocimiento
DB_FILE = "knowledge.json"

# Si no existe el archivo de conocimiento, lo creamos con respuestas iniciales
if not os.path.exists(DB_FILE):
    initial_data = {
        "hola": "¡Hola! ¿Cómo estás?",
        "como estas": "Estoy muy bien, gracias. ¿Y tú?",
        "de que te gustaria hablar": "Podemos hablar de tecnología, música, ciencia o lo que quieras."
    }
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(initial_data, f, indent=4, ensure_ascii=False)

# Cargar conocimiento
with open(DB_FILE, "r", encoding="utf-8") as f:
    knowledge = json.load(f)

print("=== Chat con Módulo de Adquisición de Conocimiento ===")
print("Escribe 'salir' para terminar.\n")

while True:
    user_input = input("Tú: ").strip().lower()
    
    if user_input == "salir":
        print("Chat finalizado. ¡Hasta luego!")
        break
    
    if user_input in knowledge:
        print("Bot:", knowledge[user_input])
    else:
        print("Bot: No sé cómo responder eso 🤔")
        new_answer = input("¿Qué debería responder a esa pregunta?: ")
        knowledge[user_input] = new_answer
        
        # Guardar nuevo conocimiento
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(knowledge, f, indent=4, ensure_ascii=False)
        
        print("Bot: ¡Gracias! He aprendido algo nuevo 🎉")
