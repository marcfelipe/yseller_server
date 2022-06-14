from itertools import product
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date, time
from controllers.connection import conectar_db
from functions import null_validation
from models.order import OrderInsert, OrderItemsInsert

import sql_variables
import pprint

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)
""" uvicorn main:app --reload --host 0.0.0.0 --port 8088


"""
#db_ = conectar_db('yanconortesrvda', 'c:/controle os/sistema_os.fdb')
db_ = conectar_db('localhost', 'c:/syspdv/syspdv_srv.fdb')
cursor = db_.cursor()

@app.get('/api/orders/all')
async def root(short: Optional[bool] = False):        
    sql = sql_variables.list_all_orders
    cursor.execute(sql)
    rs = cursor.fetchall()   
    columns = list(zip(*cursor.description))[0]
    orders = []
    for order in rs:
        order_dict = {}
        for indexcolumn, column in enumerate(columns):
            order_dict[column] = order[indexcolumn]
        orders.append(order_dict)    
    return orders



@app.get('/api/orders/status/{stacod}')
def list_orders_by_status(stacod: str):
    sql = sql_variables.list_orders_by_status
    print(sql)
    criteria = str(stacod).upper()
    cursor.execute(sql, [criteria])
    rs = cursor.fetchall()   
    columns = list(zip(*cursor.description))[0]
    orders = []
    for order in rs:
        order_dict = {}
        for indexcolumn, column in enumerate(columns):
            order_dict[column] = order[indexcolumn]
        orders.append(order_dict)    
    return orders

@app.get('/api/orders/order_number/{pvdnum}')
def find_order_by_number(pvdnum: int):
    sql = sql_variables.list_orders_by_code
    criteria = str(pvdnum).zfill(10)    
    cursor.execute(sql, [criteria])
    order_bd = cursor.fetchone()   
    columns = list(zip(*cursor.description))[0]
    order_dict = {}
    for indexcolumn, column in enumerate(columns):
        order_dict[column] = order_bd[indexcolumn]    
    return order_dict

@app.get('/api/practice')
def list_practice_bool(short: Optional[bool] = False):
    """    
    make a request: http://url:8050/api/practice?short=true
    """
    if short:
        return {'qual a visão': 'verdade'}
    else:
        return {'pega a visão': 'passado falso'}

# @app.get('/api/tickets/{id}')
# def list_specific_ticket():
#     pass
#
# @app.put('/api/tickets/{id}')
# def update_ticket():
#     pass
#
# @app.delete('/api/tickets/{id}')
# def delete_ticket():
#     pass
#
@app.get('/api/clients')
def list_clients():
    """
    make a request: http://url:8050/api/clients
    """
    sql_cliente = sql_variables.list_all_clients
    cursor.execute(sql_cliente)    
    rs = cursor.fetchall()
    columns = list(zip(*cursor.description))[0]
    clients = []
    for client in rs:
        client_dict = {}
        for indexcolumn, column in enumerate(columns):
            client_dict[column] = client[indexcolumn]
        clients.append(client_dict)    
    return clients

@app.get('/api/clients/{client_id}')
def list_client_by_id(client_id):
    """
    make a request: http://url:8050/api/clients/{client_id}
    """
    sql_client=sql_variables.list_client_by_code
    criteria = str(client_id).zfill(15)
    cursor.execute(sql_client, [criteria])
    client = cursor.fetchone()          
    columns = list(zip(*cursor.description))[0]
    client_dict = {}
    for indexcolumn, column in enumerate(columns):
        client_dict[column] = client[indexcolumn]     
    return client_dict


class TicketIn(BaseModel):
    client_code: int
    problem_reported: str
    attendant_code: str
    client_contact: Optional[str]
    description: Optional[str]
    open_date: Optional[date]
    open_time: Optional[time]


