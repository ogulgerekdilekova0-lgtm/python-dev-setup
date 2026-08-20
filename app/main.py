from db.db import SessionLocal
from db.crud import get_categories, get_books
db = SessionLocal()
print("Categories:")
for c in get_categories(db):
    print(f"- {c.id}: {c.title}")
print("\nBooks:")
for b in get_books(db):
    print(f"- {b.id}: {b.title} | {b.price} | category_id={b.category_id}")
db.close()