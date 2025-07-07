from fastapi import FastAPI
from app.routers import upload, user_role, retrieval 
from app.subscriber import start_subscriber
from app.models import Base
from app.database import engine

app = FastAPI()

# Include routers
app.include_router(upload.router, tags=["File Upload"]) # Deals with uploading files.
app.include_router(user_role.router, tags=["User Role Management"])#Deals with user role mgmt.
app.include_router(retrieval.router, tags=["Retrieval"])

@app.on_event("startup")
async def startup_event():
    """
    Initialize application on startup
    - Create database tables
    - Start background subscriber
    """
    print("Starting Document Processor...")

    # Create database tables if they do not exist
    Base.metadata.create_all(bind=engine)

    # Start background subscriber who is listening the upload events.
    await start_subscriber()
    print("Background subscriber started")


@app.get("/")
def read_root():
    return {"message": "Document Processor is running!"}
