from faker import Faker

fake = Faker("ru_RU")

print("Сгенерированные пользователи:\n")

for i in range(1, 6):
    print(f"Пользователь №{i}")
    print("  Имя:     ", fake.name())
    print("  Email:   ", fake.email())
    print("  Телефон: ", fake.phone_number())
    print("  Адрес:   ", fake.address())
    print()

