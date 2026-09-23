# Hashicorp System Administration

Docker:

        nano docker-compose.yml     # Text editor write/overwrite docker compose file
        docker compose down         # Stops services in docker-compose.yml
        docker compose up -d        # Starts services in docker-compose.yml

https://vault.netops01.tld:8443/ui/

Token: Root

In Root in the WebUi go to Secrets, Enable new engine, KV, name the path "network"

Access the container:

    docker exec -it vault sh
    export VAULT_ADDR=http://127.0.0.1:8200
    export VAULT_TOKEN=root

Vault credential configuration:

Human Users:

        vault auth enable userpass                      # Allow login type

        vault write auth/userpass/users/netadmin \      # Add a user
            password="password" \                       # Assign password
            policies="root" \                           # Assign access policy

        vault delete auth/userpass/users/netadmin       # Delete a user

Machine Users:

        vault auth enable approle

        vault write auth/approle/users/netadmin \      # Add a user
            password="password" \                       # Assign password
            policies="root" \                           # Assign access policy

        vault delete auth/userpass/users/netadmin       # Delete a user


I create policies under the Token root account in the WebGUI. 

Access control > Create ACL policy > enter the vault path example/* > and check the access rights like read and write permissions > create policy > assign policies to users

        path "secret/*" {
            capabilities = ["create", "read", "update", "delete", "list", "patch", "sudo"]
        }
        path "network/*" {
            capabilities = ["create", "read", "update", "delete", "list", "patch", "sudo"]
        }

*the * star permits access to the paths within the allowed path*


Apply new policies to users in the CLI: 

        vault write auth/approle/users/netadmin \
            policies="newpolicy"

