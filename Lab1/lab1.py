#Yusuf Bahadur CPE 202
#* Section 1 (Git)

"persnickety"

#* Section 2 (Data Definitions)

#* 1)
#a fahren is an float for fahrenheit temperature in degrees
#a cels is a float for celsius temperature in degrees celsius


#* 2)
# a Price_data is the database of prices of goods
# a price is an integer for the cost for a good denoted in cents of the good.
class Price_data:
    def __init__(self, price):
        self.price = price
    def __eq__(self, other):
        return self.price == other.price
    def __repr__(self):
        return("Cost of Good:(%f)" %(self.price))

#* 3)
#a Price_record is a combination of a good name as a string and the price of such good as an integer
class Price_record:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.price == other.price and self.name == other.name
    def __repr__(self):
        return("Good:(%s) Price:(%d)" % (self.name, self.price))

#* 4)
#an open_tab is a string that contains a URL and the date_visited
#a URL is a string representing the web address of a website
#a date_visited is a string representing the last date a website was accessed in (MM/DD/YY) format
class Open_tab:
    def __init__(self, URL, date):
        self.URL = URL
        self.date = date
    def __eq__(self, other):
        return self.URL == other.URL and self.date == other.date
    def __repr__(self):
        return("URL: (%s) Date: (%s)" % (self.URL, self.date))

#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)
# int -> int
# function accepts a price and adds sales tax

def price_total(price):
    pass

#* 2)
# string -> int
# function that looks up the price of an item in the stores database
def find_item(item):
    pass


#* 3)
# string, list -> int
# function that calculates the median income of a location in a database in which the location and database are given
def med_geo(region, database):
    pass

#* 4)
# string, list -> list
# function that checks which city in a given database overlap with a given region area
def city_overlap(region, database):
    pass

#* Section 4 (Test Cases)

#* 1)
#float float float -> float
#a function that takes three integers and returns the second largest value
def med(first, second, third):
    pass

import unittest
class TestCase(unittest.TestCase):
    def test_second_largest_1(self):
        self.assertEqual(med(3, 5, 4), 4)
    def test_second_largest_2(self):
        self.assertEqual(med(8, 9, 13), 9)
#* 2)
# string -> boolean
# a function that returns True if a given string has no uppercase letters
def upper(word):
    pass

class TestCase(unittest.TestCase):
    def test_capital_1(self):
        self.assertEqual(upper('hello'), True)
    def test_capital_2(self):
        self.assertEqual(upper('WhaT'), False)
#* 3)
# string string -> string
# a function that accepts to given states and returns the most northern state
def north(state, state1):
    pass

class TestCase(unittest.TestCase):
    def test_north_1(self):
        self.assertEqual(north("Georgia", "Oregon"), "Oregon")
    def test_north_2(self):
        self.assertEqual(north("Texas", "Washington"), "Washington")
    def test_north_3(self):
        self.assertEqual(north("Colorado", "Colorado"), "Colorado")

#* Section 5 (Whole Functions)

#* 1)
# a length is the number of feet specified
# float -> float
# the f2m function takes a given length in feet and returns the required meters

def f2m(feet):
    m = feet / 3.28
    return m


#* 2)
#a musical note represents both the pitch and duration of music segment
#a pitch is a sound frequency represented in Hz of the musical note
#a duration is the length of the note represented in seconds
#the Musical_Note class stores both the pitch and duration of the Musical Note
class Musical_Note:
    def __init__(self, pitch, duration):
        self.pitch = pitch #a pitch
        self.duration = duration #a duration
    def __repr__(self):
        return("Pitch(%f), Duration(%f)" % (self.pitch, self.duration))
    def __eq__(self, other):
        return self.pitch == other.pitch and self.duration == other.duration

#* 3)
# class -> class
# the up_one_octave function takes a note and doubles the pitch. It then returns the new note with a higher octave
#the pitch is specified in frequency Hz (float)

def up_one_octave(note):
    return Musical_Note(note.pitch * 2, note.duration)

#* 4)
#***********************************************************************************************test func
# class -> None
#the up_one_octave_m function takes in a note class mutates the note.pitch.
def up_one_octave_m(note):
    x_d = (note.pitch) * 2
    note.pitch = x_d



import unittest
class TestCase(unittest.TestCase):
    def test_f2m_1(self):
        self.assertAlmostEqual(f2m(25), 7.62195121)

    def test_up_one_octave_1(self):
        note = Musical_Note(4, 3.5)
        self.assertEqual(up_one_octave(note), Musical_Note(8, 3.5))

    def test_up_one_octave_m(self):
        note = Musical_Note(10, 8)
        self.assertEqual(up_one_octave_m(note), None)
        self.assertEqual(note, Musical_Note(20, 8))
