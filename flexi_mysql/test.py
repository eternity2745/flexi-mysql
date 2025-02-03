import __init__ as a
import string_decorator as sd
# a.connect(host="localhost", user = "root",database="test", password="", charset="utf8")
# print(a.fetchresult(table="songs", condition = "id in (5,6,7,8)", orderBy="title"))
# a.updatetable(table="t1", column = "name", setvalue="hello", condition="id = 2")
# a.insertvalue(table = "t2", columns = ['id', 'dept'], values=[3, 'waaw'])
# a.create_database("Test2")
# a.drop_database("Test2")
# a.create_table("t21", {
#     "id" : "int",
#     "name" : "varchar(255)"
# })
# d = {
#     "id" : "int",
#     "name" : "varchar(255)",
#      }
# a.add_column("t21", "new", "varchar(255)", "PRIMARY KEY")
# a.drop_column("t21", "new")
# a.modify_column("t21", "new", "int")
# a.drop_primarykey("t21")
# print(a.show_tables())
# print(a.show_databases())
# a.insert_values("t21", values=[[1, "new", 213], [2, "iaw", 232], [3, "hwa", 212]])
# print(a.describe_table('t21'))
# a.update_table("t21", ["id", "name"], [2, "razor"], where="id = 2")
# a.delete_value("t21")
# print(a.fetch_result(tables = ["t21"], columns=["id", "name"]))
myobj = a.connect(host="localhost", user = "root",database="test", password="")
print(myobj.fetch_result(tables = ["t1"], where="id = 2"))
