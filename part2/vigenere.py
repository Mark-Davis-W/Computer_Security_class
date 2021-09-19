#!/usr/bin/python3

from os import sep
import sys
from collections import Counter, deque

#taken from Wikipedia
letter_freqs = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228,
    'G': 0.02015, 'H': 0.06094, 'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025,
    'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 'R': 0.05987,
    'S': 0.06327, 'T': 0.09056, 'U': 0.02758, 'V': 0.00978, 'W': 0.02361, 'X': 0.00150,
    'Y': 0.01974, 'Z': 0.00074
}

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def pop_var(s):
    """Calculate the population variance of letter frequencies in given string."""
    freqs = Counter(s)
    mean = sum(float(v)/len(s) for v in freqs.values())/len(freqs)  
    return sum((float(freqs[c])/len(s)-mean)**2 for c in freqs)/len(freqs)


def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
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

    text = [t for t in tx]
    # print(text)
    freq = [0] * 26
    total = float(len(text))
    for l in text:
        freq[ord(l) - ord('A')] += 1
    # print("compare: ",sum(abs(f / total - E) for f, E in zip(freq, engFreq)))
    return sum(abs(f / total - E) for f, E in zip(freq, engFreq))


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
            if(absolute < compared and 1.05 > absolute < 0.95):
                big = average
                keySize = k
                absolute = compared
            print()

        print("Big :{} and key: {}".format(big,keySize))

        k += 1
    # k -=1
    # print("k: ",k)
    



if __name__ == "__main__":
    # Read ciphertext from stdin
    # Ignore line breaks and spaces, convert to all upper case
    # cipher = sys.stdin.read().replace("\n", "").replace(" ", "").upper()

    # for me to read in file instead 
    cipher = open(sys.argv[1], 'r').read().replace("\n", "").replace(" ", "").upper()
    # print(cipher)
    # print("\nPop variance: ",pop_var(cipher))
    en = encrypt(cipher, "keywor")
    # print("\n", en,end='',sep='',flush=True)
    # print("\n",decrypt(en,"keyword"),end='',sep='',flush=True)
    # sys.stdout.write(en)

    runner(en,2,13)
    # keySize = 6
    

    #################################################################
    # Your code to determine the key and decrypt the ciphertext here
