# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
from flask import Flask,make_response,json,g,jsonify,request, redirect, url_for, render_template, flash, session, abort
#from flask_httpauth import HTTPBasicAuth
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler


#initialize app before importing anything else
app = Flask(__name__)
#auth = HTTPBasicAuth()
api = Api(app)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'



#added for saving logs
def configure_logger(logger_level):
    app.logger.setLevel(logger_level)
    handler = logging.handlers.RotatingFileHandler('cloud.log',maxBytes=10000000,backupCount=10)
    formatter = logging.Formatter('%(asctime)s - [%(levelname)s/%(module)s/%(funcName)s/%(lineno)d] - %(message)s')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

configure_logger(logging.DEBUG)


