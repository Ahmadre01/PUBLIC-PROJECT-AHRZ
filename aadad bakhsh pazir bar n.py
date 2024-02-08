number = int(input("please enter a number==>"))
divisible_num = [ ]
for i in range(1,15) :
    if number % i ==0 :
        divisible_num.append(i)
print("the number",number, "are divisible by : ",divisible_num)

#طراحی برنامه ای که کاربر یک عدد را وارد کند و در نهایت ==>
#در خروجی برنامه بگوید که آن عدد بر چه عدد هایی بخش پذیر  میباشد ==>
# (تا 15 عدد بخش پذیری را بگوید )

