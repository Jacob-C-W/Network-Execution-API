
Netmiko API | API Call to Network-Execution-API

1. Start the API server/service, network-execution-api.py
2. Client calls API `GET /devices/{host}/hostname`
3. Based on inventory.json, fetch Netmiko dependencies (device_type, host, credential_profile)
4. credential_profile needs to call to Hashicorp with an API key. connectvault.py
5. Fetch credential_profile, return credential {username, password}
6. Plug (device_type, host, credential_profile{username, password}) into ssh_connect.py
7. send `hostname = connection.send_command("show system info | match hostname")`
8. return system hostname