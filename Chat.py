import pymongo
import os
import json
import gridfs

def Add_Response(Message , Response):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    AdamDb = client["ChatBotAdam"]
    Message = Message.upper()
    Msg = [{"_id":Message.strip(),"Respone":Response.rstrip()}]
    AdamDb.Respone.insert(Msg)

def Get_Response(WholeMessage):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    AdamDb = client["ChatBotAdam"]
    WholeMessage = WholeMessage.upper()
    Query = {"_id": WholeMessage}
    try:
        FinalRespone = AdamDb.Respone.find_one(Query)["Respone"]    
    except:
        print("No Record Found!")
        return ""
    else:
        return(FinalRespone)


def CanAddResponses():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    AdamDb = client["ChatBotAdam"]
    if AdamDb.ChatBot.find_one()["AddResponses"] == "Enabled":
        return True
    else:
        return False

def CanRespond():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    AdamDb = client["ChatBotAdam"]
    if AdamDb.ChatBot.find_one()["Respond"] == "Enabled":
        return True
    else:
        return False

def StoreImages():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    AdamDb = client["ChatBotAdam"]
    fs = gridfs.GridFS(AdamDb)
    stored = fs.put()
    outfile