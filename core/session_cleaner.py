# session_cleaner.py
import threading
import datetime
import time
import app_database as db
import pandas as pd

def session_cleaner_loop(interval_seconds=30, timeout_minutes=30):
    while True:
        try:
            #check_session(session_token=None)
            users_sessions = db.get_table_as_df('users_sessions')
            # trouve les sessions actives, sans token ou id
            user_session = users_sessions[
                (users_sessions['is_active'] == True)
            ]
            if user_session.empty:
                print("No active session")
            else:
                print("Active session found : ")
                print(user_session)

            now = datetime.datetime.now()
            cutoff_time = now - datetime.timedelta(minutes=timeout_minutes)

            #print("👋 [SessionCleaner] Hello")
            #print(f"🕒 Date actuelle (now)         : {now.strftime('%Y-%m-%d %H:%M:%S')}")
            #print(f"🔻 Seuil d'expiration (cutoff) : {cutoff_time.strftime('%Y-%m-%d %H:%M:%S')} ({timeout_minutes} min avant)")

            cutoff_str = cutoff_time.strftime("%Y-%m-%d %H:%M:%S")
            db.run_query(f"""
                UPDATE users_sessions
                SET is_active = False
                WHERE last_activity < '{cutoff_str}'
            """)
            print(f"[SessionCleaner] ✅ Clean OK - Inactives > {timeout_minutes} min")
        except Exception as e:
            print(f"[SessionCleaner] ❌ ERROR : {e}")
        time.sleep(interval_seconds)

def hello_loop():
    while True:
        print("👋 hello")
        time.sleep(5)

# Function to manually check the session table
def check_session(session_token):
    while True:
        try:
            df = db.get_table_as_df("users_sessions")
            # 🔥 conversion explicite de la colonne
            df["last_activity"] = pd.to_datetime(df["last_activity"], format="%Y-%m-%d %H:%M:%S.%f", errors="coerce")

            # 🔍 filtrer les sessions expirées
            expired = df[df["last_activity"] < (datetime.datetime.now() - datetime.timedelta(minutes=timeout_minutes))]
            print("---- DEBUG - Lignes expirées :")
            print(expired)
        except Exception as e:
            print(f"Erreur DEBUG pandas : {e}")


def start_cleaner_thread():
    # Thread 1 : nettoyage des sessions
    cleaner_thread = threading.Thread(target=session_cleaner_loop, daemon=True)
    cleaner_thread.start()

    # Thread 2 : hello toutes les 5 secondes
    #coucou_thread = threading.Thread(target=hello_loop, daemon=True)
    #coucou_thread.start()