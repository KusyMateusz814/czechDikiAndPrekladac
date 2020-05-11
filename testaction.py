import argparse

parser = argparse.ArgumentParser(description="Tutaj podajemy jakis opis naszego skryptu")
#pierwszy przyklad 
parser.add_argument('filename', help="Opis tego argumentu (krótkie wyjaśnienie co przyjmuje)")

#args = parser.parse_args() #parsujemy argumenty aby wyłuskać przekazane w nich wartosci i wyświetlamy je na ekranie
#print("Podana nazwa pliku: ", args.filename)

#drugi przyklad
parser.add_argument('-a', '--argument', help="Nasz opcjonalny argument", required=False)
parser.add_argument('-i', '--ilosc', help="Argument o konrkretnym typie i wartosci domysllnej", type=int, default=0, required=False)
parser.add_argument('-l', '--logihami', action='store_true', help="show debug info", required=False)
args = parser.parse_args()
print("Podana nazwa pliku: ", args.filename)
print("Wartość argumentu dodatkowego: ", args.argument)
print("Wartość argumentu z typem i domyślna wartościa: ", args.ilosc)

#trzeci przyklad

