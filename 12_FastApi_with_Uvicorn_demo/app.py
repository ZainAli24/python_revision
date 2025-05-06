from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
def home():
    return "Hey WellCome to My APP !"


@app.get("/Zain")
def Zain():
    return "Hey My Name is Zain, I am from Pakistan, Gujar Khan"

@app.post("/upload")
def handleImage(files: list[UploadFile]):
    print(files)
    return "My Image is upload successfully, \n status code : 200"

    
import uvicorn

uvicorn.run(app)
