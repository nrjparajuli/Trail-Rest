from db_service.basic_services import *


def get_all_locations():
	sql_statement = "SELECT * FROM locations"
	response = query_db(sql_statement)
	final = response['rows'] if response else False
	return final


def create_new_game(game_name, user_id):
    sql_statement = "Insert into Games (game_name,creator_id) values ('{}','{}')".format(game_name,user_id)
    response = post_db(sql_statement)
    return response


def add_attribute(game_name, user_id, location_num, location, message):
    game_id_sql_statement = "SELECT game_id FROM games WHERE game_name='{}' AND creator_id='{}'".format(game_name, user_id)
    response = query_db(game_id_sql_statement)
    game_id = response['rows'][0][0] if response else False

    insert_sql_statement = "INSERT INTO GamesLocation VALUES \
    ('{}', '{}', '{}', '{}')".format(game_id, location_num, location, message)
    final = post_db(insert_sql_statement)
    return final


def add_invitees_to_game(game_name, user_id, invitees_list):
	game_id_sql_statement = "SELECT game_id FROM games WHERE game_name='{}' AND creator_id='{}'".format(game_name, user_id)
	response = query_db(game_id_sql_statement)
	game_id = response['rows'][0][0] if response else False

	for invitee in invitees_list:
		insert_sql_statement = "INSERT INTO Invites VALUES ('{}', '{}')".format(game_id, invitee)
		response = post_db(insert_sql_statement)
	return response


def get_all_created_games(user_id):
	sql_statement = "SELECT game_name FROM games WHERE creator_id='{}'".format(user_id)
	response = query_db(sql_statement)
	final = [val[0] for val in response['rows']] if response else []
	return final

def get_invited_games(user_id):
    sql_statement = "SELECT game_name, creator_id FROM Games WHERE game_id IN \
    ( SELECT game_id FROM Invites WHERE invitee = '{}' AND completed IS NULL)".format(user_id)
    response = query_db(sql_statement)
    final = [[val[0] for val in response['rows']],[val[1] for val in response['rows']]] if response else []
    return final


def get_game_invitees(game_name, user_id):
	sql_statement = "SELECT invitee FROM Invites WHERE game_id IN \
	(SELECT game_id FROM games WHERE game_name='{}' AND creator_id='{}')".format(game_name, user_id)
	response = query_db(sql_statement)
	final = [val[0] for val in response['rows']] if response else False
	return final


def get_game_attributes(game_name, creator_id):
    sql_statement = "SELECT location_num, location, message FROM GamesLocation WHERE game_id \
    in (SELECT game_id FROM Games WHERE game_name = '{}' and creator_id = '{}')".format(game_name, creator_id)
    response = query_db(sql_statement);
    return response['rows']


def get_completed_games(user_id):
	sql_statement = "SELECT game_name, duration_min FROM Games G, Invites I WHERE \
	G.game_id=I.game_id AND completed AND invitee='{}'".format(user_id)
	response = query_db(sql_statement)
	final = [(val[0], (val[1])) for val in response['rows']] if response else []
	return final


def update_game_status(game_name, creator_id, player_id, time):
	sql_statement = "UPDATE Invites SET completed='t', duration_min='{}' WHERE invitee='{}' \
	AND game_id IN (SELECT game_id FROM Games WHERE game_name='{}' AND creator_id='{}')".format(time, player_id, game_name, creator_id)
	response = post_db(sql_statement)
	return response


def forfeit_game(game_name, creator_id, player_id):
	sql_statement = "UPDATE Invites SET completed='f' WHERE invitee='{}' \
	AND game_id IN (SELECT game_id FROM Games WHERE game_name='{}' AND creator_id='{}')".format(player_id, game_name, creator_id)
	response = post_db(sql_statement)
	return response


def delete_game_admin(game_name, user_id):
	sql_statement = "DELETE FROM Games WHERE game_name='{}' AND creator_id='{}'".format(game_name, user_id)
	response = post_db(sql_statement)
	return response


def delete_game_invitee(game_name, creator_id, player_id):
    sql_statement = "DELETE FROM Invites WHERE invitee = '{}' and game_id IN (SELECT game_id FROM Games \
    WHERE creator_id = '{}' and game_name = '{}')".format(player_id, creator_id, game_name)
    response = post_db(sql_statement)
    return response
