class OfficeEquipment:

    def get_type(self):
        pass


class Printer(OfficeEquipment):

    def get_type(self):
        return 'printer'


class Scaner(OfficeEquipment):

    def get_type(self):
        return 'scaner'

class Xerox(OfficeEquipment):

    def get_type(self):
        return 'xerox'

class Store:

    def __init__(self):
        self.equipment = {}

    def add_equipment (self, my_equipment):
        name = my_equipment.get_type()
        if not name in self.equipment:
            self.equipment[name] = 0
        self.equipment[name] += 1

    def remove_equipment(self, my_equipment):
        name = my_equipment.get_type()
        if self.equipment.get(name, 0) == 0:
            a = f'This {name} is not found'
            print(a)
            return False
        else:
            self.equipment[name] -= 1
            return True

class People:

    def __init__(self, name):
         self.name = name

class ClerkFromSthDepartment(People):

    def __init__(self, name, storekeeper):
        super(ClerkFromSthDepartment, self).__init__(name)
        self.equipment = {}
        self.storekeeper = storekeeper

    def get_eq(self, my_equipment):
        self.storekeeper.get_eq(self, my_equipment)


class Provider(People):

    def __init__(self, name, storekeeper):
        super(Provider, self).__init__(name)
        self.storekeeper = storekeeper

    def throw_on_store(self, m_eq):
        self.storekeeper.give_eq(m_eq)

class Storekeeper(People):

    def __init__(self, name, store):
        super(Storekeeper, self).__init__(name)
        self.store = store

    def get_eq(self, clerk, my_equipment):
        if not clerk.equipment.get(my_equipment.get_type(),False):
            if self.store.remove_equipment(my_equipment):
                clerk.equipment[my_equipment.get_type()] = True
                print (f'{clerk.name} взял у {self.name} {my_equipment.get_type()}')
        else:
            print((f'{clerk.name} не взял {self.name} {my_equipment.get_type()}'))

    def give_eq(self, my_equipment):
        self.store.add_equipment(my_equipment)


store = Store()
storekeeper = Storekeeper('Antosha', store)
provider = Provider('Vitusha', storekeeper)
clerk = ClerkFromSthDepartment('Ilusha', storekeeper)
provider.throw_on_store(Printer())
provider.throw_on_store(Scaner())
provider.throw_on_store(Scaner())
provider.throw_on_store(Xerox())
provider.throw_on_store(Xerox())
provider.throw_on_store(Xerox())
clerk.get_eq(Xerox())
clerk.get_eq(Printer())
clerk.get_eq(Printer())
clerk.get_eq(Scaner())