@app.post('/api/ticket/')
def open_new_ticket(ticket: TicketIn):
    client_id = str(ticket.client_code).zfill(15)
    print('Abrindo chamado para o cliente:', client_id)
    if ticket.open_date is None:
        #date_ticket = datetime.today()
        now = datetime.now()
        date_ticket = datetime.date(now)
        print('será utilizada a data atual:', date_ticket)
    else:
        date_ticket = ticket.open_date
    if ticket.open_time is None:
        time_ticket = datetime.time(now)
        print('hora:', time_ticket)
    else:
        time_ticket = ticket.open_time


    sql_insert_ticket="""insert into att_logger(codatt,attdes,attdataabe,clicod,sysserie,clides,tel1,tel2,cel,funcod,
        attprorep,atttipo,atthorabe,sitcod,contato_reportante,tppendcod)
        values (?,?,?,?,?,?,?,?,?,?,?,?,?,'01',?,'001')    
    """
    sql_client_data="""select clicod,clides,cliend,clicpfcgc,clibai,clitel,clicep,clicid,
        clinum,clicmp,cliest,stacod,clifan,clirgcgf,clidtcad,clipfpj,clitel2,clifax,
        clicon,clinumcob,cliemail,clidtalt,clitipprc,ramcod,funcod,cliretemiss,cliinscmun,
        sysserie,sysctrl,sysver
        from cliente where clicod = ?"""
    sql_gen_id = """SELECT GEN_ID( GEN_IDATENDIMENTO,1 ) FROM RDB$DATABASE;"""
    client_ticket = {}
    cursor_client = db_.cursor()
    cursor_client.execute(sql_client_data, [client_id])
    rs_client = cursor_client.fetchone()
    if rs_client is not None:
        print(rs_client)
        client_ticket['clicod'] = rs_client[0]
        client_ticket['clides'] = rs_client[1]
        client_ticket['cliend'] = rs_client[2]
        client_ticket['clicpfcgc'] = rs_client[3]
        client_ticket['clibai'] = rs_client[4]
        client_ticket['clitel'] = rs_client[5]
        client_ticket['clicep'] = rs_client[6]
        client_ticket['clicid'] = rs_client[7]
        client_ticket['clinum'] = rs_client[8]
        client_ticket['clicmp'] = rs_client[9]
        client_ticket['cliest'] = rs_client[10]
        client_ticket['stacod'] = rs_client[11]
        client_ticket['clifan'] = rs_client[12]
        client_ticket['clirgcgf'] = rs_client[13]
        client_ticket['clidtcad'] = rs_client[14]
        client_ticket['clipfpj'] = rs_client[15]
        client_ticket['clitel2'] = null_validation(rs_client[16], '')
        client_ticket['clifax'] = rs_client[17]
        client_ticket['clicon'] = rs_client[18]
        client_ticket['clinumcob'] = rs_client[19]
        client_ticket['cliemail'] = rs_client[20]
        client_ticket['clidtalt'] = rs_client[21]
        client_ticket['clitipprc'] = rs_client[22]
        client_ticket['ramcod'] = rs_client[23]
        client_ticket['funcod'] = rs_client[24]
        client_ticket['cliretemiss'] = rs_client[25]
        client_ticket['cliinscmun'] = rs_client[26]
        client_ticket['sysserie'] = rs_client[27]
        client_ticket['sysctrl'] = rs_client[28]
        client_ticket['sysver'] = rs_client[29]
    print('cliente do chamado:')
    pprint.pprint(client_ticket)
    cursor_client.close()
    #Generation of codatt with gen_id function from firebird.
    cursor.execute(sql_gen_id)
    codatt = cursor.fetchone()[0]
    print('novo atendimento:', str(codatt))
    cursor.execute(sql_insert_ticket,[codatt, ticket.description, date_ticket, client_ticket['clicod'],
                                      client_ticket['sysserie'], client_ticket['clides'],
                                      client_ticket['clitel'], client_ticket['clitel2'],
                                      '', ticket.attendant_code.zfill(6), ticket.problem_reported,
                                      'ACESSO REMOTO', time_ticket, ticket.client_contact])
    db_.commit()

    return {'codatt': codatt, 'status': 200}

