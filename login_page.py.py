import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Bienvenue sur ma page", layout="wide")

# Simuler un utilisateur connecté
VALID_USERNAME = "root"
VALID_PASSWORD = "admin123"

# Gestion de l'état de la session
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Fonction pour afficher la page de connexion
def login():
    st.title("Login")
    with st.form(key="login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button(label="Login")

    if submit_button:
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.authenticated = True
            st.session_state.page = "Accueil"
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect")

# Fonction pour afficher la page principale
def main_page():
    st.sidebar.button("Déconnexion", on_click=logout)
    st.sidebar.markdown(f"**Bienvenue _{VALID_USERNAME}_**")

    # Menu latéral
    menu = st.sidebar.radio("Navigation", ["🤩 Accueil", "🐱 Les photos de mon chat"])

    # Contenu principal
    if menu == "🤩 Accueil":
        st.title("Bienvenue sur ma page")
        st.image(
            "https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif",
            caption="Merci pour votre visite !",
        )
    elif menu == "🐱 Les photos de mon chat":
        st.title("Photos de mon chat")
        st.image(
            "https://placekitten.com/400/300",
            caption="Voici mon chat mignon !",
        )

# Fonction de déconnexion
def logout():
    st.session_state.authenticated = False

# Affichage conditionnel en fonction de l'état de la session
if not st.session_state.authenticated:
    login()
else:
    main_page()
