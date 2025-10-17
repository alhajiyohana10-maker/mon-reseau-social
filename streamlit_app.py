import streamlit as st

# Définir le titre de la page
st.set_page_config(page_title="Mon Réseau Social", page_icon=":speech_balloon:")

st.title("Bienvenue sur mon Réseau Social !")

# -----------------------------------------------------------------
# Formulaire de connexion / inscription
st.header("Connexion / Inscription")

# Champ pour l'email
email = st.text_input("Entrez votre email")

# Bouton pour se connecter
if st.button("Se connecter"):
    if email:
        st.success(f"Un lien de connexion a été envoyé à {email} !")
    else:
        st.error("Veuillez entrer un email valide.")

# -----------------------------------------------------------------
# Ici on pourra ajouter les fonctionnalités de posts, images, etc.
