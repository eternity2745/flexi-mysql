import mysql.connector as mc
__author__ = "Eternity"
__copyright__ = "Copyright 2025, Eternity"
__credits__ = ["Eternity"]
__license__ = "MIT"
__version__ = "0.5.0"
__maintainer__ = "Eternity"
__email__ = "vsdevan2006@gmail.com"

class connect():
    
    def __init__(self, host: str = "", user: str = "", database: str = "", password: str = "", charset: str="utf8", port: int = 3306):
        """
            Connect to MySQL Database
            Parameters
            ----------
                `host:(optional)` Name of host
                `user:(optional)` Username
                `database:(optional)` Name of Database to connect to
                `password:(optional)` MySQL password
                `charset:(optional)` Charset being used. Defaults to utf8
                `port:(optional)` Port number to be connected to. Defaults to 3306.

        """
        self.__con = mc.connect(host=host, user=user, database=database, password = password, charset=charset, port=port)
        self.__cursor = self.__con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__con.close()

    def create_database(self, database_name: str) -> None:
        """
            Create New Database
            Parameters
            ----------

                database_name: str
                        Name of the database to be created
            
            Returns
            -------

                None
        """
        self.__cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

    def drop_database(self, database_name: str) -> None:
        """
            Delete Database
            Parameters
            ----------

                database_name: str
                        Name of the database to be deleted
            
            Returns
            -------

                None
        """
        self.__cursor.execute(f"DROP DATABASE {database_name}")

    def create_table(self, table_name: str, table_schema: dict[str, str]) -> None:
        """
            Create a new table
            Parameters
            ----------

                table_name: str
                        Name of the table to be created
                table_schema: dict
                    Details of the table to be created in dictionary format
                    Eg: {"id" : "INT PRIMARY KEY", 
                         "name" : "varchar(255) NOT NULL"   
                         }
            
            Returns
            -------

                None
        """
        q = f"CREATE TABLE {table_name} ("
        c = 1
        for i in table_schema:
            if c == len(table_schema):
                q += f"{i} {table_schema[i]} )"
            else:
                q += f"{i} {table_schema[i]}, "
            c += 1
        self.__cursor.execute(q)

    def drop_table(self, table_name: str) -> None:
        """
            Deletes the specified table
            Parameters
            ----------

                table_name: str
                        The name of table to be deleted

            
            Returns
            -------

                None
        """
        q = f"DROP TABLE {table_name}"
        self.__cursor.execute(q)

    def truncate_table(self, table_name: str) -> None:
        """
            Deletes the contents from the specified table
            Parameters
            ----------

                table_name: str
                        The name of table to be delete the contents from
            
            Returns
            -------

                None
        """
        q = f"TRUNCATE TABLE {table_name}"
        self.__cursor.execute(q)

    def show_tables(self) -> list[tuple]:
        """
            Shows all tables in the connected database
        """
        q = f"SHOW TABLES"
        self.__cursor.execute(q)
        return self.__cursor.fetchall()

    def show_databases(self) -> list[tuple]:
        """
            Shows all databases
        """
        q = f"SHOW DATABASES"
        self.__cursor.execute(q)
        return self.__cursor.fetchall()

    def add_column(self, table_name: str, column_name: str, datatype: str, constraints: str=None) -> None:
        """
            Adds a new column to the specified table
            Parameters
            ----------
                table_name: str
                        Name of the table
                column_name: str
                        Name of column to be added
                datatype: str
                         Datatype of the column
                constraints: str
                         Constraints to be added like PRIMARY KEY
            
            Returns
            -------

                None
        """
        q = f"ALTER TABLE {table_name} ADD {column_name} {datatype}"
        if (constraints):
            q += f" {constraints}"
        self.__cursor.execute(q)
        self.__con.commit()

    def drop_column(self, table_name: str, column_name: str) -> None:
        """
            Deletes the specified column from the table
            Parameters
            ----------
                table_name: str
                        Name of the table
                column_name: str
                        Name of the column to be deleted
            
            Returns
            -------

                None
        """
        q = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"
        self.__cursor.execute(q)
        self.__con.commit()

    def modify_column(self, table_name: str, column_name: str, datatype: str, constraints: str=None) -> None:
        """
            Modify the colummn of a table
            Parameters
            ----------
                table_name: str
                        Name of the table
                column_name: str
                        Name of the column to be modified
                datatype: str
                        Datatype of the column
                constraints: str
                        Constraints to be added to the column like PRIMARY KEY
            
            Returns
            -------

                None

        """
        q = f"ALTER TABLE {table_name} MODIFY COLUMN {column_name} {datatype}"
        if (constraints):
            q += f" {constraints}"
        self.__cursor.execute(q)
        self.__con.commit()

    def drop_primarykey(self, table_name: str) -> None:
        """
            Delete the primary key from the table specfied
            Parameters
            ----------
                table_name: str
                        Name of the table from which the primary key is to be deleted

            Returns
            -------

                None
        """
        q = f"ALTER TABLE {table_name} DROP PRIMARY KEY"
        self.__cursor.execute(q)
        self.__con.commit()

    def drop_foreignkey(self, table_name: str, constraint_name: str) -> None:
        """
            Delete the foriegn key from the table specified
            Parameters
            ----------
                table_name: str
                        Name of the table from which the primary key is to be deleted
                constraint_name: str
                        The constraint name of the column which is a foriegn key
            
            Returns
            -------

                None
        """
        q = f"ALTER TABLE {table_name} DROP FOREIGN KEY {constraint_name}"
        self.__cursor.execute(q)
        self.__con.commit()

    def describe_table(self, table_name: str) -> list[tuple]:
        """
            Shows the structure of the specified table
            Parameters
            ----------
                table_name: str
                        Name of the table

            Returns
            -------

                None
        """
        try:
            q = f"DESC {table_name}"
        except:
            q = f"DESCRIBE {table_name}"
        
        self.__cursor.execute(q)
        return self.__cursor.fetchall()
        
    def fetch_result(self, tables: list[str], columns:list[str] = [], where: str = None, order_by: str = None, ascending: bool = False, descending: bool = False, group_by: str = None, having: str = None, limit: int = None) -> list[tuple]:
        """
            Used to fetch results from the database
            Parameters
            ----------
                tables: list
                        List of tables to be fetched. Eg: ["users", "songs"].
                columns: list
                        List of columns to be fetched. Selects all columns if no column is specified. Eg: ["id", "name"].
                where: str
                        Condition to be checked while fetching the results. Eg: "id = 2".
                order_by: str
                        Order by the given column. Eg: "id" or "id, name".
                ascending: bool
                        Order the result in ascending order.
                descending: bool
                        Order the result in descending order.
                group_by: str
                        Group the result using a column. Eg: "id".
                having: str
                        Used along with group_by for checking a specific condition. Eg: "gender = 'M'".
                limit: int
                        Used to limit the number of rows fetched.

            Returns
            -------

                list
                
        """
        q = f"SELECT "

        if columns == []:
            q += "* FROM "
        else:
            for i in range(len(columns)):
                if i == len(columns) - 1:
                    q += f"{columns[i]} FROM "
                else:
                    q += f"{columns[i]}, "

        for i in range(len(tables)):
            if i == len(tables) - 1:
                q += f"{tables[i]}"
            else:
                q += f"{tables[i]},"


        if (where):
            q+= f" WHERE {where}"

        if (order_by):
            q+= f" ORDER BY {order_by}"

        if(ascending or descending):
            q += f" {'ASC' if (ascending) else 'DESC'}"

        if(group_by):
            q+= f" GROUP BY {group_by}"
            if (having):
                q += f" HAVING {having}"
        
        if(limit):
            q += f" LIMIT {limit}"
        self.__cursor.execute(q)
        return self.__cursor.fetchall()

    def update_value(self, table_name: str, columns: list[str], set_values: list, where: str = None) -> None:
        """
            Update the values in the specified table.
            Parameters
            ----------
                `table_name:` Name of the table
                `columns:` List of columns to be updated. Eg: ["name", "age"]
                `set_values:` List of values to be set to the appropriate columns. Eg: ["Eternity", 67]
                `where:(optional)` Condition to be checked before updating. Eg: "id = 2"
        """
        q = f"UPDATE {table_name} SET "
        
        if len(columns) != len(set_values):
            raise "Number of columns should be equal to number of values"
        
        for i in range(len(columns)):
            if i == len(columns) - 1:
                q += f"{columns[i]} = '{set_values[i]}'"
            else:
                q += f"{columns[i]} = '{set_values[i]}', "

        if (where):
            q += f" WHERE {where}"

        self.__cursor.execute(q)
        self.__con.commit()

    def insert_value(self, table_name: str, value: list, columns:list[str] = []) -> None:
        """
            Used to insert a single set of values to the specified table.
            Parameters
            ----------
                table_name: str
                        Name of the table
                columns: list
                        List of columns where the value is to be inserted. If not specified value will be inserted into all columns in the table. Eg: ["id", "name", "age"]
                value: list
                        List of the set of values to be inserted. Eg: [1, "A", 32]

            Returns
            -------

                None
        """
        q = f"INSERT INTO {table_name}"

        if columns == []:
            q += ""
        else:
            q += "("
            for i in range(len(columns)):
                if i == len(columns) - 1:
                    q += f"{columns[i]}"
                else:
                    q += f"{columns[i]},"
            q+= ")"
        
        if value == []:
            raise "Enter Values"
        else:
            q += " VALUES("
            for i in range(len(value)):
                if i == len(value) - 1:
                    q += f"'{value[i]}'"
                else:
                    q += f"'{value[i]}',"
            q += ")"
        self.__cursor.execute(q)
        self.__con.commit()

    def insert_values(self, table_name: str, values: list[list], columns: list[str] = []) -> None:
        """
            Used to insert multiple sets of values to the specified table.
            Parameters
            ----------
                table_name: str
                        Name of the table
                columns: list
                        List of columns where the value is to be inserted. If not specified value will be inserted into all columns in the table. Eg: ["id", "name", "age"]
                values: list
                        Nested List of the sets of values to be inserted. Eg: [[1, "A", 32], [2, "B", 42], [3, "C", 43]]

            Returns
            -------

                None
        """
        q = f"INSERT INTO {table_name}"

        if columns == []:
            q += ""
        else:
            q += "("
            for i in range(len(columns)):
                if i == len(columns) - 1:
                    q += f"{columns[i]}"
                else:
                    q += f"{columns[i]},"
            q+= ")"
        
        if values == []:
            raise "Enter Values"
        else:
            q += " VALUES"
            for i in range(len(values)):
                q += " ("
                for j in range(len(values[i])):
                    if j == len(values) - 1:
                        q += f"'{values[i][j]}'"
                    else:
                        q += f"'{values[i][j]}',"
                if i != len(values) - 1:
                    q += "),"
            q += ")"
        self.__cursor.execute(q)
        self.__con.commit()

    def delete_value(self, table_name: str, where: str = None) -> None:
        """
            Deletes value(s) from the specified table
            Parameters
            ----------
                table_name: str
                        Name of the table
                where: str
                        Condition to check before deleting the value(s). If not specified will delete all the values from the table. Eg: "id = 3"
            
            Returns
            -------

                None
        """
        q = f"DELETE FROM {table_name}"

        if (where):
            q += f" WHERE {where}"
        self.__cursor.execute(q)
        self.__con.commit()

    def inner_join(self, table_name1: str, table_name2: str, columns: list[str] = [], condition: str = None) -> list[tuple]:
        """
            Used for INNER JOIN of two tables
            Parameters
            ----------
                table_name1: str
                        Name of first table
                table_name2: str
                        Name of the second table to be interjoined with first
                columns: list
                        List of columns from both the tables. Eg: ["name", "purchases"]
                condition: str
                        Condition to be checked on inner join
            
            Returns
            -------

                list
        """
        q = f"SELECT "

        if columns == []:
            q += f"* FROM {table_name1} INNER JOIN {table_name2} "
        else:
            for i in range(len(columns)):
                if i == len(columns) - 1:
                    q += f"{columns[i]} FROM {table_name1} INNER JOIN {table_name2} "
                else:
                    q += f"{columns[i]}, "
        
        if (condition):
            q += f"ON {condition}"
        
        self.__cursor.execute(q)
        return self.__cursor.fetchall()
    
    def left_join(self, table_name1: str, table_name2: str, columns: list[str] = [], condition: str = None) -> list[tuple]:
        """
            Used for LEFT JOIN of two tables
            Parameters
            ----------
                table_name1: str
                        Name of first table
                table_name2: str 
                        Name of the second table to be leftjoined with first
                columns: list
                        List of columns from both the tables. Eg: ["name", "purchases"]
                condition: str
                        Condition to be checked on left join

            Returns
            -------

                list
        """
        q = f"SELECT "

        if columns == []:
            q += f"* FROM {table_name1} LEFT JOIN {table_name2} "
        else:
            for i in range(len(columns)):
                if i == len(columns) - 1:
                    q += f"{columns[i]} FROM {table_name1} LEFT JOIN {table_name2} "
                else:
                    q += f"{columns[i]}, "
        
        if (condition):
            q += f"ON {condition}"
        
        self.__cursor.execute(q)
        return self.__cursor.fetchall()
    
    def right_join(self, table_name1: str, table_name2: str, columns: list[str] = [], condition: str = None) -> list[tuple]:
        """
            Used for RIGHT JOIN of two tables
            Parameters
            ----------
                table_name1: str
                        Name of first table
                table_name2: str
                        Name of the second table to be rightjoined with first
                columns: list
                        List of columns from both the tables. Eg: ["name", "purchases"]
                condition: str
                        Condition to be checked on right join

            Returns
            -------

                list
        """
        q = f"SELECT "

        if columns == []:
            q += f"* FROM {table_name1} RIGHT JOIN {table_name2} "
        else:
            for i in range(len(columns)):
                if i == len(columns) - 1:
                    q += f"{columns[i]} FROM {table_name1} RIGHT JOIN {table_name2} "
                else:
                    q += f"{columns[i]}, "
        
        if (condition):
            q += f"ON {condition}"
        
        self.__cursor.execute(q)
        return self.__cursor.fetchall()
    
    def cross_join(self, table_name1: str, table_name2: str, columns: list[str] = []) -> list[tuple]:
        """
            Used for CROSS JOIN of two tables
            Parameters
            ----------
                table_name1: str
                        Name of first table
                table_name2: str
                        Name of the second table to be crossjoined with first
                columns: list
                        List of columns from both the tables. Eg: ["name", "purchases"]
            
            Returns
            -------

                list
        """
        q = f"SELECT "

        if columns == []:
            q += f"* FROM {table_name1} CROSS JOIN {table_name2}"
        else:
            for i in range(len(columns)):
                if i == len(columns) - 1:
                    q += f"{columns[i]} FROM {table_name1} CROSS JOIN {table_name2}"
                else:
                    q += f"{columns[i]}, "
        
        self.__cursor.execute(q)
        return self.__cursor.fetchall()
        

    def raw_query(self, query: str) -> list[tuple]:
        """
            Used for fetching results from a table using MySQL Query
            Parameters
            ----------
                query: str
                        Query to be used for fetching results. Eg: "SELECT * FROM users"
                
            Returns
            -------

                list
        """
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def raw_update(self, query: str) -> None:
        """
            Used for updating values to a table using MySQL Query
            Parameters
            ----------
                query: str
                        Query to be used for updating the values. Eg: "UPDATE users SET name = 'C' WHERE id = 3"
            
            Returns
            -------

                None
        """
        self.__cursor.execute(query)
        self.__con.commit()

    def raw_delete(self, query: str) -> None:
        """
            Used for deleting values from a table using MySQL Query
            Parameters
            ----------
                query: str
                        Query to be used for deleting the values. Eg: "DELETE FROM users WHERE id = 3"

            Returns
            -------

                None
        """
        self.__cursor.execute(query)
        self.__con.commit()

    def close_connection(self) -> None:
        """
            Used to close the connection to the database.
        """
        self.__cursor.close()
        self.__con.close()