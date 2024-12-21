file_path = "ir.model.access.csv"  # ضع مسار الملف هنا
try:
    with open(file_path, "rb") as f:
        data = f.read()
        print(data.decode("utf-8"))
        print("The file is encoded in UTF-8 and has been read successfully.")
except UnicodeDecodeError:
    print("The file is not encoded in UTF-8. Please convert it to UTF-8.")
