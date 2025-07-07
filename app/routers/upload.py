#Deals with uploading files.

from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os
import uuid
from app.messaging import broker
import config

router = APIRouter()

# Route for uploading files.
@router.post("/upload", status_code=201)
async def upload_document(
    file: UploadFile = File(...), role: str = Form(default="Default Role")
):
    """
    TODO: Implement file upload logic
    - Create unique file name using uuid
    - Save file to uploads directory
    - Publish message to doc_uploaded topic
    - Return success response
    """
    try:
        # TODO: Save file locally

        #Generate unique file name using UUID to avoid name collisions.
        filename=f"{uuid.uuid4()}_{file.filename}"

        #Get upload directory and ensure it exists.
        upload_dir=getattr(config,"UPLOAD_DIR","uploads")
        os.makedirs(upload_dir,exist_ok=True)

        #Save the file to disk.
        file_path=os.path.join(upload_dir,filename)

        #Opens the file and writes content from the uploaded file to 
        # save the uploaded file locally to the disk.
        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(file.file,buffer)

        # TODO: Publish message to topic for processing
        # Messaging is already implemented in the messaging.py file, refer to it and use it.
        # Think of all the keys that should be present in the message while publishing the message to the topic.
        # Use: await broker.publish("doc_uploaded", message)

        message={
            "file_path":file_path,
            "original_name":filename,
            "role":role
            }

        #sends mssg to the internal mssg queue.
        await broker.publish("doc_uploaded",message) # self is automatically passed

        # message is published.
        # message looks like this. Eg:
        #         {
        #     "file_path": "/uploads/uuid_filename.pdf",
        #     "original_name": "original_filename.pdf",
        #     "role": "Analyst"
        # }

        #message on the client side.
        #the role who has uploaded the file. Only those roles can access the uploaded doc.
        return {
            "message": "File uploaded and queued for processing",
            "file_path": file_path,  # TODO: file_path
            "role": role,
        }

    #prints the error if there is any.
    except Exception as e:
        return {"error": str(e)}