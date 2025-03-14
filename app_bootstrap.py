# app_bootstrap.py
import panel as pn
from core.session_cleaner import start_cleaner_thread

pn.extension()

# Démarre le thread de fond dès que Panel démarre
start_cleaner_thread()

# Rien à afficher, juste une page vide (ou "System Ready")
pn.pane.Markdown("🛠 Application bootstrap - background thread actif").servable("app_bootstrap")
