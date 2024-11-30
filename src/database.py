import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="qlthuvien"
)
mycursor = mydb.cursor()

taikhoan = """CREATE TABLE IF NOT EXISTS taikhoan (
            id INT AUTO_INCREMENT PRIMARY KEY,
            taikhoan VARCHAR(50) NOT NULL,
            matkhau VARCHAR(50) NOT NULL
        )"""

khachhang = """CREATE TABLE IF NOT EXISTS khachhang (
            makhach VARCHAR(50) NOT NULL PRIMARY KEY,
            tenkhach VARCHAR(50) NOT NULL,
            SDT_email VARCHAR(50) NOT NULL
        )"""

tacgia = """CREATE TABLE IF NOT EXISTS tacgia (
            tentacgia VARCHAR(50) NOT NULL PRIMARY KEY
        )"""

theloai = """CREATE TABLE IF NOT EXISTS theloai (
            theloai VARCHAR(50) NOT NULL PRIMARY KEY
        )"""

nhaxuatban = """CREATE TABLE IF NOT EXISTS nhaxuatban (
            nhaxb VARCHAR(50) NOT NULL PRIMARY KEY
        )"""

# Tạo bảng book sau khi đã tạo các bảng tham chiếu
book = """CREATE TABLE IF NOT EXISTS book (
            tensach VARCHAR(50) NOT NULL,
            mota VARCHAR(50) NOT NULL,
            masach VARCHAR(50) NOT NULL PRIMARY KEY,
            theloai VARCHAR(50),
            giatien INT,
            tacgia VARCHAR(50),
            nhaxuatban VARCHAR(50),
            soluong INT
        )"""

muontra = """CREATE TABLE IF NOT EXISTS muontra (
            id INT AUTO_INCREMENT PRIMARY KEY,
            masach VARCHAR(50),
            makhach VARCHAR(50),
            trangthai VARCHAR(50) NOT NULL,
            ngay INT,
            ngaymuon DATE,
            ngaytra DATE,
            FOREIGN KEY (makhach) REFERENCES khachhang(makhach),
            FOREIGN KEY (masach) REFERENCES book(masach)
        )"""

# Thực thi tạo bảng
mycursor.execute(taikhoan)
mycursor.execute(khachhang)
mycursor.execute(tacgia)
mycursor.execute(theloai)
mycursor.execute(nhaxuatban)
mycursor.execute(book)
mycursor.execute(muontra)

# Lưu các thay đổi vào cơ sở dữ liệu
mydb.commit()

# Đóng kết nối và con trỏ
mycursor.close()
mydb.close()
