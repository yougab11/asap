from typing import Counter
from flask import Flask
from flask import jsonify, request, render_template
import re

app = Flask(__name__)

#save time not creating a database
database = [{"first_name": "Jose", "last_name": "Vasconcelos", "dob": "01/01/1961", "country": "MX"}, 
    { "first_name": "test", "last_name": "tester", "dob": "01/01/1991", "country": "US"}]


@app.route('/')
def hello():
    return 'Hi all i havent done python in a long time but it\'s alright i guess'


# /member_id [POST] JSON API Endpoint
# ● Generate a member ID
# ○ Must be verifiable (like credit card numbers or driver's license numbers)
# ○ Must be globally unique
# ● Takes a POST request with first name, last name, date of birth, and 2 character country of
# origin code.
# ● Example Payload: {"first_name": "Jose", "last_name": "Vasconcelos",
# "dob": "01/01/1961", "country": "MX"}
@app.route('/member_id', methods=['POST'])
def member_id():
    #todo test for valid types and other things
    request.json
    database.append(request.json)
    return jsonify(database)


@app.route('/members', methods=['GET'])
def members():
    return jsonify(database)

# /member_id/validate [GET, POST] HTML Endpoint
# ● Write a simple HTML view with a form that takes a Member ID and validates whether it is a
# valid Member ID generated by the mechanism in the previous task.
# ● Return a descriptive error message if the Member ID is not valid.
# ● Return a success message if the Member ID is valid.
# ● No need to spend too much time styling this. Plain HTML is fine. Minimal styling encouraged.
@app.route('/member_id/validate', methods=['POST', 'GET'])
def validate():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        dob = request.form['dob']
        country = request.form['country']
        if validate_data({"first_name": firstname, "last_name": lastname, "dob": dob, "country": country}):
            return render_template('valid_member.html', firstname = firstname, lastname= lastname, dob = dob, country = country, not_valid = False)
        else:
            return render_template('valid_member.html', firstname = firstname, lastname= lastname, dob = dob, country = country, not_valid = True)
    return render_template('valid_member.html')



def validate_data(data):
    #process data
    #very dumb validation
    valid = False
    for user in database:
        dobuser = re.sub("[^0-9]", "",user['dob'])
        dobdata = re.sub("[^0-9]", "",data['dob'])
        if user['first_name'] == data['first_name'] and user['last_name'] == data['last_name'] and dobuser == dobdata and user['country'] == data['country']:
            valid = True
    return valid


    