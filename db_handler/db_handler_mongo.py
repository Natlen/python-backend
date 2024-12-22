from pymongo.errors import ConnectionFailure
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# CFG #

db_username_envkey : str = 'MONGODB_USERNAME'
db_password_envkey : str = 'MONGODB_PASSWORD'
db_cluster_envkey : str = 'MONGODB_CLUSTER'
db_env_path : str = 'db_handler/metadata/db_handler.env'

# --- #

class DBHandlerMongo():
    
    client : AsyncIOMotorClient

    def __init__(self):
        self.client = None

    async def mongodb_cluter_connect(self) -> None:
        load_dotenv(dotenv_path=db_env_path)
        mongodbUser : str = os.getenv(db_username_envkey)
        mongodbPass : str = os.getenv(db_password_envkey)
        mongodbCluster : str = os.getenv(db_cluster_envkey)
        
        if not mongodbUser or not mongodbPass or not mongodbCluster:
            raise ValueError(f'could not load \'mongodbUser\' and \'mongodbPass\' and \'mongodbCluster\' ')
        connection_string : str = f"mongodb+srv://{mongodbUser}:{mongodbPass}@{mongodbCluster}/?retryWrites=true&w=majority"

        self.client = AsyncIOMotorClient(connection_string, serverSelectionTimeoutMS=4000)

    async def mongodb_cluster_check_connection(self) -> None:
        try:
            self.client.admin.command('ping')
            print('connection succeeded')
        except ConnectionFailure as err:
            print(f'connection failed. {err}\n')

    async def mongodb_cluter_disconnect(self) -> None:
        try:
            self.client.close()
            print('connection succeeded')
        except ConnectionFailure as err:
            print(f'connection failed. {err}\n')

db_handler_mongo : DBHandlerMongo = DBHandlerMongo()