print("="*40)
print("\t  ร้าน Beautiful Salon")
print("\t\tยินดีต้อนรับ")
print("="*40)
print("ช่วงเวลาที่ร้านเปิดให้บริการ")
print("- จันทร์-ศุกร์ 10:00-19:00 น.")
print("- เสาร์-อาทิตย์ 09:00-21:00 น.")
print("="*40)

name = input("กรุณากรอกชื่อ-นามสกุล : ")
phoneNumber = input("กรุณากรอกเบอร์โทรศัพท์ : ")
email = input("กรุณากรอกอีเมลล์ : ")
otherContact = input("กรุณากรอกช่องทางติดต่ออื่นๆเช่น line,facebook : ")
print()

time = ''
date = ''

print("\nวันสำหรับลูกค้าที่ต้องการจองคิวล่วงหน้า")
print("[1]วันจันทร์ , [2]วันอังคาร , [3]วันพุธ")
print("[4]วันพฤหัสบดี , [5]วันศุกร์ , [6]วันเสาร์")
print("[7]วันอาทิตย์")

while(True):
  date = input("กรุณาระบุวันที่ต้องการจองคิว (1-7) : ")
  if date=="1":
    date = "วันจันทร์"
    break
  elif date=="2":
    date = "วันอังคาร"
    break
  elif date=="3":
    date = "วันพุธ"
    break
  elif date=="4":
    date = "วันพฤหัสบดี"
    break
  elif date=="5":
    date = "วันศุกร์"
    break
  elif date=="6":
    date = "วันเสาร์"
    break
  elif date=="7":
    date = "วันอาทิตย์"
    break
  else:
    print("!!กรุณากรอกวันให้ถูกต้อง!!")

print("\nช่วงเวลาสำหรับลูกค้าที่ต้องการจองคิวล่วงหน้า")
print("[1]10:00-11:00 , [2]11:00-12:00 , [3]14:00-15:00")
print("[4]15:00-16:00 , [5]17:00-18:00")

while(True):
  time = input("กรุณาระบุเวลาที่ต้องการจองคิว (1-5) : ")
  if time=="1":
    time = "10:00-11:00"
    break
  elif time=="2":
    time = "11:00-12:00"
    break
  elif time=="3":
    time = "14:00-15:00"
    break
  elif time=="4":
    time = "15:00-16:00"
    break
  elif time=="5":
    time = "17:00-18:00"
    break
  else:
    print("!!กรุณากรอกเวลาให้ถูกต้อง!!")

print("="*40)
print("\t  บริการและราคาของร้าน")
print("="*40)
print("บริการและราคาเริ่มต้นของราคาทำผม")
print("1. สระไดร์ 600-1000 บาท")
print("2. ทำผมออกงาน 1200-2000 บาท")
print("3. ตัดผม 1200-3000 บาท ")
print("4. ทำสีผม สีเดียว เริ่มต้นที่ 4000 บาท")
print("5. ดัดผมปกติ 5500 บาท")
print("6. ดัดผมดิจิทัล 6500 บาท")
print("7. ทำทรีตเมนต์บำรุงผม 3500-4000 บาท")
print("8. ยืดผม 2000 บาท")
print("\nบริการและราคาเริ่มต้นของราคาทำเล็บ")
print("9. ทาสีเจลเล็บมือ/สีกากเพชร 1-2 สี 300 บาท")
print("10. ทาสีเจลเล็บเท้า/สีกากเพชร 1-2 สี 300 บาท")
print("11. ทาสีเจล/สีกากเพชร 3 สี 350 บาท")
print("12. ทาสีเจล/สีกากเพชร 4-5 สี 400 บาท")
print("13. ไล่สี/ไล่สีกากเพชร/ปลายขาว 450 บาท")
print("14. ล้างสีเจล 100 บาท (ถ้าทำสีเล็บจากที่ร้านค่าล้าง 50 บาท)")
print("15. เพนต์เล็บ 150 บาท")
print("16. ขัดเล็บกระจก/เล็บโฮโลแกรม 500 บาท")
print("17. เคลือบแก้ปัญหาเล็บบาง 100 บาท")
print("18. ต่อเล็บ PVC 200 บาท")
print("19. ถอดเล็บ PVC 100 บาท")
print("20. ต่อเล็บอะคริลิก 500 บาท")
print("21. เติมโคนอะคริลิก 1200 บาท")
print("22. ถอดเล็บอะคริลิก 500 บาท")
print("23. สปาเท้า 450 บาท")
print("24. สปามือ 450 บาท")
print("25. ตัดหนังมือ 250 บาท")
print("26. ตัดหนังเท้า 350 บาท")
print("="*40)

