class Room:
    def __init__(self, room_number, room_type, price, is_reserved):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_reserved = is_reserved

def add_room(rooms, room):
    rooms.append(room)

def reserve_room(rooms, room_number):
    for room in rooms:
        if room.room_number == room_number:
            if not room.is_reserved:
                room.is_reserved = True
                return True
            else:
                return False
    return False

def display_rooms(rooms):
    for room in rooms:
        print(f"Room {room.room_number}: {room.room_type}, Price: {room.price}, Reserved: {room.is_reserved}")

def selection_sort(rooms):
    n = len(rooms)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if rooms[j].room_number < rooms[min_index].room_number:
                min_index = j
        rooms[i], rooms[min_index] = rooms[min_index], rooms[i]

def save_to_csv(rooms, filename):
    with open(filename, 'w') as file:
        for room in rooms:
            file.write(f"{room.room_number},{room.room_type},{room.price},{room.is_reserved}\n")

def load_from_csv(filename):
    rooms = []
    with open(filename, 'r') as file:
        for line in file:
            room_data = line.strip().split(',')
            room = Room(room_data[0], room_data[1], float(room_data[2]), bool(room_data[3]))
            rooms.append(room)
    return rooms

def display_reserved_rooms(rooms):
    print("\nReserved Rooms:")
    for room in rooms:
        if room.is_reserved:
            print(f"Room {room.room_number}: {room.room_type}, Price: {room.price}")

def display_available_rooms(rooms):
    print("\nAvailable Rooms:")
    for room in rooms:
        if not room.is_reserved:
            print(f"Room {room.room_number}: {room.room_type}, Price: {room.price}")
            
def is_room_number_unique(rooms, room_number):
    for room in rooms:
        if room.room_number == room_number:
            return False
    return True

def cancel_reservation(rooms, room_number):
    for room in rooms:
        if room.room_number == room_number:
            if room.is_reserved:
                room.is_reserved = False
                return True
            else:
                return False
    return False

def main():
    rooms = []
    filename = 'room.csv'

    try:
        rooms = load_from_csv(filename)
    except FileNotFoundError:
        pass

    while True:
        print("\n1. Add Room")
        print("2. Reserve Room")
        print("3. Cancel Reservation")
        print("4. Display All Rooms")
        print("5. Display Available Rooms")
        print("6. Display Reserved Rooms")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            room_number = int(input("Enter room number: "))
            if is_room_number_unique(rooms, room_number):
                room_type = input("Enter room type: ")
                price = float(input("Enter price: "))
                room = Room(room_number, room_type, price, False)
                add_room(rooms, room)
                print("Room added successfully.")
            else:
                print("Room number already exists. Cannot add room.")

        elif choice == '2':
            room_number = int(input("Enter room number to reserve: "))
            if reserve_room(rooms, room_number):
                print("Room reserved successfully.")
            else:
                print("Room not found or already reserved.")

        elif choice == '3':
            room_number = int(input("Enter room number to cancel reservation: "))
            if cancel_reservation(rooms, room_number):
                print("Reservation canceled successfully.")
            else:
                print("Room not found or not reserved.")

        elif choice == '4':
            selection_sort(rooms)
            display_rooms(rooms)

        elif choice == '5':
            selection_sort(rooms)
            display_available_rooms(rooms)
            
        elif choice == '6':
            selection_sort(rooms)
            display_reserved_rooms(rooms)

        elif choice == '7':
            save_to_csv(rooms, filename)
            print("Data saved. Exiting...")
            break
        
        print("\n================================================")

if __name__ == "__main__":
    main()