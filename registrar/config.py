# -*- coding: utf-8 -*-
"""
    copyright: (c) 2014 by Halfmoon Labs, Inc.
    copyright: (c) 2015 by Blockstack.org
    license: MIT, see LICENSE for more details.
"""

try:
    from config_local import *
except:

    print "using default config"

    import os

    DEBUG = True

    # --------------------------------------------------
    NAMECOIND_READONLY = False

    NAMECOIND_USE_HTTPS = True

    NAMECOIND_PORT = os.environ['NAMECOIND_PORT']
    NAMECOIND_SERVER = os.environ['NAMECOIND_SERVER']
    NAMECOIND_USER = os.environ['NAMECOIND_USER']
    NAMECOIND_PASSWD = os.environ['NAMECOIND_PASSWD']
    #WALLET_PASSPHRASE = os.environ['WALLET_PASSPHRASE']
    #--------------------------------------------------

    MONGODB_URI = os.environ['MONGODB_URI']
    OLD_DB = os.environ['OLD_DB']
    AWSDB_URI = os.environ['AWSDB_URI']
    MONGOLAB_URI = os.environ['MONGOLAB_URI']

    DEFAULT_HOST = '127.0.0.1'
    MEMCACHED_PORT = '11211'
    MEMCACHED_TIMEOUT = 15 * 60

    FRONTEND_SECRET = os.environ['FRONTEND_SECRET']