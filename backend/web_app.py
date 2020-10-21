#!/usr/bin/env python3

from aiohttp.web import RouteTableDef, Response, Application, AppRunner, TCPSite
from argparse import ArgumentParser
import asyncio
from graphql import GraphQLSchema, GraphQLObjectType, GraphQLField, GraphQLString
from graphql_server.aiohttp import GraphQLView
from logging import getLogger


logger = getLogger(__name__)


schema = GraphQLSchema(
    query=GraphQLObjectType(
        name='RootQueryType',
        fields={
            'hello': GraphQLField(
                GraphQLString,
                resolve=lambda obj, info: 'world')
            }))


routes = RouteTableDef()


@routes.get('/')
async def index_handler(request):
    return Response(text='Hello World!\n')


def main():
    p = ArgumentParser()
    p.add_argument('--port', '-p', type=int, default=5000)
    args = p.parse_args()
    setup_logging()
    asyncio.run(async_main(args=args))
    logger.debug('Done')


async def async_main(args):
    app = Application()
    app.add_routes(routes)
    # GraphQLView source: https://github.com/graphql-python/graphql-server/blob/master/graphql_server/aiohttp/graphqlview.py
    GraphQLView.attach(app, schema=schema, route_path='/api/graphql', graphiql=True)
    runner = AppRunner(app)
    await runner.setup()
    try:
        site = TCPSite(runner, 'localhost', args.port)
        await site.start()
        logger.info(f'Listening on http://127.0.0.1:{args.port}')
        while True:
            await asyncio.sleep(10)
    finally:
        await runner.cleanup()


def setup_logging():
    from logging import DEBUG, basicConfig
    basicConfig(format='%(asctime)s %(name)-15s %(levelname)5s: %(message)s', level=DEBUG)


if __name__ == '__main__':
    main()
