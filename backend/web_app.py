#!/usr/bin/env python3

from aiohttp.web import RouteTableDef, Response, Application, AppRunner, TCPSite
from argparse import ArgumentParser
import asyncio
from graphene import Schema, ObjectType, Field, List
from graphene import Int, String, DateTime, Boolean
from graphene.relay import Node, Connection, ConnectionField
from graphql_server.aiohttp import GraphQLView
from logging import getLogger


logger = getLogger(__name__)

# from graphql import GraphQLSchema, GraphQLObjectType, GraphQLField, GraphQLString
#
# schema = GraphQLSchema(
#     query=GraphQLObjectType(
#         name='RootQueryType',
#         fields={
#             'hello': GraphQLField(
#                 GraphQLString,
#                 resolve=lambda obj, info: 'world')
#             }))


class Query (ObjectType):

    node = Node.Field()
    hello = Field(String)

    async def resolve_hello(root, info):
        await asyncio.sleep(0.5)
        return 'world'


schema = Schema(query=Query).graphql_schema # "schema" must be graphql.GraphQLSchema, not graphene.Schema


routes = RouteTableDef() # aiohttp handlers table


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
    GraphQLView.attach(app, schema=schema, route_path='/api/graphql', graphiql=True, enable_async=True)
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
