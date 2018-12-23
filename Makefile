all: gui

gui:
	cd app; \
	python3 main.py

gen:
	python3 db_tools/create_db.py

server:
	@mongod --dbpath ~/db/seadb/db

clean_plots:
	rm -rf app/images/plots
	mkdir app/images/plots

