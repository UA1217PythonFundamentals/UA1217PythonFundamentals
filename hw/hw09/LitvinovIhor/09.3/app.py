import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements: {e}")
        sys.exit(1)

def run_app():
    try:
        subprocess.check_call([sys.executable, 'Tk_OWM.py'])
    except subprocess.CalledProcessError as e:
        print(f"Failed to run the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
    run_app()

