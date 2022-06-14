
orders_field = ['pvdnum','funcod','clicod','trnseq','pvdtipprc',
'pvddatemi','pvdhoremi','pvddatfec','pvdhorfec','pvdstatus',
'pvddocimp','pvdobs','pvdvlr','pvddcn','pvdacr','pvdblodcn',
'pvdbloest','pvdblolimcrd','pvdclides','pvdcliend',
'pvdclibai','pvdclicid','pvdcliest','pvdclinum',
'pvdclicep','pvdclicpfcgc','pvdclitel','pvdtipefet',
'opecod','cfocod','pvdtipfrt','pvddatprev','pvdhorprev',
'pvdtipatd','pvdloccod']

list_all_orders = """select pvdnum,funcod,clicod,trnseq,pvdtipprc,
pvddatemi,pvdhoremi,pvddatfec,pvdhorfec,pvdstatus,
pvddocimp,pvdobs,pvdvlr,pvddcn,pvdacr,pvdblodcn,
pvdbloest,pvdblolimcrd,pvdclides,pvdcliend,
pvdclibai,pvdclicid,pvdcliest,pvdclinum,
pvdclicep,pvdclicpfcgc,pvdclitel,pvdtipefet,
opecod,cfocod,pvdtipfrt,pvddatprev,pvdhorprev,
pvdtipatd,pvdloccod from pedido_venda"""

list_orders_by_status = """select pvdnum,funcod,clicod,trnseq,pvdtipprc,
pvddatemi,pvdhoremi,pvddatfec,pvdhorfec,pvdstatus,
pvddocimp,pvdobs,pvdvlr,pvddcn,pvdacr,pvdblodcn,
pvdbloest,pvdblolimcrd,pvdclides,pvdcliend,
pvdclibai,pvdclicid,pvdcliest,pvdclinum,
pvdclicep,pvdclicpfcgc,pvdclitel,pvdtipefet,
opecod,cfocod,pvdtipfrt,pvddatprev,pvdhorprev,
pvdtipatd,pvdloccod from pedido_venda where pvdstatus = ?"""

list_orders_by_code = """select pvdnum,funcod,clicod,trnseq,pvdtipprc,
pvddatemi,pvdhoremi,pvddatfec,pvdhorfec,pvdstatus,
pvddocimp,pvdobs,pvdvlr,pvddcn,pvdacr,pvdblodcn,
pvdbloest,pvdblolimcrd,pvdclides,pvdcliend,
pvdclibai,pvdclicid,pvdcliest,pvdclinum,
pvdclicep,pvdclicpfcgc,pvdclitel,pvdtipefet,
opecod,cfocod,pvdtipfrt,pvddatprev,pvdhorprev,
pvdtipatd,pvdloccod from pedido_venda where pvdnum = ?"""

update_order = """update pedido_venda set funcod=?,clicod=?,trnseq=?,pvdtipprc=?,
pvddatemi=?,pvdhoremi=?,pvddatfec=?,pvdhorfec=?,pvdstatus=?,
pvddocimp=?,pvdobs=?,pvdvlr=?,pvddcn=?,pvdacr=?,pvdblodcn=?,
pvdbloest=?,pvdblolimcrd=?,pvdclides=?,pvdcliend=?,
pvdclibai=?,pvdclicid=?,pvdcliest=?,pvdclinum=?,
pvdclicep=?,pvdclicpfcgc=?,pvdclitel=?,pvdtipefet=?,
opecod=?,cfocod=?,pvdtipfrt=?,pvddatprev=?,pvdhorprev=?,
pvdtipatd=?,pvdloccod where pvdnum = ?"""

insert_order = """insert into pedido_venda(pvdnum,funcod,clicod,pvdtipprc,
pvddatemi,pvdhoremi,pvddatfec,pvdhorfec,pvdstatus,
pvddocimp,pvdobs,pvdvlr,pvddcn,pvdacr,pvdblodcn,
pvdbloest,pvdblolimcrd,pvdclides,pvdcliend,
pvdclibai,pvdclicid,pvdcliest,pvdclinum,
pvdclicep,pvdclicpfcgc,pvdclitel,pvdtipefet,
opecod,cfocod,pvdtipfrt,pvddatprev,pvdhorprev,
pvdtipatd,pvdloccod)
values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

list_items_from_order = """select pviseq,pvdnum,procod,pviqtd,pvivlruni,pvivlrdcn,pvitipdcn,
pvivlracr,pvitipacr,pviserpro,pviobs,pvitrbid,pvialqicms,pviiteemb,
pviunid,pviprodes,pviprodesdz,pviprocodaux,pvifuncod,
pviprcprat,pvitip,pviprodesvar,pvidesvlr,pvialqpis,pvicstpis,
pvialqcof,pvicstcof
from pedido_venda_item
where pvdnum = ?
"""

insert_order_items = """insert into pedido_venda_item(pviseq,pvdnum,procod,pviqtd,pvivlruni,pvivlrdcn,pvitipdcn,
pvivlracr,pvitipacr,pviserpro,pviobs,pvitrbid,pvialqicms,pviiteemb,
pviunid,pviprodes,pviprodesdz,pviprocodaux,pvifuncod,
pviprcprat,pvitip,pviprodesvar,pvidesvlr,pvialqpis,pvicstpis,
pvialqcof,pvicstcof)
values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

update_order_items = """update pedido_venda_item set pviqtd=?,pvivlruni=?,
pvivlrdcn=?,pvitipdcn=?,pvivlracr=?,pvitipacr=?,pviserpro=?,pviobs=?,
pvitrbid=?,pvialqicms=?,pviiteemb=?,
pviunid=?,pviprodes=?,pviprodesdz=?,pviprocodaux=?,pvifuncod=?,
pviprcprat=?,pvitip=?,pviprodesvar=?,pvidesvlr=?,pvialqpis=?,pvicstpis=?,
pvialqcof=?,pvicstcof
where pviseq=?,pvdnum=?,procod=?"""

list_all_clients = """select clicod,clides,cliend,clicpfcgc,clibai,clitel,clicep,
clicid,clinum,clicmp,cliest,clilimcre,clilimutl, clilimcre2,
clilimutl2,stacod,clitabprz,cliprz,clifan,clirgcgf,clipfpj,
clitel2,clifax,clicon,clidcn,cliobs,cliemail,clisex,
clipais,clicodigoibge,cliindcinscest,clisincld
from cliente"""

list_client_by_code = """select clicod,clides,cliend,clicpfcgc,clibai,clitel,clicep,
clicid,clinum,clicmp,cliest,clilimcre,clilimutl, clilimcre2,
clilimutl2,stacod,clitabprz,cliprz,clifan,clirgcgf,clipfpj,
clitel2,clifax,clicon,clidcn,cliobs,cliemail,clisex,
clipais,clicodigoibge,cliindcinscest,clisincld
from cliente where clicod = ? """

list_product_data_for_insert="""select p.procod,prodes,prodesrdz,p.trbid,t.trbalq pvialqicms,proiteemb,prounid,
procodaux, prodesvar from produto p
left join tributacao t on p.trbid=t.trbid
left join produtoaux px on p.procod=px.procod
where p.procod = ? or px.procod= ?"""

list_product_pis = """select impfedalqsai,impfedstsai from impostos_federais_produto ifp
left join impostos_federais imp on ifp.impfedsim=imp.impfedsim
where impfedtip='P' and procod = ?"""
list_product_cofins = """select impfedalqsai,impfedstsai from impostos_federais_produto ifp
left join impostos_federais imp on ifp.impfedsim=imp.impfedsim
where impfedtip='C' and procod = ?"""

#list_product_data=""""""