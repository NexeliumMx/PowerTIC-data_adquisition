import datetime as DT
import time
import math
import json
import random
from pathlib import Path
import os
#PostgreSQL Init
from upload import uploadcloud
serialnumb=''
def meter_param():
    # Constantes
    SETTINGS_DIR = Path(__file__).parent
    tempquery = SETTINGS_DIR / 'tempquery.txt'
    r=open('datademo.txt')
    rows = r.readlines()
    now = DT.datetime.now()
    then = now - DT.timedelta(days=365)
   
    vavc=0
    tva=0
    vbvc=0
    vcvc=0
    tar=0
    taf=0
    taar=0
    tabr=0
    tacr=0
    taaf=0
    tabf=0
    tacf=0
    for d in range(0,365):
        for min in range(0,288):
            ampavrg=0
            vavrg=0
            vpvrg=0
            pavrg=0
            tir=0
            tif=0
            forquery='('
            forqueryVal='('
            start=True# Adquisición de configuración
            i=0;
            for row in rows:                                   
                        parameter = row
                        set_val = ""  # Inicializar set_val para cada parámetro
                        # Data acquisition for single address
                        match i:
                            case 0|1|2:
                                set_val=random.randint(5,10)
                                ampavrg+=set_val
                            case 3:
                                set_val=random.randint(12500,13500)
                                vavrg+=set_val
                                va=set_val
                            case 4:
                                set_val=random.randint(12500,13500)
                                vavrg+=set_val
                                vb=set_val
                            case 5:
                                set_val=random.randint(12500,13500)
                                vavrg+=set_val
                                vc=set_val
                            case 6:
                                set_val=int(va*math.sqrt(3))
                            case 7:
                                set_val=int(vb*math.sqrt(3))
                            case 8:
                                set_val=int(vc*math.sqrt(3))
                            case 9:
                                set_val=random.randint(55,65)
                            case 10:
                                set_val=random.randint(10000,30000)
                                vpvrg+=set_val
                                vav=set_val
                                vavc+=set_val
                                tva+=set_val
                            case 11:
                                set_val=random.randint(10000,30000)
                                vpvrg+=set_val
                                vab=set_val
                                vbvc+=set_val
                                tva+=set_val
                            case 12:
                                set_val=random.randint(10000,30000)
                                vpvrg+=set_val
                                vac=set_val
                                vcvc+=set_val
                                tva+=set_val
                            case 13:
                                set_val=random.uniform(-1,1)
                                pavrg+=set_val
                                vap=set_val
                            case 14:
                                set_val=random.uniform(-1,1)
                                pavrg+=set_val
                                vbp=set_val
                            case 15:
                                set_val=random.uniform(-1,1)
                                pavrg+=set_val
                                vcp=set_val
                            case 16:
                                set_val=int(ampavrg)
                            case 17:
                                set_val=int(vavrg/3)
                            case 18:
                                set_val=int(vavrg*(math.sqrt(3)/3))
                            case 19:
                                set_val=(pavrg/3)
                            case 20:
                                set_val=int(vav*math.cos(vap))
                                tir+=set_val
                                tar+=set_val
                                taar+=set_val
                            case 21:
                                set_val=int(vab*math.cos(vbp))
                                tir+=set_val
                                tar+=set_val
                                tabr+=set_val
                            case 22:
                                set_val=int(vac*math.cos(vcp))
                                tir+=set_val
                                tar+=set_val
                                tacr+=set_val
                            case 23:
                                set_val=abs(int(vav*math.sin(vap)))
                                tif+=set_val
                                taf+=set_val
                                taaf+=set_val
                            case 24:
                                set_val=abs(int(vab*math.sin(vbp)))
                                tif+=set_val
                                taf+=set_val
                                tabf+=set_val
                                
                            case 25:
                                set_val=abs(int(vac*math.sin(vcp)))
                                tif+=set_val
                                taf+=set_val
                                tacf+=set_val
                            case 26:
                                set_val=tir
                            case 27:
                                set_val=taar
                            case 28:
                                set_val=tabr
                            case 29:
                                set_val=int(tacr)
                            case 30:
                                set_val=tva
                            case 31:
                                set_val=taf
                            case 32:
                                set_val=taaf
                            case 33:
                                set_val=tabf
                            case 34: 
                                set_val=tacf
                            case 36:
                                set_val=tif
                            case 36:
                                set_val=tar
                            case _:
                                set_val=random.randint(0,10000)
                        i+=1  
                        if start!=True:
                            forquery+=","
                            forqueryVal+=","
                        start=False
                        forquery+=parameter.strip('\n')
                        forqueryVal+='\''+str(set_val)+'\''                 # Almacenamiento local de configuración
            if not os.path.exists(r'temp.txt'):
                f=open(r"temp.txt","x")
            else:
                f=os.remove(r"temp.txt")
                f=open(r"temp.txt","x")
            forquery+=', Timestamp,serial_number)'
            timestamp=(then+DT.timedelta(seconds=(300*min))).isoformat()
            forqueryVal+=',\''+timestamp+'\',\''+'demosn65563'+'\')'
            f.write('insert into demopowertic.measurements '+forquery+'values'+forqueryVal)
            uploadcloud(('insert into demopowertic.measurements '+forquery+'values'+forqueryVal))

meter_param()

