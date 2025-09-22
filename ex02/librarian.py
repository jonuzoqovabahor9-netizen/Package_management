import os
import sys
import subprocess

def check_env():
    if not os.environ.get("VIRTUAL_ENV"):
        raise Exception("Siz virtual environment ichida emassiz.")
    my_env = os.path.basename(os.environ.get("VIRTUAL_ENV"))
    if my_env != "haru":
        raise Exception("Siz boshqa venv ning ichidasiz")
    
def ins_lib():
    reqs = "beautifulsoup4\npytest\n"
    with open("requirements.txt", "w") as file:
        file.write(reqs)

    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def freeze_libs():
    with open("requirements.txt", "w") as file:
        subprocess.check_call([sys.executable, "-m", "pip", "freeze"], stdout=file)


def main():
    check_env()
    ins_lib()
    freeze_libs()
    print("Ish bajarildi :)")

if __name__ == "__main__":
    main()