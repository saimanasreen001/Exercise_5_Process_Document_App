# Exercise 5 - Process Document App

  This App has three different aspects.
  1. Ingestion
  2. Storage
  3. Retrieval


## Workflow 

  A document is uploaded by a specified user role using the upload route.
  A message with the file_name, original_name and role is published to the topic "doc_uploaded".
  Document uploaded is now processeed and the attributes like chunk, summary of the chunks are stored as records in the document_data table.
  While retrieval, user role and question is required in the retrieve route. Based on filterations from the document_data table, json response is generated on the Swagger UI.

## Setup Instructions

  1. Clone the repository

      git clone https://github.com/saimanasreen001/Exercise_5_Process_Document_App.git
      cd Exercise_5_Process_Document_App

  2. Create and activate virtual environment

      python3 -m venv venv
      source venv/bin/activate

  3. Install the dependencies from requirements.txt

      pip install -r requirements.txt

  4. Run the app

      python run.py



