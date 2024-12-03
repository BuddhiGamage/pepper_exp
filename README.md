# Pepper Experiment Application

This project is a Streamlit-based web interface for interacting with the Pepper robot. It allows users to connect with the Pepper robot in either virtual or physical mode, execute animations, manage speech interactions, and perform predefined scripts like yoga and the Ultimatum Game.

## Features

- **Dual Connection Modes**: Supports both virtual and physical modes for interacting with Pepper.
- **Interactive Scripts**: Includes Yoga and Ultimatum Game scripts to demonstrate human-robot interaction.
- **Custom Speech**: Enables text-to-speech functionality with options to play audio or send speech commands.
- **Animations**: Provides predefined actions and animations accessible through an interactive button interface.
- **Dynamic Behavior Management**: Allows stopping all animations and switching modes seamlessly.

---

## Installation
1. **- [Python 3.8+](https://www.python.org/downloads/) or higher**
2. **Required libraries:**
    - sshpass
    - [Streamlit](https://streamlit.io/)
    - [Qi Framework](https://pypi.org/project/qi/)
    - [Choregraphe](https://www.aldebaran.com/en/support/pepper-naoqi-2-9/downloads-softwares)
    - [playsound](https://pypi.org/project/playsound/)

## Setup

### Steps to Install the Choregraphe Application

1. **Open Choregraphe:**

   - Launch **Choregraphe** on your computer.
   - Connect to Pepper by entering the robot’s IP address.

2. **Load the Questacon Project:**

   - Click **File > Open project** and navigate to the `questacon` folder.
   - Open the Questacon project file (`questacon.pml`).

3. **Access the Robot Applications Panel:**

   - In Choregraphe, navigate to the **Robot Applications** panel (located on the left side of the screen).
   
4. **Install the Questacon Application:**

   - In the **Robot Applications** panel, click the **Package and install** button.

5. **Verify Installation:**

   - After installation, you should see the Questacon application listed in the **Robot Applications** panel.

### App installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BuddhiGamage/pepper_streamlit.git
   cd pepper_streamlit

2. **Install dependencies:**
   ```bash
   sudo apt-get install sshpass
   
   pip install -r requirements.txt

## Running the Application

1. **Start the Streamlit server:**

    ```bash
    streamlit run app.py

## Key Functions

- animation(button_name, description, mode)
Plays animations and audio based on the selected button and mode.

- copy_audio_from_pepper_to_laptop()
Copies audio files from Pepper to the local system for playback.

- process_say()
Processes text input for speech synthesis and playback.
