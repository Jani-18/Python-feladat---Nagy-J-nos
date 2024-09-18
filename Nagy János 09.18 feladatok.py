print('1. feladat')

print('Listázza ki az alábbi országokat: Brazil, Russia, India, China, South Africa')

orszagok = ['Brazil', 'Russia', 'India', 'China', 'South Africa']
print(orszagok)

print('2. feladat')
vezetek = input('Add meg a vezetékneved: ')
kereszt = input('Add meg a keresztneved: ')
lakhely = input('Adja meg a lakhelyét: ')
evszam = int(input('Adja meg az életkorát: '))
print("Üdvözlöm", vezetek, kereszt, "!" "Ön", lakhely,  "-on él és ", evszam, "éves.")

'''
print("3. feladat")

nativeVlan = 
dataVlan = 
'''

print("4. feladat")
print("standard and extended ACL numbers")

int(input("Adjon meg egy számot: "))

def categorize_acl(number):
    if 1 <= number <= 99:
        return "standard acl"
    elif 100 <= number <= 199:
        return "extended acl"
    else:
        return "Nincs benne a standard vagy az extended kategóriában sem"

def main():
    try:
        number = int(input("Kérlek, adj meg egy ACL számot: "))
        category = categorize_acl(number)
        print(f"A(z) {number} szám kategóriája: {category}")
    except ValueError:
        print("Kérlek, érvényes egész számot adj meg.")

print("5. feladat")

def main():
    while True:
        user_input = input("Kérlek, adj meg egy számot, ameddig számolni szeretnél (vagy 'q'/'quit' a kilépéshez): ")
        
        if user_input.lower() in ['q', 'quit']:
            print("A program kilép.")
            break
        
        try:
            count_to = int(user_input)
            numbers = ' '.join(str(i) for i in range(1, count_to + 1))
            print(numbers)
        except ValueError:
            print("Kérlek, adj meg egy érvényes számot.")

if __name__ == "__main__":
    main()


print("6. feladat")
print("I don't know")