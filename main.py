import asyncio
import os
import sys
from orm import AsyncORM

sys.path.insert(1, os.path.join(sys.path[0], '..'))


AsyncORM.create_tables()

AsyncORM.insert_user()

AsyncORM.select_user()

AsyncORM.update_user()
