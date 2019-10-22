import json
import sqlite3

conn = None

def connect():
    """Connect to sqlite3"""
    global conn
    conn = sqlite3.connect('./staticdata.sqlite3')

