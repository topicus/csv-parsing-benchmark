## Results

### Parsing

#### php 
```time php parse.php```
parse.php  36.16s user 0.54s system 95% cpu 38.493 total

#### Python
```time python parse.py```
parse.py  11.48s user 0.24s system 99% cpu 11.758 total

#### Node (fast-csv)
```time node parse.js```
parse.js  57.34s user 0.91s system 97% cpu 59.982 total

#### C
```time ./parser```
parser  3.09s user 0.53s system 91% cpu 3.937 total


### Data Import

#### Python
```time python parse_and_import.py```
parse_and_import.py  139.59s user 30.19s system 45% cpu 6:15.36 total

#### MySQL
```LOAD DATA INFILE 'test.csv' INTO TABLE test_csv COLUMNS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;```
Query OK, 2737929 rows affected, 65535 warnings (19.09 sec)
Records: 2737929  Deleted: 0  Skipped: 0  Warnings: 629752

## Requirements

### Node
```npm install``

### Python
```pip install MySQL-python```