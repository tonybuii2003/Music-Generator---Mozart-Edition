# PHI LONG BUI
# lpbui
# 14555975
#
# 29/09/21
# musical_dice_game.py

import random
import simpleaudio as player
import wave
# Each of these lists corresponds to one column of the table used for the minuet
# portion Mozart's Musical Dice Game. The first two elements are set to None
# because, there is no way for a roll of two dice to return a 0 or a 1. Only the
# indices that can be the result of the roll of two dice have a value.
# Each value is the number labelling a possible musical choice for that measure.
mm01 = [None, None, "96", "32", "69", "40",
        "148", "104", "152", "119", "98", "3", "54"]
mm02 = [None, None, "22", "6", "95", "17",
        "74", "157", "60", "84", "142", "87", "130"]
mm03 = [None, None, "141", "128", "158", "113",
        "163", "27", "171", "114", "42", "165", "10"]
mm04 = [None, None, "41", "63", "13", "85",
        "45", "167", "53", "50", "156", "61", "103"]
mm05 = [None, None, "105", "46", "153", "161",
        "80", "154", "99", "140", "75", "135", "28"]
mm06 = [None, None, "122", "46", "55", "2",
        "97", "68", "133", "86", "129", "47", "37"]
mm07 = [None, None, "11", "134", "110", "159",
        "36", "118", "21", "169", "62", "147", "37"]
mm08 = [None, None, "30", "81", "24", "100",
        "107", "91", "127", "94", "123", "33", "5"]
mm09 = [None, None, "70", "117", "66", "90",
        "25", "138", "16", "120", "65", "102", "35"]
mm10 = [None, None, "121", "39", "139", "176",
        "143", "71", "155", "88", "77", "4", "20"]
mm11 = [None, None, "26", "126", "15", "7",
        "64", "150", "57", "48", "19", "31", "108"]
mm12 = [None, None, "9", "56", "132", "34",
        "125", "29", "175", "166", "82", "164", "92"]
mm13 = [None, None, "112", "174", "73", "67",
        "76", "101", "43", "51", "137", "144", "12"]
mm14 = [None, None, "49", "18", "58", "160",
        "136", "162", "168", "115", "38", "59", "124"]
mm15 = [None, None, "109", "116", "145", "52",
        "1", "23", "89", "72", "149", "173", "44"]
mm16 = [None, None, "14", "83", "79", "170",
        "93", "151", "172", "111", "8", "78", "131"]

# This table contains all of the columns of the minuet portion of Mozart's
# Musical Dice Game in order.
minuet_table = [mm01, mm02, mm03, mm04, mm05, mm06, mm07, mm08,
                mm09, mm10, mm11, mm12, mm13, mm14, mm15, mm16]

# Each of these lists corresponds to one column of the table used for the trio
# portion Mozart's Musical Dice Game. The first two elements are set to None
# because, there is no way for a roll of two dice to return a 0 or a 1. Only the
# indices that can be the result of the roll of one die have a value.
# Each value is the number labelling a possible musical choice for that measure.
tm01 = [None, "72", "56", "75", "40", "83", "18"]
tm02 = [None, "6", "82", "39", "73", "3", "45"]
tm03 = [None, "59", "42", "54", "16", "28", "62"]
tm04 = [None, "25", "74", "1", "68", "53", "38"]
tm05 = [None, "81", "14", "65", "29", "37", "4"]
tm06 = [None, "41", "7", "43", "55", "17", "27"]
tm07 = [None, "89", "26", "15", "2", "44", "52"]
tm08 = [None, "13", "71", "80", "61", "70", "94"]
tm09 = [None, "36", "76", "9", "22", "63", "11"]
tm10 = [None, "5", "20", "34", "67", "85", "92"]
tm11 = [None, "46", "64", "93", "49", "32", "24"]
tm12 = [None, "79", "84", "48", "77", "96", "86"]
tm13 = [None, "30", "8", "69", "57", "12", "51"]
tm14 = [None, "95", "35", "58", "87", "23", "60"]
tm15 = [None, "19", "47", "90", "33", "50", "78"]
tm16 = [None, "66", "88", "21", "10", "91", "31"]

# This table contains all of the columns of the trio portion of Mozart's
# Musical Dice Game in order.
trio_table = [tm01, tm02, tm03, tm04, tm05, tm06, tm07, tm08,
              tm09, tm10, tm11, tm12, tm13, tm14, tm15, tm16]

# This function takes a string as an argument and constructs a string that names
# one of the wav audio files that contains a measure of music for the minuet
# portion of Mozart's Musical Dice Game.


def minuet_filename(mmid):
    result = 'M'+mmid+'.wav'
    return result

# This function takes a string as an argument and constructs a string that names
# one of the wav audio files that contains a measure of music for the trio
# portion of Mozart's Musical Dice Game.


def trio_filename(tmid):
    result = 'T' + tmid + '.wav'
    return result

# This function takes a single interger, named 'num' as its argument. It
# generates the result of rolling 'num' many 6-sided dice.


def roll_dice(num):
    sum = 0
    for i in range(0, num):
        sum += random.randint(1, 6)
    return sum

# Inside this main function you will randomly select 16 measures from the minuet
# table, one from each column of the minuet table, and then randomly select, 16
# measures from the trio table, one from each column of the trio table. Each
# measure is represented by a string numeral, and corresponds to the name of a
# wav audio file that plays the selected measure of music.
# You must then access each of the selected wav files and play them using
# simpleaudio's interface. Make sure you wait for each measure to finish before
# playing the next measure.


def construct_waltz():
    column1 = []
    column2 = []
    play = []
    # file directory
    fileDirectory = (
        "/Volumes/GoogleDrive/My Drive/SBU/TERMS/Fall_2021/IAE101/project1/mozart/")
    for i in minuet_table:  # roll the dice twice then add the element into column1
        num1 = i[roll_dice(2)]
        column1.append(num1)
    for i in trio_table:  # roll the dice once then add the elements into column2
        num2 = i[roll_dice(1)]
        column2.append(num2)
    for i in column1:
        # format every element inside column1 into M'element'.wav then add them to play[]
        play.append(fileDirectory+minuet_filename(str(i)))
    for i in column2:
        # format every element inside column1 into T'element'.wav then add them to play[]
        play.append(fileDirectory+trio_filename(str(i)))
    for i in play:  # read every element in play[] using simpleaudio. The elements in play are files' directory
        wave_read = wave.open(i, 'rb')
        audio_data = wave_read.readframes(wave_read.getnframes())
        num_channels = wave_read.getnchannels()
        bytes_per_sample = wave_read.getsampwidth()
        sample_rate = wave_read.getframerate()
        play_obj = player.play_buffer(
            audio_data, num_channels, bytes_per_sample, sample_rate)
        play_obj.wait_done()


if __name__ == "__main__":
    construct_waltz()
