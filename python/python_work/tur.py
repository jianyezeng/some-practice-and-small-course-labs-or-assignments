import turtle as t
import cv2

t.getscreen().colormode(255)
img1 = cv2.imread('ping.jpg')[0: -2: 2]
width = len(img1[0])
height = len(img1)
t.setup(width=width / 2 + 100, height = height + 100)
t.pu()
t.goto(-width / 4 + 10, height / 2 - 10)
t.pd()
t.tracer(2000)
for k1, i in enumerate(img1):
    for j in i[::2]:
        t.pencolor((j[0], j[1], j[2]))
        t.fd(1)
    t.pu()
    t.goto(-width / 4 + 10, height / 2 - 10 - k1 - 1)
    t.pd()
t.done()

