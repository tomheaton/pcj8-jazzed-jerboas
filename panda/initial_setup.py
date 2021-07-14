import os


def initial_setup():
    with open(".env", "w") as f:
        f.write("SALT=" + os.urandom(32).hex())


if __name__ == "__main__":
    initial_setup()
