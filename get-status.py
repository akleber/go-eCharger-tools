
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
    print("version '{}'".format(jsondata['version']))
    print("car '{}' 1=Ready for Charging, 2=Charging, 3=Waiting for Car".format(jsondata['car']))
    print("amp '{}' Ampere (current setting)".format(jsondata['amp']))
    print("err '{}'".format(jsondata['err']))
    print("ast '{}' Automatic Stop ?".format(jsondata['ast']))
    print("alw '{}'".format(jsondata['alw']))
    print("stp '{}'".format(jsondata['stp']))
    print("cbl '{}' Cable capability in A, 0 for no Cable".format(jsondata['cbl']))
    print("pha '{}'".format(jsondata['pha']))
    print("tmp '{}'".format(jsondata['tmp']))
    print("dws '{}'".format(jsondata['dws']))
    print("dwo '{}'".format(jsondata['dwo']))
    print("adi '{}'".format(jsondata['adi']))
    print("uby '{}'".format(jsondata['uby']))
    print("eto '{}' Energy total 10 kWh".format(jsondata['eto']))
    print("wst '{}'".format(jsondata['wst']))

    print("nrg '{}' Voltage L1 in V".format(jsondata['nrg'][0]))
    print("nrg '{}' Voltage L2 in V".format(jsondata['nrg'][1]))
    print("nrg '{}' Voltage L3 in V".format(jsondata['nrg'][2]))
    print("nrg '{}' ?".format(jsondata['nrg'][3]))
    print("nrg '{}' Current L1 in 10 A".format(jsondata['nrg'][4]))
    print("nrg '{}' Current L2 in 10 A".format(jsondata['nrg'][5]))
    print("nrg '{}' Current L3 in 10 A".format(jsondata['nrg'][6]))
    print("nrg '{}' Power L1 in 10 kW".format(jsondata['nrg'][7]))
    print("nrg '{}' Power L2 in 10 kW".format(jsondata['nrg'][8]))
    print("nrg '{}' Power L3 in 10 kW".format(jsondata['nrg'][9]))
    print("nrg '{}' ?".format(jsondata['nrg'][10]))
    print("nrg '{}' Power Total in 100 kW".format(jsondata['nrg'][10]))
    print("nrg '{}' Powerfactor L1 in %".format(jsondata['nrg'][11]))
    print("nrg '{}' Powerfactor L2 in %".format(jsondata['nrg'][12]))
    print("nrg '{}' Powerfactor L1 in %".format(jsondata['nrg'][13]))
    print("nrg '{}' ?".format(jsondata['nrg'][14]))

    print("fwv '{}' Firmware version ?".format(jsondata['fwv']))
    print("sse '{}' Serial number".format(jsondata['sse']))
    print("wss '{}' WLan extern SSID".format(jsondata['wss']))
    print("wke '{}' WLan extern Kennwort/Password in cleartext".format(jsondata['wke']))
    print("wen '{}' WLan extern enabled?".format(jsondata['wen']))

    print("tof '{}'".format(jsondata['tof']))
    print("tds '{}'".format(jsondata['tds']))
    print("lbr '{}'".format(jsondata['lbr']))
    print("aho '{}'".format(jsondata['aho']))
    print("afi '{}'".format(jsondata['afi']))
    print("ama '{}'".format(jsondata['ama']))
    print("al1 '{} Button Ampere Level 1'".format(jsondata['al1']))
    print("al2 '{} Button Ampere Level 2'".format(jsondata['al2']))
    print("al3 '{} Button Ampere Level 3'".format(jsondata['al3']))
    print("al4 '{} Button Ampere Level 4'".format(jsondata['al4']))
    print("al5 '{} Button Ampere Level 5'".format(jsondata['al5']))
    print("cid '{}'".format(jsondata['cid']))
    print("cch '{}'".format(jsondata['cch']))
    print("cfi '{}'".format(jsondata['cfi']))
    print("ust '{}'".format(jsondata['ust']))
    print("wak '{}' WLan Hotspot Kennwort/Password'".format(jsondata['wak']))
    print("nmo '{}'".format(jsondata['nmo']))

    print("eca '{}'".format(jsondata['eca']))
    print("ecr '{}'".format(jsondata['ecr']))
    print("ecd '{}'".format(jsondata['ecd']))
    print("ec4 '{}'".format(jsondata['ec4']))
    print("ec5 '{}'".format(jsondata['ec5']))
    print("ec6 '{}'".format(jsondata['ec6']))
    print("ec7 '{}'".format(jsondata['ec7']))
    print("ec8 '{}'".format(jsondata['ec8']))
    print("ec9 '{}'".format(jsondata['ec9']))
    print("ec1 '{}'".format(jsondata['ec1']))

    print("rca '{} Reset Card RFID ID?'".format(jsondata['rca']))
    print("rcr '{}'".format(jsondata['rcr']))
    print("rcd '{}'".format(jsondata['rcd']))
    print("rc4 '{}'".format(jsondata['rc4']))
    print("rc5 '{}'".format(jsondata['rc5']))
    print("rc6 '{}'".format(jsondata['rc6']))
    print("rc7 '{}'".format(jsondata['rc7']))
    print("rc8 '{}'".format(jsondata['rc8']))
    print("rc9 '{}'".format(jsondata['rc9']))
    print("rc1 '{}'".format(jsondata['rc1']))

    print("rna '{}'".format(jsondata['rna']))
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

