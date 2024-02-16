# Import ไลบรารี csv
import csv

# ฟังก์ชันสำหรับเพิ่มห้อง
def add_room(rooms, room_number, room_type, price):
    for room in rooms:
        if room['room_number'] == room_number:
            return False
    rooms.append({'room_number': room_number, 'room_type': room_type, 'price': price})
    return True

# ฟังก์ชันสำหรับจองห้อง
def book_room(rooms, room_number):
    for room in rooms:
        if room['room_number'] == room_number:
            if not room.get('reserved', False):
                room['reserved'] = True
                return True
            else:
                return False
    return False

# ฟังก์ชันสำหรับยกเลิกการจองห้อง
def cancel_booking(rooms, room_number):
    for room in rooms:
        if room['room_number'] == room_number and room.get('reserved', False):
            room['reserved'] = False
            return True
    return False

# ฟังก์ชันสำหรับแก้ไขข้อมูลห้อง
def edit_room(rooms, room_number, new_room_type, new_price):
    for room in rooms:
        if room['room_number'] == room_number:
            room['room_type'] = new_room_type
            room['price'] = new_price
            return True
    return False

# ฟังก์ชันสำหรับลบห้อง
def delete_room(rooms, room_number):
    for room in rooms:
        if room['room_number'] == room_number:
            rooms.remove(room)
            return True
    return False

# ฟังก์ชันสำหรับแสดงข้อมูลห้อง
def display_rooms(rooms, show_option):
    if show_option == "1":
        rooms_to_display = rooms
    elif show_option == "2":
        rooms_to_display = [room for room in rooms if not room.get('reserved', False)]
    elif show_option == "3":
        rooms_to_display = [room for room in rooms if room.get('reserved', True)]
    elif show_option == "4":
        search_room_number = int(input("กรุณาป้อนเลขห้องที่ต้องการค้นหา: "))
        rooms_to_display = [room for room in rooms if room['room_number'] == search_room_number]
        
    if not rooms_to_display:
        print("ไม่มีห้องที่ต้องการแสดงผล")
        return

    sorted_rooms = selection_sort(rooms_to_display)
    for room in sorted_rooms:
        print(f"ห้องเลขที่: {room['room_number']}, ประเภทห้อง: {room['room_type']}, ราคา: {room['price']}, สถานะ: {'จองแล้ว' if room.get('reserved', False) else 'ว่าง'}")

# ฟังก์ชันสำหรับค้นหาห้องตามประเภทห้อง
def search_by_type(rooms, room_type):
    found_rooms = [room for room in rooms if room['room_type'] == room_type]
    if not found_rooms:
        print("ไม่พบห้องที่ต้องการค้นหา")
        return
    
    print("รูปแบบการแสดงผล")
    print("1. แสดงห้องทั้งหมด")
    print("2. แสดงห้องที่ยังไม่มีคนจอง")
    print("3. แสดงห้องที่มีคนจองแล้ว")
    show_option = input("กรุณาเลือกรูปแบบการแสดงผล : ")
    if show_option in ["1","2","3"]:
        display_rooms(found_rooms,show_option)
    else:
        print("ท่านเลือกไม่ถูกต้องกรุณาเลือกแค่ 1,2,3")
        
# ฟังก์ชันสำหรับการจัดเรียงห้องด้วย Selection Sort
def selection_sort(rooms):
    n = len(rooms)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if rooms[j]['room_number'] < rooms[min_idx]['room_number']:
                min_idx = j
        rooms[i], rooms[min_idx] = rooms[min_idx], rooms[i]
    return rooms

