
import sqlite3

connection = sqlite3.connect('/share/flask-orari-lavoro/database.db')
connection.row_factory = sqlite3.Row
connection.execute('CREATE TABLE IF NOT EXISTS "PRESENZE" (	"id"	integer,	"giorno"	varchar2(20),	"oranetr"	varchar2(20),	"orausci"	varchar2(20),	"pausa"	varchar2(1) DEFAULT N,	PRIMARY KEY("id" AUTOINCREMENT))'
connection.commit()
connection.close()