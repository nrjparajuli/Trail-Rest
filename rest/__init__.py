#!/usr/bin/env python3
from multiprocessing import Process
from flask import Flask, request
import json

from configuration import config
from db_service import user_services, game_services


class TrailServer:
	def __init__(self, env='dev'):
		self.app = Flask(__name__, instance_relative_config=True)
		self.server = Process(target=self.run_server)

		self.port_num = config['PORT_NUMBER']
		self.env = env

		# for game in game_services.get_all_created_games('ltnguyen14'):
		#  	game_services.delete_game_admin(game , 'ltnguyen14')

		@self.app.route("/log-in", methods=['GET', 'POST'])
		def log_in():
			data = request.get_json()
			response = user_services.authenticate(data['username'], data['password'])
			return json.dumps({'username': data['username'], 'isEcUser': response[0], 'trailUserName': response[1]})

		@self.app.route("/register-user", methods=['GET', 'POST'])
		def register_user():
			data = request.get_json()
			response = user_services.register_user(data['username'], data['fullname'])
			json.dumps({'user': data['username'], 'trailUserName': response[1]})
			return json.dumps({'user': data['username'], 'trailUserName': response[1]})

		@self.app.route("/get_all_locations", methods=['GET', 'POST'])
		def get_all_locations():
			response = game_services.get_all_locations()
			return json.dumps({'locations':[item for item in response]})

		@self.app.route("/create_new_game", methods=['GET', 'POST'])
		def create_new_game():
			data = request.get_json()
			gameid = game_services.create_new_game(data['GameName'], data['username'])
			for locationPair in data['GameAttrs']:
				game_services.add_attribute(data['GameName'], data['username'], locationPair['rank'],
												locationPair['location'], locationPair['message'])
			game_services.add_invitees_to_game(data['GameName'], data['username'], data['Invitees'])
			#game_services.add_invitees_to_game(data['GameName'], data['username'], [data['username']])
			return 'true'

		@self.app.route("/get_game_attributes", methods=['GET', 'POST'])
		def get_game_attributes():
			data = request.get_json()
			response = game_services.get_game_attributes(data['game_name'], data['creator_id'])
			return json.dumps({'attributes':response})

		@self.app.route("/get_all_created_games", methods=['GET', 'POST'])
		def get_all_created_games():
			data = request.get_json()
			response = game_services.get_all_created_games(data['user_id'])
			return json.dumps({'games':response})

		@self.app.route("/get_invited_games", methods=['GET', 'POST'])
		def get_invited_games():
			data = request.get_json()
			response = game_services.get_invited_games(data['user_id'])
			return json.dumps({'games':response})

		@self.app.route("/get_completed_games", methods=['GET', 'POST'])
		def get_completed_games():
			data = request.get_json()
			response = game_services.get_completed_games(data['user_id'])
			if response == []:
				return json.dumps([])
			else:
				return json.dumps({'games':[item[0] for item in response]})

		@self.app.route("/add_invitees_to_game", methods=['GET', 'POST'])
		def add_invitees_to_game():
			data = request.get_json()
			response = game_services.add_invitees_to_game(data['game_name'], data["user_id"], [data["invitees_list"]])
			return json.dumps({'response':response})

		@self.app.route("/get_game_invitees", methods=['GET', 'POST'])
		def get_game_invitees():
			data = request.get_json()
			response = game_services.get_game_invitees(data['game_name'], data["user_id"])
			return json.dumps({'invitees':response})

		@self.app.route("/update_game_status", methods=['GET', 'POST'])
		def update_game_status():
			data = request.get_json()
			response = game_services.update_game_status(data['game_name'], data["creator_id"], data['player_id'], data["time"])
			return json.dumps({'update':response})

		@self.app.route("/delete_game_admin", methods=['GET', 'POST'])
		def delete_game_admin():
			data = request.get_json()
			response = game_services.delete_game_admin(data['game_name'], data["user_id"])
			return json.dumps({'update':response})

	def start(self):
		self.server.start()

	def run_server(self):
		if self.env == 'dev':
			self.app.run(debug=True, port=self.port_num, use_reloader=False)
		elif self.env == 'prod':
			self.app.run(debug=True, host="0.0.0.0", port=self.port_num, use_reloader=False)
