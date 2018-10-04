import pickle
from tkinter import *


class Service:
    service_name = 'ASO Toyota'
    service_address = 'Milionowa 1'
    service_city = 'Lodz'

    def print_service(self):
        print('--Car service-- \n'
              'Name: {} \n'
              'Address: {} \n'
              'City: {} \n'
              .format(self.service_name, self.service_address, self.service_city))


class Station(Service):
    station_number = 1
    mechanic = 'Filip Waski'
    hours = 2.5

    def print_station(self):
        print('--Station-- \n'
              'Number: {} \n'
              'Mechanic: {} \n'
              'Time to finish repair: {} \n'
              .format(self.station_number, self.mechanic, self.hours))


class Parts(Station):
    parts_number = 1120
    parts_name = 'gear box'
    parts_price = 2550

    def print_parts(self):
        print('--Parts-- \n'
              'Number: {} \n'
              'Name: {} \n'
              'Price: {} \n'
              .format(self.parts_number, self.parts_name, self.parts_price))


class Car(Parts):
    model = 'Toyota Yaris'
    year = 2010
    mileage = 125000

    def print_car(self):
        print('--Car-- \n'
              'Model: {} \n'
              'Year {} \n'
              'Mileage: {} \n'
              .format(self.model, self.year, self.mileage))


class Customer(Car):
    name = 'Filip Waski'
    address = 'Slaska 12'
    city = 'Lodz'
    telephone = 660600600

    def print_customer(self):
        print('--Customer-- \n'
              'Name: {} \n'
              'Address: {} \n'
              'City: {} \n'
              'Telephone number: {} \n'
              .format(self.name, self.address, self.city, self.telephone))


client1 = Customer()
client1.print_service()
client1.print_customer()
client1.print_car()
client1.print_station()
client1.print_parts()

client2 = Customer()
client2.service_name = 'Jaspol'
client2.service_address = 'Pilsudskiego 2'
client2.service_city = 'Lodz'
client2.print_service()
client2.name = 'Adam Slim'
client2.address = 'Tatrzanska 1'
client2.city = 'Lodz'
client2.telephone = 890123456
client2.print_customer()
client2.model = 'Opel Insignia'
client2.year = 2011
client2.mileage = 160500
client2.print_car()
client2.station_number = 2
client2.mechanic = 'Lech Krzywy'
client2.hours = 2.0
client2.print_station()
client2.parts_number = 5560
client2.parts_name = 'exhaust'
client2.parts_price = 5000
client2.print_parts()

client3 = Customer()
client3.service_name = 'ACS'
client3.service_address = 'Gdanska 22'
client3.service_city = 'Lodz'
client3.print_service()
client3.name = 'Krzysztof Cieslik'
client3.address = 'Gromska 1'
client3.city = 'Lodz'
client3.telephone = 555666789
client3.print_customer()
client3.model = 'BMW M3'
client3.year = 2018
client3.mileage = 50
client3.print_car()
client3.station_number = 1
client3.mechanic = 'Wojciech Prosty'
client3.hours = 1.0
client3.print_station()
client3.parts_number = 'fsa45'
client3.parts_name = 'tires'
client3.parts_price = 3000
client3.print_parts()

lists_clients = [client1, client2, client3]

bin_file = open('pickle.bin', 'wb')
dump = pickle.dump(lists_clients, bin_file)
bin_file.close()

print('New:')
lists_clients_2 = pickle.load(open('pickle.bin', 'rb'))
for i in lists_clients_2:
    i.print_customer()


def new_button():
    done = Toplevel(top)
    button = Button(done, text='Done')
    button.pack()


top = Tk()

menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New', command=new_button)
filemenu.add_command(label='Open', command=new_button)
filemenu.add_command(label='Save', command=new_button)
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Help')

top.config(menu=menubar)
top.mainloop()
