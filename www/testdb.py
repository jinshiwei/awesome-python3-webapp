#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Testing database.
'''

__author__ = 'Shiwei Jin'

import orm, asyncio
from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):

    yield from orm.create_pool(loop=loop, user='www-data', password='www-data', db='www')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()


if __name__ == '__main__':
    main()
