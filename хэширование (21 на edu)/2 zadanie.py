import string
import random
def stroka():
    e = []
    q = string.digits
    w = string.digits
    q1 = string.ascii_uppercase
    q2 = string.ascii_lowercase
    for i in range (len(q1)):
        e.append(q2[i])
    for i in range (len(q1)):
        e.append(q1[i])
    for i in range(len(q)):
      e.append(q[i])
    return random.sample(e, len(w))

new = stroka()
w = "На улице светло и идёт снег"
w = w.split()
t = dict(zip(new, w))
print(t)
