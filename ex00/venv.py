import os
def venv():
    my_venv = os.getenv("VIRTUAL_ENV")
    return my_venv

if __name__=="__main__":
    print(f"Your current virtual env is {venv()}")