from db_service.basic_services import *
from ldap_service import *


def authenticate(user_id, password):
	print("Authenticating {}...".format(user_id))
	ldap_msg = ldapAuth(user_id, password)
	traildb_msg = check_for_user(user_id) if ldap_msg else False
	print('LDAP Auth: {}; Trail User: {}'.format(ldap_msg, traildb_msg))
	return ldap_msg, traildb_msg


def check_for_user(user_id):
	sql_statement = "SELECT first_name FROM users WHERE user_id = '{}'".format(user_id)
	response = query_db(sql_statement)
	final = response['rows'][0][0] if response else False
	print("=> Query    : ", sql_statement)
	print("   Response : ", final)
	return final


def register_user(user_id, name):
	sql_statement = "INSERT INTO users VALUES ('{}', '{}')".format(user_id, name)
	response = post_db(sql_statement)
	if response:
		final = response
		print("=> Query    : ", sql_statement)
		print("   Response : ", final)
		user_data = check_for_user(user_id)
		return user_data
	else:
		return False
