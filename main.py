from flask import Flask, Response
from plivo import plivoxml

app = Flask(__name__)

@app.route('/waiting_room', methods=['GET'])
def waiting_room():
    response = plivoxml.ResponseElement()
    response.add(
        plivoxml.ConferenceElement(
            'Waiting Room',
            wait_sound='https://<yourdomain>.com/waitmusic/',
            enter_sound=''))
    return Response(response.to_string(), mimetype='application/xml')

@app.route('/operator_room', methods=['GET'])
def operator_room():
    operator_response = plivoxml.ResponseElement()
    operator_response.add(
        plivoxml.ConferenceElement(
            'Waiting Room', enter_sound='', end_conference_on_exit=True))
    return Response(operator_response.to_string(), mimetype='application/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
