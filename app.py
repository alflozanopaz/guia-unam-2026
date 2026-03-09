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
    tema = st.sidebar.selectbox("Selecciona el tema:", ["1. Funciones de la lengua", "2. Formas del discurso"])
    
    # ---------------------------------------------------------
    # TEMA 1: FUNCIONES DE LA LENGUA
    # ---------------------------------------------------------
    if tema == "1. Funciones de la lengua":
        st.header("1. Funciones de la lengua")
        tab1, tab2, tab3, tab4 = st.tabs(["📖 Teoría", "🗂️ Flashcards", "📝 Quiz", "🎥 Recursos"])
        
        with tab1:
            st.subheader("Resumen Teórico")
            st.markdown("""
            * **1.1 Referencial:** Informa hechos objetivos. Ej: *La Tierra gira alrededor del Sol.*
            * **1.2 Apelativa:** Busca convencer u ordenar. Ej: *¡Compra ahora!*
            * **1.3 Poética:** Se enfoca en la belleza del mensaje. Ej: *Tus ojos son luceros.*
            """)
        with tab2:
            st.info("Flashcards en el Tema 2 tienen la nueva función aleatoria. ¡Ve a revisarlas!")
        with tab3:
            st.write("Cuestionario configurado en el Tema 2.")
        with tab4:
            st.markdown("[▶️ Unitips: Funciones de la Lengua](https://www.youtube.com/results?search_query=unitips+funciones+de+la+lengua)")

    # ---------------------------------------------------------
    # TEMA 2: FORMAS DEL DISCURSO (NUEVO)
    # ---------------------------------------------------------
    elif tema == "2. Formas del discurso":
        st.header("2. Formas del discurso")
        
        tab1, tab2, tab3, tab4 = st.tabs(["📖 Teoría", "🗂️ Flashcards", "📝 Quiz", "🎥 Recursos"])
        
        with tab1:
            st.subheader("Resumen Teórico")
            st.markdown("""
            La forma del discurso es la estructura que utilizamos para organizar la información según lo que queremos lograr. En el examen UNAM (Especialmente en Lectura de Comprensión) debes identificar tres:

            * **2.1 Descriptivo:** Dice *cómo es* algo o alguien. Utiliza muchos **adjetivos** y detalles. Crea una "pintura con palabras".
              * *Ejemplo:* "La casa era antigua, de muros grises y ventanas rotas que rechinaban con el viento frío."
            * **2.2 Narrativo:** Cuenta *qué pasó*. Se desarrolla en un tiempo y espacio determinado, usando muchos **verbos** de acción.
              * *Ejemplo:* "Juan abrió la puerta, miró a su alrededor y salió corriendo hacia la calle."
            * **2.3 Argumentativo:** Intenta *demostrar, convencer o defender una idea* (Tesis) usando razones (Premisas). Es clave en ensayos y artículos de opinión.
              * *Ejemplo:* "El uso de la energía solar es imperativo porque reduce la huella de carbono y fomenta la economía sustentable."
            """)
            st.warning("⚠️ **Ojo para Área 1:** En las lecturas de física o matemáticas del examen, a menudo te pondrán textos argumentativos donde un autor defiende una teoría. Debes saber identificar su 'Tesis' principal.")
            
            st.subheader("Mapa Conceptual Visual")
            st.markdown("""
            ```text
            FORMAS DEL DISCURSO
            │
            ├── NARRATIVO ───> Relata acciones en el tiempo (Cuentos, novelas) ──> Usa Verbos
            ├── DESCRIPTIVO ─> Señala características (Retratos, topografías) ──> Usa Adjetivos
            └── ARGUMENTATIVO > Defiende una postura (Ensayos, artículos) ──────> Usa Premisas/Tesis
            ```
            """)

        with tab2:
            st.subheader("🔀 Flashcards Aleatorias")
            
            # Base de datos de Flashcards
            if 'flashcards_t2' not in st.session_state:
                st.session_state.flashcards_t2 = [
                    {"Q": "¿Qué discurso usa abundancia de adjetivos?", "A": "Descriptivo."},
                    {"Q": "¿Qué discurso relata hechos o acciones en el tiempo?", "A": "Narrativo."},
                    {"Q": "¿Cuál es el objetivo del discurso argumentativo?", "A": "Convencer o defender una tesis."},
                    {"Q": "Un cuento o una novela utilizan principalmente el discurso...", "A": "Narrativo."},
                    {"Q": "Un ensayo científico utiliza principalmente el discurso...", "A": "Argumentativo."},
                    {"Q": "¿Qué discurso plasma un 'retrato' con palabras?", "A": "Descriptivo."},
                    {"Q": "Si un texto intenta persuadirte de cambiar de opinión, es...", "A": "Argumentativo."},
                    {"Q": "Palabra clave del discurso narrativo:", "A": "Verbos (acciones)."},
                    {"Q": "Una receta de cocina paso a paso, ¿qué discurso es?", "A": "Suele mezclarse, pero la secuencia temporal es narrativa."},
                    {"Q": "Idea central que se defiende en un texto argumentativo:", "A": "Tesis."}
                ]

            if st.button("🔀 Barajar Flashcards"):
                random.shuffle(st.session_state.flashcards_t2)

            # Mostrar las primeras 5 para no saturar la pantalla
            for i, fc in enumerate(st.session_state.flashcards_t2[:5]):
                with st.expander(f"Tarjeta {i+1}: {fc['Q']}"):
                    st.success(fc['A'])

        with tab3:
            st.subheader("Banco de Preguntas Tipo UNAM")
            st.write("Selecciona la respuesta correcta. La explicación aparecerá al elegir.")
            
            p1 = st.radio(
                "1. 'El perro de raza mastín tiene un pelaje corto, color arena y una musculatura prominente'. ¿Qué forma de discurso predomina?",
                ("Selecciona...", "A) Narrativo", "B) Argumentativo", "C) Descriptivo", "D) Científico", "E) Literario")
            )
            if p1 == "C) Descriptivo":
                st.success("¡Correcto! Solo enumera características físicas y usa adjetivos (corto, arena, prominente).")
            elif p1 != "Selecciona...":
                st.error("Incorrecto. Recuerda: no está contando una historia, está diciendo 'cómo es' algo.")

            st.divider()

            p2 = st.radio(
                "2. Forma del discurso en la que el autor trata de convencer al lector de una idea principal llamada Tesis.",
                ("Selecciona...", "A) Narrativo", "B) Argumentativo", "C) Descriptivo", "D) Informativo", "E) Épico")
            )
            if p2 == "B) Argumentativo":
                st.success("¡Correcto! La clave aquí es la palabra 'convencer' y 'Tesis'.")
            elif p2 != "Selecciona...":
                st.error("Incorrecto. Intenta recordar cuál discurso se usa en los debates o ensayos.")

        with tab4:
            st.subheader("Video Tutoriales")
            st.markdown("[▶️ Profe Cristian: Formas del discurso](https://www.youtube.com/results?search_query=profe+cristian+formas+del+discurso)")
            st.markdown("[▶️ Pasatuexamen: Textos argumentativos, descriptivos y narrativos](https://www.youtube.com/results?search_query=pasatuexamen+formas+del+discurso)")

else:
    st.info("🚧 Tema en construcción.")
