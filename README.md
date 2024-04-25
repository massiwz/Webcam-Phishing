# Webcam Security Project

## Overview

This project is a aimed at exploring vulnerabilities in webcams and mobile phone cams, specifically focusing on security risks associated with camera access. The project involves the development of a Python-based script capable of launching a PHP server, which is then made accessible on the public internet using a service called localhustrun. The generated link and QR code direct users to a phishing webpage, mimicking legitimate sites like Netflix. Once users grant camera access on the phishing site, photos are silently uploaded to a designated server every 2 seconds without their knowledge.

## Usage


1. **Update and Upgrade System**: Run the following commands to update and upgrade your system packages:
    ```bash
    sudo apt update && sudo apt upgrade
    ```

2. **Install Required Dependencies**: Install the required dependencies by running the following commands:
    ```bash
    sudo apt install python -y
    sudo apt install wget -y
    sudo apt install php -y
    sudo apt install openssh-client -y
    sudo apt install jq -y
    ```

3. **Generate SSH Key**: Generate an SSH key pair with the following command and accept the default settings:
    ```bash
    ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa <<< y >/dev/null 2>&1
    ```

4. **Clone the Repository**: Clone the project repository by running the following command:
    ```bash
    git clone https://github.com/massiwz/Webcam-Phishing.git
    ```

5. **Run the Project**: Navigate to the project directory and execute the main Python script to launch the project:
    ```bash
    cd Webcam-Phishing
    python3 main.py
    ```

Once the project is running, you can access the generated link or scan the QR code to visit the phishing webpage. Grant camera access when prompted on the phishing site to initiate photo capture.

## Disclaimer

**Important**: This project is intended for educational and research purposes only. It should only be executed in controlled environments under the supervision of professionals. The project creators do not condone or support any illegal or unethical activities. Use of this project for unauthorized surveillance or exploitation of individuals' privacy is strictly prohibited.
