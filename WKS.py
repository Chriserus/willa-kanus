from enum import *
from random import *



Klasa = Enum('Klasa postaci', {'Banan': 'Banan',
                               'Pytalski':'Pytalski',
                               'Farciarz': 'Farciarz'})


torba = 300

trasa = choices (['prawo', 'lewo', 'prosto'], k=5)

szczescie = 1

kaska = [0, 200, 800, 2000]


Osoba = IntEnum ('Osoba', 'Bambus Falo Artur')

osobaSzansa ={Osoba.Bambus: 0.2,
              Osoba.Falo: 0.7,
              Osoba.Artur: 0.1}

osobyLista = list (osobaSzansa.keys())

sznasaLista = list (osobaSzansa.values())



ListaArtefaktow = IntEnum ('artefakty', ["Złamany_szlug", "Kij_golfowy", "Flaszka", "Joint", "PIWKO_330"])

Artefakty = list(ListaArtefaktow)

def aproksymacja(nagroda):
    przychod = round (uniform (nagroda - 0.1*nagroda, nagroda + 0.1))
    return przychod


def nagroda():
    if (szczescie == 1):
        zdobytyArtefakt =  choices(Artefakty, [30, 25, 20, 15, 5], k=1)[0]
    elif (szczescie == 2):
        zdobytyArtefakt =  choices(artefakty, [15, 25, 20, 15, 10], k=1)[0]
        
    if (zdobytyArtefakt == ListaArtefaktow.Złamany_szlug):
        print ('Ehhhh pierdolone zwierzęta .... miały być artefakty a jedyne co znalazłeś to:', ListaArtefaktow.Złamany_szlug.name, ', który jest nic nie warty')
        return 0
    elif (zdobytyArtefakt == ListaArtefaktow.Kij_golfowy):
        print (ListaArtefaktow.Kij_golfowy.name, '! To może być coś warte!')
        wartosc = aproksymacja(100)
        print (f"""

                Otrzymujesz {wartosc} zł

                    """)
        return wartosc
    elif (zdobytyArtefakt == ListaArtefaktow.Joint):
        print (ListaArtefaktow.Joint.name, '! Sprzedam go Bambuswoi!')
        wartosc = aproksymacja(300)
        print (f"""

                Otrzymujesz {wartosc} zł

                """)
        return wartosc
    elif (zdobytyArtefakt == ListaArtefaktow.Flaszka):
        print (ListaArtefaktow.Flaszka, '! To na pewno jest coś warte!')
        wartosc = aproksymacja(200)
        print (f"""

                Otrzymujesz {wartosc} zł

                """)
        return wartosc
    elif (zdobytyArtefakt == ListaArtefaktow.PIWKO_330):
        print ("NIE WIERZĘ WŁASNYM OCZOM!!!")
        print (ListaArtefaktow.PIWKO_330.name)
        wartosc = aproksymacja(700)
        print (f"""

                Otrzymujesz {wartosc} zł

                """)
        return wartosc
    else:
        print ('nie dla psa')









print ("""Witaj w WILLA KANUS SIMULATOR 1.2
Zasady są bardzo proste. Twoim celem będzie przejście przez Wille Kanus - siedzibę legendranego opactwa!
Jak tego dokonać? Będziesz musiał wskazywać kierunek w którym ma się poruszać Twoja postać. Tylko jedna dorga jest właściwa! Czasy są ciężkie....
Polski ład
inflacja...
w związku z czym za każde jednorazowe, błędne wskazanie kierunku zapłacisz stuwę xd!
Swoją podróż zaczynasz z 300 zł w portfelu jednak po wskazaniu poprawnej drogi masz sporą szansę na trafienie, któregoś z legendarnych artefaktów, który poprawi Twój dobrobyt!


Wielcy polegli w Willi Kanus...
Ci któzy przetrwali, napisali legendę!



""")



imie = input('Podaj Twoję imię przywoływaczu: ')

print('\nWitaj', imie, 'sprawdźmy czy jesteś gotowy na wyjście cało z tej mistycznej posiadłości \n')


