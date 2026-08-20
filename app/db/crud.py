from .models import Category, Book
  # Categories
def create_category(db, title: str):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category
def get_categories(db):
    return db.query(Category).all()
def get_category(db, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()
def update_category(db, category_id: int, new_title: str):
    category = get_category(db, category_id)
    if category:
        category.title = new_title
        db.commit()
        db.refresh(category)
    return category
def delete_category(db, category_id: int):
    category = get_category(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category
# Books
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
def get_books(db, category_id: int = None):
    query = db.query(Book)
    if category_id is not None:
        query = query.filter(Book.category_id == category_id)
    return query.all()
def get_book(db, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()
def update_book(db, book_id: int, title: str, description: str, price: float, category_id: int, url: str = ""):
    book = get_book(db, book_id)
    if book:
        book.title = title
        book.description = description
        book.price = price
        book.category_id = category_id
        book.url = url
        db.commit()
        db.refresh(book)
    return book
def delete_book(db, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book