#!bin/bash

IP_HOST="192.168.56.102"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"
DATA_FORMAT="application/yang-data+json"
LOOPBACK_INTERFACE="Loopback199"
LOOPBACK_IP="10.1.99.1"

api_url_get=https://$IP_HOST/restconf/data/ietf-interfaces:interfaces

H1="Content-type:$DATA_FORMAT"
H2="Accept:$DATA_FORMAT"
basicauth="$RESTCONF_USERNAME:$RESTCONF_PASSWORD"


curl -i -k -X "GET" "$api_url_get" -H "$H1" -H "$H2" -u "$basicauth"