total_price = 0
total_order = ""
while(True):
  while(True):
    order = input("กรุณาระบุรายการที่ต้องการทำ(กรอกเฉพาะตัวเลข 1-26 เท่านั้น) : ")
    if order == '1':
      print("1. สระไดร์ 600-1000 บาท")
      while(True):
        hair = input("กรุณาระบุความยาวผมของลูกค้า[1]ผมยาว ,[2]ผมสั้น : ")
        if hair == '1':
          print("สระไดร์ / ผมยาว - 1000 บาท")
          total_order += "สระไดร์ / ผมยาว - 1000 บาท\n"
          total_price += 1000
          break
        elif hair == '2':
          print("สระไดร์ / ผมสั้น - 600 บาท")
          total_order += "สระไดร์ / ผมสั้น - 600 บาท\n"
          total_price += 600
          break
        else:
          print("กรุณากรอกแค่ตัวเลข [1] และ [2] เท่านั้น")
      break

    elif order == '2':
      print("2. ทำผมออกงาน 1200-2000 บาท")
      while(True):
        hair = input("กรุณาระบุความยาวผมของลูกค้า[1]ผมยาว ,[2]ผมสั้น : ")
        if hair == '1':
          print("ทำผมออกงาน / ผมยาว - 2000 บาท")
          total_order += "ทำผมออกงาน / ผมยาว - 2000 บาท\n"
          total_price += 2000
          break
        elif hair == '2':
          print("ทำผมออกงาน / ผมสั้น - 1200 บาท")
          total_order += "ทำผมออกงาน / ผมสั้น - 1200 บาท\n"
          total_price += 1200
          break
        else:
          print("กรุณากรอกแค่ตัวเลข [1] และ [2] เท่านั้น")
      break

    elif order == '3':
      print("3. ตัดผม 1200-3000 บาท")
      while(True):
        hair = input("กรุณาระบุความยาวผมของลูกค้า[1]ผมยาว ,[2]ผมสั้น : ")
        if hair == '1':
          print("ตัดผม / ผมยาว - 3000 บาท")
          total_order += "ตัดผม / ผมยาว - 3000 บาท\n"
          total_price += 3000
          break
        elif hair == '2':
          print("ตัดผม / ผมสั้น - 1200 บาท")
          total_order += "ตัดผม / ผมสั้น - 1200 บาท\n"
          total_price += 1200
          break
        else:
          print("กรุณากรอกแค่ตัวเลข [1] และ [2] เท่านั้น")
      break

    elif order == '4':
      print("4. ทำสีผม สีเดียว เริ่มต้นที่ 4000 บาท")
      total_order += "ทำสีผม สีเดียว 4000 บาท\n"
      total_price += 4000
      break

    elif order == '5':
      print("5. ดัดผมปกติ 5500 บาท")
      total_order += "ดัดผมปกติ 5500 บาท\n"
      total_price += 5000
      break

    elif order == '6':
      print("6. ดัดผมดิจิทัล 6500 บาท")
      total_order += "ดัดผมดิจิทัล 6500 บาท\n"
      total_price += 6500
      break

    elif order == '7':
      print("7. ทำทรีตเมนต์บำรุงผม 3500-4000 บาท")
      while(True):
        hair = input("กรุณาระบุความยาวผมของลูกค้า[1]ผมยาว ,[2]ผมสั้น : ")
        if hair == '1':
          print("ทำทรีตเมนต์บำรุงผม / ผมยาว - 4000 บาท")
          total_order += "ทำทรีตเมนต์บำรุงผม / ผมยาว - 4000 บาท\n"
          total_price += 4000
          break
        elif hair == '2':
          print("ทำทรีตเมนต์บำรุงผม / ผมสั้น - 3500 บาท")
          total_order += "ทำทรีตเมนต์บำรุงผม / ผมสั้น - 3500 บาท\n"
          total_price += 3500
          break
        else:
          print("กรุณากรอกแค่ตัวเลข [1] และ [2] เท่านั้น")
      break

    elif order == '8':
      print("8. ยืดผม 2000 บาท")
      total_order += "ยืดผม 2000 บาท\n"
      total_price += 2000
      break
    
    elif order == '9':
      print("9. ทาสีเจลเล็บมือ/สีกากเพชร 1-2 สี 300 บาท")
      total_order += "ทาสีเจลเล็บมือ/สีกากเพชร 1-2 สี 300 บาท\n"
      total_price += 300
      break

    elif order == '10':
      print("10. ทาสีเจลเล็บเท้า/สีกากเพชร 1-2 สี 300 บาท")
      total_order += "ทาสีเจลเล็บเท้า/สีกากเพชร 1-2 สี 300 บาท\n"
      total_price += 300
      break

    elif order == '11':
      print("11. ทาสีเจล/สีกากเพชร 3 สี 350 บาท")
      total_order += "ทาสีเจล/สีกากเพชร 3 สี 350 บาท\n"
      total_price += 350
      break

    elif order == '12':
      print("12. ทาสีเจล/สีกากเพชร 4-5 สี 400 บาท")
      total_order += "ทาสีเจล/สีกากเพชร 4-5 สี 400 บาท\n"
      total_price += 400
      break

    elif order == '13':
      print("13. ไล่สี/ไล่สีกากเพชร/ปลายขาว 450 บาท")
      total_order += "ไล่สี/ไล่สีกากเพชร/ปลายขาว 450 บาท\n"
      total_price += 450
      break

    elif order == '14':
      print("14. ล้างสีเจล 100 บาท (ถ้าทำสีเล็บจากที่ร้านค่าล้าง 50 บาท)")
      while(True):
        choose = input("ลูกค้าได้ทำสีเล็บจากร้านเราไหม (Y/N) : ")
        if choose=='Y' or choose=='y' or choose=='Yes' or choose=='yes':
          print("ล้างสีเจล / ทำสีเล็บจากที่ร้าน - 50 บาท")
          total_order += "ล้างสีเจล / ทำสีเล็บจากที่ร้าน - 50 บาท\n"
          total_price += 50
          break
        elif choose=='N' or choose=='n' or choose=='No' or choose=='no':
          print("ล้างสีเจล / ไม่ได้ทำจากที่ร้าน - 100 บาท")
          total_order += "ล้างสีเจล / ไม่ได้ทำจากที่ร้าน - 100 บาท"
          total_price += 100
          break
        else:
          print("กรุณากรอกแค่ Y / N เท่านั้น")
      break
    
    elif order == '15':
      print("15. เพนต์เล็บ 150 บาท")
      total_order += "เพนต์เล็บ 150 บาท\n"
      total_price += 150
      break

    elif order == '16':
      print("16. ขัดเล็บกระจก/เล็บโฮโลแกรม 500 บาท")
      total_order += "ขัดเล็บกระจก/เล็บโฮโลแกรม 500 บาท\n"
      total_price += 500
      break
      
    elif order == '17':
      print("17. เคลือบแก้ปัญหาเล็บบาง 100 บาท")
      total_order += "เคลือบแก้ปัญหาเล็บบาง 100 บาท\n"
      total_price += 100
      break

    elif order == '18':
      print("18. ต่อเล็บ PVC 200 บาท")
      total_order += "ต่อเล็บ PVC 200 บาท\n"
      total_price += 200
      break

    elif order == '19':
      print("19. ถอดเล็บ PVC 100 บาท")
      total_order += "ถอดเล็บ PVC 100 บาท\n"
      total_price += 100
      break

    elif order == '20':
      print("20. ต่อเล็บอะคริลิก 500 บาท")
      total_order += "ต่อเล็บอะคริลิก 500 บาท\n"
      total_price += 500
      break

    elif order == '21':
      print("21. เติมโคนอะคริลิก 1200 บาท")
      total_order += "เติมโคนอะคริลิก 1200 บาท\n"
      total_price += 1200
      break

    elif order == '22':
      print("22. ถอดเล็บอะคริลิก 500 บาท")
      total_order += "ถอดเล็บอะคริลิก 500 บาท\n"
      total_price += 500
      break

    elif order == '23':
      print("23. สปาเท้า 450 บาท")
      total_order += "สปาเท้า 450 บาท\n"
      total_price += 450
      break

    elif order == '24':
      print("23. สปามือ 450 บาท")
      total_order += "สปามือ 450 บาท\n"
      total_price += 450
      break

    elif order == '25':
      print("25. ตัดหนังมือ 250 บาท")
      total_order += "ตัดหนังมือ 250 บาท\n"
      total_price += 250
      break

    elif order == '26':
      print("26. ตัดหนังเท้า 350 บาท")
      total_order += "ตัดหนังเท้า 350 บาท\n"
      total_price += 350
      break
    
    else:
      print("!! กรุณากรอกแค่ตัวเลข 1 - 26 เท่านั้น !!")

  ch = ""
  while(True):
    ch = input("ต้องการทำรายการเพิ่มหรือไม่ (Y/N) : ")
    if ch=='Y' or ch=='y' or ch=='Yes' or ch=='yes':
      print()
      break
    elif ch=='N' or ch=='n' or ch=='No' or ch=='no':
      break
    else:
      print("กรุณากรอกแค่ Y / N เท่านั้น")
  
  if ch=='N' or ch=='n' or ch=='No' or ch=='no':
    break

