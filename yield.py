import time


def monday():
    return "Dushanba"


def tuesday():
    return "Seshanba"


def wednesday():
    return "Chorshanba"


def thursday():
    return "Payshanba"


def friday():
    return "Juma"


def saturday():
    return "Shanba"


def sunday():
    return "Yakshanba"


def weeks():
    print("Hafta kunlari yield orqali chiqarildi")
    time.sleep(0.7)
    yield monday()
    time.sleep(0.7)
    yield tuesday()
    time.sleep(0.7)
    yield wednesday()
    time.sleep(0.7)
    yield thursday()
    time.sleep(0.7)
    yield friday()
    time.sleep(0.7)
    yield saturday()
    time.sleep(0.7)
    yield sunday()


for i in weeks():
    print(i)
