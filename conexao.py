#import psycopg2
import sqlite3 as conexao

conn = conexao.connect('jdbc:sqlite:{file}')

query = conn.cursor()

