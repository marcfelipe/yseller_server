import fdb

def conectar_db(host, database='c:/syspdv/syspdv_srv.fdb'):
    connection = fdb.connect(host=host,
                      database=database,
                      user='SYSDBA',
                      password='masterkey')
    return connection

def conectar_db_linux(host, database='c:/syspdv/syspdv_srv.fdb'):
    connection = fdb.connect(host=host,
                      database=database,
                      user='SYSDBA',
                      password='masterkey',
                      charset='ISO8859_1')
    return connection    