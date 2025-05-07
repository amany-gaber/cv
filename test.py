yaz@gpu:~/specific_job$ docker compose up id
no such service: id
yaz@gpu:~/specific_job$ docher compose up -d
Command 'docher' not found, did you mean:
  command 'docker' from snap docker (27.5.1)
  command 'docker' from deb docker.io (26.1.3-0ubuntu1~24.04.1)
  command 'docker' from deb podman-docker (4.9.3+ds1-1ubuntu0.2)
See 'snap info <snapname>' for additional versions.
yaz@gpu:~/specific_job$ ls
api  docker-compose.yml  README.md
yaz@gpu:~/specific_job$ cd api
yaz@gpu:~/specific_job/api$ ls
dockerfile  Makefile  README.md  requirements.txt  src
yaz@gpu:~/specific_job/api$ cd src
yaz@gpu:~/specific_job/api/src$ ls
config  main.py  __pycache__  routes  schemas  services  static
yaz@gpu:~/specific_job/api/src$ cd config
yaz@gpu:~/specific_job/api/src/config$ ls
__init__.py  __pycache__  setting.py
yaz@gpu:~/specific_job/api/src/config$ cd schema
bash: cd: schema: No such file or directory
yaz@gpu:~/specific_job/api/src/config$ cd ..
yaz@gpu:~/specific_job/api/src$ cd schema
bash: cd: schema: No such file or directory
yaz@gpu:~/specific_job/api/src$ cd schemas
yaz@gpu:~/specific_job/api/src/schemas$ ls
error.py  __init__.py  __pycache__  user.py
yaz@gpu:~/specific_job/api/src/schemas$ cd ..
yaz@gpu:~/specific_job/api/src$ cd services
yaz@gpu:~/specific_job/api/src/services$ ls
__init__.py  main.py  __pycache__
yaz@gpu:~/specific_job/api/src/services$ cd ..
yaz@gpu:~/specific_job/api/src$ cd static
yaz@gpu:~/specific_job/api/src/static$ ls
job_data.csv
yaz@gpu:~/specific_job/api/src/static$ ^C
yaz@gpu:~/specific_job/api/src/static$ 








from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_ROOT: str = "/api/v0"
    APP_NAME: str = "jobs"
    APP_DESCRIPTION: str = "specific-job"
    DOMAIN: str = "0.0.0.0"
    BACKEND_PORT: int = 8080
    DEBUG_MODE: bool = True


import uvicorn
from fastapi import APIRouter
from services import *

service = APIRouter(
    prefix="/specific-job",
    tags=["Perdict"]
)


if __name__ == "__main__":
    uvicorn.run(service)

# uvicorn main:app --reload



from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from services.main import JobMatcher

router = APIRouter(
    prefix="/specific job",
    tags=["specific job"]
)

job_matcher = JobMatcher()

@router.post("/inference")
async def match_cv(
    file: UploadFile = File(...),
    job_title: str = Form(...),
    governorate: str = Form(...),
    level: str = Form(...)
):
    if not file.filename.endswith((".pdf", ".docx", ".txt")):
        raise HTTPException(status_code=400, detail="Only PDF, DOCX, and TXT files are supported.")

    try:
        result = job_matcher.match_job(file, job_title, governorate, level)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




import os
import re
import pandas as pd
import PyPDF2
import docx
import nltk
from fastapi import UploadFile
from io import BytesIO

# Download NLTK data (punkt for tokenization)
try:
    nltk.download('punkt', quiet=True)
except Exception as e:
    print(f"Warning: Failed to download NLTK punkt: {e}")

# Constants
STOPWORDS = set([
    "a", "the", "of", "and", "to", "up", "i", "com", "student", "education", "experience"
])

