class User:
    def __init__ (self, first_name, last_name, full_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name +" "+ last_name
        
    def sayFirstName (self):
           print("Меня зовут:", self.first_name)
               
    def sayLastName(self):
         print("Моя фамилия:", self.last_name)
    def sayfull_name (self):
         print("Мое полное имя:", self.full_name)

user = User ("Egor", "Petrov", "Egor Petrov")
user.sayFirstName()
user.sayLastName()
user.sayfull_name()
