"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurant_small.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    name_to_rating, price_to_names, cusine_to_names = read_restaurant(file)

    
    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cusine(names_matching_price, cusine_to_names, cusines_list)
 
    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result


def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names_final = ['Queen St. Cafe', 'Dumplings R Us']
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """
    list1=[]
    list2 = []
    
    for name in names_final:
        #making a list [%rating, restaurant name] for each restaurant in names_final.
        list1 = name_to_rating[name], name
        #making a list of lists withh all rating and names of restaurants in names_final. 
        list2.append(list1)
    #returning list of lists which are sorted by % rating of a restauarants.
    sorted_list = sorted(list2,key=lambda x: x[0],  reverse = True) 
    return sorted_list

    


    
def filter_by_cusine(names_matching_price,cusine_to_names,cusine_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuis = 'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """
    names_of_restaurants = []
    
    for cus in cusine_list:
        for nam in names_matching_price:
            if nam in cusine_to_names[cus]:
              names_of_restaurants.append(nam)              
    return names_of_restaurants
        
        

def read_restaurant(file):
    """(file) - > (dict,dict,dic)

    Return a touple of three dictonaries based on the information  in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    """
    #creating dict which will store data from file
    name_to_rating = {}
    price_to_names = {'$':[], '$$' : [], '$$$' : [], '$$$$' : []}
    cusine_to_names = {}
    
    name = open(FILENAME,"r")
    i= 0
    restaurant_name=''
    rating=''
    price=''
    cusine= ''
    for line in name:
        if i == 0:
            restaurant_name = line.strip()
            i = i +1
        elif i ==1:
            rating = line.strip()
            i = i +1
        elif i ==2:
            price = line.strip()
            i = i +1
        elif i ==3:
            cusine = line.strip()
            i = i +1
        elif i ==4:
            name_to_rating[restaurant_name] = rating
            price_to_names[price] = restaurant_name
            cusine_to_names[cusine] = restaurant_name
            i=0
    print('name to rating: ', name_to_rating)
    print('price to names: ', price_to_names)
    print('cusine to names: ', cusine_to_names)
        
        
    
    
