from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/signup')
def display_signup():
	return render_template('signup.html', title='Signup', username='', password='', verify_password='', email='')

def is_empty(input):
	if not input:
		return True

def has_space(input):
	if ' ' in input:
		return True

def within_character_limit(input):
	if 2 < len(input) < 21:
		return True

def passwords_match(password, verification):
	if password == verification:
		return True

def has_single_at_symbol(input):
	if input.count('@') == 1:
		return True
 
def has_single_period(input):
	if input.count('.') == 1:
		return True   


@app.route('/signup', methods=['POST'])
def validate_signup():
	username=request.form['username']
	error_username=''
	
	password=request.form['password']
	error_password=''
	verify_password=request.form['verify-password']
	error_verify_password=''

	email=request.form['email']
	error_email=''

	# Username validation
	# Errors if blank, outside character limit, or has space
	if (     is_empty(username)
		or   has_space(username)
		or   not within_character_limit(username)
		):
		error_username = "That's not a valid username"

	# Password validation
	# Errors if blank, oustisde character limit, or has space 
	if (     is_empty(password)
		or   has_space(password)
		or   not within_character_limit(password)
		):
		error_password = "That's not a valid password"

	# Password verification validation
	# Errors if blank, does not match password
	if (     is_empty(verify_password)
		or   not passwords_match(password,verify_password)
		):
		error_verify_password = "Passwords don't match"	

	# Email validation
	# If entered, error if space, outside char limit, 
	# improper @ and . quantities
	if not is_empty(email):
		if (     has_space(email)
			or   not within_character_limit(email)
			or   not has_single_period(email)
			or   not has_single_at_symbol(email)
			):
			error_email = "That's not a valid email"


	if (    not error_username
		and not error_password
		and not error_verify_password
		and not error_email):
		return render_template('welcome.html', username=username, title='Welcome')


	return render_template('signup.html', 
							username=username,
							email=email,
							error_username=error_username,
							error_password=error_password,
							error_verify_password=error_verify_password,
							error_email=error_email,
							tite=Signup)


app.run()