import smtplib
from dotenv import load_dotenv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Connexion Informations to serveur SMTP
load_dotenv()
smtp_server = 'smtp.mail.me.com'
smtp_port = 587
smtp_username = os.getenv('SMTP_USERNAME')
smtp_password = os.getenv('SMTP_PASSWORD')

# List of recipients
destinataires = [ "m.almahmud@yahoo.com"]
projects = "test"

# Eemail Informations
sujet = 'Recherche Alternance chef de projet IA'
corps = f"""
Madame, Monsieur,
Je souhaite réjoindre votre entreprise car mon sens de l'organisation, ma rigueur,
et ma capacité à gérer des équipes pluridisciplinaires me permettent de mener à 
bien vos projets: {projects}
A la rentrée prochaine, j'entame une reconversion en tant que Chef de projet
Intelligence Artificielle (Bac+5)
à Agoriade https://www.agoriade.fr/devenir-Chef-de-Projet-IA 
et recherche actuellement une alternance en tant que Chef de Projet IA au sein 
de votre entreprise.

Actuellement data scientist, developpeur wordpress freelance et formateur chez
le Wagon, je serai prêt, à l'issue de cette formation, à développer des compétences
en gestion de projets technologiques et en développement d'applications IA.

Je pourrai acculturer et former vos équipes en IA, élaborer des solutions via
le design thinking, et piloter, développer, et déployer des projets d'IA.

Je suis motivé à contribuer à vos projets et serai heureux de discuter de 
vive voix de ma candidature.

Cordialement
Mohamed ALMAHMOUD
06.22.00.26.20
https://www.linkedin.com/in/mohamedalmahmoud/

"""
# Connexion to serveur SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Try to log in and handle potential authentication errors
try:
    server.login(smtp_username, smtp_password)
except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Check your credentials and email provider's security settings.")
    # Here you would typically guide the user to check their settings or provide alternative authentication methods
    exit()  # Exit the script since we can't proceed without authentication

# Sending emails
for i, destinataire in enumerate(destinataires):
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = destinataire
    msg['Subject'] = sujet
    time.sleep(0.1)

    msg.attach(MIMEText(corps, 'plain'))

    try:
        server.sendmail(smtp_username, destinataire, msg.as_string())
        print(f"{i} Email envoyé à {destinataire}")
    except Exception as e:
        print(f"{i} Erreur lors de l'envoi à {destinataire}: {e}")
        # Instead of reconnecting, it's generally better to handle the error and move on to the next recipient
        # Reconnecting and retrying immediately might not solve the underlying issue and could lead to issues like being temporarily blocked by the server

# Closing of connexion
server.quit()
