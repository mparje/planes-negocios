import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Crear una interfaz de usuario con streamlit
st.title("Generador de planes de negocios")

# Solicitar al usuario que ingrese su idea de negocio
wish = st.text_input("¿Qué idea tienes? O deja en blanco y espera.")

# Utilizar ChatGPT para generar un plan de negocios para la idea del usuario
model_engine = "davinci"
prompt = (f"Hola, estoy interesado en crear una empresa basada en la idea '{wish}'. ¿Podrías ayudarme a crear un plan de negocios? Incluye nombre de la idea, una línea corta, persona objetivo del usuario, puntos de dolor del usuario a resolver, principales propuestas de valor, descripción detallada de la idea, canales de ventas y marketing, fuentes de ingresos por ventas, estructuras de costos, actividades clave, recursos clave, socios clave, pasos de validación de la idea, costo estimado del primer año de operación y desafíos comerciales potenciales a considerar.")

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

# Obtén el texto del resultado del plan de negocios
business_plan = completions.choices[0].text

# Muestra el plan de negocios en la aplicación
st.markdown(business_plan)
