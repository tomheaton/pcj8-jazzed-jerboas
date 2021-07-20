![Jazzed Jerboas](https://github.com/tomheaton/pcj8-jazzed-jerboas/blob/main/images/logo-128.jpeg?raw=true)

# Python Discord Code Jam 8 - Jazzed Jerboas

This is the Jazzed Jerboa's submission to the Python Discord Summer Code Jam 2021 (Code Jam 8)

## ThaBox

Introducing **ThaBox**, a text-based `[REDACTED]` application.

![ThaBox](https://github.com/tomheaton/pcj8-jazzed-jerboas/blob/main/images/ThaBox.png?raw=true)

- built using the Rich framework

## How to set up the project

#### Creating the environment
Create a virtual environment in the folder `clone_of_repo\.venv`.
```shell
$ python -m venv path/to/new/venv
```

#### Enter the environment
It will change based on your operating system and shell.
```shell
# Linux, Bash
$ source clone_of_repo/.venv/bin/activate
# Linux, Fish
$ source clone_of_repo/.venv/bin/activate.fish
# Linux, Csh
$ source clone_of_repo/.venv/bin/activate.csh
# Linux, PowerShell Core
$ clone_of_repo/.venv/bin/Activate.ps1
# Windows, cmd.exe
> clone_of_repo\.venv\Scripts\activate.bat
# Windows, PowerShell
> clone_of_repo\.venv\Scripts\Activate.ps1
```

#### Installing the Dependencies
Once the environment is created and activated, use this command to install the development dependencies.
```shell
$ pip install -r dev-requirements.txt
```

#### Starting the Scripts


Use this command to start the server. (Needs to be done before running client)
```shell
$ python server/server.py
```
Finally, use this command to start the client interface.
```shell
$ python client/client.py
```

## Using the project

#### Testing the project
Testing of the project has to be done locally. (Tom Heathon could not get his server up :| R.I.P server)

For testing of the messages you need to terminals up running client/client.py and one terminal runing server/server.py (For client to work the server needs to run in the backround first)

#### Tips
If you are using windows we reccomend using the new and modern `Windows Terminal` which you can find in the Microsoft Store

## Authors

Team Jazzed Jerboas - tomheaton, MikeNoCap, HiPeople21, TahU28, ryoflux, b-a-b-i-s
