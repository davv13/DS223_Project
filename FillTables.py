import pandas as pd 
from customer_retention_toolkit.db.sql_interactions import  SqlHandler
import os
# os.chdir(".")

df  = pd.read_csv("updated_telecom_data.csv")

def InsertToTables():
    table_names = ['State','PlanDetails','DayUsage','EveUsage','NightUsage','IntlUsage']
    
    sql = SqlHandler('temp','State')
    sql.get_table_columns()
    sql.insert_many(df)
    sql.close_cnxn()
    

    sql = SqlHandler('temp','PlanDetails')
    sql.get_table_columns()
    sql.insert_many(df)
    sql.close_cnxn()
    
    sql = SqlHandler('temp','DayUsage')
    sql.get_table_columns()
    sql.insert_many(df)
    sql.close_cnxn()

    sql = SqlHandler('temp','EveUsage')
    sql.get_table_columns()
    sql.insert_many(df)
    sql.close_cnxn()

    sql = SqlHandler('temp','NightUsage')
    sql.get_table_columns()
    sql.insert_many(df)
    sql.close_cnxn()

    sql = SqlHandler('temp','IntlUsage')
    sql.get_table_columns()
    sql.insert_many(df)
    sql.close_cnxn()

    sql = SqlHandler('temp','CustomerMetrics')
    sql.get_table_columns()
    sql.insert_many(df)
    sql.close_cnxn()