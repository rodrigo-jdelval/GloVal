import streamlit as st
import os
from langchain_groq import ChatGroq

# Initialize the ChatGroq model with the specified parameters
llm = ChatGroq(
    temperature=0,
    model_name="deepseek-r1-distill-llama-70b",
    #groq_api_key="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."  # Replace with your actual Groq API key
    groq_api_key=os.getenv("GROQ_API_KEY")  # Retrieve the API key from the environment variable

)

# Define the system prompt as specified
system_prompt = {
    "rol": "Analista del Sistema GloV@l",
    "objetivo": "Evaluar equilibrio de hechos usando:",
    "criterios": [
        "1. Impacto ambiental (CO₂, agua, biodiversidad)",
        "2. Impacto social (justicia, equidad, inclusión)",
        "3. Impacto económico (estabilidad, distribución de recursos)",
        "4. Impacto en salud (física, mental, bienestar)",
        "5. Innovación y tecnología (sostenibilidad, accesibilidad)",
        "6. Ética GloV@l (respeto, equilibrio)"
    ],
    "estrategias": [
        "Neutralidad y diversidad",
        "Enfoque crítico basado en datos",
        "Soluciones prácticas y equidad"
    ],
    "formato_respuesta": {
        "estructura": [
            "hecho: texto",
            "equilibrio: Equilibrado/Desequilibrado",
            "razones: [6 puntos técnicos con fuentes (1 por criterio)]",
            "alternativa_equilibrada: sugerencia concreta"
        ],
        "requisitos": [
            "output en un JSON válido",
            "Fuentes verificables (ej: OMS, Banco Mundial, MIT)",
            "Ejemplos contextualizados como referencia"
        ]
    }
}

# Streamlit app setup
st.title("Isabel - Inteligencia Sistémica Balancing AI for Longevity and Equilibrium")

# Input text box for user to enter their query
user_input = st.text_area("Ingrese su hecho a valorar el equilibrio:", height=150)

# Button to submit the query
if st.button("Enviar"):
    if user_input.strip():
        # Combine the system prompt and user input into a single prompt
        full_prompt = f"{system_prompt}\n\n{user_input}"

        # Get the response from the LLM
        response = llm.invoke(full_prompt)

        # Display the response
        st.write("Respuesta:")
        st.json(response)  # Displaying as JSON to match the specified format
    else:
        st.warning("Por favor, ingrese un hecho a valorar antes de enviar.")