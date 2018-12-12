all: gui

gui:
	python3 qt/main.py

gen:
	python3 db_tools/create_db.py

server:
	@mongod --dbpath ~/db/seadb/db

