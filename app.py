import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mi Guía UNAM 2026", page_icon="🎓", layout="wide")

# Título principal
st.title("🎓 MI GUÍA DE ESTUDIO UNAM 2026 - Área 1")
st.markdown("---")

# Menú lateral
st.sidebar.header("📚 Temario")
materia = st.sidebar.selectbox("Selecciona la materia:", ["Español", "Matemáticas", "Física"])

if materia == "Español":
    tema = st.sidebar.selectbox("Selecciona el tema:", ["1. Funciones de la lengua", "2. Formas del discurso"])
    
    if tema == "1. Funciones de la lengua":
        st.header("1. Funciones de la lengua")
        
        # Pestañas interactivas
        tab1, tab2, tab3, tab4 = st.tabs(["📖 Teoría", "🗂️ Flashcards", "📝 Quiz", "🎥 Recursos"])
        
        with tab1:
            st.subheader("Resumen Teórico")
            st.markdown("""
            Las funciones de la lengua son los propósitos con los que usamos el lenguaje. Para el examen, domina estas tres:
            
            * **1.1 Referencial:** Su objetivo es **informar** hechos o datos de manera objetiva. Ej: *La Tierra gira alrededor del Sol.*
            * **1.2 Apelativa (Conativa):** Busca **convencer, ordenar o persuadir** al receptor. Ej: *¡Compra ahora y obtén un descuento!* o *Cierra la puerta.*
            * **1.3 Poética:** Se enfoca en la **belleza del mensaje**, utilizando figuras retóricas. Ej: *Tus ojos son dos luceros.*
            """)
            st.info("💡 Tip Área 1: En las lecturas de comprensión de ciencias, casi siempre predomina la función referencial.")
            
        with tab2:
            st.subheader("Flashcards")
            if st.button("Mostrar/Ocultar Respuesta 1"):
                st.success("**Respuesta:** Función Apelativa (Busca persuadir o dar una orden).")
            else:
                st.write("¿Qué función predomina en un discurso político?")
                
            st.write("---")
            if st.button("Mostrar/Ocultar Respuesta 2"):
                st.success("**Respuesta:** Función Referencial.")
            else:
                st.write("¿Qué función de la lengua se usa en una noticia periodística?")

        with tab3:
            st.subheader("Banco de Preguntas")
            q1 = st.radio(
                "1. En el enunciado 'El agua hierve a 100 grados Celsius', ¿qué función de la lengua predomina?",
                ("Selecciona una opción", "A) Poética", "B) Apelativa", "C) Referencial", "D) Fática", "E) Metalingüística")
            )
            if q1 != "Selecciona una opción":
                if q1 == "C) Referencial":
                    st.success("¡Correcto! Informa un dato objetivo sin adornos ni opiniones.")
                else:
                    st.error("Incorrecto. Recuerda que solo está dando un dato objetivo.")
                    
        with tab4:
            st.subheader("Video Tutoriales Sugeridos")
            st.markdown("[▶️ Unitips: Funciones de la Lengua (YouTube)](https://www.youtube.com/results?search_query=unitips+funciones+de+la+lengua)")
            st.markdown("[▶️ Pasatuexamen: Español UNAM (YouTube)](https://www.youtube.com/results?search_query=pasatuexamen+funciones+de+la+lengua)")

else:
    st.info("🚧 Tema en construcción. ¡Pronto agregaremos más contenido!")
