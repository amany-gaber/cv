from fastapi import APIRouter, UploadFile, File, HTTPException
from services import CVMatcher

router = APIRouter(
    prefix="/cv",
    tags=["CV Matching"]
)

cv_matcher = CVMatcher()

@router.post("/inference")
async def match_cv(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx", ".txt")):  # Support all file types CVMatcher can handle
        raise HTTPException(status_code=400, detail="Only PDF, DOCX, and TXT files are supported.")

    try:
        result = cv_matcher.process_cv(file)  # Call process_cv instead of run_inference
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))