print("="*40)
print("ข้อมูลการจอง")
print("ชื่อ-นามสกุล :",name)
print("เบอร์โทรศัพท์ :",phoneNumber)
print("อีเมลล์ :",email)
print("ช่องทางติดต่ออื่นๆ :",otherContact)
print("วันที่จอง :",date)
print("เวลาที่จอง :",time)
print("="*40)
print("รายการทั้งหมด")
print(total_order,end='')
print("="*40)
print("รวมราคาทั้งหมด :",total_price,"บาท")
print("="*40)

print("ช่องทางการชำระเงิน")
print("[1]ชำระเงินสด , [2]โอนเงินผ่านธนาคาร")
chs = ''
while(True):
  chs = input("กรุณาเลือกช่องทางการชำระเงิน : ")
  if chs =='1':
    money = float(input("กรุณากรอกจำนวนเงิน : "))
    while(money<total_price):
      print("จำนวนเงินไม่พอจ่าย ขาดอยู่",total_price-money,"บาท")
      money2 = float(input("กรุณากรอกจำนวนเงินเพิ่ม : "))
      money += money2
    change = money - total_price
    print("เงินทอน",change,"บาท")
    if change > 0:
      print("แบงก์ร้อย",change//100,"ใบ")
      c = change%100
      print("แบงก์ห้าสิบ",change//50,"ใบ")
      c = c%50
      print("แบงก์ยี่สิบ",change//20,"ใบ")
      c = c%20
      print("เหรียญสิบ",c//10," เหรียญ")
      print("เหรียญบาท",c%10," เหรียญ")
    break
  elif chs == '2':
    print("ธนาคารกรุงไทย")
    print("เลขที่บัญชี 111 1 11111 1")
    print("ชื่อบัญชี Beautiful Salon")
    break
  else:
    print("!!กรุณากรอกแค่ 1 และ 2 เท่านั้น!!")

print("="*40)
print("   ความคิดเห็นและความพึงพอใจในการใช้บริการ")
print("="*40)
print("[1]แย่มาก")
print("[2]แย่")
print("[3]พอใช้")
print("[4]ดี")
print("[5]ดีมาก")
while(True):
  star = input("กรุณาระบุความพึงพอใจ (1-5) : ")
  if star!="1" and star!="2" and star!="3" and star!="4" and star!="5":
    print("!!กรุณากรอกให้ถูกต้อง!!")
  else:
    break
comment = input("แสดงความคิดเห็น : ")

print("="*40)
print("\t    ขอบคุณที่ใช้บริการ")
print("="*40)