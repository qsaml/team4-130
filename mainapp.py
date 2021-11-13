from flask import Flask, render_template, request
from flask_table import Table, Col
import urllib.request
import json
import random
import queue

app = Flask(__name__)

@app.route('/')
def student():
	return render_template('index.html')

class ObjTable(Table):
	title_song = Col('Title of Song')
	singer = Col('Singer')

class Obj(object):
	def __init__(self, title_song, singer):
		self.title_song =  title_song
		self.singer = singer

class Singer:
	def __init__(self, name_singer, rate_singer):
		self.name_singer = name_singer
		self.rate_singer = rate_singer

class Song:
	def __init__(self, title_song, rate_song):
		self.title_song = title_song
		self.rate_song = rate_song


