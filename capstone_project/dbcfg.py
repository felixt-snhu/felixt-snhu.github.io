DB_USER_NAME = "snhu_capstone_felix"
DB_USER_PASSWORD = "snhu_capstone_felix"
SERVER_SOCK = "cluster0-shard-00-00-krzka.mongodb.net:27017"
SERVER_OPTIONS = "test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
SERVER_CONNECTION_STRING = "mongodb://%s:%s@%s/%s" % (DB_USER_NAME, DB_USER_PASSWORD, SERVER_SOCK, SERVER_OPTIONS)
