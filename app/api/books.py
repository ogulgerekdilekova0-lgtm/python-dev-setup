from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookOut
router = APIRouter(prefix="/books", tags=["books"])
@router.get("/", response_model=list[BookOut])
def read_books(category_id: Optional[int] = Query(None), db: Session = Depends(get_db)):
    return crud.get_books(db, category_id)
@router.get("/{book_id}", response_model=BookOut)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
@router.post("/", response_model=BookOut, status_code=201)
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, data.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.create_book(
        db,
        data.title,
        data.description,
        data.price,
        data.category_id,
        data.url,
    )
@router.put("/{book_id}", response_model=BookOut)
def update_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):
    category = crud.get_category(db, data.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    book = crud.update_book(
        db,
        book_id,
        data.title,
        data.description,
        data.price,
        data.category_id,
        data.url,
    )
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
@router.delete("/{book_id}", response_model=BookOut)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book