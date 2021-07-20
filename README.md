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
$ cd 'path/to/clone_of_repo'
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
$ cd 'path/to/clone_of_repo'
$ pip install -r dev-requirements.txt
```

#### Starting the Scripts


Use this command to start the server. (Needs to be done before running client)
```shell
$ cd 'path/to/clone_of_repo'
$ python server/server.py
```
Finally, use this command to start the client interface.
```shell
$ cd 'path/to/clone_of_repo'
$ python client/client.py
```

## Using the project

#### Testing the project
Testing of the project has to be done locally. (Tom Heathon could not get his server up :| R.I.P server)

For testing of the messages you need to terminals up running client/client.py and one terminal runing server/server.py (For client to work the server needs to run in the backround first)

#### Info
If you are using windows we reccomend using the new and modern `Windows Terminal` which you can find in the Microsoft Store. (This makes animation much smoother)

The project will not work on Linux unless you are root because of how the keyboard module works.

When typing out password you will not see what you type. (This is to hide your password from hackers who look over your shoulder while you are typing your password lol)

## Authors

Team Jazzed Jerboas - tomheaton, MikeNoCap, HiPeople21, TahU28, ryoflux, b-a-b-i-s
