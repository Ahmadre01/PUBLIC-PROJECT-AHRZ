print(" < namayesh username va password >")
# از کاربر نام کاربری را دریافت می‌کنیم
username = input("ENTER YOUR USERNAME ==>")
# از کاربر رمز عبور را برای هر نام کاربری دریافت می‌کنیم
password = input(f"ENTER PASSWORD FOR {username} ==> ")
# تعریف یک دیکشنری از نام کاربری‌ها و رمز عبورها 
username_PASS = {
    "AHMADREZA" : "AHRZ123",
    "ALIREZAEI" :"ALI245",
    "MORTEZA" : "MRZ423"
}
if username in username_PASS and username_PASS[username] == password:
    print(f"USERNAME AND PASSWORD ==> TRUE , YOUR PASSWORD ==> {password}")
else:
    print(" USERNAME VA PASSWORD  ==> False")
    print("USERNAME VA PASSWORD VARED SHODE :  username =",username  ,"/" ,"password =",password)
