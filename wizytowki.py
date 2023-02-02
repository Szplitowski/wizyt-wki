from faker import Faker

fake = Faker()
fake_people = []

people = [
    (
        "Amadeusz",
        "Chmielewski",
        "Red Food",
        "Installer",
        "Chmielewski@armyspy.com",
        "111111",
        "011110",
    ),
    (
        "Weronika",
        "Wieczorek",
        "Endicott Shoes",
        "Editor",
        "Wieczorek@armyspy.com",
        "222222",
        "022220",
    ),
    (
        "Wojtek",
        "Rutkowski",
        "Klopfensteins",
        "Specialist",
        "Rutkowski@teleworm.us",
        "333333",
        "033330",
    ),
    (
        "Maksymilian",
        "Zielinski",
        "Korvette",
        "Worker",
        "Zielinski@teleworm.us",
        "444444",
        "044440",
    ),
]


class BaseContact:
    def __init__(
        self, first_name, last_name, company, position, email, number, profnumber
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email
        self.number = number
        self.profnumber = profnumber

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    def contact(self):
        print(f"Kontaktuję się z {self.first_name} {self.last_name}, {self.email}")

    @property
    def contact_length(self):
        self._contact_length = len(self.first_name + self.last_name) + 1
        print(
            f"Imię i nazwisko ze wskazanej wzizytkówki ma {self._contact_length} znaków (włączając spację)"
        )
        return self._contact_length


class BusinessContact(BaseContact):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.position} {self.company} {self.profnumber}"

    def __repr__(self):
        return f"{self.position} {self.company} {self.profnumber}"

    def contact_prof(self):
        print(f"Kontaktuję się z {self.first_name} {self.last_name}, {self.profnumber}")

    @property
    def contact_length(self):
        self._contact_length = len(self.first_name + self.last_name) + 1
        print(
            f"Imię i nazwisko ze wskazanej wzizytkówki ma {self._contact_length} znaków (włączając spację)"
        )
        return self._contact_length


def create_contacts():
    ile = input("Podaj liczbe wizytówek do stworzenia:  ")

    for i in range(0, int(ile)):
        fake_people.append(
            (
                fake.first_name(),
                fake.last_name(),
                fake.company(),
                fake.job(),
                fake.email(),
                fake.phone_number(),
                fake.phone_number(),
            )
        )
        pass
    print(fake_people)


# create_contacts()

cards = [BaseContact(*person) for person in people]
cards_prof = [BusinessContact(*person) for person in people]


# for card in cards:
#   print(f"{card.first_name} {card.last_name}, {card.email}")
#   print("-" * 60)


# by_name = sorted(cards, key=lambda BaseContact: BaseContact.first_name)
# by_lastname = sorted(cards, key=lambda BaseContact: BaseContact.last_name)
# by_email = sorted(cards, key=lambda BaseContact: BaseContact.email)


# cards[0].contact()
# cards[0].contact_length

# cards_prof[0].contact_prof()
# cards_prof[0].contact_length
