from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
print("🌱 Seeding DB...")

engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()

users = [
    User(username="BugsBunnyFanatic"),
    User(username="WackyDaffy91"),
    User(username="TazmanianTornado22"),
    User(username="SylvesterSneakyCat"),
    User(username="RoadRunnerSpeedster"),
]

session.bulk_save_objects(users)
session.commit()

print("✅ Done seeding!")


