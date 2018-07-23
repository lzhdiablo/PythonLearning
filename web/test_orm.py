from web.orm import Model, StringField, TextField, IntegerField, create_pool
from web.models import User
import asyncio

async def test_user_save():
    await create_pool()
    user = User(id='123', name='lzh')
    await user.save()

async def test_user_selectAll():
    await create_pool()
    users = await User.findAll()
    for user in users:
        print('id: %d, name: %s' % (user.id, user.name))

async def test_user_update():
    await create_pool()
    user = User(id='123', name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await user.update()

async def test_user_remove():
    await create_pool()
    user = User(id='123')
    await user.remove()

loop = asyncio.get_event_loop();
loop.run_until_complete(test_user_update())