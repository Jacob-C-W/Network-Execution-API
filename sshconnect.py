# sshconnect.py

from netmiko import ConnectHandler

def execute(device, credentials, command):

    connection = ConnectHandler(
        device_type=device["device_type"],
        host=device["host"],
        username=credentials["username"],
        password=credentials["password"]
    )

    try:
        return connection.send_command(command)

    finally:
        connection.disconnect()