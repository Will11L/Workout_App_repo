import subprocess
import sys
import time
import platform

# Fonction pour tuer tous les processus Panel (Windows uniquement)
def kill_all_panels_windows():
    if platform.system() != "Windows":
        print("⚠️ Système non-Windows détecté. Aucune tâche Panel ne sera tuée.")
        return

    try:
        print("🔪 Killing all Panel processes on Windows...")
        tasks = subprocess.check_output(["tasklist"]).decode()
        panel_tasks = [line for line in tasks.splitlines() if "panel" in line.lower() and "python.exe" in line.lower()]
        
        for task in panel_tasks:
            pid = task.split()[1]
            print(f"   → Killing process ID: {pid}")
            subprocess.run(["taskkill", "/F", "/PID", pid])
        
        print("✅ All Panel processes have been terminated.")
    except Exception as e:
        print(f"❌ Error while killing Panel processes: {e}")

# Fonction pour lancer le serveur Panel
def launch_panel():
    command = [
        "panel", 
        "serve",
        "app_bootstrap.py", 
        "login_page.py", 
        "main_page.py", 
        "database_page.py",
        "page_1.py",
        "page_2.py",
        "--address=0.0.0.0",
        "--port=8080",
        "--allow-websocket-origin=*",
        "--index=login_page.py",
        "--dev"
    ]

    try:
        time.sleep(1)
        print("✅ Panel server is starting...")
        print("\n🌐 Access your application in your browser:")
        print("   → http://localhost:8080/login_page (login page)")
        print("   → http://localhost:8080/main_page")
        print("   → http://localhost:8080/database_page")
        print("   → http://localhost:8080/page1")
        print("   → http://localhost:8080/page2")
        print("\n📎 Note: In logs, '0.0.0.0' means the server is listening on all interfaces.")
        print("--------------------------------------\n")
        
        subprocess.run(command)

    except KeyboardInterrupt:
        print("\n🛑 Keyboard interruption. Shutting down Panel.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error while launching Panel: {e}")
        sys.exit(1)

# Point d'entrée principal
if __name__ == "__main__":
    kill_all_panels_windows()
    launch_panel()
