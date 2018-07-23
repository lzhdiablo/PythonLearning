import asyncio
import sqlalchemy as sa

from aiomysql.sa import create_engine

metadata = sa.MetaData()
tbl = sa.Table('employee', metadata,
               sa.Column('FIRST_NAME', sa.CHAR),
               sa.Column('LAST_NAME', sa.CHAR),
               sa.Column('AGE', sa.INT),
               sa.Column('SEX', sa.CHAR),
               sa.Column('INCOME', sa.FLOAT))

async def test():
    engine = await create_engine(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='root',
                                 db='pymysql')
    async with (engine.acquire()) as conn:
        # trans = await conn.begin()
        # await conn.execute(tbl.insert().values(FIRST_NAME='liu', LAST_NAME='zehua', AGE='22', SEX='M', INCOME='5555'))
        # await trans.commit()
        row_count = (await conn.execute(tbl.select())).rowcount
        print(row_count)
        for row in await (await conn.execute(tbl.select())).fetchall():
            print("%s %s %d %c %d" % (row['FIRST_NAME'], row['LAST_NAME'], row['AGE'], row['SEX'], row['INCOME']))
        scalar = await (await conn.execute(tbl.select())).scalar() #返回第一行第一列数据
        print(scalar)
    engine.close() #不是coroutine
    await engine.wait_closed() #用在engine.close()之后，等待连接关闭

loop = asyncio.get_event_loop()
loop.run_until_complete(test())