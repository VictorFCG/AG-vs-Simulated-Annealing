import starter_generator as sg
from numpy import exp
from random import randint

CAPACIDADE_MAXIMA = 400
MAX_IT = 100
INITIAL_TEMP = 90

#Considera a capacidade da mochila para adicionar ou não
def randomChoiceSimAne(items, max_c):
        choice = []
        total_w = []
        for i in range(len(items)):
            choice.append(randint(0, 1))
            if choice[i] == 1:
                if sum(total_w) + items[i] <= max_c:
                    total_w.append(items[i])
                else:
                    choice[i] = 0

        return choice

def tempCalc(currTemp, count):
    print(f'TEMPERATURA RECEBIDA: {currTemp}\nCONTADOR {count}: %d')
    ct = ((INITIAL_TEMP - 0) * pow(((MAX_IT-count)/MAX_IT),2))
    print("\nTEMPERATURA ATUAL:",ct)
    return ct

def difCalc(cur,nex,val):
    total_c = []
    total_n = []
    print("\n",nex,cur)
    for i in range(len(cur)):
        if cur[i] == 1:
            total_c.append(val[i])
        if nex[i] == 1:
            total_n.append(val[i])
    print("\nPrint valores total next e total current: ", sum(total_n),sum(total_c))
    return sum(total_n) - sum(total_c)

def main():
    print("INICIO")
    temperature = INITIAL_TEMP #fazer uma função q retorna o valor de t baseado no tempo
    weight, value = sg.init(15,100,100)
    current = randomChoiceSimAne(weight,CAPACIDADE_MAXIMA)

    count = 0

    while True:
        count = count + 1
        temperature = tempCalc(temperature, count)
        if temperature == 0:
            return current
        next = randomChoiceSimAne(weight,CAPACIDADE_MAXIMA)
        dif = difCalc(current,next,value)
        print("\ndiferença:",dif)
        if dif >= 0:
            current = next
        else:
            prob = exp(dif/temperature)
            print(f'\nprobabilidade: {prob}')
            if prob >= 0.8:
                current = next

if __name__ == "__main__":
    main()
