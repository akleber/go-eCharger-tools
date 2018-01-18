
"""
Example:
python3 get-status.py
"""

import requests
import sys
import os
import json
import time
from datetime import timedelta, date, datetime

hostname = "go-echarger"

def main(argv):

    datestring = datetime.now().strftime("%Y_%m_%d-%H-%M-%S")

    url = "http://" + hostname + "/status"

    r = requests.get(url, timeout=5)
    r.raise_for_status()
    jsondata = r.json()

    # remove some private data
    jsondata['wke'] = '***'
    jsondata['wak'] = '***'
    jsondata['rca'] = '***'
    jsondata['sse'] = '000000'

    # write data to file
    with open("status_" + datestring + ".json", 'w') as f:
        json.dump(jsondata, f, indent=4)

    # print infos
    print("version '{}'".format(jsondata['version'])) #api version, the code below only supports version B
    print("car '{}' 1=Ready for Charging, 2=Charging, 3=Waiting for Car".format(jsondata['car']))
    print("amp '{}' Ampere (current setting)".format(jsondata['amp']))
    print("err '{}'".format(jsondata['err'])) # error state, 1:RCCB, 3:PHASE, 8:NO_GROUND, 10:INTERNAL
    print("ast '{}' Automatic Stop ?".format(jsondata['ast']))# access state, 0:OPEN, 1:RFID_REQ
    print("alw '{}'".format(jsondata['alw'])) # allow charging, 0:false, 1:true
    print("stp '{}'".format(jsondata['stp'])) # 0: STOP_STATE_NONE, 2:STOP_STATE_KWH
    print("cbl '{}' Cable capability in A, 0 for no Cable".format(jsondata['cbl']))
    print("pha '{}'".format(jsondata['pha'])) # number of phases
    print("tmp '{}'".format(jsondata['tmp'])) # mainboard temperature
    print("dws '{}'".format(jsondata['dws'])) # deka-watt-seconds, 1000 equals, 10.000 Ws charged in this charge process
    print("dwo '{}'".format(jsondata['dwo'])) # turn off value for dws (for charge XY kWh function)
    #                                           if(dwo!=0 && dws/36000>=dwo)alw=0
    print("adi '{}'".format(jsondata['adi'])) # adapter_in, 0:NO_ADAPTER, 1:16A_ADAPTER
    print("uby '{}'".format(jsondata['uby'])) # unlocked by RFID card no.
    print("eto '{}' Energy total .1 kWh".format(jsondata['eto'])) # value of 120 means 12 kWh charged
    print("wst '{}'".format(jsondata['wst'])) # wifi state, 3:connected, default:unconnected

    print("nrg '{}' Voltage L1 in V".format(jsondata['nrg'][0]))
    print("nrg '{}' Voltage L2 in V".format(jsondata['nrg'][1]))
    print("nrg '{}' Voltage L3 in V".format(jsondata['nrg'][2]))
    print("nrg '{}' ?".format(jsondata['nrg'][3]))# voltage on N, is !=0 when Schuko adapter is plugged in reversed
    print("nrg '{}' Current L1 in .1 A".format(jsondata['nrg'][4]))
    print("nrg '{}' Current L2 in .1 A".format(jsondata['nrg'][5]))
    print("nrg '{}' Current L3 in .1 A".format(jsondata['nrg'][6]))
    print("nrg '{}' Power L1 in .1 kW".format(jsondata['nrg'][7]))
    print("nrg '{}' Power L2 in .1 kW".format(jsondata['nrg'][8]))
    print("nrg '{}' Power L3 in .1 kW".format(jsondata['nrg'][9]))
    print("nrg '{}' ?".format(jsondata['nrg'][10]))# Power on N
    #            if(Math.floor(pha/8) ==1 && parseInt(nrg[3])>parseInt(nrg[0])){
    #              nrg[0]=nrg[3]
    #              nrg[7]=nrg[10]
    #              nrg[11]=nrg[14]
    #            }
    print("nrg '{}' Power Total in 100 kW".format(jsondata['nrg'][10]))
    print("nrg '{}' Powerfactor L1 in %".format(jsondata['nrg'][11]))
    print("nrg '{}' Powerfactor L2 in %".format(jsondata['nrg'][12]))
    print("nrg '{}' Powerfactor L1 in %".format(jsondata['nrg'][13]))
    print("nrg '{}' ?".format(jsondata['nrg'][14]))# Powerfactor on N

    print("fwv '{}' Firmware version ?".format(jsondata['fwv']))# this code only supports below 020
    print("sse '{}' Serial number".format(jsondata['sse'])) # formatted as %06d string
    print("wss '{}' WLan extern SSID".format(jsondata['wss']))
    print("wke '{}' WLan extern Kennwort/Password in cleartext".format(jsondata['wke']))
    print("wen '{}' WLan extern enabled?".format(jsondata['wen']))

    print("tof '{}'".format(jsondata['tof'])) # time_offset for internal battery powered RTC
    print("tds '{}'".format(jsondata['tds'])) # use daylight saving time for internal RTC
    print("lbr '{}'".format(jsondata['lbr'])) # led brightness, 0-255
    print("aho '{}'".format(jsondata['aho'])) # awattar hours to charge
    print("afi '{}'".format(jsondata['afi'])) # awattar hour:00 to be finished
    print("ama '{}'".format(jsondata['ama'])) # absolute max ampere
    print("al1 '{} Button Ampere Level 1'".format(jsondata['al1']))
    print("al2 '{} Button Ampere Level 2'".format(jsondata['al2']))
    print("al3 '{} Button Ampere Level 3'".format(jsondata['al3']))
    print("al4 '{} Button Ampere Level 4'".format(jsondata['al4']))
    print("al5 '{} Button Ampere Level 5'".format(jsondata['al5']))
    print("cid '{}'".format(jsondata['cid'])) # color idle, parseInt(HEX_CODE), 24bit
    print("cch '{}'".format(jsondata['cch'])) # color charging, parseInt(HEX_CODE), 24bit
    print("cfi '{}'".format(jsondata['cfi'])) # color finished, parseInt(HEX_CODE), 24bit
    print("ust '{}'".format(jsondata['ust'])) # unlock method, 0:standard, 1:auto_unlock, 2:always_locked
    print("wak '{}' WLan Hotspot Kennwort/Password'".format(jsondata['wak']))
    print("nmo '{}'".format(jsondata['nmo'])) # norway mode, 0:false, 1:true

    print("eca '{}'".format(jsondata['eca']))# energy charged with card 1, in .1kWh (name shema below)
    print("ecr '{}'".format(jsondata['ecr']))
    print("ecd '{}'".format(jsondata['ecd']))
    print("ec4 '{}'".format(jsondata['ec4']))
    print("ec5 '{}'".format(jsondata['ec5']))
    print("ec6 '{}'".format(jsondata['ec6']))
    print("ec7 '{}'".format(jsondata['ec7']))
    print("ec8 '{}'".format(jsondata['ec8']))
    print("ec9 '{}'".format(jsondata['ec9']))
    print("ec1 '{}'".format(jsondata['ec1']))

    # parameter names generated automatically, takes first character || first character after '_', 
    #    and next character that yields an unused paramter name
    # rfid_card_1 --> rca
    # rfid_card_2 --> rcr (because rca was already used and c was the next character that yields an unused paramter name
    # rfid_card_3 --> crd
    # rfid_card_4 --> rc4 ...
    
    print("rca '{}'".format(jsondata['rca']))# rfid card1 UID (only available for fwv<020)
    print("rcr '{}'".format(jsondata['rcr']))
    print("rcd '{}'".format(jsondata['rcd']))
    print("rc4 '{}'".format(jsondata['rc4']))
    print("rc5 '{}'".format(jsondata['rc5']))
    print("rc6 '{}'".format(jsondata['rc6']))
    print("rc7 '{}'".format(jsondata['rc7']))
    print("rc8 '{}'".format(jsondata['rc8']))
    print("rc9 '{}'".format(jsondata['rc9']))
    print("rc1 '{}'".format(jsondata['rc1']))

    print("rna '{}'".format(jsondata['rna']))#rfid name1 (only available for fwv<020)
    print("rnm '{}'".format(jsondata['rnm']))
    print("rne '{}'".format(jsondata['rne']))
    print("rn4 '{}'".format(jsondata['rn4']))
    print("rn5 '{}'".format(jsondata['rn5']))
    print("rn6 '{}'".format(jsondata['rn6']))
    print("rn7 '{}'".format(jsondata['rn7']))
    print("rn8 '{}'".format(jsondata['rn8']))
    print("rn9 '{}'".format(jsondata['rn9']))
    print("rn1 '{}'".format(jsondata['rn1']))






if __name__ == "__main__":
    main(sys.argv)

