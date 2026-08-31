### LIBRARIES ###

# main lib
import json
from fastapi import FastAPI, HTTPException

# custom lib
from connectvault import get_credentials
from sshconnect import execute

# define the app
app = FastAPI(
    title="Network Execution API",
    version="0.1"
)

### FUNCTIONS ###

# load inventory function
def load_inventory():
# read inventory.json
    with open("inventory.json", "r") as f:
        inventory = json.load(f)
    return inventory


### API CALLS ###

# api get api service name and status
@app.get("/")
def root():
    return {
        "service": "network-execution-api",
        "status": "running"
    }

# api get device inventory
@app.get("/devices")
def get_devices():
    inventory = load_inventory()

    return inventory["devices"]

# api get host hostname from inventory
@app.get("/devices/{device}")
def get_device(device: str):
    inventory = load_inventory()

    for host in inventory["devices"]:

        if (
        host["host"]== device
        or host["hostname"] == device
    ):
            return host

    raise HTTPException(
            status_code=404,
            detail="Host not found."
        )



# Debug and test below using the above, tested, commands as references. 

@app.get("/devices/{hostname}/hostname")
def get_hostname(hostname: str):

    inventory = load_inventory()
    if hostname not in inventory:
        raise HTTPException(
        status_code=404,
        detail="Device not found"
    )
    device = inventory[hostname]

    credentials = get_credentials(
    device["credential_profile"]
    )

    command_output = execute(
    host=device["host"],
    device_type=device["device_type"],
    username=credentials["username"],
    password=credentials["password"],
    command="show running-config | include hostname"
    )

    actual_hostname = (
    command_output
    .replace("hostname", "")
    .strip()
    )

    return {
    "inventory_hostname": hostname,
    "device_hostname": actual_hostname,
    "match": hostname == actual_hostname
    }

# run the api with the following command
# uvicorn network_execution_api:app --reload
# use /docs to test and see all API calls