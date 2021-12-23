import os
import time

def worng(par,user):
    error = 0
    for i in range(len(par)):
        try:
            if par[i] != user[i]:
                error+= error
        except:
            error+=error
    return error
def speed_test(time_s,time_e,u_input):
    time_dealy = time_e-time_s
    time_round = round(time_dealy,2)
    speed = len(u_input)/time_round
    return round(speed)


text = "More powerful examples of pattern matching can be found in languages such as Scala and Elixir. With structural pattern matching, the approach is “declarative” and explicitly states the conditions (the patterns) for data to match"

print("*************** Typing Tester ******************\n")
print(text)
print("\n\n")
time_1 = time.time()
userinput = input("Enter: ")
time_2 = time.time()

print(f"Speed: {speed_test(time_1,time_2,userinput)} w/sec")
print(f"Error: {worng(text,userinput)}")