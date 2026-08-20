from db.db import Base, engine, SessionLocal
from db.crud import create_category, create_book
Base.metadata.create_all(bind=engine)
db = SessionLocal()
cat1 = create_category(db, "Programming")
cat2 = create_category(db, "Databases")
create_book(db, "Python Basics", "Intro to Python", 19.99, cat1.id)
create_book(db, "Advanced Python", "Deep dive into Python", 29.99, cat1.id)
create_book(db, "PostgreSQL 101", "Beginner PostgreSQL guide", 24.50, cat2.id)
create_book(db, "SQLAlchemy Guide", "ORM in practice", 27.00, cat2.id)
db.close()
print("Database initialized with categories and books.")