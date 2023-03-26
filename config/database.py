from pymongo import MongoClient

from core import config

client = MongoClient("mongodb+srv://"+config.settings.user_name+":"+config.settings.pass_word+"@"+config.settings.host+"/test")
#client = MongoClient("mongodb+srv://root:1234@cluster0.l78dbvc.mongodb.net/test")


db = client.swe_classroom

collection_name = db["courses"]
