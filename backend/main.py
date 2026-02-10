from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import db

app=FastAPI()

#Cors configuration, to allow backend to talk to frontend, since both run on different server
origins=[
    #copy the address from forwared port for react app in github 
    "https://---.app.github.dev" #this should be a string
]
app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Data model for item
class Item (BaseModel):
    name:str
    description:str | None=None

#sanity check mongodb connection
@app.get("/ping")
async def ping_db():
    try:
        result = await db.command("ping")
        return {"mongo":"conneccted",
                "result":result}
    except Exception as e:
        return {"mongo":"error",
                "detail":str(e)}
    
#root 
@app.get("/") #aman
def root():
    return {"message": "FastAPI + MongoDB is alive!!!!",
            "dari angelpy": "lanjut bjiirr, dont despair of Allah's mercy!"}

#get items
@app.get("/items") #aman
async def get_items():
    try:
        items=[]
        cursor=db.items.find({})
        async for item in cursor:
            item["_id"]=str(item["_id"])
            items.append(item)
        return items
    except Exception as e:
        print("ERROR: ",e)
        raise HTTPException(status_code=500, detail=str(e))

#post items
@app.post("/items") #aman,  PPLEASE ERROR HANDLING IS SOOO IMPORTANTTTT
async def create_item(item:Item):
    try:
        item_dict=item.dict()
        result=await db.items.insert_one(item_dict)
        return {"id": str(result.inserted_id)} 
    except Exception as e:
        print("ERROR: ",e)
        raise HTTPException(status_code=500, detail=str(e))