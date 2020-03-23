"""
HDF5 to SQLServer
"""

from argparse import ArgumentParser
import os
import sys
import pandas as pd
from sqlalchemy import create_engine
import yaml

op = ArgumentParser()
op.add_argument('hdf', help='Path to HDF5 file')
op.add_argument('config', help='Path to YAML config file')
args = op.parse_args()

with open(args.config) as f:
    config = yaml.load(f, Loader=yaml.CLoader)

cstring = config['Database']['sqlalchemy_connection_string']
engine = create_engine(cstring)

def node_to_table(node):
    """Translate HDF node name to valid table name"""
    node = node.lstrip('/')
    path = node.split('/')
    table_name = "_".join(path)
    return table_name

schema = config.get('Database').get('schema', None)
nodes = config['HDF']['nodes']
for node in nodes:
    df = pd.read_hdf(node)
    table = node_to_table(node)
    print("INFO: %s -> %s" % (node, table))
    df.to_sql(table, engine, schema=schema)