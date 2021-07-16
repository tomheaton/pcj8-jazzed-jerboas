![Jazzed Jerboas](https://github.com/tomheaton/pcj8-jazzed-jerboas/blob/main/images/logo-128.jpeg?raw=true)

# Python Discord Code Jam 8 - Jazzed Jerboas

This is the Jazzed Jerboa's submission to the Python Discord Summer Code Jam 2021 (Code Jam 8)

## ThaBox

Introducing **ThaBox**, a text-based `[REDACTED]` application.

![ThaBox](https://github.com/tomheaton/pcj8-jazzed-jerboas/blob/main/images/ThaBox.png?raw=true)

- built using the Rich framework

## How to set up the project

#### Creating the environment
Create a virtual environment in the folder `.venv`.
```shell
$ python -m venv .venv
```

#### Enter the environment
It will change based on your operating system and shell.
```shell
# Linux, Bash
$ source .venv/bin/activate
# Linux, Fish
$ source .venv/bin/activate.fish
# Linux, Csh
$ source .venv/bin/activate.csh
# Linux, PowerShell Core
$ .venv/bin/Activate.ps1
# Windows, cmd.exe
> .venv\Scripts\activate.bat
# Windows, PowerShell
> .venv\Scripts\Activate.ps1
```

#### Installing the Dependencies
Once the environment is created and activated, use this command to install the development dependencies.
```shell
$ pip install -r dev-requirements.txt
```

#### Starting the Scripts
Use this command to start the server.
```shell
$ python server.py
```
Finally, use this command to start the client interface.
```shell
$ python client.py
```

## Authors

Team Jazzed Jerboas - tomheaton, MikeNoCap, HiPeople21, TahU28, ryoflux, b-a-b-i-s