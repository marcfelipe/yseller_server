from connection import conectar_db


#banco = 'c:/syspdv/syspdv_srv_ARAFAT.fdb'   #ruim
#banco = 'c:/syspdv/syspdv_srv_HIPERSACOLAO_LJ2.fdb'
#banco = 'c:/syspdv/syspdv_srv_I C DA SILVA.fdb'
#banco = 'c:/syspdv/syspdv_srv_SJMD_CAMPOS_SALES.fdb'
#banco = 'c:/syspdv/syspdv_srv_SUPERJB.fdb'
#banco = 'c:/syspdv/syspdv_srv_JESUS ME DEU CANARANAS SOMENTE CADASTRO.fdb'

db_ = conectar_db('localhost', banco)
cursor = db_.cursor()

sql = "select procod,prodes,seccod,proprcvdavar from produto where procod<999 order by procod"

cursor.execute(sql)
rs = cursor.fetchall()

for line in rs:
    print(line)