print("""
Czas na wybranie klasy postaci! Każda klasa cechuje się inną specjalną umiejętnością...
1: Banan - zaczynasz grę z dodatkową ilością złota, jednak pamiętaj, że jego ilość nie jest gwarantowana i zależy od tego czy Twoi rodzice mają dobry humor!
2: Pytalski - Masz unikalną szansę dowiedzenia się na wejściu jaka jest właściwa droga do wyjścia! Jednak nigdy nie wiadomo, kogo tam spotkasz i w jakim akurat będzie stanie...
3: Farciarz - masz 2 razy większą szansę na trafienie legendarnych artefaktów

""")


while True:
    wybor = input('Jaki jest Twój wybór? Napisz klasę postaci, którą chcesz wybrać!: ')
    if (wybor == Klasa.Banan.value):
        otrzymanaKaska = choices(kaska,[0.15, 0.20, 0.55, 0.10], k=1)[0]
        if (otrzymanaKaska == 0):
            print('Jesteś takim giga grzybem, że stary nie zostawiłby Ci nawet złamanego pensa! radź sobie sam xd')
        elif (otrzymanaKaska == 200):
            print ('Masz tu 2 stówy, nie dzwoń o więcej!')
            torba += otrzymanaKaska
        elif (otrzymanaKaska == 800):
            print ('Nie po to tatuś się tyle namęczył, żeby jego potomek nie potrafił przejść przez jakąś letniskową chatke! Masz tutaj 800 zł ode mnie!')
            torba += otrzymanaKaska
        elif (otrzymanaKaska == 2000):
            print ('Dla mojego ukochanego wszystko. Myślę że 2000 zamkną wszystki usta!')
            torba+= otrzymanaKaska
        break
    elif (wybor == Klasa.Pytalski.value):
        kto = choices (osobyLista, sznasaLista, k=1)[0]
        if (kto == Osoba.Bambus):
            print (f"""<widzisz Bambusa z czerwonymi oczami, jakby przez godzine pływał na basenie bez okularów>
OOOO siema {imie}, jasne byczq już Ci mówię trasę... To było tak:
{trasa[0]}
kurwa sorry {imie} ,ale w chuj się zjarałem i nie pamiętam dalej... powodzenia xd""")
        elif (kto == Osoba.Falo):
            print (f""" <Słyszysz szmer drapania się po skórze, domyślasz sie, że poblizu musi byc gdzieś Falo!>
{imie}!! Co tam morda? Pewnie że pamiętam trasę...To było:
{trasa[0]}
{trasa[1]}
{trasa[2]}
kurwa pamięć jak zwykle zawodzi xd ale i tak dużo powiedziałem to chyba dasz radę""")
        elif (kto == Osoba.Artur):
            print(f"""<przed drzwiami widisz Artura którego cała twarz jest czerwona od słońca.>
O cześć {imie}. Jasne, że znam trasę! To bedzie:
{trasa[0]}
{trasa[1]}
{trasa[2]}
{trasa[3]}
ostatniego Ci nie powiem bo byo za łatwo xd""")
        break    
    elif (wybor == Klasa.Farciarz.value):
        szczescie = 2
        print ('Wiesz co mówią o tych co liczą na szczęście?!')
        break
    else:
        print ('Chyba się za bardzo zjarałeś i nie potrafisz czytać ze zrozumieniem!')





print ('Czas na rozgrywkę!')
start = int(input('Jeśli chcesz zobaczyć zawartosc Twojego portfela naciśnij liczbę 1, jeśli chcesz od razu zacząć grę kliknij 2: '))


# czy tutaj kombinowac cos zeby nie bylo start == 1 v 2   np enum ... portfel 
if (start == 1):
    print ('W portfelu masz: ', torba)
    print ('Jeśli już wiesz ile masz w kieszeni to zaczynajmy!')
elif (start == 2):
    print ('Zaczynamy!')
