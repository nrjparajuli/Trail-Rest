import psycopg2
from psycopg2 import extras
from configuration import config


def query_db(user_query):
	try:
		conn = psycopg2.connect(
			"dbname='{}' user='{}' host='{}' password='{}'".format(config['DB_NAME'],
			                                                       config['DB_USERNAME'],
			                                                       config['API_URL'],
			                                                       config['DB_PWD']))
		cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

		cursor.execute(user_query)
		col_names = [desc[0] for desc in cursor.description]
		rows = cursor.fetchall()
		conn.close()

		result = False if (len(rows) == 0) else {'column_names': col_names, 'rows': rows}
		return result

	except:
		print("We are having troubles connecting to our database at this point. Please try again later.")
		return False


def post_db(user_query):
	try:
		conn = psycopg2.connect(
			"dbname='{}' user='{}' host='{}' password='{}'".format(config['DB_NAME'],
			                                                       config['DB_USERNAME'],
			                                                       config['API_URL'],
			                                                       config['DB_PWD']))
		cursor = conn.cursor()
		cursor.execute(user_query)
		conn.commit()
		conn.close()
		return True
	except:
		print("ERROR    ==: ")
		print("We are having troubles connecting to our database at this point. Please try again later.")
		print("ERROR AT ==> ", user_query)
		return False