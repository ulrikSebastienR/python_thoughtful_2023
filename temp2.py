#Calculate age of a user

sd = int(input('enter your date of birth'))
sm = int(input('enter your month of birth'))
sy = int(input('enter your year'))

print(sd, type(sd), sm, type(sm), type(sy))

def age(sd, sm, sy):
    import datetime

    now = datetime.datetime.now()
    print(datetime.datetime.now())
    print(type(now))
   


  

    user = datetime.datetime(sy,sm,sd)
    print(user, type(user))

    age = now - user

    return age,type(age)
