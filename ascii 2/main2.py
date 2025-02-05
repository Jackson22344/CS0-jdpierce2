"""
    StdIO Lab 1B
    ASCII Art 2 - using literals and variables
    
    Updated By: Jackson Pierce 
    Date: ... 2/4/25
    
    This program produces an ASCII art on the console.
    It should look something like this.


         /\         ************************************************************      /~~   ~~\
        /##\                                                                       /~~         ~~\
       /#""#\                               Ascii Art 2                           {               }
      /#"##"#\                                 CS110                               \  _-     -_  /
     /#"#""#"#\                              Spring 25                              ~  \\   //  ~
    /#"#CMU!#"#\                            Corin Chepko                          _- -   | | _- _
         ||                                                                         _ -  | |   -_
         ||         ************************************************************        // \\

    Algorithm steps: 
    1. Use variables to store art and data
    2. Write a series of print statements to print the data/values to the console, using the .center() method
        to keep the strings centered.
    
    Note: You can add more lines or print differt ASCII arts of your choice if you'd like...
"""
name = input("What is your name? ")   
print("Nice meeting you, " + name + "\n") 

# prompt user to enter the semester and store the value into semester variable using input function
semester: str = input("What semester is this [Fall/Spring]? ")

# FIXME5: prompt user to enter the course name and store the value into a variable using input function
course: str = input("What is the name of this course? ")

# FIXME6: prompt user to enter the lab title and store the value into a variable using input function
lab: str = input("Enter this labs title ")
print("Hope you like my ASCII art...\n\n")

# construct the art using set of three strings, one for art on the left, 
# one for the center text, and one for the art on the right
# We use 16 spaces for each art column and 30 spaces for the text in the center and border
left_width = 20
right_width = 20
center_width = 40  # Can change for smaller screens

# The extra spaces are not nessesary, but I used them to help line up the art
treeA_1: str = "      /\\     "
treeA_2: str = "     /##\\    "
treeA_3: str = "    /#\"\"#\\    "
treeA_4: str = "   /#\"##\"#\\   "
treeA_5: str = "  /#\"#\"\"#\"#\\ "
treeA_6: str = "  /#\"#CMU!#\"#\ "
treeA_7: str = "        ||       "
treeA_8: str = "        ||       "

treeB_1: str = "   /~~   ~~\\  "
treeB_2: str = "  /~~         ~~\\"
treeB_3: str = "  {               } "
treeB_4: str = "   \  _-     -_  / "
treeB_5: str = "    ~  \\\   //  ~  "
treeB_6: str = "  _- -   | | _- _   "
treeB_7: str = "    _ -  | |   -_  "
treeB_8: str = "        // \\\       "
# FIXMEs7-8: use variables to add the rest of the art

asterics: str = "*"*center_width
spaces: str = " "*center_width
text: str = " Ascii Art 2 "
text2: str = " CS110 "
text3: str = " Spring 25 "
text4: str = " Corin Chepko "

print(treeA_1.center(left_width) + asterics.center(center_width) + treeB_1.center(right_width))
print(treeA_2.center(left_width) + spaces.center(center_width) + treeB_2.center(right_width))
print(treeA_3.center(left_width) + text.center(center_width) + treeB_3.center(right_width))
print(treeA_4.center(left_width) + text2.center(center_width) + treeB_4.center(right_width))
print(treeA_5.center(left_width) + text3.center(center_width) + treeB_5.center(right_width))
print(treeA_6.center(left_width) + text4.center(center_width) + treeB_6.center(right_width))
print(treeA_7.center(left_width) + spaces.center(center_width) + treeB_7.center(right_width))
print(treeA_8.center(left_width) + asterics.center(center_width) + treeB_8.center(right_width))

# FIXME9-10: print the rest of the art, including the collected name, lab title, course, and semester
# Note: You can add more lines or print differt ASCII arts of your choice if you'd like...

print("\nGood bye...  \n")