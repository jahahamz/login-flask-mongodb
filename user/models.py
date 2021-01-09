from flask import Flask, jsonify, request
import uuid
from passlib.hash import pbkdf2_sha256

class User:

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


        return jsonify(user), 200