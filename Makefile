all: gui

gui:
	cd qt; \
	python3 main.py

gen:
	python3 db_tools/create_db.py

server:
	@mongod --dbpath ~/db/seadb/db

