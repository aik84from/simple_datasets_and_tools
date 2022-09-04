from aiohttp import web


async def dataset(request):
    return web.json_response(get_dataset())


app = web.Application()
app.add_routes([web.get('/api/v1/dataset', dataset)])


if __name__ == '__main__':
    web.run_app(app)
