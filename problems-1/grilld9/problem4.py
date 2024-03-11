import unittest

orig_print = print
song = []
s = ""
def mock_print(string, **kwargs):
    song.append(string)

print = mock_print

def sing_the_song():

    green = "green"
    bottle = "bottle"
    templ_wall = "hanging on the wall"
    templ_fall = "should accidentally fall"
    templ_will = "There’ll be"
    amounts = ["ten", "nine", "eight", "seven", "six", "five", "four", "three", "two", "one", "no"]
    for i in range(10):
        print("{} {} {} {},".format(amounts[i].capitalize(), green, bottle if i == 9 else bottle + "s", templ_wall))
        print("{} {} {} {},".format(amounts[i].capitalize(), green, bottle if i == 9 else bottle + "s", templ_wall))
        print("{} {} {} {} {},".format("And if", amounts[9], green, bottle, templ_fall))
        print("{} {} {} {} {}.".format(templ_will, amounts[i+1], green, bottle if i + 1 == 9 else bottle + "s", templ_wall))

sing_the_song()

print = orig_print
song = "\n".join(song)

class BottleSongTest(unittest.TestCase):

    def test(self):
        self.assertEqual(song,
"""Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be nine green bottles hanging on the wall.
Nine green bottles hanging on the wall,
Nine green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be eight green bottles hanging on the wall.
Eight green bottles hanging on the wall,
Eight green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be seven green bottles hanging on the wall.
Seven green bottles hanging on the wall,
Seven green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be six green bottles hanging on the wall.
Six green bottles hanging on the wall,
Six green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be five green bottles hanging on the wall.
Five green bottles hanging on the wall,
Five green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be four green bottles hanging on the wall.
Four green bottles hanging on the wall,
Four green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be three green bottles hanging on the wall.
Three green bottles hanging on the wall,
Three green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be two green bottles hanging on the wall.
Two green bottles hanging on the wall,
Two green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be one green bottle hanging on the wall.
One green bottle hanging on the wall,
One green bottle hanging on the wall,
And if one green bottle should accidentally fall,
There’ll be no green bottles hanging on the wall.""")