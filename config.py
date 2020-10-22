

from os import environ

config = {
    "tms" : {
        "base_url" : "http://data.tmsapi.com/v1.1",
        "key" : "3jtjdcn5fdzcqut3t9pww5b9",
        "lineupId" : "USA-TX42500-X",
        "zip_code" : "78701"
    },
    "database": {
        "mysql": {
            "host_port": 'localhost:8889',
            # "port": int(environ.get('SMSC_GATEWAY_MYSQL_PORT')),
            "username": 'root',
            "password": 'root',
            "database": "dataframe"
        },
    }

}