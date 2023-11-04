import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.title("ŞANLI SANCAK")         # Başlık
w.setup(width=720, height=420)   # Pencere Boyutu
w.bgcolor("red")                # Arka Plan Kırmızı Yap

# İlk daire
t.up()
t.goto(-100, -100)               # Fare imleci lokasyonu
t.color('white')                # Beyaz renk
t.begin_fill()                  # Beyaz rengi doldur
t.circle(120)                   # Çapı
t.end_fill()

# Hilal yapabilmek için ikinci daire
t.goto(-70, -80)                 # Fare imleci lokasyonu
t.color('red')                  # Kırmızı renk
t.begin_fill()                  # Kırmızı rengi doldur
t.circle(100)                   # Çapı
t.end_fill()                    # Dolguyu Bitir

# Yıldız için hazırlık
t.penup()
t.goto(50, 35)
t.fillcolor("white")
t.begin_fill()

# Yıldızı çizmek için döngü kullanarak köşelere gidin ve aralardaki noktayı çizin
for i in range(5):
    t.forward(40)
    t.right(144)
    t.forward(40)
    t.left(72)

t.end_fill()

t.penup()
t.goto(0, -190)
t.color("white")
t.write("100.Yılımız Kutlu olsun 🥳", align="center", font=("Verdana", 17, "bold"))

# Fare imleci ekranda durup görüntü bozmasın diye uzaklaştırıyoruz :)
t.goto(-999, -0)

# Ekrana tıklayınca programın kapanmasını sağlar.
w.exitonclick()
