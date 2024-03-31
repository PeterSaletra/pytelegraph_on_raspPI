# Pytelegraph on RaspPI
## University assigment

## Table of contents
* [General info](#general-info)
* [Electronic Circiut Design](#electronic-circiut-design)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
It is telegraph project on Raspberry Pi

## Electronic Circiut Design


## Technologies
Project is created with:
* Python 3.9
* Raspberry Pi 2B+
* gpiozero
* I2C

## Setup

- Install all dependencies and libraries

```
$ sudo apt-get install -y i2c-tools python3-smbus
$ pip3 install -r requirements.txt
```

- Enable i2c on Raspbery Pi
- Run main.py

```
$ python3 main.py
```
- Run server.py

```
$ python3 server.py
```

