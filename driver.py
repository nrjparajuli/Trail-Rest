#!/usr/bin/env python3
from rest import TrailServer


def main():
	server = TrailServer(env='prod') # use 'dev' or 'prod'
	server.start()

if __name__ == "__main__":
	main()
