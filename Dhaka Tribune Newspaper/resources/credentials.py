import random
import string

class Constantinope:
    dhakatribune = "https://bangla.dhakatribune.com/"

    automation_text = "Automation_user_"

    ran_words = "created by Automation  " + ( ''.join(random.choice(string.ascii_letters) for i in range(40)) )
    ran_numbers = ( ''.join(random.choice(string.digits) for i in range(10)) )

    ran_username = automation_text + ( ''.join(random.choice(string.ascii_letters) for i in range(3)))
    ran_email = "Automated_email_" + ( ''.join(random.choice(string.ascii_letters) for i in range(2))) + "@gmail.com"
    
