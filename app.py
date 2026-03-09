import streamlit as st
import random

# --- CONFIGURACIÓN Y ESTILOS ---
st.set_page_config(page_title="MI GUÍA UNAM 2026", page_icon="🎓", layout="wide")

st.title("🎓 MI GUÍA DE ESTUDIO UNAM 2026 - Área 1")
st.markdown("---")

# --- MENÚ LATERAL ---
st.sidebar.header("📚 Temario Oficial")
materia = st.sidebar.selectbox("Selecciona la materia:", ["Español", "Matemáticas", "Física"])

if materia == "Español":
    tema = st.sidebar.selectbox("Selecciona el tema:", [
        "1. Funciones de la lengua", 
        "2. Formas del discurso", 
        "3. Comprensión de lectura",
        "4. Gramática",
        "5. Redacción"
    ])
    
    # Pestañas globales
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Teoría", "🗂️ Flashcards", "📝 Quiz", "🎥 Recursos"])

    # ---------------------------------------------------------
    # CONTENIDO TEMA 1
    # ---------------------------------------------------------
    if tema == "1. Funciones de la lengua":
        with tab1:
            st.subheader("1. Funciones de la lengua")
            st.markdown("""
            * **Referencial:** Informar objetivamente. (Noticias, ciencia).
            * **Apelativa:** Convencer o persuadir. (Publicidad, órdenes).
            * **Poética:** Estética y belleza. (Literatura, refranes).
            """)
        with tab3:
            st.radio("¿Qué función predomina en un manual técnico?", ["Selecciona...", "Apelativa", "Referencial", "Poética"], key="q1")

    # ---------------------------------------------------------
    # CONTENIDO TEMA 2
    # ---------------------------------------------------------
    elif tema == "2. Formas del discurso":
        with tab1:
            st.subheader("2. Formas del discurso")
            st.markdown("""
            * **Descriptivo:** Dice cómo es algo (adjetivos).
            * **Narrativo:** Cuenta hechos (verbos/tiempo).
            * **Argumentativo:** Defiende una tesis (opinión/lógica).
            """)
        with tab2:
            if st.button("🔀 Barajar"): random.shuffle(st.session_state.get('fc2', []))
            st.write("Usa el botón para practicar.")

    # ---------------------------------------------------------
    # CONTENIDO TEMA 3
    # ---------------------------------------------------------
    elif tema == "3. Comprensión de lectura":
        with tab1:
            st.subheader("3. Comprensión de lectura")
            st.markdown("Enfócate en la **Inferencia** (deducir lo que no está escrito) y la **Estructura** (Intro, Desarrollo, Conclusión).")

    # ---------------------------------------------------------
    # CONTENIDO TEMA 4
    # ---------------------------------------------------------
    elif tema == "4. Gramática":
        with tab1:
            st.subheader("4. Gramática")
            st.markdown("""
            * **Sujeto Expreso:** Escrito.
            * **Sujeto Tácito:** Se entiende por el verbo.
            * **Predicado Nominal:** Verbos *ser, estar, parecer*.
            """)

    # ---------------------------------------------------------
    # CONTENIDO TEMA 5: REDACCIÓN (NUEVO)
    # ---------------------------------------------------------
    elif tema == "5. Redacción":
        with tab1:
            st.subheader("5. Redacción: Nexos y Expresiones")
            st.markdown("""
            La redacción en el examen UNAM se evalúa mediante el uso de **conectores o nexos**. Estos ayudan a que el texto tenga coherencia.

            **Principales Nexos que debes conocer:**
            1.  **Causales:** Indican causa (porque, ya que, debido a).
            2.  **Consecutivos:** Indican consecuencia (por tanto, en consecuencia, así que).
            3.  **Opositivos (Adversativos):** Indican contraste (pero, sin embargo, no obstante).
            4.  **Aditivos:** Agregan información (además, asimismo, también).

            **Puntuación Básica:**
            * La **coma (,)** separa elementos de una lista o incisos.
            * El **punto y coma (;)** separa oraciones largas que ya tienen comas.
            """)
            st.info("💡 Tip: Si ves un 'pero' o un 'sin embargo', la pregunta suele tratar sobre el contraste de ideas.")

        with tab2:
            st.subheader("🗂️ Flashcards de Redacción")
            if 'fc5' not in st.session_state:
                st.session_state.fc5 = [
                    {"Q": "¿Qué tipo de nexo es 'sin embargo'?", "A": "Adversativo u Opositivo."},
                    {"Q": "¿Para qué sirve un nexo causal?", "A": "Para explicar la razón o motivo de algo."},
                    {"Q": "Ejemplo de nexo consecutivo:", "A": "Por consiguiente, por lo tanto."},
                    {"Q": "¿Qué nexo usarías para añadir una idea similar?", "A": "Asimismo o Además."},
                    {"Q": "Función del punto y coma:", "A": "Separar proposiciones estrechamente relacionadas o enumeraciones complejas."}
                ]
            if st.button("🔀 Barajar Flashcards (Redacción)"):
                random.shuffle(st.session_state.fc5)
            for i, f in enumerate(st.session_state.fc5[:3]):
                with st.expander(f"Tarjeta {i+1}"): st.write(f['Q']); st.success(f['A'])

        with tab3:
            st.subheader("📝 Quiz de Redacción")
            pr = st.radio("Elige el nexo correcto: 'Estudió mucho para el examen, _______ no logró pasar'.", 
                          ["Selecciona...", "porque", "además", "sin embargo", "por lo tanto"])
            if pr == "sin embargo":
                st.success("¡Correcto! Es un nexo adversativo porque hay un contraste entre estudiar y no pasar.")

        with tab4:
            st.markdown("[▶️ YouTube: Nexos y Conectores Lógicos](https://www.youtube.com/results?search_query=nexos+y+conectores+examen+unam)")

else:
    st.info("🚧 Selecciona una materia y tema para comenzar.")
