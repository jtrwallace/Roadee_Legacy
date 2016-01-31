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

def add_review():
    db.review.update_or_insert((db.review.uuid == request.vars.unique_id),
            waypointID = request.vars.data["waypointID"],
            userID = request.vars.data["userID"],
            rating = request.vars.data["rating"],
            mycost = request.vars.data["cost"],
            reviewDescription = request.vars.data["reviewDescription"]
            )

    waypoint = db(db.waypoint.uuid == request.vars.unique_id).select().first()
    newRating = (waypoint.rating + request.vars.data["rating"]) / 2
    newReviewList = waypoint.reviewList
    newReviewList.append(request.vars.unique_id)
    newAverageCost = (waypoint.averageCost + request.vars.data["cost"]) / 2

    db.waypoint.update((db.waypoint.uuid == request.vars.data["waypointID"]),
            rating = newRating,
            reviewList = newReviewList,
            averageCost = newAverageCost
            )

def add_route():
    db.route.update_or_insert((db.route.uuid == request.vars.unique_id),
            startingPointLatitude = request.vars.data["startingPointLatitude"],
            startingPointLongitude = request.vars.data["startingPointLongitude"],
            endingPointLatitude = request.vars.data["endingPointLatitude"],
            endingPointLongitude = request.vars.data["endingPointLongitude"],
            userID = request.vars.data["userID"],
            routeName = request.vars.data["routeName"],
            routeType = request.vars.data["routeType"]
            )

def add_waypoint():
    db.waypoint.update_or_insert((db.waypoint.uuid == request.vars.unique_id),
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

def add_waypoint_to_route():
    route = db(db.route.uuid == request.vars.unique_id).select().first()
    waypoint = db(db.waypoint.uuid == request.vars.waypointID).select().first()

    newWaypointList = route.waypointList
    newWaypointList.append(request.vars.waypointID)
    
    db.route.update((db.route.uuid == request.vars.unique_id),
            waypointList = newWaypointList,
            totalDistance = request.vars.data["totalDistance"],
            totalTime = request.vars.data["totalTime"]
            )

def add_waypoint_photo():
    waypoint = db(db.waypoint.uuid == request.vars.unique_id).select().first()
    newPhotosURLList = waypoint.photosURLList
    newPhotosURLList.append(request.vars.data["photoURL"])

    db.waypoint.update_or_insert((db.waypoint.uuid == request.vars.unique_id),
            photosURLList = newPhotosURLList
            )

def get_reviews_by_waypoint():
    reviews = db(db.review.waypointID == request.vars.unique_id).select()
    return response.json(reviews)

def get_routes_by_user():
    routes = db(db.route.userID == request.vars.unique_id).select().first()
    return response.json(routes)

def get_waypoints_by_route():
    route = db(db.route.uuid == request.vars.unique_id).select()

    waypoints = []
    for waypointID in route.waypointList:
        waypoints.append(db(db.waypoint.uuid == waypointID).select().first())

    return response.json(waypoints)

def get_waypoints_by_name():
    search_input = request.vars.unique_id.lower()
    waypoints = db().select(db.waypoint.ALL)

    matched_waypoints = []
    for waypoint in waypoints:
        first_chars = waypoint["waypointName"][:len(search_input)].lower()
        if search_input == first_chars:
            matched_waypoints.append(waypoint)

    return response.json(matched_waypoints)

def get_waypoints_by_area():
    minlo = request.vars.data["west"]
    maxlo = request.vars.data["east"]
    minla = request.vars.data["south"]
    maxla = request.vars.data["north"]

    containsLocation = lambda lo, la : minlo <= lo and lo <= maxlo and minla <= la and la <= maxla

    waypoints = db().select(db.waypoint.ALL)

    matched_waypoints = []
    for waypoint in waypoints:
        if containsLocation(waypoint.locationLongitude, waypoint.locationLatitude):
            matched_waypoints.append(waypoint)

    return response.json(matched_waypoints)

def remove_waypoint_from_route():
    route = db(db.route.uuid == request.vars.unique_id).select().first()
    newWaypointList = filter(lambda waypointID : waypointID == request.vars.unique_id, route.waypointList)

    db.route.update_or_insert((db.route.uuid == request.vars.unique_id),
            waypointList = newWaypointList
            )

def remove_route():
    db(db.route.uuid == request.vars.unique_id).select().first().delete()

def remove_review_from_waypoint():
    review = db(db.review.uuid == request.vars.unique_id).select().first()
    waypoint = db(db.waypoint.uuid == review.waypointID).select().first()
    newRating = (waypoint.rating * len(waypoint.reviewList) - review.rating) / (len(waypoint.reviewList) - 1)
    newAverageCost = (waypoint.averageCost * len(waypoint.reviewList) - review.mycost) / (len(waypoint.reviewList) - 1)
    newReviewList = filter(lambda reviewID : reviewID == request.vars.unique_id, waypoint.reviewList)

    db.waypoint.update_or_insert((db.waypoint.uuid == review.waypointID),
            rating = newRating,
            averageCost = newAverageCost,
            reviewList = newReviewList
            )

    review.delete()
