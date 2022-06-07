from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date, time

class OrderItemsInsert(BaseModel):
    procod: str
    pvdnum: str
    pviqtd: float
    pvivlruni: float
    pvivlrdcn: float
    pvitipdcn: str
    pvivlracr: float
    pvitipacr: str
    pviprcprat: str
    pvitip = '1'
    pviserpro: Optional[str]

class OrderInsert(BaseModel):
    pvdnum: int
    funcod: str
    clicod: str
    pvdtipprc: str
    pvdstatus =  'A'
    pvddocimp = 'N'    
    pvdvlr: float
    pvddcn = 0.00
    pvdacr = 0.00
    pvdblodcn = 'N'
    pvdbloest = 'N'
    pvdblolimcrd = 'N'
    opecod: str
    cfocod: str
    pvdtipfrt = 'CIF'
    pvdtipatd = 'B'
    pvdloccod = '01'
    order_items: List[OrderItemsInsert]    
    pvdtipefet: str
    pvdobs: Optional[str]
    pvddatemi: Optional[str]
    pvdhoremi: Optional[str]
    pvddatprev: Optional[str]
    pvdhorprev: Optional[str]
    pvddatfec: Optional[str]
    pvdhorfec: Optional[str]


class OrderUpdate(BaseModel):
    pvdnum: int
    funcod: str
    clicod: str
    pvdtipprc: str
    pvddatemi: str
    pvdhoremi: str
    pvdstatus: str
    pvddocimp: str
    pvdobs: str
    pvdvlr: float
    pvddcn: str
    pvdacr: str
    pvdblodcn: str
    pvdbloest: str
    pvdblolimcrd: str
    opecod: str
    cfocod: str
    pvdtipfrt: str
    pvdtipatd: str
    pvdloccod: str    
    pvdclides: Optional[str]
    pvdcliend: Optional[str]
    pvdclibai: Optional[str]
    pvdclicid: Optional[str]
    pvdcliest: Optional[str]
    pvdclinum: Optional[str]
    pvdclicep: Optional[str]
    pvdclicpfcgc: Optional[str]
    pvdclitel: Optional[str]
    pvdtipefet: Optional[str]
    pvddatprev: Optional[str]
    pvdhorprev: Optional[str]
    pvddatfec: Optional[str]
    pvdhorfec: Optional[str]


