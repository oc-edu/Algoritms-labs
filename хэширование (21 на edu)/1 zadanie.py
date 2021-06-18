import string
import random
def spisok():
    e = []
    q = string.digits
    q1 = string.ascii_uppercase
    q2 = string.ascii_lowercase
    for i in range (len(q1)):
        e.append (q2[i])
    for i in range (len(q1)):
        e.append (q1[i])
    for i in range (len(q)):
      e.append (q[i])
    return random.sample(e, 10)

spisok()
