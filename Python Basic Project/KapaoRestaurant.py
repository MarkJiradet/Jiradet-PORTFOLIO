print("*"*110)
print("\t\t\t\t\t  ร้านกะเพราโบราณ")
print("*"*110)
print("1.กะเพราหมูสับ(50 บาท)   2.กะเพราหมูกรอบ(60 บาท)   3.กะเพราทะเล(70 บาท)   4.เครื่องดื่มโค้ก(25 บาท)   5.สิ้นสุดการสั่งซื้อ")
print("*"*110)
print("\t\t\t\t  ### โปรโมชั่นรับหน้าร้อน ###")
print("\t\t1.เมื่อซื้ออาหารครบ 200 บาท แถมฟรีนํ้าเก๊กฮวย 1 ขวด")
print("\t\t2.เมื่อซื้อกะเพราหมูสับ 3 กล่องขึ้นไปแถมฟรี กะเพราหมูสับ 1 กล่อง")
print("*"*110)

while True:
    menu_order = [0,0,0,0]
    total_price = 0
    
    while True:
        menu_select = int(input("กรุณาเลือกรายการ (1-5) : "))
        if menu_select==1:
            quantity = int(input("กรุณากรอกจำนวนกล่อง : "))
            menu_order[0] = quantity + menu_order[0]
        elif menu_select==2:
            quantity = int(input("กรุณากรอกจำนวนกล่อง : "))
            menu_order[1] = quantity + menu_order[1]
        elif menu_select==3:
            quantity = int(input("กรุณากรอกจำนวนกล่อง : "))
            menu_order[2] = quantity + menu_order[2]
        elif menu_select==4:
            quantity = int(input("กรุณากรอกจำนวนกล่อง : "))
            menu_order[3] = quantity + menu_order[3]
        elif menu_select==5:
            print("เลือกสินค้าเสร็จเรียบร้อย")
            break

    total_price = menu_order[0]*50 +  menu_order[1]*60 +  menu_order[2]*70 +  menu_order[3]*25
    print("\n-----------------------------------------------")
    print("\t\tร้านกะเพราโบราณ\n")
    if menu_order[0]!=0:
        print("กะเพราหมูสับ\t50.00 x {p} = {price:.2f} บาท".format(p = menu_order[0],price = menu_order[0]*50))
    if menu_order[1]!=0:
        print("กะเพราหมูกรอบ\t60.00 x {p} = {price:.2f} บาท".format(p = menu_order[1],price = menu_order[1]*60))
    if menu_order[2]!=0:
        print("กะเพราทะเล\t70.00 x {p} = {price:.2f} บาท".format(p = menu_order[2],price = menu_order[2]*70))
    if menu_order[3]!=0:
        print("เครื่องดิ่มโค้ก\t25.00 x {p} = {price:.2f} บาท".format(p = menu_order[3],price = menu_order[3]*25))
    if total_price>=200:
        print("แถมฟรีนํ้าเก๊กฮวย 1 ขวด")
    if menu_order[0]>=3:
        print("แถมฟรีกะเพราหมูสับ 1 กล่อง")
    print("-----------------------------------------------")
    print("ภาษีมูลค่าเพิ่ม 7% = {vat:.2f} บาท".format(vat = total_price*0.07))
    print("รวมเป็นเงิน = {total:.2f} บาท".format(total = (total_price*0.07)+total_price))
    print("-----------------------------------------------")
    
    choose = input("ต้องการทำรายการอีกครั้งหรือไม่ (ใช่/ไม่) :")
    if choose == "ไม่":
        break
    print("\n")
    
print("\nขอบคุณที่ใช้บริการ")