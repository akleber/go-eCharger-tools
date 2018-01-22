
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
    jsondata['sse'] = '******'

    # write data to file
    with open("status_" + datestring + ".json", 'w') as f:
        json.dump(jsondata, f, indent=4)

    # print infos
    print("version '{}' api version, the code below only supports version B".format(jsondata['version']))
    print("car '{}' 1=ready for charging, 2=charging, 3=waiting for car".format(jsondata['car']))
    print("amp '{}' ampere (current setting)".format(jsondata['amp']))
    print("err '{}' error state, 1:RCCB, 3:PHASE, 8:NO_GROUND, 10:INTERNAL".format(jsondata['err']))
    print("ast '{}' access state, 0:OPEN, 1:RFID_REQ".format(jsondata['ast']))
    print("alw '{}' allow charging, 0:false, 1:true".format(jsondata['alw']))
    print("stp '{}' 0: STOP_STATE_NONE, 2:STOP_STATE_KWH".format(jsondata['stp']))
    print("cbl '{}' cable capability in A, 0 for no cable".format(jsondata['cbl']))
    print("pha '{}' number of phases".format(jsondata['pha']))
    print("tmp '{}' mainboard temperature".format(jsondata['tmp']))
    print("dws '{}' deka-watt-seconds, 1000 equals, 10.000 Ws charged in this charge process".format(jsondata['dws']))
    print("dwo '{}' turn off value for dws (for charge XY kWh function), if(dwo!=0 && dws/36000>=dwo)alw=0".format(jsondata['dwo']))                                         
    print("adi '{}' adapter_in, 0:NO_ADAPTER, 1:16A_ADAPTER".format(jsondata['adi']))
    print("uby '{}' unlocked by RFID card no.".format(jsondata['uby']))
    print("eto '{}' Energy total .1 kWh (value of 120 means 12 kWh charged)".format(jsondata['eto']))
    print("wst '{}' wifi state, 3:connected, default:unconnected".format(jsondata['wst']))

    print("nrg '{}' voltage L1 in V".format(jsondata['nrg'][0]))
    print("nrg '{}' voltage L2 in V".format(jsondata['nrg'][1]))
    print("nrg '{}' voltage L3 in V".format(jsondata['nrg'][2]))
    print("nrg '{}' voltage on N, is !=0 when Schuko adapter is plugged in reversed".format(jsondata['nrg'][3]))
    print("nrg '{}' current L1 in .1 A".format(jsondata['nrg'][4]))
    print("nrg '{}' current L2 in .1 A".format(jsondata['nrg'][5]))
    print("nrg '{}' current L3 in .1 A".format(jsondata['nrg'][6]))
    print("nrg '{}' power L1 in .1 kW".format(jsondata['nrg'][7]))
    print("nrg '{}' power L2 in .1 kW".format(jsondata['nrg'][8]))
    print("nrg '{}' power L3 in .1 kW".format(jsondata['nrg'][9]))
    print("nrg '{}' power on N".format(jsondata['nrg'][10]))

    #            if(Math.floor(pha/8) ==1 && parseInt(nrg[3])>parseInt(nrg[0])){
    #              nrg[0]=nrg[3]
    #              nrg[7]=nrg[10]
    #              nrg[11]=nrg[14]
    #            }

    print("nrg '{}' power total in 100 kW".format(jsondata['nrg'][10]))
    print("nrg '{}' powerfactor L1 in %".format(jsondata['nrg'][11]))
    print("nrg '{}' powerfactor L2 in %".format(jsondata['nrg'][12]))
    print("nrg '{}' powerfactor L1 in %".format(jsondata['nrg'][13]))
    print("nrg '{}' powerfactor N".format(jsondata['nrg'][14]))

    print("fwv '{}' firmware version (this code only supports below 020)".format(jsondata['fwv']))
    print("sse '{}' serial number (formatted as %06d string)".format(jsondata['sse']))
    print("wss '{}' wlan extern SSID".format(jsondata['wss']))
    print("wke '{}' wlan extern kennwort/password in cleartext".format(jsondata['wke']))
    print("wen '{}' wlan extern enabled".format(jsondata['wen']))

    print("tof '{}' time_offset for internal battery powered RTC".format(jsondata['tof']))
    print("tds '{}' use daylight saving time for internal RTC".format(jsondata['tds']))
    print("lbr '{}' led brightness, 0-255".format(jsondata['lbr']))
    print("aho '{}' awattar hours to charge".format(jsondata['aho']))
    print("afi '{}' awattar hour:00 to be finished".format(jsondata['afi']))
    print("ama '{}' absolute max ampere".format(jsondata['ama']))
    print("al1 '{}' button ampere level 1'".format(jsondata['al1']))
    print("al2 '{}' button ampere level 2'".format(jsondata['al2']))
    print("al3 '{}' button ampere level 3'".format(jsondata['al3']))
    print("al4 '{}' button ampere level 4'".format(jsondata['al4']))
    print("al5 '{}' button ampere level 5'".format(jsondata['al5']))
    print("cid '{}' color idle, parseInt(HEX_CODE), 24bit".format(jsondata['cid']))
    print("cch '{}' color charging, parseInt(HEX_CODE), 24bit".format(jsondata['cch']))
    print("cfi '{}' color finished, parseInt(HEX_CODE), 24bit".format(jsondata['cfi']))
    print("ust '{}' unlock method, 0:standard, 1:auto_unlock, 2:always_locked".format(jsondata['ust']))
    print("wak '{}' wlan hotspot kennwort/password'".format(jsondata['wak']))
    print("nmo '{}' norway mode, 0:false, 1:true".format(jsondata['nmo']))

    print("eca '{}' energy charged with card 1, in .1kWh".format(jsondata['eca']))
    print("ecr '{}' energy charged with card 2, in .1kWh".format(jsondata['ecr']))
    print("ecd '{}' energy charged with card 3, in .1kWh".format(jsondata['ecd']))
    print("ec4 '{}' energy charged with card 4, in .1kWh".format(jsondata['ec4']))
    print("ec5 '{}' energy charged with card 5, in .1kWh".format(jsondata['ec5']))
    print("ec6 '{}' energy charged with card 6, in .1kWh".format(jsondata['ec6']))
    print("ec7 '{}' energy charged with card 7, in .1kWh".format(jsondata['ec7']))
    print("ec8 '{}' energy charged with card 8, in .1kWh".format(jsondata['ec8']))
    print("ec9 '{}' energy charged with card 9, in .1kWh".format(jsondata['ec9']))
    print("ec1 '{}' energy charged with card 10, in .1kWh".format(jsondata['ec1']))

    # parameter names generated automatically, takes first character || first character after '_', 
    #    and next character that yields an unused paramter name
    # rfid_card_1 --> rca
    # rfid_card_2 --> rcr (because rca was already used and c was the next character that yields an unused paramter name
    # rfid_card_3 --> crd
    # rfid_card_4 --> rc4 ...
    
    print("rca '{}' rfid card1 UID (only available for fwv<020)".format(jsondata['rca']))
    print("rcr '{}'".format(jsondata['rcr']))
    print("rcd '{}'".format(jsondata['rcd']))
    print("rc4 '{}'".format(jsondata['rc4']))
    print("rc5 '{}'".format(jsondata['rc5']))
    print("rc6 '{}'".format(jsondata['rc6']))
    print("rc7 '{}'".format(jsondata['rc7']))
    print("rc8 '{}'".format(jsondata['rc8']))
    print("rc9 '{}'".format(jsondata['rc9']))
    print("rc1 '{}'".format(jsondata['rc1']))

    print("rna '{}' rfid name1 (only available for fwv<020)".format(jsondata['rna']))
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

