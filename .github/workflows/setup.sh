#!/bin/sh

sudo apt update -y
sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update -y
sudo apt install python3.13 -y

alias python=python3.13
alias pip='python3.13 -m pip'