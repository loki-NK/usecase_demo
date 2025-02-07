import streamlit as st
from plivo import plivoxml

def generate_waiting_room_xml():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.ConferenceElement(
            'Waiting Room',
            wait_sound='https://<yourdomain>.com/waitmusic/',
            enter_sound=''))
    return response.to_string()

def generate_operator_room_xml():
    operator_response = plivoxml.ResponseElement()
    operator_response.add(
        plivoxml.ConferenceElement(
            'Waiting Room', enter_sound='', end_conference_on_exit=True))
    return operator_response.to_string()

st.title("Plivo Conference XML Generator")
option = st.selectbox("Choose XML to Generate:", ["Waiting Room", "Operator Room"])

if option == "Waiting Room":
    st.code(generate_waiting_room_xml(), language='xml')
elif option == "Operator Room":
    st.code(generate_operator_room_xml(), language='xml')
