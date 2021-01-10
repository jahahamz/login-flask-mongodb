from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print(request.form)

        # Create user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
        }

        # Encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email in database
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Oops! Looks like there's already an account associated with this email"}), 400
        
        if db.users.insert_one(user):
            return self.start_session(user)
        
        return jsonify({"error": "Hmmm, something went wrong. Please check your email / password and try again"}), 400

    def logout(self):
        session.clear()
        return redirect('/')
    
    def login(self):

        user = db.users.find_one({
            "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)
        if not user:
            return jsonify({"error": "Hmmm, looks like there's is no account associated with this email"}), 401
        
        return jsonify({"error": "Ooops, something went wrong. Please check your email / password and try again"}), 401
