from database.database import Base, async_engine, async_session_factory
from database.models import UsersORM


class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            async_engine.echo = True

    @staticmethod
    async def insert_user(user_id, created_at, status, status_updated_at):
        async with async_session_factory() as session:
            user = UsersORM(id=user_id, created_at=created_at, status=status, status_updated_at=status_updated_at)
            session.add(user)
            await session.flush()
            await session.commit()

    @staticmethod
    async def select_user(user_id):
        async with async_session_factory() as session:
            user = await session.get(UsersORM, user_id=user_id)
            return user

    @staticmethod
    async def update_user(user_id, status_updated_at):
        async with async_session_factory() as session:
            user = await session.get(UsersORM, user_id)
            user.status_updated_at = status_updated_at
            await session.commit()





 #   @staticmethod
 #   async def update_user(user_id, updated_at, status):
#        async with async_session_factory() as session:
 #           user = await session.get(UsersORM, user_id=user_id)
 #           user.updated_at = updated_at
 #           user.status = status
  #          await session.refresh(user)
  #          await session.commit()


#@staticmethod
#async def create_tables():
#    async with async_engine.begin() as conn:
#        await conn.run_sync(Base.metadata.create_all)