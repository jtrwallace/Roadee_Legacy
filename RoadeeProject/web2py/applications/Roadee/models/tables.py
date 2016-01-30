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
    Field('uuid', 'string', default=str(uuid.uuid4())),
    Field('startingPointLatitude', 'decimal(9,6)'),
    Field('startingPointLongitude', 'decimal(9,6)'),
    Field('endingPointLatitude', 'decimal(9,6)'),
    Field('endingPointLongitude', 'decimal(9,6)'),
    Field('waypointList', 'list:string'),
    Field('totalDistance', 'double'),
    Field('userID', 'string'),
    Field('routeName', 'string'),
    Field('totalTime', 'integer'),
    Field('routeType', 'string')
)

db.define_table('waypoint',
    Field('uuid', 'string', default=str(uuid.uuid4())),
    Field('rating', 'integer'),
    Field('photosURLList', 'list:string'),
    Field('locationLatitude', 'decimal(9,6)'),
    Field('locationLongitude', 'decimal(9,6)'),
    Field('description', 'string'),
    Field('address', 'string'),
    Field('waypointName', 'string'),
    Field('phoneNumber', 'string'),
    Field('averageCost', 'double'),
    Field('reviewList', 'list:string'),
    #Field('numberOfReviews', 'integer'),
    #Field('routeTypeList', 'list:string'),
    #Field('timeSpentList', 'list:string')
)

db.define_table('review',
    Field('uuid', 'string', default=str(uuid.uuid4())),
    Field('waypointID', 'string'),
    Field('userID', 'string'),
    Field('rating', 'integer'),
    Field('reviewDescription', 'string'),
    Field('postingTime', default=datetime.utcnow()),
    Field('postingTimeString', 'string', default=str(datetime.utcnow()))
)
