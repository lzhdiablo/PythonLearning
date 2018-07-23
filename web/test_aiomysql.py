import asyncio
import aiomysql

loop = asyncio.get_event_loop()

async def test1():
    async with aiomysql.create_pool(host='localhost', port=3306, user='root', password='root', db='pymysql') as pool:
        async with pool.get() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("select * from employee")
                results = await cursor.fetchall()
                print("111111111")
                await asyncio.sleep(1)
                for row in results:
                    firstname = row[0]
                    lastname = row[1]
                    age = row[2]
                    sex = row[3]
                    income = row[4]
                    print("%s %s %d %c %d" % (firstname, lastname, age, sex, income))
                conn.close()
                print("2222222222")

async def test2():
    async with aiomysql.connect(host='localhost', port=3306, user='root', password='root', db='pymysql') as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("select * from employee")
            results = await cursor.fetchall()
            print("33333")
            await asyncio.sleep(1)
            for row in results:
                firstname = row[0]
                lastname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                print("%s %s %d %c %d" % (firstname, lastname, age, sex, income))
            print("444444")
tasks = [test2(), test2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.run_forever()