class JobMatcher:
    def __init__(self):
        # Resolve the path to job_data.csv relative to this file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_path = '/home/yaz/specific_job/api/src/static/job_data.csv'
        self.df, self.error = self.load_data()
        if self.error:
            raise ValueError(self.error)
        self.all_skills = self.get_all_skills()

    def load_data(self):
        try:
            if not os.path.exists(self.data_path):
                return None, f"File not found: {self.data_path}"
            df = pd.read_csv(self.data_path)
            required_columns = ['Job Title', 'skills', 'Governorate']
            for col in required_columns:
                if col not in df.columns:
                    return None, f"Missing column: {col}"
            level_col = 'professional level' if 'professional level' in df.columns else 'professional Level'
            if level_col not in df.columns:
                return None, "Missing professional level column"
            return df, None
        except Exception as e:
            return None, f"Error loading data: {e}"

    def extract_text_from_cv(self, file: UploadFile):
        text = ""
        ext = file.filename.split('.')[-1].lower()
        try:
            file_content = file.file.read()  # Read file content into memory
            if ext == 'pdf':
                reader = PyPDF2.PdfReader(BytesIO(file_content))
                for page in reader.pages:
                    text += page.extract_text() or ""
            elif ext == 'docx':
                doc = docx.Document(BytesIO(file_content))
                text = "\n".join([para.text for para in doc.paragraphs])
            elif ext == 'txt':
                text = file_content.decode('utf-8')
            else:
                return None, f"Unsupported file format: {ext}"
            return text, None
        except Exception as e:
            return None, str(e)

    def extract_skills(self, text, skills_list):
        if not text:
            return []
        text = text.lower()
        found = [s for s in skills_list if re.search(r'\b' + re.escape(s.lower()) + r'\b', text)]
        filtered = [s for s in found if s.lower() not in STOPWORDS and len(s) > 2]
        return list(set(filtered))

    def analyze_skills(self, user_skills, job_skills):
        user_lower = set(s.lower() for s in user_skills)
        matched = [s for s in job_skills if s.lower() in user_lower]
        missing = [s for s in job_skills if s.lower() not in user_lower]
        return matched, missing

    def get_all_skills(self):
        if self.df is None:
            raise ValueError("DataFrame not loaded. Check the job_data.csv file.")
        all_skills = []
        for skill_text in self.df['skills']:
            skills = [s.strip() for s in str(skill_text).split(',')]
            all_skills.extend(skills)
        return list(set(all_skills))

    def match_job(self, file: UploadFile, job_title: str, governorate: str, level: str):
        # Validate inputs
        job_title = job_title.strip().lower()
        governorate = governorate.strip().lower()
        level = level.strip().lower()
        if not all([job_title, governorate, level]):
            return {"error": "Job title, governorate, and level must not be empty."}

        # Extract text from CV
        text, error = self.extract_text_from_cv(file)
        if error:
            return {"error": error}

        # Extract user skills
        user_skills = self.extract_skills(text, self.all_skills)
        if not user_skills:
            return {"error": "No valid skills found in CV."}

        # Normalize DataFrame for matching
        if self.df is None:
            return {"error": "DataFrame not available for matching."}
        df = self.df.copy()  # Use a copy to avoid modifying the original
        level_col = 'professional level' if 'professional level' in df.columns else 'professional Level'
        df['job_title_lower'] = df['Job Title'].str.strip().str.lower()
        df['governorate_lower'] = df['Governorate'].str.strip().str.lower()
        df['level_lower'] = df[level_col].str.strip().str.lower()

        # Find matching job
        job_row = df[
            (df['job_title_lower'] == job_title) &
            (df['governorate_lower'] == governorate) &
            (df['level_lower'] == level)
        ]

        if job_row.empty:
            job_row = df[df['job_title_lower'] == job_title]
            if job_row.empty:
                return {"error": f"No matching job found for title '{job_title}'."}

        # Extract job skills
        job_skills = [s.strip() for s in job_row.iloc[0]['skills'].split(',')]
        matched, missing = self.analyze_skills(user_skills, job_skills)
        percent = round((len(matched) / len(job_skills)) * 100, 2) if job_skills else 0
        top_missing = missing[:5] if len(missing) > 5 else missing

        return {
            "summary": f"You match {len(matched)} out of {len(job_skills)} required skills ({percent:.1f}%) for the job '{job_title.title()}' in {governorate.title()} ({level} level).",
            "cv_skills_found": user_skills,
            "matched_skills": {
                "count": len(matched),
                "skills": matched
            },
            "missing_skills": {
                "count": len(missing),
                "skills": missing
            },
            "top_missing_suggestions": top_missing,
            "recommendation": f"To improve your chances, consider learning or highlighting these skills in your CV: {', '.join(top_missing)}."
        }




from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes.user import router
import uvicorn
from config import settings

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes from src/routes/user.py
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Click /docs to see the API documentation"}

@app.exception_handler(404)
def not_found_error(request, exc):
    return {"detail": "Page Not Found. Click /docs to see the API documentation"}

@app.exception_handler(Exception)
def handle_exception(request, exc):
    return {"message": f"Oops! {str(exc)}. Please try again!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # Runs relative to the current directory (api/src/)
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT,
        reload=settings.DEBUG_MODE if hasattr(settings, "DEBUG_MODE") else False,
    )



FROM ubuntu:20.04 AS builder-image
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel \
    build-essential git \
    ffmpeg libavcodec-extra libopus0
RUN python3.9 -m venv /home/docker/venv
ENV PATH="/home/docker/venv/bin:$PATH"
RUN python3.9 -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM ubuntu:20.04 AS runner-image
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.9 python3-venv \
    ffmpeg libavcodec-extra libopus0
RUN useradd --create-home docker
COPY --from=builder-image /home/docker/venv /home/docker/venv
USER docker
RUN mkdir /home/docker/app
WORKDIR /home/docker/app
COPY ./src /home/docker/app
EXPOSE 8080
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/home/docker/venv
ENV PATH="/home/docker/venv/bin:$PATH"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "3", "--log-level", "debug", "--timeout-keep-alive", "1000"]
