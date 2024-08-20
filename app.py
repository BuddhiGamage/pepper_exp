import streamlit as st
from connection import Connection
import qi
from playsound import playsound
import os
import time

# Header
st.title('Pepper Experiment')
session = None

# Initialize session state for the text input
if 'port_value' not in st.session_state:
    st.session_state.port_value = ""
if 'last_port_value' not in st.session_state:
    st.session_state.last_port_value = ""

def update_port():
    # Update the text input value based on the selected radio button
    if st.session_state.radio == 'Physical':
        st.session_state.last_port_value = st.session_state.port_value
        st.session_state.port_value = '9559'
    elif st.session_state.radio == 'Virtual':
        st.session_state.port_value = st.session_state.last_port_value

try:
        
    #UI selecting pepper mode
    col_1, col_2, col_3 = st.columns([1.5,2.5,1])
    with col_1:
        mode = st.radio(
            "Set the pepper mode 👉",
            options=["Virtual", "Physical"],
            key='radio',
            on_change=update_port
        )
    with col_2:
        port = st.text_input("Port:", key='port_value', max_chars=5)

    #creating the connection
    st.session_state.pepper = Connection()
    ip=''
    if(mode=="Virtual"):
        ip='127.0.0.1'
    else:
        ip='10.0.0.244'
    st.session_state.session = st.session_state.pepper.connect(ip, port)

    # Create a proxy to the AL services
    st.session_state.behavior_mng_service = st.session_state.session.service("ALBehaviorManager")
    st.session_state.tts_service = st.session_state.session.service("ALTextToSpeech")

    with col_3:
        st.write("")
        st.write("")
        if st.button("Stop Animation", type="primary"):  # Create the button
            st.session_state.behavior_mng_service.stopAllBehaviors()

    # setting parameters
    st.session_state.tts_service.setParameter("speed", 85)

    # set the aldebaran image in physical robot
    if(mode=="Physical"):
        tabletService = st.session_state.session.service("ALTabletService")
        tabletService.showImage("https://lh7-us.googleusercontent.com/docsz/AD_4nXfJtrHluXnAqOKaCKUdys9z2Bq4X9DeQqhlRQLCBEAoCG0D1EBPCrP3s7PS3FjLks1-nlJwXgb4DyfyrZJ3_TixESl4DPpAc-9HFSUFru90zGfy1xjB0Y4V1WlisA84_NmL28Kj7DLg4vULv7Ne69J0fiJ1?key=kjxxw8M2y0vUZpf5IGI7aA")
        posture_service = st.session_state.session.service("ALRobotPosture")
        posture_service.goToPosture("StandInit", 1.0)

    # Play an animation
    def animation(button_name,description,mode):

        st.session_state.behavior_mng_service .stopAllBehaviors()
        st.session_state.behavior_mng_service .startBehavior("exp/"+button_name)
        
        if(mode=="Virtual"):        
            playsound('wav/'+button_name+'.wav')
        elif(mode=="Physical"):
            st.session_state.tts_service.say(description)

    def copy_audio_from_pepper_to_laptop():
        ip_address = '10.0.0.244'
        file_path_on_pepper = "/home/nao/sharni/say.wav"
        file_path_on_laptop = "/home/buddhi/pepper/Malith/pepper_web/pepper_streamlit/wav"
        print("Copy started.............................")
        os.system("sshpass -p 'nao' scp nao@{}:{} {}".format(ip_address, file_path_on_pepper, file_path_on_laptop))
        print("Copy finished ********************************")


    # Scripts
    scripts = {
        "Yoga": {
            "yoga_1": "Hello, my name is Pepper. How are you today?",
            "yoga_2": "I would like to ask for your help if that would be okay. I am training to become a Yoga instructor and need to practice taking clients through a series of gentle stretches. Would you mind being my client?",
            "yoga_3": "Please move to the space marked on the floor.",
            "yoga_4": "Please follow my instructions through these gentle stretches. If you feel any discomfort please stop immediately and let me know.",
            "yoga_5": "Please stretch your left arm out in front like this and flex your hand.",
            "yoga_6": "Please stretch your right arm out in front like this and flex your hand.",
            "yoga_7": "Please stretch your both arms out in front like this and flex your hands.",
            "yoga_8": "Please move your left arm out to the side like this and flex your hand.",
            "yoga_9": "Please move your right arm out to the side like this and flex your hand.",
            "yoga_10": "Please move your both arms out to the side like this and flex your hands.",
            "yoga_11": "Please lift your left arm over your head like this and flex your hand.",
            "yoga_12": "Please lift your right arm over your head like this and flex your hand.",
            "yoga_13": "Please lift your both arms over your head like this and flex your hands.",
            "yoga_14": "Thank you for being my client. To show my appreciation I would like to play a quick game with you. Would you mind?"
        },
        "Ultimatum": {
            "ult_1": "I will explain the game and the rules. This game is called the Ultimatum Game. Let’s pretend that we have been given 100 dollars to share and I have to decide how we split the money. I will make you an offer that you can accept or reject. We will play for 3 rounds. Are you ready?",
            "ult_2": "I will offer you 30 dollars and will keep 70 dollars. Do you accept or reject?",
            "ult_3": "I will offer you 40 dollars and will keep 60 dollars. Do you accept or reject?",
            "ult_4": "I will offer you 50 dollars and will keep 50 dollars. Do you accept or reject?",
            "ult_5": "I will offer you 60 dollars and will keep 40 dollars. Do you accept or reject?",
            "ult_6": "I will offer you 70 dollars and will keep 30 dollars. Do you accept or reject?",
            "ult_7": "That was fun. Thank you for playing with me. Please let the researcher know we have finished. It was nice to meet you."
        }
    }

    # Apply CSS to ensure buttons have the same width
    st.markdown("""
        <style>
        .stButton button {
            width: 100%;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Create a list of button labels and their corresponding messages
    buttons = [
        ("Thank you!", "Thank you!", "thk"),
        ("Okay!", "Okay!", "okay"),
        ("Great!", "Great!", "great_1"),
        ("Excellent!", "Excellent!", "great_2"),
        ("Now...", "Now...", "now"),
        ("for the last stretch...", "for the last stretch...", "last"),
        ("Hello!", "Hello!", "hello"),
        ("Wonderful!", "Wonderful!", "wonder"),
        ("Secondly...", "Secondly...", "second"),
        ("Excuse me!", "Please excuse me!", "exc"),
        ("Pardon me!", "Pardon me!", "prd"),
        ("Minute please.", "Can you please give me a minute.", "min"),
        ("Sorry!", "Sorry!", "sorry"),
        ("Could you repeat", "Could you repeat that please!", "repeat"),
        ("Bye!", "Bye! have a nice day.", "bye_1"),
        ("See you later.", "See you later.", "bye_2")
    ]

    # Split the buttons list into two halves
    half_index = len(buttons) // 2
    buttons_col1 = buttons[:half_index]
    buttons_col2 = buttons[half_index:]
    

    cl1, cl2 = st.columns([1.5,2.5])
    with cl1:
        st.write("Actions:")
        # Create two columns
        cl1_1, cl1_2 = st.columns(2)

        # Add buttons to the first column
        with cl1_1:
            for label, message, action in buttons_col1:
                if st.button(label):
                    st.write(message)
                    animation(action, message, mode)

        # Add buttons to the second column
        with cl1_2:
            for label, message, action in buttons_col2:
                if st.button(label):
                    st.write(message)
                    animation(action, message, mode)

    with cl2:
        # Dropdown to select the script, defaulting to "Yoga"
        selected_script = st.selectbox("Select a script", options=list(scripts.keys()), index=0)
        # Display buttons and descriptions based on the selected script
        for button_name, description in scripts[selected_script].items():
            col1, col2 = st.columns([1.5, 3.5])  # Adjust the ratio as needed
            with col1:
                if st.button(button_name):  # Create the button
                    st.write(f"{button_name} pressed")
                    animation(button_name,description,mode)
            with col2:
                st.write(description)  # Display the description        

    # Function to handle the say button logic
    def process_say():
        txt = st.session_state.txt

        if mode == "Virtual":
            try:
                st.session_state.session.close()
            except:
                pass
            st.session_state.pepper = Connection()
            st.session_state.session = st.session_state.pepper.connect('10.0.0.244', 9559)
            tts = st.session_state.session.service("ALTextToSpeech")
            tts.setParameter("speed", 85)
            tts.sayToFile(txt, "/home/nao/sharni/say.wav")
            copy_audio_from_pepper_to_laptop()
            time.sleep(1)
            try:
                st.session_state.session.close()
            except:
                pass
            st.session_state.pepper = Connection()
            st.session_state.session = st.session_state.pepper.connect('127.0.0.1', port)
            st.session_state.behavior_mng_service = st.session_state.session.service("ALBehaviorManager")
            st.session_state.tts_service = st.session_state.session.service("ALTextToSpeech")
            
        animation("say", txt, mode)
        


    col9, col10 = st.columns([4, 1])   
    with col9:
        st.text_input("Type the text to say:", key="txt", on_change=process_say)

    with col10:
        st.write("")
        st.write("")

        if st.button("Say"):
            process_say()
        if st.session_state.txt:
            st.write(st.session_state.txt)
except KeyboardInterrupt:
    print("Keyboard interrupt received. Closing connection.")
    if session:
        st.session_state.session.close()
finally:
    if session:
        st.session_state.session.close()