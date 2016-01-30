# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

import json

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

def roadtrip():
    return dict(message=T('Welcome to web2py!'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def user_login():
    return dict()

def user_sign_up():
    return dict()

def add_review():
    db.review.update_or_insert((db.review.uuid == request.vars.data["reviewID"]),
            waypointID = request.vars.data["waypointID"],
            userID = request.vars.data["userID"],
            rating = request.vars.data["rating"],
            reviewDescription = request.vars.data["reviewDescription"]
            )

    waypoint = db(db.waypoint.uuid == request.vars.data["waypointID"]).select().first()
    newRating = (waypoint.rating + request.vars.data["rating"]) / 2
    newReviewList = waypoint.reviewList
    newReviewList.append(request.vars.data["reviewID"])
    newAverageCost = (waypoint.averageCost + request.vars.data["cost"]) / 2

    db.waypoint.update((db.waypoint.uuid == request.vars.data["waypointID"]),
            rating = newRating,
            reviewList = newReviewList,
            averageCost = newAverageCost
            )

    return

def add_waypoint():
    db.waypoint.update_or_insert((db.waypoint.uuid == request.vars.data["waypointID"]),
            rating = request.vars.data["rating"],
            locationLatitude = request.vars.data["locationLatitude"],
            locationLongitude = request.vars.data["locationLongitude"],
            description = request.vars.data["description"],
            address = request.vars.data["address"],
            waypointName = request.vars.data["waypointName"],
            phoneNumber = request.vars.data["phoneNumber"],
            averageCost = request.vars.data["averageCost"],
            #routeTypeList = request.vars.data["routeTypeList"],
            #timeSpentList = request.vars.data["timeSpentLis"]t
            )

    return

def add_waypoint_photo():
    waypoint = db(db.waypoint.uuid == request.vars.data["waypointID"]).select().first()
    newPhotosURLList = waypoint.photosURLList
    newPhotosURLList.append(request.vars.data["photoURL"])

    db.waypoint.update_or_insert((db.waypoint.uuid == request.vars.data["waypointID"]),
            photosURLList = newPhotosURLList
            )


    return 0;

def get_reviews_by_waypoint():
    reviews = db(db.review.waypointID == request.vars.data["waypointID"]).select()
    return response.json(list(reviews))

def get_routes_by_user():
    routes = db(db.route.userID == request.vars.data["userID"]).select().first()
    return response.json(dict(routes))

def get_waypoints_by_route():
    route = db(db.route.uuid == request.vars.data["routeID"]).select()

    waypoints = []
    for waypointID in route.waypointList:
        waypoints.append(db(db.waypoint.uuid == waypointID).select().first())

    return response.json(list(waypoints))

def get_waypoints_by_name():
    search_input = request.vars.data["waypointName"].lower()
    waypoints = db().select(db.waypoint.ALL)

    matched_waypoints = []
    for waypoint in waypoints:
        first_chars = waypoint["waypointName"][:len(search_input)].lower()
        if search_input == first_chars:
            matched_waypoints.append(waypoint)

    return response.json(list(matched_waypoints))

def get_waypoints_by_area():
    minlo = request.vars.data["minLongitude"]
    maxlo = request.vars.data["maxLongitude"]
    minla = request.vars.data["minLatitude"]
    maxla = request.vars.data["maxLatitude"]

    containsLocation = lambda lo, la : minlo <= lo and lo <= maxlo and minla <= la and la <= maxla

    waypoints = db().select(db.waypoint.ALL)

    matched_waypoints = []
    for waypoint in waypoints:
        if containsLocation(waypoint.locationLongitude, waypoint.locationLatitude):
            matched_waypoints.append(waypoint)

    return response.json(list(matched_waypoints))

def update_route():
    return 0;

def update_waypoint():
    return 0;
