from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
from database import engine, sessionLocal
import models
from sqlalchemy.orm import Session

app = FastAPI ()
models.Base.metadata.create_all(bind = engine)

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase (BaseModel): 
    question_text: str
    choices: List[ChoiceBase]

def get_db(): 
    db = sessionLocal()
    try:
        yield db
    finally: 
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


# endpoints
@app.post("/questions/")
async def create_questions(questions: QuestionBase, db: db_dependency): 
    db_question = models.Questions(question_text = questions.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    for choice in questions.choices: 
        db_choice = models.Choices(choice_text = choice.choice_text,
                                    is_correct = choice.is_correct,
                                    question_id = db_question.id )
        db.add(db_choice)
    db.commit() 
    return {" message": "Questions created succwsfully"}

# @app.get("/questions/{id}")
# async def get_data(id: int, questions: QuestionBase, db: db_dependency): 

