#########################################################################
## Define your tables below; for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

from datetime import datetime

db.define_table('routes',
    Field('startingPoint','decimal(9,6)'),
    Field('endingPoint','decimal(9,6)'),
    ##field for waypointList
    Field('totalDistance', 'double'),
    Field('userID','integer'),
    Field('routeName','string'),
    Field('totalTime','integer'),
    Field('routeType','string')
)

db.define_tables('review',
    Field('waypointID', 'integer'),
    Field('userID', 'integer'),
    Field('reviewDescription', 'string'),
    Field('postingTime',default=datetime.utcnow()),
    Field('postingTimeString','string', default=str(datetime.utcnow()))
)