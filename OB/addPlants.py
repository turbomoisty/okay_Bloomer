from OB import create_site, db
from OB.models import plantType

app = create_site()
# Add plants to the plant type class. Don't forget to remove any existing elements, otherwise you are
#going to get duplicates
with app.app_context():
    plant_types = ['Cactus', 'Fern', 'Bonsai', 'Succulent', 'Orchid']

    for type_name in plant_types:
        plant_type = plantType(typeName=type_name)
        db.session.add(plant_type)

    db.session.commit()
    print("Plant types added successfully!")
