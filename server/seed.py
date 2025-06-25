from server.app import app, db
from server.models.guest import Guest
from server.models.episode import Episode

with app.app_context():
    db.drop_all()
    db.create_all()

    g1 = Guest(name="Trevor Noah", occupation="Comedian")
    g2 = Guest(name="Serena Williams", occupation="Tennis Player")

    e1 = Episode(date="2023-01-01", number=1)
    e2 = Episode(date="2023-01-08", number=2)

    db.session.add_all([g1, g2, e1, e2])
    db.session.commit()
