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
    db.review.update_or_insert((db.review.uuid == request.vars.uuid),
            waypointID = request.vars.waypointID,
            userID = request.vars.userID,
            rating = request.vars.rating,
            reviewDescription = request.vars.reviewDescription
            )

    waypoint = db.waypoint[request.vars.uuid]
    newRating = (waypoint.rating + request.vars.rating) / 2
    newReviewList = waypoint.reviewList
    newReviewList.append(request.vars.uuid)
    newAverageCost = (waypoint.averageCost + request.vars.cost) / 2

    db.waypoint.update((db.waypoint.uuid == request.vars.uuid),
            rating = newRating,
            reviewList = newReviewList,
            averageCost = newAverageCost
            )

def add_waypoint():
    db.waypoint.update_or_insert((db.waypoint.uuid == request.vars.uuid),
            rating = request.vars.rating,
            locationLatitude = request.vars.locationLatitude,
            locationLongitude = request.vars.locationLongitude,
            description = request.vars.description,
            address = request.vars.address,
            waypointName = request.vars.waypointName,
            phoneNumber = request.vars.phoneNumber,
            averageCost = request.vars.averageCost,
            #routeTypeList = request.vars.routeTypeList,
            #timeSpentList = request.vars.timeSpentList
            )

def add_waypoint_photo():
    waypoint = db.waypoint[request.vars.uuid]

    waypoint = db.waypoint[request.vars.uuid]
    newPhotosURLList = waypoint.photosURLList
    newPhotosURLList.append(request.vars.photoURL)

    db.waypoint.update_or_insert((db.waypoint.uuid == request.vars.uuid),
            photosURLList = newPhotosURLList
            )
