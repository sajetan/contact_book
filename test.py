from project.tables import db, Contact
from faker import Factory

def test_contact():
    print("creating dummy contacts")
    fake = Factory.create()
    db.drop_all()
    db.create_all()
    # Make 100 fake contacts
    for num in range(1000):
        fullname = fake.name().split()
        name = fullname[0]
        surname = ' '.join(fullname[1:])
        email = fake.email()
        phone = fake.phone_number()
        # Save in database
        contact_data = Contact(name=name, surname=surname, email=email, phone=phone)
        db.session.add(contact_data)
    try:
        db.session.commit()
    except:
        print("Error creating db - please run the file again")
        db.session.rollback()


if __name__ == '__main__':
    test_contact()
