import sqlalchemy as sa

def init_db(env):
    #implement later
    host=env['datasource']['host']
    username=env['datasource']['username']
    password=env['datasource']['password']
    port=env['datasource']['port']
    database=env['datasource']['database']
    cnxString = 'mssql+pyodbc://{}:{}@{}/{}'.format(username,password,host,database)
    engine = sa.create_engine(cnxString)
    print("initialized the database")
    return engine
