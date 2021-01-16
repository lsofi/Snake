import turtle
pluma = turtle.Turtle()

#se va a la derecha 100 pixeles, gira 90 grados y sube 100
#pluma.forward(100)
#pluma.left(90)
#pluma.forward(100)

#pluma.speed(30)

for i in range (0, 4):
    pluma.forward(100)
    pluma.left(90)

#para que no se me cierre la ventana ran rapido
turtle.mainloop()