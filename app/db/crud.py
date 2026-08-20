from .models import Category, Book
  # Categories CRUD
def create_category(db, title: str):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category
def get_categories(db):
    return db.query(Category).all()
def update_category(db, category_id: int, new_title: str):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        category.title = new_title
        db.commit()
        db.refresh(category)
    return category
def delete_category(db, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
    return category
# Books CRUD
def create_book(db, title: str, description: str, price: float, category_id: int, url: str = ""):
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book
def get_books(db):
    return db.query(Book).all()
def update_book_price(db, book_id: int, new_price: float):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.price = new_price
        db.commit()
        db.refresh(book)
    return book
def delete_book(db, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book