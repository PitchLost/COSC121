'''Assignment #1'''

def get_translations(translations): 
    '''Get the translations from a string and return a list of tuples'''
    translations = translations.splitlines()

    translations_tuple = []
    for string in translations:
        translations_tuple.append(tuple(string.split(',')))
    
    translations_order = translations_tuple.pop(0)

    # Check the translations order
    for i in range(len(translations_order)):
        if translations_order[i] != 'māori' and translations_order[i] != 'english':
            return 'Header language not recognized!'


    return translations_tuple

        
        

	
string = '''māori,english
Aotearoa,New Zealand
Te Ika-a-Māui,North Island
Te Waipounamu,South Island
Te Whanganui a Tara,Wellington
Ōtautahi,Christchurch
Kirikiriroa,Hamilton
Tāmaki Makaurau,Auckland
'''

for terms in get_translations(string):
    print(terms)