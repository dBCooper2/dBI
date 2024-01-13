# Written with Phind, prompt was: ""
# With the pythonTrader_schema.sql passed in as an additional argument

import sqlite3
conn = sqlite3.connect("pythonTrader_test.db")

with open('pythonTrader_schema.sql') as fp:
   cur = conn.cursor()
   cur.execute_script(fp.read())

conn.commit()


