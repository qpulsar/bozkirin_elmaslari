from turtle import *
color("black","black")
pozisyon_dizi = [-40,140,120,100,150,-7,120,-110,-40,-160,-180,-110,-230,-7,-250,100]
yazilar = ["Merhamet","Şefkat","Sabretmek","Doğruluk","Sır tutmak","Sadakat","Cömertlik","Rabbine şükretmek"]
renk =["red","blue","green","yellow","black","cyan","purple","magenta"]
speed(10)
begin_fill()
for b in range (8):
    for a in range (4):
        forward(100)
        right(90)
    right(45) 
end_fill()

i=0
while (i<7):
     for c in range(0,16,2):
         penup()
         goto(pozisyon_dizi[c],pozisyon_dizi[c+1])
         pendown()
         color(renk[i])
         write(yazilar[i],font=("Verdana",12,"bold"))
         i=i+1
penup()
goto(-999,-0)



