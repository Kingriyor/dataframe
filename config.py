
config = {
    "tms" : {
        "base_url" : "http://data.tmsapi.com/v1.1",
        "key" : "f7rwk42v8wvmgw5gcfpe5fgd", # https://developer.tmsapi.com/apps/mykeys  to register and get a new API key
        # "key" : "3jtjdcn5fdzcqut3t9pww5b9",
        "lineupId" : "USA-TX42500-X",
        "zip_code" : "78701"
    },
    "database": {
        "mysql": {
            "host_port": 'localhost:8889',
            "username": 'root',
            "password": 'root',
            "database": "dataframe"
        },
    }

}