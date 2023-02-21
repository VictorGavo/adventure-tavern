from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets

# Set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return Player.query.get(user_id)

class Player(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable=True, default='')
    email = db.Column(db.String(150), nullable=True)
    password = db.Column(db.String, nullable=True, default='')
    g_auth_verify = db.Column(db.Boolean, default=False)
    token = db.Column(db.String, default='', unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'
    
class Character(db.Model):
    id = db.Column(db.String, primary_key=True)
    info = db.Column(db.String)
    choices = db.Column(db.String)
    inventory = db.Column(db.String, default='', unique=True)
    token = db.Column(db.String, default='', unique=True)
    player_token = db.Column(db.String, db.ForeignKey('player.token'), nullable=False)

    def __init__(self, info, choices, inventory, player_token, level=1, token='', id=''):
        self.id = self.set_id()
        self.info = info
        self.level = level
        self.choices = choices
        self.token = self.set_token(24)
        self.inventory = inventory
        self.player_token = player_token

    def __repr__(self):
        return f'The mortal {self.name} seeks fortune as an adventurer.'
    
    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return (secrets.token_urlsafe())

# class Inventory(db.Model):
#     id = db.Column(db.String, primary_key=True)
#     character_token = db.Column(db.String, db.ForeignKey('character.token'), nullable=False)
#     max_carry = db.Column(db.String(5))
#     current_carry = db.Column(db.String(5))
#     bag = db.Column(db.String)

class CharacterSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'level', 'race', 'background', 'inventory']

char_schema = CharacterSchema()
chars_schema = CharacterSchema(many=True)