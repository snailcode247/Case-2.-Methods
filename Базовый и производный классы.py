class Pet: #базовый класс

    def __init__(self, species, name): #конструктор базового класса
        self.species = species #инициализация  атрибутов: вид и имя
        self.name = name

    def eating(self): #метод для состояния "ест"
        return f"{self.species} {self.name} ест."

    def sleeping(self): #метод для состояния "спит"
        return f"{self.species} {self.name} спит."

class DefinedPet(Pet): #производный класс

    def __init__(self, species, name, color): #конструктор производного класса
        super().__init__(species,name)  #вызов конструктора базового класса для инициализации общих атрибутов
        self.color = color #инициализация нового атрибута color - цвет

    def playing(self, toy): #уникальный метод производного класса
        return f"{self.color} {self.species} {self.name} игрет с {toy}!"

    def sleeping(self): #переопределние метода sleeping
        return f"{self.color} {self.species} {self.name} громко храпит"

#точка входа в программу
if __name__ == "__main__":
    pet = Pet("питомец", "неизвестный") #создаём объект базового класса
    #вызываем его методы
    print(pet.eating()) #должно быть питомец неизвестный ест.
    print(pet.sleeping()) #должно быть питомец неизвестный спит.

    cat = DefinedPet("кот", "Василий", "чёрный") #создаём объект производного класса DefinedPet
    #вызываем переопределённый метод sleeping
    print(cat.sleeping()) #должно быть "чёрный кот василий громко храпит"
    #вызываем наследованный метод eating
    print(cat.eating()) #должно быть "чёрный кот василий ест"
    #вызываем уникальный метод playing
    print(cat.playing("резиночка")) #должно быть чёрный кот василий играет с резиночка

    input()