import factory
from faker import Faker

fake = Faker()


class CriaUsuarioNovo(factory.Factory):
    class Meta:
        model = dict

    name = factory.LazyAttribute(lambda _: fake.name())
    username = factory.LazyAttribute(lambda _: fake.user_name())
    email = factory.LazyAttribute(lambda _: fake.email())
    address = factory.Dict({
        "street": fake.street_name(),
        "suite": f"Apt. {fake.building_number()}",
        "city": fake.city(),
        "zipcode": fake.zipcode(),
        "geo": {
            "lat": str(fake.latitude()),
            "lng": str(fake.longitude())
        }
    })
    phone = factory.LazyAttribute(lambda _: fake.phone_number())
    website = factory.LazyAttribute(lambda _: fake.url())
    company = factory.Dict({
        "name": fake.company(),
        "catchPhrase": fake.catch_phrase(),
        "bs": fake.bs()
    })

    @classmethod
    def cria_usuario_invalido(cls):
        return cls(
            name=2456,
            username="123",
            email="email-invalido",
            address={
                "street": "",
                "suite": "aleatorio",
                "city": fake.city(),
                "zipcode": "123",
                "geo": {
                    "lat": str(fake.latitude()),
                    "lng": str(fake.longitude())
                }
            },
            phone="phone-invalido",
            website="url-invalido",
            company={
                "name":"",
                "catchPhrase": fake.catch_phrase(),
                "bs": fake.bs()
            }
        )
