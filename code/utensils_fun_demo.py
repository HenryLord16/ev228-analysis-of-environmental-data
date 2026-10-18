'''utensils_fun_demo
Demonstrate plotting counts in discrete bins with utensil choices using 
functions.
'''
from icecream import ic
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

font_path = '/Users/danielhueholt/Library/Fonts/'
for font in fm.findSystemFonts(font_path):
    fm.fontManager.addfont(font)

def bar_by_utensils(dict_names):
    ''' Demonstrate plotting counts in discrete bins with utensil choices '''
    ic(dict_names)
    chosen_utensils = [
        len(dict_names["knife"]), len(dict_names["spoon"]), 
        len(dict_names["fork"]), len(dict_names["chopsticks"]), 
        len(dict_names["tongs"])]
    utensil_names = ['Knife', 'Spoon', 'Fork', 'Chopsticks', 'Tongs']
    plt.rcParams.update({'font.family': 'Figtree'})
    fig, ax = plt.subplots()
    ax.bar(utensil_names, chosen_utensils, color='#6e7aaa')
    plt.xlabel('Utensils', fontsize=14)
    plt.xticks(fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.yticks(fontsize=14)
    plt.title('Number of people choosing each utensil')
    plt.savefig('/Users/danielhueholt/Documents/Figures/ev228_fig/utensils_2026.pdf')

#  Enter names of people who chose each utensil here
dict_names_b326 = {
    "knife": [],
    "spoon": [],
    "fork": [],
    "chopsticks": [],
    "tongs": [],
}

bar_by_utensils(dict_names_b326)