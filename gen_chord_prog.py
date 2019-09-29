from random import randint


def rand_chord_num(low,high):
    return randint(low,high)

def rand_prog(length):
    chord_prog = []
    for i in range(int(length)):
        chord_prog.append(rand_chord_num(1,6))
    return chord_prog

key_chord_chart = [["Key","I","ii","iii","IV","V","vi"],
                   ["C","C","Dm","Em","F","G","Am"],
                   ["C#","C#","D#m","E#m","F#","G#","A#m"],
                   ["Db","Db","Ebm","Fm","Gb","Ab","Bbm"],
                   ["D","D","Em","F#m","G","A","Bm"],
                   ["Eb","Eb","Fm","Gm","Ab","Bb","Cm"],
                   ["E","E","F#m","G#m","A","B","C#m"],
                   ["F","F","Gm","Am","Bb","C","Dm"],
                   ["F#","F#","G#m","A#m","B","C#","D#m"],
                   ["Gb","Gb","Abm","Bbm","Cb","Db","Ebm"],
                   ["G","G ","Am","Bm","C","D","Em"],
                   ["Ab","Ab","Bbm","Cm","Db","Eb","Fm"],
                   ["A","A","Bm","C#m","D","E","F#m"],
                   ["Bb","Bb","Cm","Dm","Eb","F","Gm"],
                   ["B","B","C#m","D#m","E","F#","G#m"],
                   ["Cb","Cb","Dbm","Ebm","Fb","Gb","Abm"]]

def pick_key():
    keynum = rand_chord_num(1,len(key_chord_chart))
    key = key_chord_chart[keynum][0]
    return key, keynum

def print_key(key):
    for i in range(7):
        if i == 0:
            print("{}:\t{}".format(key_chord_chart[0][i], key_chord_chart[keynum][i]))
            print("--------------\n")
        else:
            print("{}:\t{}".format(key_chord_chart[0][i], key_chord_chart[keynum][i]))

def rand_chord_names(key, rand_chords):
    for i in range(len(rand_chords)):
        print("{}:\t{}".format(key_chord_chart[0][rand_chords[i]],key_chord_chart[key][rand_chords[i]]))
            
def rand_chords(movements):
    chord_nums = rand_prog(movements)
    return chord_nums

key, keynum = pick_key()
print_key(key)
print("\nRandom Chord Progression")
print("---------\n")
for i in range(2):
    rand_chord_names(keynum,rand_chords(4))
    print("\n---------\n")
