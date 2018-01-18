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
