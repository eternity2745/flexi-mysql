# Flexi MySQL
[![PyPI version](https://badge.fury.io/py/flexi-mysql.svg)](https://badge.fury.io/py/flexi-mysql) [![PyPI Downloads](https://static.pepy.tech/badge/flexi-mysql)](https://pepy.tech/projects/flexi-mysql) [![Downloads](https://static.pepy.tech/badge/flexi-mysql/month)](https://pepy.tech/project/flexi-mysql) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<p>Flexi MySQL is a Python module designed to streamline the process of interacting with MySQL databases. This module offers a variety of functions that significantly reduce the need for manually typing queries, executing them, and handling the results or committing data to the database. Additionally, for scenarios requiring raw SQL queries, the module provides support for creating such queries using MySQL

## Examples
### Fetching results from the database
```py
import flexi_mysql
myobj = flexi_mysql.connect(host="localhost", user = "root",database="test", password="")
print(myobj.fetch_result(tables = ["t1"], where="id = 2"))
```
### Close connection
```py
import flexi_mysql 
myobj = flexi_mysql.connect(host="localhost", user = "root",database="test", password="")
myobj.close_connection()
```
### Update value in a table
```py
import flexi_mysql
myobj =  flexi_mysql.connect(host="localhost", user="root", database="test")
myobj.update_value(table_name="t1", columns = ["name"], value="Eternity", where = "id = 4")
```
### Fetching results from database using with statement
```py
import flexi_mysql
with flexi_mysql.connect(host="localhost", user="root", database="test") as myobj:
    print(myobj.fetch_result(tables = ["t1"], where="id = 2"))
```
## Documentation

| Name | Description |
|:--|:--|
| `create_database` | Create New Database |
| `drop_database` | Delete Database |
| `create_table` | Create a new table |
| `drop_table` | Deletes the specified table |
| `truncate_table` | Deletes the contents from the specified table |
| `show_tables` | Shows all tables in the connected database |
| `show_databases` | Shows all databases |
| `add_column` | Adds a new column to the specified table |
| `drop_column` | Deletes the specified column from the table |
| `modify_column` | Modify the colummn of a table |
| `drop_primarykey` | Delete the primary key from the table specfied |
| `drop_foreignkey` | Delete the foriegn key from the table specified |
| `describe_table` | Shows the structure of the specified table |
| `fetch_result` | Used to fetch results from the database |
| `update_value` | Update the values in the specified table. |
| `insert_value` | Used to insert a single set of values to the specified table. |
| `insert_values` | Used to insert multiple sets of values to the specified table. |
| `delete_value` | Deletes value(s) from the specified table |
| `inner_join` | Used for INNER JOIN of two tables |
| `left_join` | Used for LEFT JOIN of two tables |
| `right_join` | Used for RIGHT JOIN of two tables |
| `cross_join` | Used for CROSS JOIN of two tables |
| `raw_query` | Used for fetching results from a table using MySQL Query |
| `raw_update` | Used for updating values to a table using MySQL Query |
| `raw_delete` | Used for deleting values from a table using MySQL Query |
| `close_connection` | Used to close the connection to the database. |


