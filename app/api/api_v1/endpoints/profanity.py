from fastapi import APIRouter, Body, Depends, HTTPException

from app.utils import DFAFilter, NaiveFilter

router = APIRouter()

@router.get("/")
def profanity(text: str):
    "Return True if there are any profanity words"
    filter = NaiveFilter()
    filter.parse('/home/conrad/creator/bad_words.txt')
    if '*' in filter.filter(text):
        return True
    else:
        return False