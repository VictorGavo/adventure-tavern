from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, Player, Character, char_schema, chars_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/tavern', methods=['POST'])
@token_required
def create_char(current_user_token):
    print(f'BIG TESTER: {current_user_token}')

    name = request.json['name']
    race = request.json['race']
    background = request.json['background']
    inventory = request.json['inventory']
    player_token = current_user_token.token


    char = Character(name, race, background, inventory, player_token)

    db.session.add(char)
    db.session.commit()

    response = char_schema.dump(char)
    return jsonify(response)

@api.route('/tavern', methods=['GET'])
@token_required
def get_char(current_user_token):
    a_user = current_user_token.token
    chars = Character.query.filter_by(player_token=a_user).all()
    response = chars_schema.dump(chars)
    return jsonify(response)

@api.route('/tavern/<id>', methods=['GET'])
@token_required
def get_single_char(current_user_token, id):
    char = Character.query.get(id)
    response = char_schema.dump(char)
    return jsonify(response)

@api.route('/tavern/<id>', methods=['POST', 'PUT'])
@token_required
def update_char(current_user_token, id):
    char = Character.query.get(id)
    char.name = request.json['name']
    char.level = request.json['level']
    char.race = request.json['race']
    char.background = request.json['background']
    char.inventory = request.json['inventory']
    char.player_token = current_user_token.token

    db.session.commit()
    response = char_schema.dump(char)
    return jsonify(response)

@api.route('/tavern/<id>', methods=['DELETE'])
@token_required
def delete_char(current_user_token, id):
    char = Character.query.get(id)
    db.session.delete(char)
    db.session.commit()
    response = char_schema.dump(char)
    return jsonify(response)