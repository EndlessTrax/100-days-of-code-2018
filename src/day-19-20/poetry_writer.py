'''
Write a script poetry_writer.py based on the poem generator created in chapter Lists and Dictionaries 
that assists the user in creating beautiful poetry through a GUI.
1. The user should be instructed (in a label) to enter words into each list, separating words with commas. 
    You can use the string split() method to generate lists of individual words.
2. Provide a grid layout with labels for Nouns, Verbs, Adjectives, Prepositions and Adverbs, 
    where the user can supply a list of words for each by typing them into entry boxes.
3. Add a “Create your poem” button centered at the bottom of the window that, when clicked, 
    will generate and display a random poem in a label below the button. If the user does not supply enough words, 
    the “poem” label should instead display text letting the user know the error.
4. Add a “Save your poem” button centered below the poem that, when clicked, allows the user to save the poem
    currently being displayed as a “.TXT” file by prompting the user with a “Save As” dialog box. 
    Add a default file extension of “.txt” and make sure that your program does not generate an error if the user 
    clicks “Cancel” on the file save dialog box.
5. You can assume that the user will not supply any duplicate words in any of the word lists.
6. Bonus: Add a function checkUnique() that takes a list of words as an argument and returns True or False based on
    whether or not that list contains only unique entries. Use this function to alert the user if duplicate words are
    present within any of the word lists by displaying the error in the “poem” label. 
    (Without this check, we run the risk of our program entering an infinite loop!)
'''

from tkinter import *
from random import choice
from tkinter import filedialog


# Empty Lists for later
noun = []
verb = []
adjective = []
preposition = []
adverb = []


class App(Frame):
    ''' Instantiate the App '''
    def __init__(self, master):
        Frame.__init__(self, master)


def save_file():
    ''' Save File '''
    type_list = [("Text files", "*.txt")]
    file_name = filedialog.asksaveasfilename(filetypes=type_list,
                                             defaultextension=".txt")
    if file_name != "":
        output_file = open(file_name, "w")
        output_file.writelines(result_poem.cget("text"))
        output_file.close()


def make_poem():
   ''' Create a randomly generated poem '''
    # Add the users words to empty lists
    nouns = noun_entry.get().split(',')
    for n in nouns:
        noun.append(n)
    verbs = verb_entry.get().split(',')
    for v in verbs:
        verb.append(v)
    adjectives = adjective_entry.get().split(',')
    for adj in adjectives:
        adjective.append(adj)
    prepositions = preposition_entry.get().split(',')
    for p in prepositions:
        preposition.append(p)
    adverbs = adverb_entry.get().split(',')
    for ad in adverbs:
        adverb.append(ad)
        
    # Pull three nouns randomly
    n1 = choice(noun)
    n2 = choice(noun)
    n3 = choice(noun)
    
    # Make sure that all the nouns are different
    while n1 == n2:
        n2 = choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = choice(noun)

    # Pull three different verbs
    v1 = choice(verb)
    v2 = choice(verb)
    v3 = choice(verb)
    while v1 == v2:
        v2 = choice(verb)
    while v1 == v3 or v2 == v3:
        v3 = choice(verb)

    # Pull three different adjectives
    adj1 = choice(adjective)
    adj2 = choice(adjective)
    adj3 = choice(adjective)
    while adj1 == adj2:
        adj2 = choice(adjective)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = choice(adjective)

    # Pull two different prepositions
    prep1 = choice(preposition)
    prep2 = choice(preposition)
    while prep1 == prep2:
        prep2 = choice(preposition)

    # Pull one adverb
    adv1 = choice(adverb)

    if "aeiou".find(adj1[0]) != -1:  # first letter is a vowel
        article = "An"
    else:
        article = "A"

    # Add lines to poem
    poem = "{} {} {}\n\n".format(article, adj1, n1)
    poem = poem + "{} {} {} {} {} the {} {}\n".format(
        article, adj1, n1, v1, prep1, adj2, n2
    )
    poem = poem + "{}, the {} {}\n".format(adv1, n1, v2)
    poem = poem + "the {} {} {} a {} {}".format(n2, v3, prep2, adj3, n3)

    result_poem.config(text=poem)


# Make the window
window = Tk()
window.geometry("400x600")

# Make some Labels
main_label = Label(text="Please enter a list of words below to create your poem.") 
main_label_2 = Label(text="(Please separate words by a comma.)")
noun_label = Label(text="Nouns")
verb_label = Label(text="Verbs")
adjective_label = Label(text="Adjectives")
preposition_label = Label(text="Prepositions")
adverb_label = Label(text="Adverbs")
result_poem = Label()

# Make entry boxes
noun_entry = Entry(width=50)
verb_entry = Entry(width=50)
adjective_entry = Entry(width=50)
preposition_entry = Entry(width=50)
adverb_entry = Entry(width=50)

# Make buttons
make_poem_button = Button(text="Make Poem", command=make_poem)
save_poem_button = Button(text="Save Poem", command=save_file)

# Add everything to the window using grid
# Start with labels
main_label.grid(row=1 , column=2 , sticky=N)
main_label_2.grid(row=2, column=2, sticky=N)
noun_label.grid(row=3, column=1, sticky=E)
verb_label.grid(row=4, column=1, sticky=E)
adjective_label.grid(row=5, column=1, sticky=E)
preposition_label.grid(row=6, column=1, sticky=E)
adverb_label.grid(row=7, column=1, sticky=E)
# Add entry boxes
noun_entry.grid(row=3, column=2, sticky=W)
verb_entry.grid(row=4, column=2, sticky=W)
adjective_entry.grid(row=5, column=2, sticky=W)
preposition_entry.grid(row=6, column=2, sticky=W)
adverb_entry.grid(row=7, column=2, sticky=W)
# Add buttons
make_poem_button.grid(row=8, column=2)
save_poem_button.grid(row=9, column=2)
# Add space for the poem
result_poem.grid(row=10, column=1, rowspan=5, columnspan=2)


def main():
    ''' Main function '''  
    my_app = App(window)
    my_app.master.title("Poetry Writer")
    my_app.mainloop()


if __name__ == '__main__':
    main()