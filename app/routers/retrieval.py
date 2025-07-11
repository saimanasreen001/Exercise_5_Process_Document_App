from fastapi import APIRouter, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.database import SessionLocal
from app.models import DocumentData
from app.ollama_client import ask_ollama

router = APIRouter()

@router.get("/retrieve")
# while accessing this route, role and question is given as input.
def retrieve_answer(role: str = Query(..., description="role of user"),question: str = Query(..., description="user question")):
    print(f"Received role: {role}")
    print(f"Received question: {question}")

    # extracts keywords from the question and question prompt is created
    question_prompt = (
        "Extract exactly 5 keywords from this question. "
        "Return only the keywords, separated by commas, all in lowercase, no numbering, no extra text:\n"
        f"{question}"
    )
    keywords = ask_ollama(question_prompt).strip() # holds keywords string separated by commas
    print(f"Extracted keywords string: {keywords}")

    keyword_list = [k.strip() for k in keywords.split(",")] # list of keyword is created
    print(f"Keyword list: {keyword_list}")

    db: Session = SessionLocal() # new db session is created
    try: 
        #filter records from document_data based on input role 
        query = db.query(DocumentData).filter(DocumentData.role == role)

        # filter those records from query where keywords are present.
        keyword_filters = [DocumentData.keywords.ilike(f"%{kw}%") for kw in keyword_list]
        print(f"Keyword filters: {keyword_filters}")

        chunks = query.filter(or_(*keyword_filters)).all() # holds all matching records
        print(f"Number of matching chunks: {len(chunks)}")

        if not chunks:
            print("No relevant chunks found.")
            return {"answer": "No relevant information found.", "matched_keywords": keyword_list}

        context = "\n".join([c.chunk_content for c in chunks]) # joins all chunks
        print(f"Context sent to Ollama (first 500 chars): {context[:500]}")

        prompt = (
            f"Given the following document content:\n{context}\n\n"
            f"Answer the following question concisely:\n{question}"
        )
        answer = ask_ollama(prompt)
        print(f"Ollama answer: {answer}")

        #returns json response on swagger UI
        return {"answer": answer, "matched_keywords": keyword_list}
    finally:
        db.close()



