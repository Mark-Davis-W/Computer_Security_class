#!/usr/bin/python3

from os import P_OVERLAY, sep
import sys
from collections import Counter, deque, OrderedDict

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228,
    'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025,
    'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 'R': 0.05987,
    'S': 0.06327, 'T': 0.09056, 'U': 0.02758, 'V': 0.00978, 'W': 0.02361, 'X': 0.00150,
    'Y': 0.01974, 'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

mapped = {
    'A':  0, 'B':  1, 'C':  2, 'D':  3, 'E':  4, 'F':  5, 'G':  6, 'H':  7, 'I':  8,
    'J':  9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
    'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    # print("freqs: ",freqs)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)


def encrypt(plaintext, key):
    # key_length = len(key)
    newkey = (key * (len(plaintext)))[:len(plaintext)].upper()
    print(newkey,plaintext,len(plaintext),len(newkey), end='')
    key_as_int = [ord(i) for i in newkey]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''

    for i in range(len(plaintext_int)):
        shift = key_as_int[i] - 65
        value = (plaintext_int[i] - 65 + shift) % 26
        # print(value,chr(value +65))
        ciphertext += chr(value + 65)
        
    ciphertext.replace(" ", "").replace("\n",'')
    # print(ciphertext)
    return str(ciphertext)

# def shift_check(ciphertext, key):
#     # key_length = 1
#     # key_as_int = ord(key)
#     ciphertext_int = [ord(i) for i in ciphertext]
#     plaintext = ''
#     print("CHECKING: ",key)
#     for i in range(len(ciphertext_int)):
#         value = (ciphertext_int[i] - key) % 26
#         plaintext += chr(value + 65)
#     return plaintext

def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    # print("key in decrypt: ",key)
    ciphertext_int = [ord(i) for i in ciphertext]
    # print(ciphertext_int)
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        # print(value)
        plaintext += chr(value + 65)
        # print(plaintext)
    return plaintext

# Take text and box size and split it into boxes
def split(text, x):
    boxes = ['' for i in range(x)]
    for i in range(len(text)):
        boxes[i%x] = boxes[i%x] + text[i]
    return boxes

def freqSum(boxes):
    frq = [0.0 for x in range(len(boxes))]
    freqS = 0
    for i in range(len(boxes)):
        frq[i] = pop_var(boxes[i])
    for f in frq:
        freqS += f
    return freqS

def compare_let_freq(tx):

    # Compare the letter distribution of the given text with normal English. Lower is closer.
    # Performs a simple sum of absolute difference for each letter

    engFreq = letter_freqs.values()

    text = [t for t in tx if t in alphabet]
    # print(text)
    freq = [0] * 26
    total = float(len(text))
    for l in text:
        freq[ord(l) - ord('A')] += 1
    # print("compare: ",sum(abs(f / total - E) for f, E in zip(freq, engFreq)))
    return sum(abs(f / total - E) for f, E in zip(freq, engFreq))


def solve_problem(txt,n):
    counts = [''] * n
    best = []
    key = [None] * n

    for i in range(1,n+1):
        # print(i)
        # print(txt)
        for l in range(n):
            c2 = ""
            # print(l)
            for y in range(l,int(len(txt)/2),7):
                # print("y: ",y)
                if(y < len(txt)):
                    c2 += txt[y]
            counts[l] = c2

        # counts = nthParse(txt,i)
        print("counts: ",counts)
        shifts = []

        for j in alphabet:
            shifts.append((compare_let_freq(decrypt(counts[i-1],j)),j))
            # print(shifts)
            # print(j)
        
        # print(key)
        key[i-1] = min(shifts, key=lambda x: x[0])[1]
        print(key)
    best.append("".join(key))
    # best.sort(key=lambda key: compare_let_freq(decrypt(txt,key)))
    print(''.join([str(l) for l in best]))

            
    

# def selected(tx):
#     # if (len(tx) == 1):
#     # print(len(tx))
#     # print(tx)

#     return "".join([k for k,v in mapped.items() if v in tx])

# # def nthParse(txt,n):
# #     return txt[::n]

# Run all functions
def runner(text,x=2,y=13):
    big = 0.000001
    keySize = x
    k = x
    absolute = 0

    while(k < y+1):
        boxes = split(text,k)
        ttl = freqSum(boxes)

        average = ttl/k
        compared = 0;
        print("Average of ({}) : {}".format(k, average))
        if(average > big):
            # if(k%(keySize*1.1) < 1):
            for i in boxes:
                compared += compare_let_freq(i)
            compared /= k
            print("Compared: ",compared)
            if(absolute < compared and absolute < 0.95):
                big = average
                keySize = k
                absolute = compared

        print("Big :{} and key: {}".format(big,keySize))

        k += 1
    print("About to solve: ",text)
    solve_problem(text,keySize)
    # k -=1
    # print("k: ",k)
    



if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    # cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()

    # for me to read in file instead 
    cipher = open(sys.argv[1], 'r').read().replace("\n", "").replace(" ", "").upper()
    print(len(cipher))
    # print("\nPop variance: ",pop_var(cipher))
    # keywordshere = 11,5,24,15,18,4,19,8,5,18,5
    en = encrypt(cipher, "clothes")
    print("\n",en)
    # print("\n", en,end='',sep='',flush=True)
    # print("\n",decrypt(en,"keyword"),end='',sep='',flush=True)
    # sys.stdout.write(en)

    runner(en,2,13)
    # print(compare_let_freq(cipher))
    # keySize = 6
    

    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
