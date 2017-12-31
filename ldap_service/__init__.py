#!/usr/bin/env python3
import ldap3
from ldap3 import Server, Connection, ALL


def ldapAuth(username, pwd):
	try:
		try_login(username, pwd)
	except:
		return False
	return True


def try_login(username, pwd):
	server = Server('ldap://jet.earlham.edu', port=389, use_ssl=True, get_info=ALL)
	conn = Connection(server, 'uid='+ username +',ou=students,ou=people,dc=earlham,dc=edu', pwd, auto_bind=True)
