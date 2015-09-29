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


def load_infile(filename, cur, con):
  sql = 'LOAD DATA INFILE "' + filename + '"  INTO TABLE test_csv COLUMNS TERMINATED BY "," LINES TERMINATED BY "\n" IGNORE 1 LINES';
  cur.execute(sql)
  con.commit()


load_infile(os.path.abspath("test.csv"), cur, con)