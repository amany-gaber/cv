yaz@gpu:~/specific_job$ cd ~/specific_job
docker compose down  # Stop and remove any existing containers
docker compose up -d --build
WARN[0000] /home/yaz/specific_job/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] /home/yaz/specific_job/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 1.1s (19/19) FINISHED                                                                                                                            docker:default
 => [api internal] load build definition from dockerfile                                                                                                                0.0s
 => => transferring dockerfile: 929B                                                                                                                                    0.0s
 => [api internal] load metadata for docker.io/library/python:3.9-slim                                                                                                  1.0s
 => [api internal] load .dockerignore                                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => CANCELED [api builder-image 1/9] FROM docker.io/library/python:3.9-slim@sha256:bef8d69306a7905f55cd523f5604de1dde45bbf745ba896dbb89f6d15c727170                     0.0s
 => => resolve docker.io/library/python:3.9-slim@sha256:bef8d69306a7905f55cd523f5604de1dde45bbf745ba896dbb89f6d15c727170                                                0.0s
 => => sha256:c8ecde0b63a4881272d794f7fcf2ba2ed4c0f7594c8d783905423e7e964ade28 1.75kB / 1.75kB                                                                          0.0s
 => => sha256:9a041530811d5397b63cb7255cdcdd27195706cf5faf81d77242cd01d7a68da8 5.29kB / 5.29kB                                                                          0.0s
 => => sha256:bef8d69306a7905f55cd523f5604de1dde45bbf745ba896dbb89f6d15c727170 10.41kB / 10.41kB                                                                        0.0s
 => [api internal] load build context                                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => CACHED [api builder-image 2/9] RUN apt-get update && apt-get install -y --no-install-recommends     build-essential██                                               0.0s
 => CACHED [api builder-image 3/9] RUN pip install --upgrade pip                                                                                                        0.0s
 => CACHED [api builder-image 4/9] RUN pip install nltk                                                                                                                 0.0s
 => CACHED [api builder-image 5/9] RUN python3 -m nltk.downloader punkt                                                                                                 0.0s
 => CACHED [api builder-image 6/9] RUN pip cache purge                                                                                                                  0.0s
 => ERROR [api builder-image 7/9] COPY api/requirements.txt .                                                                                                           0.0s
 => CACHED [api runner-image 2/7] RUN apt-get update && apt-get install -y --no-install-recommends     ffmpeg libavcodec-extra libopus0                                 0.0s
 => CACHED [api runner-image 3/7] RUN useradd --create-home docker                                                                                                      0.0s
 => CACHED [api builder-image 8/9] RUN pip install --no-cache-dir -r requirements.txt                                                                                   0.0s
 => CACHED [api builder-image 9/9] RUN pip install --no-cache-dir --force-reinstall numpy==1.26.4 pandas==2.2.2                                                         0.0s
 => CACHED [api runner-image 4/7] COPY --from=builder-image /usr/local /usr/local                                                                                       0.0s
 => CACHED [api runner-image 5/7] RUN mkdir /home/docker/app                                                                                                            0.0s
 => CACHED [api runner-image 6/7] WORKDIR /home/docker/app                                                                                                              0.0s
 => ERROR [api runner-image 7/7] COPY ./api/src /home/docker/app                                                                                                        0.0s
------
 > [api builder-image 7/9] COPY api/requirements.txt .:
------
------
 > [api runner-image 7/7] COPY ./api/src /home/docker/app:
------
failed to solve: failed to compute cache key: failed to calculate checksum of ref d2d47a88-b07d-466b-8ece-43836925ba61::uoc0pj9gxov0u2pnxawb3zkzz: "/api/src": not found
yaz@gpu:~/specific_job$ ls -R ~/specific_job/api
/home/yaz/specific_job/api:
dockerfile  Makefile  README.md  requirements.txt  src

/home/yaz/specific_job/api/src:
config  main.py  __pycache__  routes  schemas  services  static

/home/yaz/specific_job/api/src/config:
__init__.py  __pycache__  setting.py

/home/yaz/specific_job/api/src/config/__pycache__:
__init__.cpython-312.pyc  setting.cpython-312.pyc

/home/yaz/specific_job/api/src/__pycache__:
main.cpython-312.pyc

/home/yaz/specific_job/api/src/routes:
__init__.py  __pycache__  service.py  user.py

/home/yaz/specific_job/api/src/routes/__pycache__:
__init__.cpython-312.pyc  user.cpython-312.pyc

/home/yaz/specific_job/api/src/schemas:
error.py  __init__.py  __pycache__  user.py

/home/yaz/specific_job/api/src/schemas/__pycache__:
error.cpython-312.pyc  __init__.cpython-312.pyc  user.cpython-312.pyc

/home/yaz/specific_job/api/src/services:
__init__.py  main.py  __pycache__

/home/yaz/specific_job/api/src/services/__pycache__:
__init__.cpython-312.pyc  main.cpython-312.pyc

