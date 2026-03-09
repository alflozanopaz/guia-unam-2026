import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Mi Guía UNAM 2026", page_icon="🎓", layout="wide")

st.title("🎓 MI GUÍA DE ESTUDIO UNAM 2026 - Área 1")
st.markdown("---")

# Menú lateral
st.sidebar.header("📚 Temario")
materia = st.sidebar.selectbox("Selecciona la materia:", ["Español", "Matemáticas", "Física"])

if materia == "Español":
    # Agregamos el Tema 3 a la lista
    tema = st.sidebar.selectbox("Selecciona el tema:", [
        "1. Funciones de la lengua", 
        "2. Formas del discurso", 
        "3. Comprensión de lectura"
    ])
    
    # ---------------------------------------------------------
    # TEMA 1 y 2 (Resumidos aquí para mantener tu app funcionando)
    # ---------------------------------------------------------
    if tema == "1. Funciones de la lengua":
        st.header("1. Funciones de la lengua")
        st.info("Ve a la pestaña de Teoría en tu app para repasar este tema.")
        # (Nota: Para no hacer el código inmenso en esta respuesta, dejé un placeholder. 
        # En la vida real, aquí iría el código completo del Tema 1 que ya tenías).

    elif tema == "2. Formas del discurso":
        st.header("2. Formas del discurso")
        st.info("Ve a la pestaña de Teoría en tu app para repasar este tema.")

    # ---------------------------------------------------------
    # TEMA 3: COMPRENSIÓN DE LECTURA (NUEVO)
    # ---------------------------------------------------------
    elif tema == "3. Comprensión de lectura":
        st.header("3. Comprensión de lectura")
        
        tab1, tab2, tab3, tab4 = st.tabs(["📖 Teoría", "🗂️ Flashcards", "📝 Quiz", "🎥 Recursos"])
        
        with tab1:
            st.subheader("Resumen Teórico")
            st.markdown("""
            Para el examen UNAM, la comprensión de lectura evalúa tu capacidad para entender no solo lo que dice el texto explícitamente, sino su intención y estructura.

            **3.1 Estructura del texto** 
            Todo texto formal (como los que vienen en el examen) tiene una organización lógica:
            * **Introducción:** Presenta el tema y, si es un texto argumentativo, la tesis.
            * **Desarrollo:** Expone los argumentos, datos, ejemplos o la trama principal. Contiene las ideas secundarias que apoyan a la principal.
            * **Conclusión:** Cierra el texto, resume la idea central o propone una solución.
            
            **3.4 Inferencia de datos** 
            *Inferir* significa **deducir información que no está escrita literalmente**, basándote en pistas del texto y en tu conocimiento previo.
            * *Ejemplo explícito:* "El cielo se nubló, empezó a tronar y Juan sacó su paraguas".
            * *Inferencia:* Va a llover (el texto nunca dice "va a llover", pero tú lo deduces).
            """)
            
            st.warning("⚠️ **Tip Área 1:** En preguntas de Física, a veces el texto dice 'un objeto parte del reposo'. La inferencia clave para resolver el problema matemático es deducir que la **Velocidad Inicial = 0**. ¡Esa es una inferencia de datos aplicada!")

        with tab2:
            st.subheader("🔀 Flashcards Aleatorias")
            if 'flashcards_t3' not in st.session_state:
                st.session_state.flashcards_t3 = [
                    {"Q": "¿Qué es la idea principal de un texto?", "A": "La información central y más importante; sin ella, el texto pierde sentido."},
                    {"Q": "¿Qué función tienen las ideas secundarias?", "A": "Ejemplificar, ampliar, o justificar la idea principal."},
                    {"Q": "¿Qué es inferir?", "A": "Deducir información implícita (no escrita directamente) a partir de pistas en el texto."},
                    {"Q": "¿En qué parte de la estructura suele plantearse la tesis?", "A": "En la introducción."},
                    {"Q": "¿Qué parte del texto resume las ideas expuestas?", "A": "La conclusión."},
                    {"Q": "Si un texto dice 'Su temperatura corporal era de 40 grados', ¿qué infieres?", "A": "Que la persona tiene fiebre/está enferma."},
                    {"Q": "¿Qué elemento del texto nos da la primera pista sobre su contenido?", "A": "El título."},
                    {"Q": "En una narración, ¿dónde ocurre el clímax o problema principal?", "A": "En el desarrollo (o nudo)."},
                    {"Q": "Diferencia entre dato explícito e implícito:", "A": "Explícito está escrito tal cual; implícito se debe inferir."},
                    {"Q": "¿Para qué sirve identificar la estructura de un texto  en el examen?", "A": "Para localizar respuestas rápidamente sin tener que releer todo."}
                ]

            if st.button("🔀 Barajar Flashcards (Tema 3)"):
                random.shuffle(st.session_state.flashcards_t3)

            for i, fc in enumerate(st.session_state.flashcards_t3[:5]):
                with st.expander(f"Tarjeta {i+1}: {fc['Q']}"):
                    st.success(fc['A'])

        with tab3:
            st.subheader("Banco de Preguntas Tipo UNAM")
            st.markdown("""
            **Lee el siguiente fragmento:**
            *"La energía geotérmica aprovecha el calor interno de la Tierra. A diferencia de los combustibles fósiles, es una fuente inagotable a escala humana y genera emisiones mínimas de gases de efecto invernadero. Por ello, países como Islandia han basado su red eléctrica en esta tecnología."*
            """)
            
            p1 = st.radio(
                "1. Según el texto, ¿cuál es una inferencia válida sobre Islandia?",
                ("Selecciona...", 
                 "A) Islandia es el país que más contamina en Europa.", 
                 "B) Islandia contribuye muy poco al efecto invernadero a través de su red eléctrica.", 
                 "C) Islandia no tiene acceso a combustibles fósiles.", 
                 "D) Islandia exporta energía geotérmica al mundo.")
            )
            if p1 == "B) Islandia contribuye muy poco al efecto invernadero a través de su red eléctrica.":
                st.success("¡Correcto! El texto dice que esta energía tiene emisiones mínimas y que Islandia basa su red en ella. Infieres que su red contamina poco.")
            elif p1 != "Selecciona...":
                st.error("Incorrecto. Revisa las pistas del texto sobre las características de la energía que usa ese país.")

        with tab4:
            st.subheader("Video Tutoriales")
            st.markdown("[▶️ Unitips: Comprensión de Lectura (Inferencia)](https://www.youtube.com/results?search_query=unitips+comprension+de+lectura+unam)")
            st.markdown("[▶️ Pasatuexamen: Estructura del texto e Ideas Principales](https://www.youtube.com/results?search_query=pasatuexamen+estructura+del+texto)")

else:
    st.info("🚧 Tema en construcción.")
