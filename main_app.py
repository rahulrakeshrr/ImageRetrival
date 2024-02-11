from fastapi import FastAPI, Response,UploadFile,File, UploadFile,Form
from sqlalchemy import create_engine, Column, Integer, LargeBinary, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from typing import Optional, List
from fastapi import HTTPException, Depends,File
from pydantic import BaseModel

from PIL import Image
from io import BytesIO


# Replace   with the actual database URL
DATABASE_URL = "mysql://root:"your password"@localhost/fab_detec"

# Create a FastAPI app
app = FastAPI(title="Handloom Fabric  World!")

# Create a SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base for the SQLAlchemy models
Base = declarative_base()

# Define the Image model
class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    img = Column(LargeBinary)

# Model to handle image ID as input
class ImageRequest(BaseModel):
    image_id: int


# To load model and architecture
class Simple_Model():
    def __init__(self):
        super(Simple_Model,self).__init__()

# assigning class into model
#model = Simple_Model()
#model.eval()


# root attribute 
@app.get("/")
async def root():
    return {"Handloom Fabric  World!"}


@app.post("/files/uploading")
async def upload_file(file: UploadFile):
    return ({'file':file.file, 'file': file.filename,"file_content_name":file.content_type})


@app.post("/file2/upload2")
async def upload_files(file2: UploadFile,file3: bytes=File(),name: str=Form()):
    return ({'file': file2.filename,"file_size":len(file3),'author_name':name})


@app.post("/file4/uploading4")
async def upload_file(file4: UploadFile):
    data=file4.read()
    if file4.content_type == "application/jpeg":
        raise HTTPException(400, detail='invalid format')
    return ({'file': file4.filename, 'file_name':data })


# To retrive image from database using image id 
@app.get("/get_image/{image_id}")
async def get_image(image_id: int):
    # Fetch image from the database based on the provided image_id
    db = SessionLocal()
    image = db.query(Image).filter(Image.id == image_id).first()
    db.close()
    #Exception message
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    # Return the image as a response object
    response = Response(content=image.img, media_type="image/jpeg")
    return response