/home/yaz/specific_job/api/src/static:
job_data.csv
yaz@gpu:~/specific_job$ cd ~/specific_job
docker compose down  # Stop and remove any existing containers
docker compose up -d --build
WARN[0000] /home/yaz/specific_job/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] /home/yaz/specific_job/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
Compose can now delegate builds to bake for better performance.
 To do so, set COMPOSE_BAKE=true.
[+] Building 382.5s (21/21) FINISHED                                                                                                                          docker:default
 => [api internal] load build definition from dockerfile                                                                                                                0.0s
 => => transferring dockerfile: 986B                                                                                                                                    0.0s
 => [api internal] load metadata for docker.io/library/python:3.9-slim                                                                                                  1.0s
 => [api internal] load .dockerignore                                                                                                                                   0.0s
 => => transferring context: 2B                                                                                                                                         0.0s
 => [api internal] load build context                                                                                                                                   0.0s
 => => transferring context: 265.23kB                                                                                                                                   0.0s
 => [api builder-image 1/9] FROM docker.io/library/python:3.9-slim@sha256:bef8d69306a7905f55cd523f5604de1dde45bbf745ba896dbb89f6d15c727170                             14.3s
 => => resolve docker.io/library/python:3.9-slim@sha256:bef8d69306a7905f55cd523f5604de1dde45bbf745ba896dbb89f6d15c727170                                                0.0s
 => => sha256:d691b80d5159dfbcf2c1daad72a24c0fb9a55b6d90d6a11dcd46384ff1afa64d 3.51MB / 3.51MB                                                                          4.5s
 => => sha256:84b1a677eccc72224f1c1f6beece7da2221414861259d64d106a62d9b1f704e0 14.93MB / 14.93MB                                                                       13.6s
 => => sha256:fb95b45635cb4f373b9afdfb37bc513f1cc179ce6bd32904fb5570188eee2f29 249B / 249B                                                                              0.4s
 => => sha256:bef8d69306a7905f55cd523f5604de1dde45bbf745ba896dbb89f6d15c727170 10.41kB / 10.41kB                                                                        0.0s
 => => sha256:c8ecde0b63a4881272d794f7fcf2ba2ed4c0f7594c8d783905423e7e964ade28 1.75kB / 1.75kB                                                                          0.0s
 => => sha256:9a041530811d5397b63cb7255cdcdd27195706cf5faf81d77242cd01d7a68da8 5.29kB / 5.29kB                                                                          0.0s
 => => extracting sha256:d691b80d5159dfbcf2c1daad72a24c0fb9a55b6d90d6a11dcd46384ff1afa64d                                                                               0.2s
 => => extracting sha256:84b1a677eccc72224f1c1f6beece7da2221414861259d64d106a62d9b1f704e0                                                                               0.7s
 => => extracting sha256:fb95b45635cb4f373b9afdfb37bc513f1cc179ce6bd32904fb5570188eee2f29                                                                               0.0s
 => [api builder-image 2/9] RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     ffmpeg libavcodec-extra libopus0                 257.1s
 => [api runner-image 2/7] RUN apt-get update && apt-get install -y --no-install-recommends     ffmpeg libavcodec-extra libopus0                                      202.2s
 => [api runner-image 3/7] RUN useradd --create-home docker                                                                                                             0.2s
 => [api builder-image 3/9] RUN pip install --upgrade pip                                                                                                               5.5s
 => [api builder-image 4/9] RUN pip install nltk                                                                                                                        5.5s
 => [api builder-image 5/9] RUN python3 -m nltk.downloader punkt                                                                                                       10.1s
 => [api builder-image 6/9] COPY requirements.txt .                                                                                                                     0.0s
 => [api builder-image 7/9] RUN pip install --no-cache-dir -r requirements.txt                                                                                         48.0s
 => [api builder-image 8/9] RUN pip install --no-cache-dir --force-reinstall numpy==1.26.4 pandas==2.2.2                                                               33.8s
 => [api builder-image 9/9] RUN pip cache purge                                                                                                                         0.5s
 => [api runner-image 4/7] COPY --from=builder-image /usr/local /usr/local                                                                                              1.8s
 => [api runner-image 5/7] RUN mkdir /home/docker/app                                                                                                                   0.2s
 => [api runner-image 6/7] WORKDIR /home/docker/app                                                                                                                     0.0s
 => [api runner-image 7/7] COPY src /home/docker/app                                                                                                                    0.0s
 => [api] exporting to image                                                                                                                                            2.6s
 => => exporting layers                                                                                                                                                 2.6s
 => => writing image sha256:bc2cf340c2e73690a5c74fc1ddb640c09b991cdc88be8e419aeff85b38d782ba                                                                            0.0s
 => => naming to docker.io/library/specificjob-api                                                                                                                      0.0s
 => [api] resolving provenance for metadata file                                                                                                                        0.0s
[+] Running 3/3
 ✔ api                         Built                                                                                                                                    0.0s 
 ✔ Network spisficjob_default  Created                                                                                                                                  0.0s 
 ✔ Container spisficjob-api-1  Started                                                                                                                                  0.3s 
yaz@gpu:~/specific_job$ 

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
