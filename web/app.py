import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(text='<h1>Awesome</h1>')

async def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', '9000')
    await site.start()
    logging.info('server started at http://127.0.0.1:9000...')

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()