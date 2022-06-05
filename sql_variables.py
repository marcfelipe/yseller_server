
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


list_all_clients = """select clicod,clides,cliend,clicpfcgc,clibai,clitel,clitel,
clicid,clinum,clicmp,cliest,clilimcre,clilimutl, clilimcre2,
clilimutl2,stacod,clitabprz,cliprz,clifan,clirgcgf,clipfpj,
clitel2,clifax,clicon,clidcn,cliobs,cliemail,clisex,
clipais,clicodigoibge,cliindcinscest,clisincld
from cliente"""

list_client_by_code = """select clicod,clides,cliend,clicpfcgc,clibai,clitel,clitel,
clicid,clinum,clicmp,cliest,clilimcre,clilimutl, clilimcre2,
clilimutl2,stacod,clitabprz,cliprz,clifan,clirgcgf,clipfpj,
clitel2,clifax,clicon,clidcn,cliobs,cliemail,clisex,
clipais,clicodigoibge,cliindcinscest,clisincld
from cliente where clicod = ? """