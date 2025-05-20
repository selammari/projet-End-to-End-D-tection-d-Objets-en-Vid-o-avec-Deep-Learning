@echo off
setlocal

:: Dossier actuel = dossier contenant le .bat (app)
set APP_DIR=%~dp0

:: Chemin absolu de l'environnement virtuel (dans le dossier parent "Projet3")
set VENV_PATH=%APP_DIR%..\..\..\yolov8-app

:: Vérifier si streamlit.exe existe dans l'env virtuel
if not exist "%VENV_PATH%\Scripts\streamlit.exe" (
    echo === Création de l'environnement virtuel "yolov8-app" ===
    python -m venv "%VENV_PATH%"

    echo === Activation et installation des dépendances ===
    call "%VENV_PATH%\Scripts\activate.bat"
    pip install --upgrade pip
    pip install streamlit opencv-python ultralytics pillow
)

:: Lancer streamlit avec chemin complet
echo === Lancement de l'application Streamlit ===
start "" "%VENV_PATH%\Scripts\streamlit.exe" run st.py --server.headless=false

pause
