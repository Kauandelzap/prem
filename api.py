import os
import requests
from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route("/")
def ok():
    return "compre api com o kauan del zap: +5511959263200"
    
    
    
@app.route("/acccheck/<email>/<senha>/bykauan")
def acccheck(email, senha):
    payload = {     
                "email": email,
                "password": senha
              }
    re = requests.post('https://discord.com/api/v6/auth/login', json=payload).json()
    if 'email' in re:
     return f"senha ou email incorreto"
    else:
        return f"token: {re['token']}\n\n\n NEXUS API"
        
        
    
@app.route("/tokencheck/<token>/bykauan")
def tokencheck(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    re = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
    if 'status' in re:
     return f"token incorreto"
    else:
        return f"TOKEN: {token}\n\nID: {re['id']}\n USUARIO: {re['username']}#{re['discriminator']}\nLOCALIZAÇÃO: {re['locale']}\nEMAIL: {re['email']}\nNUMERO: {re['phone']}\nNSFW: {re['nsfw_allowed']}\nVERIFICADO: {re['verified']}\nV2E: {re['mfa_enabled']}\nBIO: {re['bio']}\n\n\n NEXUS API"
        
        

app.run(debug = False)