# ฟังก์ชันสำหรับบันทึกข้อมูลห้องลงในไฟล์ CSV
def save_to_csv(rooms, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ห้องเลขที่", "ประเภทห้อง", "ราคา", "สถานะ"])
        for room in rooms:
            writer.writerow([room['room_number'], room['room_type'], room['price'], 'จองแล้ว' if room.get('reserved', False) else 'ว่าง'])

# ฟังก์ชันสำหรับโหลดข้อมูลห้องจากไฟล์ CSV
def load_from_csv(filename):
    rooms = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                for row in reader:
                    room_number, room_type, price, status = row
                    rooms.append({'room_number': int(room_number), 'room_type': room_type, 'price': float(price), 'reserved': status == 'จองแล้ว'})
    except FileNotFoundError:
        pass
    return rooms

# โปรแกรมหลัก
def main():
    filename = 'hotel_rooms.csv'
    rooms = load_from_csv(filename)

    while True:
        print("\n===== โปรแกรมจัดการข้อมูลการจองห้องพักโรงแรม =====")
        print("1. เพิ่มห้อง")
        print("2. จองห้อง")
        print("3. ยกเลิกการจองห้อง")
        print("4. แก้ไขข้อมูลห้อง")
        print("5. ลบห้อง")
        print("6. แสดงผลห้อง")
        print("7. ค้นหาห้องตามประเภท")
        print("8. บันทึกข้อมูล")
        print("9. ออกจากโปรแกรม")

        choice = input("กรุณาเลือกทำรายการ: ")

        if choice == '1':
            room_number = int(input("เลขห้อง: "))
            room_type = input("ประเภทห้อง: ")
            price = float(input("ราคา: "))
            if add_room(rooms, room_number, room_type, price):
                print("เพิ่มห้องสำเร็จ")
            else:
                print("ไม่สามารถเพิ่มห้องได้ (เลขห้องซ้ำ)")

        elif choice == '2':
            room_number = int(input("เลขห้องที่ต้องการจอง: "))
            if book_room(rooms, room_number):
                print("จองห้องสำเร็จ")
            else:
                print("ไม่สามารถจองห้องได้ (ห้องไม่ว่างหรือมีคนจองแล้ว)")

        elif choice == '3':
            room_number = int(input("เลขห้องที่ต้องการยกเลิกการจอง: "))
            if cancel_booking(rooms, room_number):
                print("ยกเลิกการจองสำเร็จ")
            else:
                print("ไม่สามารถยกเลิกการจองได้ (ห้องนี้ยังไม่ถูกจอง)")

        elif choice == '4':
            room_number = int(input("เลขห้องที่ต้องการแก้ไข: "))
            found_room = None
            for room in rooms:
                if room['room_number'] == room_number:
                    found_room = room
                    break

            if found_room:
                new_room_type = input("ประเภทห้องใหม่: ")
                new_price = float(input("ราคาใหม่: "))
                edit_room(rooms, room_number, new_room_type, new_price)
                print("แก้ไขข้อมูลห้องสำเร็จ")
            else:
                print("ไม่พบห้องที่ต้องการแก้ไข")

        elif choice == '5':
            room_number = int(input("เลขห้องที่ต้องการลบ: "))
            if delete_room(rooms, room_number):
                print("ลบห้องสำเร็จ")
            else:
                print("ไม่พบห้องที่ต้องการลบ")
                
        elif choice == '6':
            print("รูปแบบการแสดงผล")
            print("1. แสดงห้องทั้งหมด")
            print("2. แสดงห้องที่ยังไม่มีคนจอง")
            print("3. แสดงห้องที่มีคนจองแล้ว")
            print("4. แสดงผลเฉพาะเลขห้องที่ต้องการ")
            show_option = input("กรุณาเลือกรูปแบบการแสดงผล : ")
            if show_option in ["1","2","3","4"]:
                display_rooms(rooms,show_option)
            else:
                print("ท่านเลือกไม่ถูกต้องกรุณาเลือกแค่ 1,2,3")
                
        elif choice == '7':
            room_type = input("ประเภทห้องที่ต้องการค้นหา: ")
            search_by_type(rooms, room_type)

        elif choice == '8':
            save_to_csv(rooms, filename)
            print("บันทึกข้อมูลสำเร็จ")

        elif choice == '9':
            print("ออกจากโปรแกรม")
            break

        else:
            print("กรุณาเลือกทำรายการใหม่")

if __name__ == "__main__":
    main()