else:
    print ('Chyba się za bardzo zjarałeś i nie potrafisz czytać ze zrozumieniem!..... Tak czy siak zaczynamy!')



print("""





WILLA KANUS




to napis, który widzisz gdy zbliżasz się do budynku. Każdy mały chłopiec marzył, żeby tu trafić i przejść do histroii!!!!



Dziś to może być Twój dzień! Wystarczy że wyjdziesz z niej cały...



""")


print ("""Stoisz u progu Willi! Czas podjąć decyzję .... Aby poruszyć swoją postacią musisz napisać jeden z następujacych kierunków:

lewo
prawo
prosto

""")




if (torba > 0):


    while True:
        
        PierwszyKrok = input ("Jaki jest Twój ruch: ")


        if (PierwszyKrok == trasa[0]):
            print ('Pierwszy krok za Tobą! Chwała co raz bliżej')
            print ('W związku ze wskazaniem dobrej drogi otrzymujesz: ')
            bonus = nagroda()
            torba += bonus
            print ('Zawartość Twojego portfela to:', torba)
            print ("""



            Zblizasz się do celu!




""")
            break
        
        elif (PierwszyKrok != trasa[0]):
            
            torba -= 100
            if (torba <0):
                print("""




NIE KAŻDY MOŻE ZOSTAĆ KOLEJNĄ LEGENDĄ""")
                break
            else:
                print ("""Niestety wybrałeś źle... nie ty pierwszy nie ty ostatni!
Tak jak wspominałem będzie Cię to kosztowało 100 zł""")
                print (f"""Zawartość Twojego portfela to: {torba}
                       """)
else:
    print("""




NIE KAŻDY MOŻE ZOSTAĆ KOLEJNĄ LEGENDĄ""")





for z in range (1,4):

    if (torba >= 0):
        
        while True:
        
            ruch = input ("Jaki jest Twój kolejny ruch: ")


            if (ruch == trasa[z]):
                print ('Chwała co raz bliżej')
                print (' W związku ze wskazaniem dobrej drogi otrzymujesz: ')
                bonus = nagroda()
                torba += bonus
                print ('Zawartość Twojego portfela to:', torba)
                print ("""



Zblizasz się do celu!


""")
                break
            elif (ruch != trasa[z]):
                
                torba -= 100
                if (torba <0):
                    break
                else:
                    print ("""Niestety wybrałeś źle... nie ty pierwszy nie ty ostatni!
Tak jak wspominałem będzie Cię to kosztowało 100 zł
                        """)
                    print ('Zawartość Twojego portfela to:', torba)
            
            
    else:
        print("""


        NIE KAŻDY MOŻE ZOSTAĆ KOLEJNĄ LEGENDĄ""")
        
        break




if (torba >=0):

    print ("""


JESTEŚ BLISKO DO STANIA SIĘ ZYWĄ LEGENDĄ!

TERAZ
ALBO NIGDY.....


""")

    
    while True:
        
            ruch = input ("Czy kolejny ruch pozwoli Ci zostać kimś, kim zawsze chciałeś się stać? Jaki jest Twój kolejny krok?  ")


            if (ruch == trasa[4]):
                print (f"""


    PRZESZEDLES WILLE TO DOSTANIESZ ZWROTE!

    KAMIL TO WCIAŻ PIZDA

    A ty {imie}, {imie} JESTEŚ KOTEM""")
                break
            elif (ruch != trasa[4]):
                
                torba -= 100
                if (torba <0):
                    print("""




        NIE KAŻDY MOŻE ZOSTAĆ KOLEJNĄ LEGENDĄ""")
                    break
                else:
                    print ("""Niestety wybrałeś źle... nie ty pierwszy nie ty ostatni!
    Tak jak wspominałem będzie Cię to kosztowało 100 zł
                        """)
                    print ('Zawartość Twojego portfela to:', torba)
else:
    print("""




        NIE KAŻDY MOŻE ZOSTAĆ KOLEJNĄ LEGENDĄ""")





print ('dzięki za gierkie, miłego dnia')












    
