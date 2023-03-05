from peewee import *

from LabSettings.settings import db


class Announce(Model):
    image = TextField(null=True)
    price = CharField(max_length=100, null=True)
    added_at = CharField(max_length=200, null=True)
    date = CharField(max_length=20)

    class Meta:
        database = db


db.connect()
Announce.create_table()
db.close()