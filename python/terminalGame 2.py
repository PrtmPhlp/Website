# Created from PrtmPhlp

print ('Willkommen zu PrtmPhlps Spiel!')

ans = input('Bist du bereit? (ja/nein)')
score = 0
total_q = 4

if ans.lower() == 'ja':
    ans = input('1. Was ist die beste Programmier Sprache?')
    if ans.lower() == 'python' or ans == 'peter':
        score += 1
        print('Richtig 🥳') 
    else:
        print('Falsch :(')

    ans = input('2. Was ist 2 + 8 + 9 - 1')
    if ans == '18':
        score += 1
        print('Richtig🥳')
    else:
        print('Falsch :(')

    ans = input('3. Was hat bessere GPU Werte? Ein A10X oder ein A12 Prozessor?')
    if ans.lower() == 'a10x':
        score += 1
        print('Richtig🥳')
    else:
        print('Falsch :(')

    ans = input('3. Was ist die Hauptstadt von Deutschland?')
    if ans.lower() == 'berlin' or ans.lower() == 'peter':
        score += 1
        print('Richtig🥳')
    else:
        print('Falsch :(')

    print('Danke fürs spielen, du hast', score, 'Fragen richtig beantwortet')
    mark = (score/total_q) * 100
    print("Quote:", str(mark) + '%')
print('Tschüssi')