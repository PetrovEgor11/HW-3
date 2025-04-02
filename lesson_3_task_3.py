from Mailing import Mailing
from Adress import Address

        # self.to_address=to_address
        # self.from_address=from_address
        # self.cost=cost
        # self.track=track
def say_to_address (self):
    print ("Обращаться к", self.to_address)
def say_from_address (self):
    print ("С адреса", self.from_address)
def say_cost (self):
    print ("Дом", self.cost)
def say_track (self):
    print ("Стоимость", self.track)

    # Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.
departure = Mailing ("Egor","Moscow", "26", "750")
departure.say_to_address()
departure.say_from_address()
departure.say_cost ()
departure.say_track ()