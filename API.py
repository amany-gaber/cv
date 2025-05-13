from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
import uuid
from services.text_to_speech import text_to_speech_stream
from services.interview import InterviewSession
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_community.vectorstores import Chroma
from config import topic_mapping
from typing import Optional, List

AVATAR_URL = os.getenv("AVATAR_URL", "http://localhost:8002/sync")

app = FastAPI()

# In-memory session store (for demo/dev)
sessions = {}

# Get base directory (directory where this file is located)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Allow overriding via environment variable, otherwise use relative path
CHROMA_DIR = os.getenv("CHROMA_DIR", os.path.join(BASE_DIR, "docs", "chroma"))

# Models
class StartInterviewRequest(BaseModel):
    topic: str
    subtopics: List[str]
    num_questions: int 
    candidate_info: Optional[str] = None

class StartInterviewResponse(BaseModel):
    session_id: str
    first_question: str

class NextQuestionRequest(BaseModel):
    session_id: str
    answer: Optional[str] = None

class NextQuestionResponse(BaseModel):
    question: Optional[str] = None
    finished: bool = False

class FeedbackRequest(BaseModel):
    session_id: str

class FeedbackResponse(BaseModel):
    feedback: str

class TTSRequest(BaseModel):
    text: str

class TTSResponse(BaseModel):
    avatar_video_url: Optional[str] = None

# Helper to get or create model/embeddings/vectordb
def get_model_stack():
    try:
        embeddings = OllamaEmbeddings(model="deepseek-r1:1.5b")
        model = OllamaLLM(model="deepseek-r1:1.5b", temperature=0.7)
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Failed to initialize Ollama models (deepseek-r1:1.5b): {str(e)}")
    try:
        vectordb = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    except Exception as e:
        print(f"Error initializing Chroma vector DB: {e}")
        vectordb = None
    return model, embeddings, vectordb

@app.post("/start_interview", response_model=StartInterviewResponse)
def start_interview(req: StartInterviewRequest):
    if req.topic not in topic_mapping:
        raise HTTPException(status_code=400, detail=f"Invalid topic. Valid topics: {list(topic_mapping.keys())}")
    model, embeddings, vectordb = get_model_stack()
    session = InterviewSession(model, embeddings, vectordb)
    session.topic = req.topic
    session.subtopics = req.subtopics or ["general"]
    session.num_questions = req.num_questions
    session.candidate_info = req.candidate_info
    session.current_q_idx = 0
    session.finished = False
    # Generate first question
    subtopic = session.subtopics[0]
    question = session.generator.generate_question(session.topic, subtopic, session.previous_questions)
    session.previous_questions.append(question)
    session.current_question = question
    # Store session
    session_id = str(uuid.uuid4())
    sessions[session_id] = session
    return StartInterviewResponse(session_id=session_id, first_question=question)

@app.post("/next_question", response_model=NextQuestionResponse)
def next_question(req: NextQuestionRequest):
    session = sessions.get(req.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session.finished:
        return NextQuestionResponse(question=None, finished=True)
    # Store previous answer
    if req.answer is not None:
        session.memory.chat_memory.add_user_message(req.answer)
    # If finished
    if session.current_q_idx + 1 >= session.num_questions:
        session.finished = True
        return NextQuestionResponse(question=None, finished=True)
    # Generate next question
    session.current_q_idx += 1
    subtopic = session.subtopics[session.current_q_idx % len(session.subtopics)]
    question = session.generator.generate_question(session.topic, subtopic, session.previous_questions)
    session.previous_questions.append(question)
    session.current_question = question
    return NextQuestionResponse(question=question, finished=False)

@app.post("/feedback", response_model=FeedbackResponse)
def feedback(req: FeedbackRequest):
    session = sessions.get(req.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    fb = session.get_feedback(session.topic)
    session.finished = True
    return FeedbackResponse(feedback=fb)

@app.post("/tts", response_model=TTSResponse)
def tts(req: TTSRequest):
    audio_path = text_to_speech_stream(req.text)
    with open(audio_path, "rb") as audio_file:
        avatar_resp = requests.post(
            AVATAR_URL,
            files={"audio": ("output.mp3", audio_file, "audio/mpeg")}
        )
    try:
        video_url = avatar_resp.json().get("video_url")
    except Exception:
        video_url = None
    return TTSResponse(avatar_video_url=video_url)