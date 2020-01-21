#Herodotus: The_Story_Composer
#By Emmanuel.O

import random

def first_para():
#Print first paragraph
    choice = random.randrange(0,3)
    if choice == 0:
        print "Jack is a young, poor boy living with his widowed mother Rose, with a dairy cow on a farm cottage."
        print "The cow's milk was their only source of income. When the cow stops giving milk, Jack's mother tells"
        print "him to take her to the market to be sold. On the way, Jack meets a bean dealer who offers magic beans"
        print "in exchange for the cow, and Jack makes the trade. When he arrives home without any money," 
        print "his mother-Rose becomes angry, throws the beans out of the window, and sends Jack to bed without dinner."
    elif choice == 1:
        print "In 1912 Southampton, 17-year-old first-class passenger Rose Bukater, her fiance Cal Hockley, and her mother"
        print "Ruth board the luxurious Titanic. Ruth emphasizes that Rose's marriage will resolve their family's financial"
        print "problems and allow them to retain their upper-class status. Distraught over the engagement, Rose climbs over"
        print "the stern and contemplates suicide; Jack Dawson, a penniless artist, intervenes and discourages her."
        print "Discovered with Jack, Rose tells a concerned Cal that she was peering over the edge and Jack"
        print "saved her from falling. When Cal becomes indifferent, she suggests to him that Jack deserves"
        print "a reward. He invites Jack to dine with them in first-class the following night. Jack and Rose"
        print "develop a tentative friendship, despite Cal and Ruth being wary of him. Following dinner, Rose "
        print "secretly joins Jack at a party in third class."
    elif choice == 2:
        print "School-teacher-turned-writer Jack Torrance arrives at the remote Overlook Hotel in the Rocky Mountains to"
        print "be interviewed for the position of winter caretaker. The hotel, which opened in 1909 and was built on the"
        print "site of a Native American burial ground, closes during the snowed-in months. Once hired, Jack plans to use"
        print "the hotel's solitude to write. Manager Stuart Ullman tells Jack about the hotel's history and warns him about"
        print "its reputation: a previous caretaker supposedly developed cabin fever and killed his family and himself."
        print "Despite the troubling story, Jack is impressed with the hotel and gets the job."

def second_para():
#Print second paragraph
    choice = random.randrange(0,3)
    if choice == 0:
        print "During the night, a gigantic beanstalk has grown outside Jack's window. The next morning, Jack climbs the"
        print "beanstalk to a land high in the sky. He finds an enormous castle and sneaks in. Soon after, the castle's"
        print "owner, a giant, returns home. He smells that Jack is nearby, and speaks a rhyme. The giant's wife persuades"
        print "him that he is mistaken and helps Jack hide because the woman knows that he is poor. When the giant falls"
        print "asleep, Jack steals a bag of gold coins and makes his escape down the beanstalk to return home. Unbeknownst"
        print "to Jack he had taken back home with him a little more than a bag of gold coins."
    elif choice == 1:
        print "After braving several obstacles, Jack and Rose return to a boat deck. The lifeboats have departed and"
        print "passengers are falling to their deaths as the stern rises out of the water. The ship breaks in half, dropping"
        print "the stern into the water. Jack and Rose ride it into the ocean and he helps her onto a wooden panel buoyant"
        print "enough for only one person. He assures her that she will die an old woman, warm in her bed. Jack dies of"
        print "hypothermia but Rose is saved. Alas this is not the end!"
    elif choice == 2:
        print "With a sudden feeling of dread, she goes out in search of Jack. While searching for Jack, She discovers that"
        print "her now-deranged man has been typing pages filled with the phrase 'All work and no play makes Jack a dull boy."
        print "She begs Jack to leave, but he threatens her. Rose knocks him unconscious with a baseball bat and locks"
        print "him in the kitchen pantry. Jack converses through the pantry door and moments later the door is unlocked,"
        print "freeing Jack."

def third_para():
#Print third paragraph
    choice = random.randrange(0,3)
    if choice == 0:
        print "We see a world where Jack learns of a unique treasure of a magic harp which plays by itself. Jack then calls"
        print "to his mother for an axe before the giant that is death reaches him, causing the giant to fall. Fear and pain"
        print "now far and far away. Forever."
    elif choice == 1:
        print "We are then taken to a vision where Jack and Rose, his dear one are together again, happy, as it once was."
    elif choice == 2:
        print "Jack starts chanting and drawing the word 'REDRUM' When Rose sees the word reversed in the mirror,"
        print "the word is revealed to be 'MURDER'. Jack hacks through the quarters' already detached main door"
        print "with an axe and pursues her. Rose lays a false trail to mislead Jack and hides."
        print "She escapes from the hands of malevolence, while Jack freezes to death."

def heading():
#Print title
    title = random.randrange(0,8)	
    if title == 0:
        print "Love at Night:"
    elif title == 1:
        print "Jack:"
    elif title == 2:
        print "Spell Danger:"
    elif title == 3:
        print "Rose's Beloved:"
    elif title == 4:
        print "Gentle Jack:"
    elif title == 5:
        print "A different Day:"
    elif title == 6:
        print "A Penny for your Kisses:"
    elif title == 7:
        print "A Violent Day:"
  
def compose_story():
#Collate and compose stories
    print "Herodotus: A tale I have for you my friend, and I tell it as I so remember it"
    print" "
    heading()
    first_para()
    second_para()
    third_para()
    print" "
    print "That is it for now, my friend. But maybe an ending can be a new beginning"

compose_story()
