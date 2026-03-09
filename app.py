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
        "5. Redacción",
        "6. Vocabulario",
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
# =========================================================
    # UNIDAD 6: VOCABULARIO
    # =========================================================
    elif tema == "6. Vocabulario":
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📖 Teoría", "🌿 Mapa Conceptual", "🗂️ Flashcards", "📝 Banco de Preguntas", "🎥 Videos"
        ])
        
        with tab1:
            st.header("6. Vocabulario")
            st.write("Esta unidad se enfoca en el manejo preciso de las palabras y sus significados.")
            
            st.markdown("### 6.3 Antónimos")
            st.write("Son palabras que tienen significados **opuestos** o contrarios entre sí. Deben pertenecer a la misma categoría gramatical (sustantivo con sustantivo, etc.).")
            st.info("**Ejemplo:** Efímero ↔ Duradero | Omitir ↔ Mencionar.")
            
            st.markdown("### 6.4 Homófonos")
            st.write("Son palabras que **suenan igual** pero se escriben de forma distinta y tienen significados diferentes.")
            st.warning("**Ejemplo de examen:** \n* **Bello** (hermoso) / **Vello** (pelo corto).\n* **Valla** (cerca/obstáculo) / **Vaya** (del verbo ir) / **Baya** (fruto).")
            
        with tab2:
            st.subheader("Mapa Conceptual: Relaciones Semánticas")
            st.graphviz_chart('''
                digraph {
                    Vocabulario -> Antónimos
                    Vocabulario -> Homófonos
                    Antónimos -> "Significado Opuesto"
                    Homófonos -> "Sonido Igual"
                    Homófonos -> "Escritura Diferente"
                }
            ''')

        with tab3:
            st.subheader("Flashcards de Vocabulario")
            if 'fc6' not in st.session_state:
                st.session_state.fc6 = [
                    {"Q": "Antónimo de 'Altruista':", "A": "Egoísta."},
                    {"Q": "Homófono: ¿'Acerbo' o 'Acervo' para cultura?", "A": "Acervo (con 'v')."},
                    {"Q": "Antónimo de 'Sapiencia':", "A": "Ignorancia."},
                    {"Q": "Homófono: ¿'Cocer' o 'Coser' para ropa?", "A": "Coser (con 's')."},
                    {"Q": "¿Qué es un antónimo directo?", "A": "Palabras que niegan totalmente a la otra (Vivo/Muerto)."}
                ]
            if st.button("🔀 Mezclar Vocabulario"): random.shuffle(st.session_state.fc6)
            for f in st.session_state.fc6[:5]:
                with st.expander(f["Q"]): st.success(f["A"])

        with tab4:
            st.subheader("Banco de Preguntas")
            v1 = st.radio("1. Elige el antónimo de la palabra en mayúsculas: 'Su actitud fue LAUDABLE'.", 
                          ["Selecciona...", "A) Elogiable", "B) Censurable", "C) Notable", "D) Admirable"])
            if v1 == "B) Censurable":
                st.success("¡Correcto! Laudable significa digno de alabanza; lo opuesto es algo digno de crítica o censura.")
            
            st.divider()
            
            v2 = st.radio("2. Elige la opción que completa correctamente: 'Necesitas ____ la ropa antes de que ____ el agua'.",
                          ["Selecciona...", "A) coser / cocer", "B) cocer / coser", "C) coser / coser", "D) cocer / cocer"])
            if v2 == "A) coser / cocer":
                st.success("¡Correcto! Coser es unir con hilo; Cocer es hervir alimentos.")
else:
    st.info("🚧 Selecciona una materia y unidad para ver el contenido completo.")
