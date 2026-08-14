    # Seatwork 1
from pyscript import display, document

fullname = 'Alexa Marie dela Peña Cunanan' # string
ag3_s = 15 # integer
h3ight = 168 # integer
countries_ = ['Switzerland', 'Egypt', 'Spain'] #list
student_type = False # boolean
student_info = {
    'color': 'Pink',
    'car_brand': 'Tesla',
    'shoe_size': 7,
    'best_friend': 'Carlos Ezequiel Barja Borromeo'
} # dictionary
favorite_fruits = {'Mango', 'Banana', 'Strawberry', 'Rambutan', 'Pear'} # set
days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') # tuple

display(f'hello! My name is {fullname}. I am {ag3_s} years old.', target='result')
document.getElementById('result').innerHTML = f''' Hello! My name is <i>{fullname}</i>. <br> 
I am currently {ag3_s} years old, turning 16 on the 13th of November. <br> 
My height as of now is {h3ight} cm. 

<br><br>

The countries that I wish to visit are the following: {countries_} <br><br>

Am I a new student? {student_type} <br> 
My student information: {student_info} <br><br>

I love {favorite_fruits} <br>
The days of the week are: {days_week}. '''