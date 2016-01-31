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
    return dict()

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

def add_review_to_waypoint():
    db.review.update_or_insert((db.review.uuid == request.vars["uuid"]),
            waypointID = request.vars["waypointID"],
            userID = request.vars["userID"],
            rating = request.vars["rating"],
            placeCost = request.vars["cost"],
            reviewDescription = request.vars["reviewDescription"]
            )

    waypoint = db(db.waypoint.uuid == request.vars["uuid"]).select().first()
    newRating = (waypoint.rating + request.vars["rating"]) / 2
    newReviewList = waypoint.reviewList
    newReviewList.append(request.vars["uuid"])
    newAverageCost = (waypoint.averageCost + request.vars["cost"]) / 2

    db.waypoint.update((db.waypoint.uuid == request.vars["waypointID"]),
            rating = newRating,
            reviewList = newReviewList,
            averageCost = newAverageCost
            )

def add_route():
    db.route.update_or_insert((db.route.uuid == request.vars["uuid"]),
            startingPointLatitude = request.vars["startingPointLatitude"],
            startingPointLongitude = request.vars["startingPointLongitude"],
            endingPointLatitude = request.vars["endingPointLatitude"],
            endingPointLongitude = request.vars["endingPointLongitude"],
            userID = request.vars["userID"],
            routeName = request.vars["routeName"],
            routeType = request.vars["routeType"]
            )

def add_waypoint():
    db.waypoint.update_or_insert((db.waypoint.uuid == request.vars["uuid"]),
            rating = request.vars["rating"],
            locationLatitude = request.vars["locationLatitude"],
            locationLongitude = request.vars["locationLongitude"],
            description = request.vars["description"],
            address = request.vars["address"],
            waypointName = request.vars["waypointName"],
            phoneNumber = request.vars["phoneNumber"],
            averageCost = request.vars["averageCost"],
            #routeTypeList = request.vars["routeTypeList"],
            #timeSpentList = request.vars["timeSpentLis"]t
            )

def add_waypoint_to_route():
    route = db(db.route.uuid == request.vars["uuid"]).select().first()
    waypoint = db(db.waypoint.uuid == request.vars["waypointID"]).select().first()

    newWaypointList = route.waypointList
    newWaypointList.append(request.vars["waypointID"])
    
    db.route.update((db.route.uuid == request.vars["uuid"]),
            waypointList = newWaypointList,
            totalDistance = request.vars["totalDistance"],
            totalTime = request.vars["totalTime"]
            )

def add_photo_to_waypoint():
    waypoint = db(db.waypoint.uuid == request.vars["uuid"]).select().first()
    newPhotosURLList = waypoint.photosURLList
    newPhotosURLList.append(request.vars["photoURL"])

    db.waypoint.update_or_insert((db.waypoint.uuid == request.vars["uuid"]),
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
    search_input = request.vars["userInput"].lower()
    waypoints = db().select(db.waypoint.ALL)

    matched_waypoints = []
    for waypoint in waypoints:
        check_length = len(search_input) if len(search_input) <= len(waypoint["waypointName"]) else len(waypoint["waypointName"])
        first_chars = waypoint["waypointName"][:check_length].lower()
        if search_input == first_chars:
            matched_waypoints.append(waypoint)

    return response.json(matched_waypoints)

def get_waypoints_by_area():
    minlo = request.vars["west"]
    maxlo = request.vars["east"]
    minla = request.vars["south"]
    maxla = request.vars["north"]

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
    newAverageCost = (waypoint.averageCost * len(waypoint.reviewList) - review.placeCost) / (len(waypoint.reviewList) - 1)
    newReviewList = filter(lambda reviewID : reviewID == request.vars.unique_id, waypoint.reviewList)

    db.waypoint.update_or_insert((db.waypoint.uuid == review.waypointID),
            rating = newRating,
            averageCost = newAverageCost,
            reviewList = newReviewList
            )

    review.delete()

def update_route():
    return 0

def update_waypoint():
    return 0

def test():
    return dict(form=auth.login())
