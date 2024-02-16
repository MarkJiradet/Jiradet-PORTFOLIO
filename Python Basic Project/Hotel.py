class Room:
    def __init__(self, room_number, room_type, price, is_reserved):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_reserved = is_reserved

def add_room(rooms, room):
    rooms.append(room)

def reserve_room(room):
    if not room.is_reserved:
        room.is_reserved = True
        return True
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

def main():
    rooms = []
    filename = 'rooms.csv'

    try:
        rooms = load_from_csv(filename)
    except FileNotFoundError:
        pass

    while True:
        print("\n1. Add Room")
        print("2. Reserve Room")
        print("3. Display Rooms")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            room_number = input("Enter room number: ")
            room_type = input("Enter room type: ")
            price = float(input("Enter price: "))
            room = Room(room_number, room_type, price, False)
            add_room(rooms, room)
            print("Room added successfully.")

        elif choice == '2':
            room_number = input("Enter room number to reserve: ")
            for room in rooms:
                if room.room_number == room_number:
                    if reserve_room(room):
                        print("Room reserved successfully.")
                    else:
                        print("Room is already reserved.")
                    break
            else:
                print("Room not found.")

        elif choice == '3':
            selection_sort(rooms)
            display_rooms(rooms)

        elif choice == '4':
            save_to_csv(rooms, filename)
            print("Data saved. Exiting...")
            break

if __name__ == "__main__":
    main()
