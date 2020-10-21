#!/usr/bin/env python3

from aiohttp.web import RouteTableDef, Response, Application, AppRunner, TCPSite
from argparse import ArgumentParser
import asyncio
from datetime import datetime
from graphql import print_schema
from graphene import Schema, ObjectType, Field, List
from graphene import Int, String, DateTime, Boolean
from graphene.relay import Node, Connection, ConnectionField
from graphql_server.aiohttp import GraphQLView
from logging import getLogger
from pathlib import Path


logger = getLogger(__name__)


notes_data = [
    {
        'id': 'n1',
        'created': datetime(2020, 10, 20, 12, 0),
        'text': 'První poznámka'
    },
    {
        'id': 'n2',
        'created': datetime(2020, 10, 21, 15, 30),
        'text': 'Text druhé poznámky'
    },
]


class Note (ObjectType):

    class Meta:
        interfaces = (Node, )

    created = DateTime()
    text = String()
    wordCount = Int()

    @classmethod
    async def get_node(cls, info, id):
        raise NotImplementedError()

    async def resolve_wordCount(note, info):
        return len(note['text'].split())


class NoteConnection (Connection):

    class Meta:
        node = Note


class Query (ObjectType):

    node = Node.Field()
    hello = String()
    upper = String(s=String())
    notes = ConnectionField(NoteConnection)

    async def resolve_hello(root, info):
        return 'world'

    async def resolve_upper(root, info, s):
        await asyncio.sleep(1)
        return s.upper()

    async def resolve_notes(root, info, **kwargs):
        logger.debug('resolve_notes kwargs: %r', kwargs)
        return notes_data


schema = Schema(query=Query).graphql_schema


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


# print graphql schema to frontend/schema.graphql (needed by frontend Relay)
schema_file = Path(__file__).parent / '../frontend/schema.graphql'
schema_file.write_text(print_schema(schema))


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
    basicConfig(
        format='%(asctime)s %(name)-15s %(levelname)5s: %(message)s',
        level=DEBUG)


if __name__ == '__main__':
    main()
