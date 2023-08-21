katz_deli = []

def line(waitlist):
    if len(waitlist)== 0:
        print("The line is currently empty.")
    else:
        print(f"The line is currently: " + " ".join([f'{index+1}. {name}' for index, name in enumerate(waitlist)]))
    pass

def take_a_number(waitlist, name):
    waitlist.append(name)
    print(f'Welcome, {name}. You are number {len(waitlist)} in line.')
    pass

def now_serving(waitlist):
    if len(waitlist) > 0:
        print(f"Currently serving {waitlist.pop(0)}.")
        
    else:
        print("There is nobody waiting to be served!")
    pass

