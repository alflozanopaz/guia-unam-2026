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
    # Agregamos el Tema 4 a la lista
    tema = st.sidebar.selectbox("Selecciona el tema:", [
        "1. Funciones de la lengua", 
        "2. Formas del discurso", 
        "3. Comprensión de lectura",
        "4. Gramática"
    ])
    
    # ---------------------------------------------------------
    # TEMAS ANTERIORES (Simplificados para navegación)
    # ---------------------------------------------------------
    if tema == "1. Funciones de la lengua":
        st.header("1. Funciones de la lengua")
        st.info("Repasa: Referencial, Apelativa y Poética.")
    elif tema == "2. Formas del discurso":
        st.header("2. Formas del discurso")
        st.info("Repasa: Descriptivo, Narrativo y Argumentativo.")
    elif tema == "3. Comprensión de lectura":
        st.header("3. Comprensión de lectura")
        st.info("Repasa: Estructura del texto e Inferencia.")

    # ---------------------------------------------------------
    # TEMA 4: GRAMÁTICA (NUEVO)
    # ---------------------------------------------------------
    elif tema == "4. Gramática":
        st.header("4. Gramática: La Oración, Sujeto y Predicado")
        
        tab1, tab2, tab3, tab4 = st.tabs(["📖 Teoría", "🗂️ Flashcards", "📝 Quiz", "🎥 Recursos"])
        
        with tab1:
            st.subheader("Resumen Teórico")
            st.markdown("""
            **4.1 La Oración**
            Es la unidad mínima de lenguaje con sentido completo. Se divide principalmente en Sujeto y Predicado.

            **4.2 Uso del Sujeto**
            Es quien realiza la acción del verbo o de quien se dice algo.
            * **Sujeto Explícito (Expreso):** Aparece escrito en la oración. 
                * *Ej:* "**El átomo** es la unidad básica."
            * **Sujeto Tácito (Morfológico/Implícito):** No está escrito, pero se sobreentiende por la terminación del verbo.
                * *Ej:* "Estudiamos para el examen." (Sujeto: Nosotros).

            **4.3 Uso del Predicado**
            Es lo que se dice del sujeto. Su núcleo siempre es un **verbo conjugado**.
            * **Predicado Nominal:** Usa verbos copulativos (ser, estar, parecer). Atribuye una cualidad al sujeto.
                * *Ej:* "La física **es fascinante**."
            * **Predicado Verbal:** Usa verbos de acción.
                * *Ej:* "La luz **viaja en el vacío**."
            """)
            
            st.markdown("### Mapa de la Estructura")
            st.code("""
            ORACIÓN BIMEMBRE
            ├── SUJETO (¿Quién?)
            │    └── Núcleo: Sustantivo o Pronombre
            └── PREDICADO (¿Qué hace / Qué es?)
                 └── Núcleo: Verbo Conjugado
            """)

        with tab2:
            st.subheader("🔀 Flashcards de Gramática")
            if 'flashcards_t4' not in st.session_state:
                st.session_state.flashcards_t4 = [
                    {"Q": "¿Qué es el sujeto tácito?", "A": "Aquel que no está escrito pero se infiere por la conjugación del verbo."},
                    {"Q": "¿Cuál es el núcleo del sujeto?", "A": "Un sustantivo o un pronombre."},
                    {"Q": "¿Cuál es el núcleo del predicado?", "A": "Un verbo conjugado."},
                    {"Q": "¿Qué verbos caracterizan al predicado nominal?", "A": "Ser, estar o parecer (verbos copulativos)."},
                    {"Q": "En 'Corrimos por el parque', ¿cuál es el sujeto?", "A": "Sujeto tácito: Nosotros."},
                    {"Q": "En 'La gravedad es una fuerza', ¿qué tipo de predicado hay?", "A": "Predicado nominal (verbo 'es')."},
                    {"Q": "¿Cuál es el sujeto en: 'A los ingenieros les gusta el cálculo'?", "A": "El cálculo (porque es lo que realiza la acción de gustar)."},
                    {"Q": "¿Qué es una oración bimembre?", "A": "Aquella que tiene sujeto y predicado claramente definidos."},
                    {"Q": "¿Cómo se llama el sujeto que sí aparece escrito?", "A": "Sujeto Expreso o Explícito."},
                    {"Q": "Identifica el núcleo del predicado: 'El sol emite radiación'.", "A": "Emite."}
                ]

            if st.button("🔀 Barajar Flashcards (Gramática)"):
                random.shuffle(st.session_state.flashcards_t4)

            for i, fc in enumerate(st.session_state.flashcards_t4[:5]):
                with st.expander(f"Tarjeta {i+1}: {fc['Q']}"):
                    st.success(fc['A'])

        with tab3:
            st.subheader("Simulador de Preguntas UNAM")
            
            p1 = st.radio(
                "1. Identifica el sujeto en la siguiente oración: 'En el laboratorio de química, realizaron el experimento los alumnos'.",
                ("Selecciona...", "A) El laboratorio", "B) Realizaron", "C) Los alumnos", "D) El experimento", "E) Química")
            )
            if p1 == "C) Los alumnos":
                st.success("¡Correcto! Aunque esté al final, 'los alumnos' son quienes realizan la acción de realizar.")
            elif p1 != "Selecciona...":
                st.error("Incorrecto. Recuerda preguntar al verbo: ¿Quiénes realizaron?")

            st.divider()

            p2 = st.radio(
                "2. ¿Qué tipo de sujeto tiene la oración: 'Mañana iremos a la biblioteca'?",
                ("Selecciona...", "A) Expreso", "B) Compuesto", "C) Tácito", "D) Indefinido", "E) Nominal")
            )
            if p2 == "C) Tácito":
                st.success("¡Correcto! El sujeto no está escrito, pero se entiende que es 'Nosotros'.")
            elif p2 != "Selecciona...":
                st.error("Incorrecto. Como no ves el pronombre escrito, es morfológico o tácito.")

        with tab4:
            st.subheader("Recursos de Apoyo")
            st.markdown("[▶️ YouTube: El Sujeto y el Predicado para el examen UNAM](https://www.youtube.com/results?search_query=sujeto+y+predicado+examen+unam)")
            st.markdown("[▶️ YouTube: Sujeto Tácito y Expreso](https://www.youtube.com/results?search_query=sujeto+tacito+y+expreso+ejemplos)")

else:
    st.info("🚧 Sección de Ciencias en desarrollo.")
