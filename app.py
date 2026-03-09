import streamlit as st
import random

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="MI GUÍA UNAM 2026", page_icon="🎓", layout="wide")

# Estilos CSS para que se vea profesional y sea fácil de leer
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #e1e4e8; 
        border-radius: 5px 5px 0 0; 
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] { 
        background-color: #004b8d !important; 
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 MI GUÍA DE ESTUDIO UNAM 2026")
st.subheader("Área 1: Ciencias Físico-Matemáticas y de las Ingenierías")
st.divider()

# --- NAVEGACIÓN LATERAL ---
st.sidebar.header("📂 CONTENIDO")
materia = st.sidebar.selectbox("Materia", ["Español", "Matemáticas", "Física"])

if materia == "Español":
    # PASO A: Aquí es donde se enlistan las unidades
    tema = st.sidebar.selectbox("Unidad", [
        "1. Funciones de la lengua", 
        "2. Formas del discurso", 
        "3. Comprensión de lectura",
        "4. Gramática",
        "5. Redacción","6. Vocabulario"
    ])

    # Creación de las pestañas
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Teoría", "🌿 Mapa Conceptual", "🗂️ Flashcards", "📝 Banco de Preguntas", "🎥 Videos"
    ])

    # =========================================================
    # UNIDAD 1: FUNCIONES DE LA LENGUA
    # =========================================================
    if tema == "1. Funciones de la lengua":
        with tab1:
            st.header("1. Funciones de la lengua")
            st.write("**Definición:** Son los diferentes objetivos, propósitos y servicios que se le dan al lenguaje al comunicarse.")
            
            st.markdown("### 1.1 Función Referencial")
            st.write("Su intención es **informar** hechos, datos o conceptos de manera objetiva. Evita opiniones personales.")
            st.success("**Ejemplo:** 'La fórmula del agua es H2O' o 'El examen de la UNAM es en mayo'.")
            
            st.markdown("### 1.2 Función Apelativa")
            st.write("Busca **convencer o persuadir** al receptor para que piense o actúe de una manera determinada.")
            st.success("**Ejemplo:** '¡Compra este libro ahora!' o '¿Podrías cerrar la ventana?'.")
            
            st.markdown("### 1.3 Función Poética")
            st.write("Busca **belleza o armonía** en el mensaje. No importa solo qué se dice, sino cómo se dice (refranes, poesía, literatura).")
            st.success("**Ejemplo:** 'Tus ojos son luceros' o 'Camarón que se duerme, se lo lleva la corriente'.")
            
        with tab2:
            st.subheader("Mapa Conceptual: Funciones")
            st.graphviz_chart('''
                digraph {
                    "Funciones de la lengua" -> "Referencial (Informa)"
                    "Funciones de la lengua" -> "Apelativa (Persuade)"
                    "Funciones de la lengua" -> "Poética (Belleza)"
                }
            ''')

        with tab3:
            st.subheader("Flashcards (Barajar para estudiar)")
            if 'fc1' not in st.session_state:
                st.session_state.fc1 = [
                    {"Q": "¿Qué función predomina en una noticia?", "A": "Referencial"},
                    {"Q": "¿Qué función busca una reacción en el oyente?", "A": "Apelativa"},
                    {"Q": "¿Qué función usa figuras literarias?", "A": "Poética"}
                ]
            if st.button("🔀 Mezclar Orden"): random.shuffle(st.session_state.fc1)
            for f in st.session_state.fc1:
                with st.expander(f["Q"]): st.info(f["A"])

        with tab4:
            st.subheader("Banco de Preguntas")
            p1 = st.radio("1. Identifica la función: '¡No tires basura!'", ["Selecciona...", "Poética", "Referencial", "Apelativa"])
            if p1 == "Apelativa": st.success("Correcto: Es una orden/petición.")

    # =========================================================
    # UNIDAD 2: FORMAS DEL DISCURSO
    # =========================================================
    elif tema == "2. Formas del discurso":
        with tab1:
            st.header("2. Formas del discurso")
            st.markdown("""
            **2.1 Descriptivo:** Describe cualidades o características. Usa muchos adjetivos. Es una 'pintura verbal'.
            **2.2 Narrativo:** Relata acciones en orden cronológico. Usa verbos de acción.
            **2.3 Argumentativo:** Expone razones para defender una tesis o convencer al lector.
            """)
            st.info("**Bibliografía sugerida:** Gramática Española, Real Academia Española.")
        with tab3:
            st.write("Flashcards listas para estudiar formas del discurso.")

    # =========================================================
    # UNIDAD 3: COMPRENSIÓN DE LECTURA
    # =========================================================
    elif tema == "3. Comprensión de lectura":
        with tab1:
            st.header("3. Comprensión de lectura")
            st.markdown("""
            **3.1 Estructura:** Introducción (Tesis), Desarrollo (Argumentos), Conclusión (Resumen).
            **3.4 Inferencia:** Deducir información no escrita (implícita).
            """)

    # =========================================================
    # UNIDAD 4: GRAMÁTICA
    # =========================================================
    elif tema == "4. Gramática":
        with tab1:
            st.header("4. Gramática")
            st.markdown("""
            * **Sujeto Expreso:** Está escrito.
            * **Sujeto Tácito:** Se entiende por el verbo.
            * **Predicado Nominal:** Verbos copulativos (ser, estar, parecer).
            """)

    # =========================================================
    # UNIDAD 5: REDACCIÓN
    # =========================================================
    elif tema == "5. Redacción":
        with tab1:
            st.header("5. Redacción")
            st.write("El uso de nexos (pero, aunque, porque) es fundamental para la coherencia.")

# --- MENSAJE DE ESPERA ---
else:
    st.info("🚧 Selecciona una materia y unidad para ver el contenido completo.")
# =========================================================
# UNIDAD 6: VOCABULARIO (BLOQUE MANUAL)
# =========================================================
elif tema == "6. Vocabulario":
    with tab1:
        st.header("6. Vocabulario")
        st.write("Aquí va la teoría de Antónimos y Homófonos...")
    with tab2:
        st.write("Aquí diseñas el mapa conceptual...")
    with tab3:
        st.write("Aquí pegas las 10 flashcards...")
    with tab4:
        st.write("Aquí pones las 10 preguntas...")
