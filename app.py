import streamlit as st
import random

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="MI GUÍA UNAM 2026", page_icon="🎓", layout="wide")

# Estilo personalizado para mejorar la legibilidad
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #f0f2f6; border-radius: 4px 4px 0px 0px; gap: 1px; }
    .stTabs [aria-selected="true"] { background-color: #004b8d; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 MI GUÍA DE ESTUDIO UNAM 2026")
st.subheader("Área 1: Ciencias Físico-Matemáticas y de las Ingenierías")
st.markdown("---")

# --- MENÚ LATERAL ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/c/c9/Escudo-UNAM-escalable.svg", width=100)
st.sidebar.header("📌 Navegación")
materia = st.sidebar.selectbox("Materia:", ["Español", "Matemáticas", "Física"])

if materia == "Español":
    tema = st.sidebar.selectbox("Unidad:", [
        "1. Funciones de la lengua", 
        "2. Formas del discurso", 
        "3. Comprensión de lectura",
        "4. Gramática",
        "5. Redacción"
    ])

    # Definición de Pestañas
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Teoría Detallada", "🗂️ Flashcards Interactivas", "📝 Banco de Preguntas", "🎥 Videos y Recursos"])

    # =========================================================
    # UNIDAD 1: FUNCIONES DE LA LENGUA
    # =========================================================
    if tema == "1. Funciones de la lengua":
        with tab1:
            st.header("1. Funciones de la lengua")
            st.markdown("""
            Las funciones de la lengua representan la intención comunicativa del hablante.
            
            * **1.1 Función Referencial:** Su intención es transmitir conocimientos, datos o hechos de manera objetiva. Se centra en el mensaje y el contexto. Es común en textos científicos, noticias y monografías.
                * *Ejemplo:* "El punto de ebullición del agua es de 100°C."
            * **1.2 Función Apelativa (Conativa):** Busca convencer, persuadir o influir en el receptor para que actúe de cierta forma. Se usa en publicidad, discursos políticos y órdenes.
                * *Ejemplo:* "¡Cómpralo ya!" o "Por favor, guarda silencio."
            * **1.3 Función Poética:** Su fin es estético. Lo más importante es la forma en que se transmite el mensaje, usando figuras retóricas para embellecerlo.
                * *Ejemplo:* "Las perlas de tu boca" (en lugar de dientes).
            """)
            st.info("💡 **Dato UNAM:** Identifica la intención. Si informa = Referencial. Si convence = Apelativa. Si es artístico = Poética.")

        with tab2:
            f1 = [{"Q": "¿Qué función informa hechos?", "A": "Referencial"}, {"Q": "¿Qué función persuade?", "A": "Apelativa"}, {"Q": "¿Qué función es estética?", "A": "Poética"}]
            if st.button("🔀 Mezclar"): random.shuffle(f1)
            for i, f in enumerate(f1):
                with st.expander(f"Tarjeta {i+1}: {f['Q']}"): st.success(f['A'])

        with tab3:
            q1 = st.radio("Identifica la función: '¡Vota por el partido verde!'", ["Selecciona...", "Poética", "Referencial", "Apelativa"])
            if q1 == "Apelativa": st.success("¡Correcto! Busca influir en el voto.")

    # =========================================================
    # UNIDAD 2: FORMAS DEL DISCURSO
    # =========================================================
    elif tema == "2. Formas del discurso":
        with tab1:
            st.header("2. Formas del discurso")
            st.markdown("""
            Se refiere a cómo se organiza el texto según su propósito:
            
            * **2.1 Descriptivo:** Presenta características de objetos, personas o lugares (usa muchos adjetivos). "Dibuja con palabras".
            * **2.2 Narrativo:** Relata eventos en una secuencia temporal (predominan los verbos de acción). Cuentos, novelas, noticias.
            * **2.3 Argumentativo:** Defiende una opinión o tesis mediante razones o argumentos. Su objetivo es convencer de un punto de vista.
            """)
        with tab2:
            f2 = [{"Q": "Discurso que usa adjetivos:", "A": "Descriptivo"}, {"Q": "Discurso que cuenta historias:", "A": "Narrativo"}, {"Q": "Discurso que defiende una tesis:", "A": "Argumentativo"}]
            if st.button("🔀 Mezclar"): random.shuffle(f2)
            for i, f in enumerate(f2):
                with st.expander(f"Tarjeta {i+1}: {f['Q']}"): st.success(f['A'])
        
        with tab3:
            q2 = st.radio("Un ensayo sobre el calentamiento global es:", ["Selecciona...", "Narrativo", "Descriptivo", "Argumentativo"])
            if q2 == "Argumentativo": st.success("¡Correcto! Defiende una postura científica.")

    # =========================================================
    # UNIDAD 3: COMPRENSIÓN DE LECTURA
    # =========================================================
    elif tema == "3. Comprensión de lectura":
        with tab1:
            st.header("3. Comprensión de lectura")
            st.markdown("""
            **3.1 Estructura del texto:**
            * **Introducción:** Plantea el tema o tesis.
            * **Desarrollo:** Expone argumentos, ejemplos y datos.
            * **Conclusión:** Resume y cierra la idea principal.
            
            **3.4 Inferencia de datos:**
            Es la capacidad de obtener información que no está escrita explícitamente pero se deduce lógicamente del texto.
            """)

    # =========================================================
    # UNIDAD 4: GRAMÁTICA
    # =========================================================
    elif tema == "4. Gramática":
        with tab1:
            st.header("4. Gramática")
            st.markdown("""
            **4.1 La Oración:** Unidad con sentido completo.
            **4.2 El Sujeto:** Quien realiza la acción.
            * **Explícito:** Escrito (Juan corre).
            * **Tácito:** No escrito (Corremos -> Nosotros).
            **4.3 El Predicado:** Lo que se dice del sujeto.
            * **Nominal:** Verbos ser, estar, parecer.
            * **Verbal:** Verbos de acción (correr, saltar, estudiar).
            """)

    # =========================================================
    # UNIDAD 5: REDACCIÓN
    # =========================================================
    elif tema == "5. Redacción":
        with tab1:
            st.header("5. Redacción")
            st.markdown("""
            Se enfoca en la coherencia y cohesión del texto mediante **Nexos**:
            
            1.  **Causales:** Expresan causa (porque, ya que, pues).
            2.  **Consecutivos:** Expresan consecuencia (por tanto, así que, en consecuencia).
            3.  **Adversativos:** Expresan oposición (pero, sin embargo, no obstante).
            4.  **Aditivos:** Suman ideas (además, asimismo, también).
            """)
        with tab3:
            q5 = st.radio("Completa: 'No estudió, ______ pasó el examen'.", ["Selecciona...", "porque", "sin embargo", "asimismo"])
            if q5 == "sin embargo": st.success("¡Correcto! Indica oposición.")

    # Recursos comunes (Videos)
    with tab4:
        st.subheader("Videos recomendados")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Ejemplo, reemplazar con links reales de UNAM
        st.write("Busca en YouTube: 'Español UNAM Área 1' para más contenido.")

else:
    st.info("🚧 Selecciona una materia en el menú lateral para cargar el contenido.")
