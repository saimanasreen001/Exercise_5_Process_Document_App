#Entry point to run FastAPI server.
"""
Simple script to run the Document Processor API
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", host="0.0.0.0", port=8000, reload=True, log_level="info"
    )

 ## Ingestion
 
 ## upload.py --> message_processor.py

 # upload.py --> helps in uploading a document by a specified user role. 
                 # Message is created and published to the topic "doc_uploaded".

# message_processor.py --> processes the message published. i.e. extracts the file uploaded 
                        #  creates chunk and stores records in document_data table in db.
