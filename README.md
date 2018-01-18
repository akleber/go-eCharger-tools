# go-eCharger-tools
Python tools to work with the json data of the go-eCharger API.

Currently it saves the content from the /status url in a formatted .json file
and prints the values with explanations.

# Requirements
* Python 3.6

# Usage
Create, activate and setup venv:

```
cd go-eCharger-tools
python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

Then set the right hostname or ip address in get_status.py if different from "go-echarger" and call

```
python3 get_status.py
```

# Known parameters

| Parameter | Description | Example |
| ------------- |:-------------:| -----:|
| version | go-eCharger version | B | |
| car | status of car | 1=ready for charging, 2=charging, 3=waiting for car | |
| amp | charging limit in ampere  | 20 | |
| err | | | |
| ast | access control | 0 | |
| alw | activation needed | 0 | |
| stp | | | |
| cbl | | | |
| pha | | | |
| tmp | temperature | 20 | |
| dws | | | |
| dwo | automatic stop [kWh] | 10.5 | |
| adi | | | |
| uby | | | |
| eto | energy total [kWh] | 10 | |
| wst | | | |
| nrg | 1-3 L1-3 voltage, 5-7 L1-3 current, 8-10 power, 12 total power, 12-14 power factor  | [234,234,234,0,0,0,0,0,0,0,0,0,0,0,0,0] | |
| fwv | firmware version | 012 | |
| sse | serialnumber | 000144 | |
| wss | wireless ssid | wifi | |
| wke | wireless key | secretpw | |
| wen | wireless enabled | 1 | |
| tof | | | |
| tds | | | |
| lbr | led brightness | 255 | |
| aho | | | | 
| afi | | | |
| ama | | | |
| al1 | button ampere level 1 | 6 | |
| al2 | button ampere level 2 | 10 | |
| al3 | button ampere level 3 | 20 | |
| al4 | button ampere level 4 | 32 | |
| al5 | button ampere level 5 | 32 | |
| cid | | | |
| cch | | | |
| cfi | | | |
| ust | unlock mode | 0 | |
| wak | adhoc wireless password | secretpw | |
| nmo | ground check | 0 | |
| eca | | | |
| ecr | | | |
| ecd | | | |
| ec4 | | | |
| ec5 | | | |
| ec6 | | | |
| ec7 | | | |
| ec8 | | | |
| ec9 | | | |
| ec1 | | | |
| rca | reset card rfid id | ae4ffb90 | |
| rcr | | | |
| rcd | | | |
| rc4 | | | |
| rc5 | | | |
| rc6 | | | |
| rc7 | | | |
| rc8 | | | |
| rc9 | | | |
| rc1 | | | |
| rna | | | |
| rnm | | | |
| rne | | | |
| rn4 | | | |
| rn5 | | | |
| rn6 | | | |
| rn7 | | | |
| rn8 | | | |
| rn9 | | | |
| rn1 | | | |