@app.post('/api/order')
def open_new_order(order: OrderInsert):
    client_id = str(order.clicod).zfill(15)
    order_id = str(order.pvdnum).zfill(10)
    funcod = str(order.funcod).zfill(6)
    pvdtipprc = str(order.pvdtipprc)
    pvdvlr = str(order.pvdvlr)
    opecod = str(order.opecod).zfill(4)
    cfocod = str(order.cfocod)
    pvdtipefet = str(order.pvdtipefet)
    pvdobs = str(order.pvdobs)
    if order.pvddatemi is None:        
        now = datetime.now()
        order_date = datetime.date(now)
        print('será utilizada a data atual:', order_date)
    else:
        order_date = order.pvddatemi
    
    if order.pvdhoremi is None:
        order_time = datetime.time(now)
        order_time = str(order_time.hour)+str(order_time.minute)
        print('hora:', order_time)
    else:
        order_time = order.pvdhoremi

    cursor_client_order = db_.cursor()
    #client_order = {}
    cursor_client_order.execute(sql_variables.list_client_by_code,[client_id])
    client_data = cursor_client_order.fetchone()
    print('cliente encontrado')
    print(client_data)
    pvdclides = client_data[1]
    pvdcliend = client_data[2]
    pvdclibai = client_data[4]
    pvdclicid = client_data[7]
    pvdcliest = client_data[10]
    pvdclinum = client_data[8]
    pvdclicep = client_data[6]
    pvdclicpfcgc = client_data[3]
    pvdclitel = client_data[5]

    cursor.execute(sql_variables.insert_order,[order_id, funcod, client_id, pvdtipprc,
    order_date, order_time, order.pvddatfec, order.pvdhorfec, order.pvdstatus,
    order.pvddocimp,pvdobs,pvdvlr,order.pvddcn,order.pvdacr,order.pvdblodcn,
    order.pvdbloest,order.pvdblolimcrd,pvdclides,pvdcliend,
    pvdclibai,pvdclicid,pvdcliest,pvdclinum,
    pvdclicep,pvdclicpfcgc,pvdclitel,pvdtipefet,
    opecod,cfocod,order.pvdtipfrt,order.pvddatprev,order.pvdhorprev,
    order.pvdtipatd,order.pvdloccod])
    db_.commit()
    print('=====PEDIDO GRAVADO, INICIANDO INCLUSÃO DE ITENS======')
    product_seq = 1
    for order_item in order.order_items:
        print('Product seq:', product_seq,'product code:', order_item.procod, 'valor: ', order_item.pvivlruni)
        #TODO implement search for tax data and item data
        procod = str(order_item.procod).zfill(14)
        cursor.execute(sql_variables.list_product_data_for_insert,[procod, procod])        
        product_db_data = cursor.fetchone()
        print('Produto encontrado:\n', product_db_data)
        pviprodes = product_db_data[1]
        pviprodesdz = product_db_data[2]
        pvitrbid = product_db_data[3]
        pvialqicms = product_db_data[4]
        pviiteemb = product_db_data[5]
        pviunid = product_db_data[6]
        pviprocodaux = product_db_data[7]
        pviprodesvar = product_db_data[8]
        pvidesvlr = 0.00
        pviqtd = order_item.pviqtd
        pvivlruni = order_item.pvivlruni
        pvivlrdcn = order_item.pvivlrdcn
        pvitipdcn = order_item.pvitipdcn
        pvivlracr = order_item.pvivlracr
        pvitipacr = order_item.pvitipacr        
        pviserpro = order_item.pviserpro        
        pviobs = order_item.pviobs
        pvifuncod = order_item.pvifuncod
        pvitip = order_item.pvitip
        pviprcprat = order_item.pviprcprat
        print('Descrição:', pviprodes, '|Descrição reduzida', pviprodesdz)
        cursor.execute(sql_variables.list_product_pis,[procod])
        product_pis = cursor.fetchone()
        if product_pis is not None:
            pvialqpis = product_pis[0]
            pvicstpis = product_pis[1]
        else:
            pvialqpis = None
            pvicstpis = None
        cursor.execute(sql_variables.list_product_cofins,[procod])
        product_cofins = cursor.fetchone()    
        if product_cofins is not None:      
            pvialqcof = product_cofins[0]
            pvicstcof = product_cofins[1]
        else:
            pvialqcof = None
            pvicstcof = None
        print('Impostos federais alq pis: {}, cst pis: {}, alq cofins: {}, cst cofins: {}'.format(pvialqpis,pvicstpis,
                                                                                                  pvialqcof,pvicstcof))
        cursor.execute(sql_variables.
                       insert_order_items,[product_seq, order_id, procod,
                                            pviqtd, pvivlruni,pvivlrdcn,pvitipdcn,
                                            pvivlracr,pvitipacr,pviserpro,pviobs,
                                            pvitrbid, pvialqicms, pviiteemb,
                                            pviunid, pviprodes, pviprodesdz,
                                            pviprocodaux, pvifuncod, pviprcprat,
                                            pvitip, pviprodesvar, pvidesvlr, pvialqpis,
                                            pvicstpis, pvialqcof, pvicstcof])
        db_.commit()
        product_seq += 1
    print('PEDIDO INCLUSO COM SUCESSO!')
    






