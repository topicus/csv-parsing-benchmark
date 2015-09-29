import csv
import MySQLdb as mdb
import sys
import os

try:
    con = mdb.connect('localhost', 'root', '', 'datastore');
    cur = con.cursor()
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

def create_table(table_name, fields, mysql):
  sql = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' ('
  for field in fields:
    sql += field + " VARCHAR(255),"
  sql = sql[:-1]
  sql = sql + ');'
  mysql.execute(sql)

def insert(table_name, fields, mysql):
  sql = 'INSERT INTO ' + table_name + ' VALUES ('
  for field in fields:
    sql +=  '"' + con.escape_string(field) + '",'
  sql = sql[:-1]
  sql = sql + ');'
  mysql.execute(sql)

def sanitize(field):
  field = '__' + field
  field = field.replace(" ", "_")
  field = field.replace("/", "")
  field = field.replace(":", "")
  return field.lower()


table_name = 'test'
table_suffix = '_csv';
batch_size = 1000

with open(table_name + '.csv', 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
  fields = [sanitize(l) for l in spamreader.next()]
  create_table(table_name + table_suffix, fields, cur)
  row_count = 0;
  for row in spamreader:
    insert(table_name + table_suffix, row, cur)
    if (row_count % batch_size == 0):
      con.commit()
    row_count += 1
  con.commit()