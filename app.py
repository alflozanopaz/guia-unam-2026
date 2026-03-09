import streamlit as st
import random

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="MI GUÍA UNAM 2026", page_icon="🎓", layout="wide")

st.title("🎓 MI GUÍA DE ESTUDIO UNAM 2026")
st.subheader("Área 1: Ciencias Físico-Matemáticas y de las Ingenierías")
st.markdown("---")

# --- MENÚ LATERAL ---
st.sidebar.header("📌 Navegación del Temario")
materia = st.sidebar.selectbox("Selecciona Materia:", ["Español", "Matemáticas", "Física"])

if materia == "Español":
    # Aquí es donde registramos los temas que existen
    tema = st.sidebar.selectbox("Selecciona Unidad:", [
        "1. Funciones de la lengua", 
        "2. Formas del discurso", 
        "3. Comprensión de lectura",
        "4. Gramática",
        "5. Redacción"
    ])

    # Pestañas Universales
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Teoría Detallada", "🗂️ Flashcards", "📝 Banco de Preguntas", "🎥 Recursos"])

    # =========================================================
    # BLOQUE TEMA 1: FUNCIONES DE LA LENGUA
    # =========================================================
    if tema == "1. Funciones de la lengua":
        with tab1:
            st.header("1. Funciones de la lengua")
            st.markdown("""
            * **1.1 Referencial:** Su intención es **informar** hechos, datos y conceptos de manera objetiva. Se centra en el mensaje y el contexto. Común en noticias y textos científicos.
                * *Ejemplo:* "La Ciudad de México se fundó en 1325."
            * **1.2 Apelativa (Conativa):** Busca **convencer o influir** en la conducta del receptor. Se manifiesta en órdenes, peticiones o publicidad.
                * *Ejemplo:* "¡Haz tu tarea ahora!" o "Vota por el progreso."
            * **1.3 Poética:** Su fin es **estético**. Se utiliza para embellecer el mensaje mediante figuras retóricas (metáforas, rimas).
                * *Ejemplo:* "El tiempo es oro."
            """)
        with tab2:
            st.subheader("Flashcards T1")
            if 'fc1' not in st.session_state:
                st.session_state.fc1 = [
                    {"Q": "¿Qué función busca convencer?", "A": "Apelativa"},
                    {"Q": "¿Qué función es objetiva e informativa?", "A": "Referencial"},
                    {"Q": "¿Qué función usa figuras retóricas?", "A": "Poética"}
                ]
            if st.button("🔀 Mezclar T1"): random.shuffle(st.session_state.fc1)
            for i, f in enumerate(st.session_state.fc1):
                with st.expander(f"Tarjeta {i+1}"): st.write(f['Q']); st.success(f['A'])
        with tab3:
            st.radio("¿Qué función predomina en una enciclopedia?", ["...", "Poética", "Referencial", "Apelativa"], key="q1")

    # =========================================================
    # BLOQUE TEMA 2: FORMAS DEL DISCURSO
    # =========================================================
    elif tema == "2. Formas del discurso":
        with tab1:
            st.header("2. Formas del discurso")
            st.markdown("""
            * **2.1 Descriptivo:** Dice *cómo es* algo o alguien. Usa abundantes adjetivos para detallar características físicas o psicológicas.
                * *Ejemplo:* "Era un edificio alto, gris y con ventanas rotas."
            * **2.2 Narrativo:** Relata *qué pasa*. Se estructura en una secuencia temporal con verbos de acción. (Cuentos, noticias).
                * *Ejemplo:* "Abrió la puerta, miró el reloj y salió corriendo."
            * **2.3 Argumentativo:** Intenta *demostrar o convencer* sobre una idea (tesis) usando argumentos lógicos.
                * *Ejemplo:* "Es necesario reciclar porque reduce la contaminación global."
            """)
        with tab2:
            if 'fc2' not in st.session_state:
                st.session_state.fc2 = [{"Q": "¿Usa adjetivos?", "A": "Descriptivo"}, {"Q": "¿Usa verbos de acción?", "A": "Narrativo"}]
            if st.button("🔀 Mezclar T2"): random.shuffle(st.session_state.fc2)
            for i, f in enumerate(st.session_state.fc2):
                with st.expander(f"Tarjeta {i+1}"): st.write(f['Q']); st.success(f['A'])

    # =========================================================
    # BLOQUE TEMA 3: COMPRENSIÓN DE LECTURA
    # =========================================================
    elif tema == "3. Comprensión de lectura":
        with tab1:
            st.header("3. Comprensión de lectura")
            st.markdown("""
            **3.1 Estructura del texto:**
            * **Introducción:** Presenta el tema y la tesis.
            * **Desarrollo:** Expone argumentos, ejemplos e ideas secundarias.
            * **Conclusión:** Resumen final o cierre de la idea principal.
            
            **3.4 Inferencia de datos:**
            Es deducir información implícita (no escrita) a partir de pistas.
            * *Pista:* "Llevaba abrigo y bufanda". *Inferencia:* Hace frío.
            """)

    # =========================================================
    # BLOQUE TEMA 4: GRAMÁTICA
    # =========================================================
    elif tema == "4. Gramática":
        with tab1:
            st.header("4. Gramática: Sujeto y Predicado")
            st.markdown("""
            * **4.2 Sujeto Explícito:** Aparece escrito. "Los alumnos estudian".
            * **4.2 Sujeto Tácito:** Se deduce por el verbo. "Estudiamos" (Nosotros).
            * **4.3 Predicado Nominal:** Usa verbos copulativos (Ser, Estar, Parecer). "Ella **es** inteligente".
            * **4.3 Predicado Verbal:** Usa verbos de acción. "Ella **corre** mucho".
            """)
        with tab3:
            st.radio("Sujeto en: 'Ayer Juan compró pan'", ["...", "Ayer", "Juan", "Pan"], key="q4")

    # =========================================================
    # BLOQUE TEMA 5: REDACCIÓN
    # =========================================================
    elif tema == "5. Redacción":
        with tab1:
            st.header("5. Redacción: Nexos y Marcadores")
            st.markdown("""
            Los nexos unen ideas y dan coherencia:
            * **Causales:** Explicación (porque, puesto que).
            * **Adversativos:** Oposición (pero, sin embargo, no obstante).
            * **Consecutivos:** Resultado (por lo tanto, así que).
            * **Aditivos:** Suma (además, asimismo).
            """)
        with tab3:
            st.radio("Nexo de oposición:", ["...", "Porque", "Pero", "Además"], key="q5")

else:
    st.info("🚧 Selecciona un tema para cargar el contenido detallado.")
