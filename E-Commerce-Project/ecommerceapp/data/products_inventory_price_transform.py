import pandas as pd



aisles_by_department = {
    'missing': {
        'missing': {'price': 0, 'inventory': 1258},
    },
    'household': {
        'air fresheners candles': {'price': 3.99, 'inventory': 355},
        'cleaning products': {'price': 5.99, 'inventory': 655},
        'paper goods': {'price': 4.99, 'inventory': 322},
        'trash bags liners': {'price': 3.99, 'inventory': 112},
        'more household': {'price': 3.99, 'inventory': 308},
        'kitchen supplies': {'price': 4.99, 'inventory': 218},
        'food storage': {'price': 2.99, 'inventory': 206},
        'plates bowls cups flatware': {'price': 3.99, 'inventory': 199},
        'dish detergents' : {'price': 2.99, 'inventory': 125},
        'laundry' : {'price': 10.99, 'inventory': 250},
    },
    'international': {
        'asian foods': {'price': 5.99, 'inventory': 605},
        'indian foods': {'price': 6.99, 'inventory': 108},
        'kosher foods': {'price': 6.99, 'inventory': 169},
        'latino foods': {'price': 5.99, 'inventory': 257},
    },
    'babies': {
        'baby accessories': {'price': 4.99, 'inventory': 44},
        'baby bath body care': {'price': 4.99, 'inventory': 132},
        'baby food formula': {'price': 5.99, 'inventory': 718},
        'diapers wipes': {'price': 6.99, 'inventory': 187},
    },
    'bakery': {
        'bakery desserts': {'price': 3.99, 'inventory': 297},
        'bread': {'price': 4.99, 'inventory': 557},
        'breakfast bakery': {'price': 5.99, 'inventory': 226},
        'buns rolls': {'price': 3.99, 'inventory': 195},
        'tortillas flat bread': {'price': 4.99, 'inventory': 241},
    },
    'pantry': {
        'baking ingredients': {'price': 3.99, 'inventory': 623},
        'baking supplies decor': {'price': 2.99, 'inventory': 290},
        'condiments': {'price': 4.99, 'inventory': 466},
        'doughs gelatins bake mixes': {'price': 3.99, 'inventory': 463},
        'dry pasta': {'price': 2.99, 'inventory': 457},
        'oils vinegars': {'price': 4.99, 'inventory': 375},
        'preserved dips spreads': {'price': 3.99, 'inventory': 264},
        'salad dressing toppings': {'price': 3.99, 'inventory': 560},
        'pasta sauce': {'price': 3.99, 'inventory': 399},
        'spices seasonings': {'price': 4.99, 'inventory': 797},
        'spreads': {'price': 4.99, 'inventory': 493},
        'honeys syrups nectars': {'price': 4.99, 'inventory': 229},
        'marinades meat preparation': {'price': 4.99, 'inventory': 180},
        'pickled goods olives': {'price': 3.99, 'inventory': 50},
    },
    'personal care': {
        'beauty': {'price': 5.99, 'inventory': 178},
        'body lotions soap': {'price': 4.99, 'inventory': 504},
        'cold flu allergy': {'price': 6.99, 'inventory': 427},
        'deodorants': {'price': 3.99, 'inventory': 317},
        'digestion': {'price': 4.99, 'inventory': 338},
        'eye ear care': {'price': 5.99, 'inventory': 113},
        'facial care': {'price': 5.99, 'inventory': 277},
        'feminine care': {'price': 5.99, 'inventory': 285},
        'first aid': {'price': 4.99, 'inventory': 240},
        'muscles joints pain relief': {'price': 6.99, 'inventory': 172},
        'oral hygiene': {'price': 3.99, 'inventory': 565},
        'protein meal replacements': {'price': 6.99, 'inventory': 325},
        'shave needs': {'price': 4.99, 'inventory': 198},
        'skin care': {'price': 5.99, 'inventory': 245},
        'soap': {'price': 4.99, 'inventory': 525},
        'vitamins supplements': {'price': 6.99, 'inventory': 1038},
        'hair care': {'price': 8.99, 'inventory': 70},
    },
    'alcohol': {
        'beers coolers': {'price': 6.99, 'inventory': 385},
        'red wines': {'price': 9.99, 'inventory': 232},
        'white wines': {'price': 9.99, 'inventory': 147},
        'spirits': {'price': 19.99, 'inventory': 195},
        'specialty wines champagnes': {'price': 29.99, 'inventory': 95},
    },
    'snacks': {
        'candy chocolate': {'price': 2.99, 'inventory': 1246},
        'chips pretzels': {'price': 3.99, 'inventory': 989},
        'cookies cakes': {'price': 3.99, 'inventory': 874},
        'crackers': {'price': 2.99, 'inventory': 747},
        'energy granola bars': {'price': 3.99, 'inventory': 832},
        'fruit vegetable snacks': {'price': 4.99, 'inventory': 356},
        'mint gum': {'price': 1.99, 'inventory': 168},
        'popcorn jerky': {'price': 3.99, 'inventory': 316},
        'trail mix snack mix': {'price': 4.99, 'inventory': 69},
        'ice cream toppings': {'price': 3.99, 'inventory': 85},
        'nuts seeds dried fruit': {'price': 5.99, 'inventory': 70},
    },
    'beverages': {
        'cocoa drink mixes': {'price': 3.99, 'inventory': 223},
        'coffee': {'price': 7.99, 'inventory': 680},
        'energy sports drinks': {'price': 2.99, 'inventory': 294},
        'juice nectars': {'price': 4.99, 'inventory': 792},
        'refrigerated': {'price': 4.99, 'inventory': 675},
        'soft drinks': {'price': 2.99, 'inventory': 463},
        'tea': {'price': 3.99, 'inventory': 894},
        'water seltzer sparkling water': {'price': 1.99, 'inventory': 344},
    },
    'breakfast': {
        'breakfast bars pastries': {'price': 3.99, 'inventory': 173},
        'cereal': {'price': 3.99, 'inventory': 454},
        'granola': {'price': 4.99, 'inventory': 185},
        'hot cereal pancake mixes': {'price': 2.99, 'inventory': 303},
    },
    'meat seafood': {
        'hot dogs bacon sausage': {'price': 4.99, 'inventory': 387},
        'meat counter': {'price': 6.99, 'inventory': 105},
        'packaged meat': {'price': 5.99, 'inventory': 100},
        'packaged poultry': {'price': 5.99, 'inventory': 99},
        'packaged seafood': {'price': 9.99, 'inventory': 80},
        'seafood counter': {'price': 7.99, 'inventory': 54},
        'poultry counter': {'price': 7.99, 'inventory': 54},
    },
    'produce': {
        'fresh fruits': {'price': 2.99, 'inventory': 382},
        'fresh herbs': {'price': 1.99, 'inventory': 86},
        'fresh vegetables': {'price': 2.99, 'inventory': 569},
        'fresh dips tapenades': {'price': 3.99, 'inventory': 327},
        'packaged vegetables fruits': {'price': 4.99, 'inventory': 615},
        'packaged produce': {'price': 5.99, 'inventory': 32},
    },
    'dairy eggs': {
        'butter': {'price': 2.99, 'inventory': 150},
        'cream': {'price': 1.99, 'inventory': 161},
        'eggs': {'price': 2.99, 'inventory': 125},
        'other creams cheeses': {'price': 3.99, 'inventory': 191},
        'packaged cheese': {'price': 3.99, 'inventory': 891},
        'refrigerated pudding desserts': {'price': 4.99, 'inventory': 98},
        'yogurt': {'price': 3.99, 'inventory': 1026},
        'specialty cheeses': {'price': 5.99, 'inventory': 70},
        'soy lactosefree': {'price': 3.99, 'inventory': 80},
        'milk': {'price': 1.99, 'inventory': 80},
        
    },
    'frozen': {
        'frozen appetizers sides': {'price': 4.99, 'inventory': 386},
        'frozen breads doughs': {'price': 3.99, 'inventory': 81},
        'frozen breakfast': {'price': 3.99, 'inventory': 296},
        'frozen dessert': {'price': 4.99, 'inventory': 112},
        'frozen juice': {'price': 2.99, 'inventory': 47},
        'frozen meals': {'price': 5.99, 'inventory': 880},
        'frozen meat seafood': {'price': 9.99, 'inventory': 229},
        'frozen pizza': {'price': 5.99, 'inventory': 335},
        'frozen produce': {'price': 3.99, 'inventory': 361},
        'frozen vegan vegetarian': {'price': 5.99, 'inventory': 189},
        'ice cream ice': {'price': 3.99, 'inventory': 632},
    },
    'deli': {
        'packaged cheese': {'price': 4.99, 'inventory': 124},
        'prepackaged deli': {'price': 5.99, 'inventory': 212},
        'prepared soups salads': {'price': 4.99, 'inventory': 201},
        'sandwiches': {'price': 5.99, 'inventory': 186},
        'fresh dips tapenades': {'price': 5.99, 'inventory': 186},
        'lunch meat': {'price': 8.99, 'inventory': 186},
        'prepared meals': {'price': 15.99, 'inventory': 186},
        'tofu meat alternatives': {'price': 17.99, 'inventory': 186},
        
        
    },
    'canned goods': {
        'canned fruit applesauce': {'price': 2.99, 'inventory': 268},
        'canned meals beans': {'price': 3.99, 'inventory': 596},
        'canned meat seafood': {'price': 4.99, 'inventory': 293},
        'canned pasta sauce': {'price': 3.99, 'inventory': 437},
        'canned soups broth': {'price': 2.99, 'inventory': 548},
        'canned vegetables': {'price': 2.99, 'inventory': 617},
        'canned jarred vegetables': {'price': 2.99, 'inventory': 250},
        'soup broth bouillon': {'price': 2.99, 'inventory': 250},
        
        
    },
    'pets': {
        'cat food care': {'price': 4.99, 'inventory': 113},
        'dog food care': {'price': 5.99, 'inventory': 198},
        'other pet supplies': {'price': 4.99, 'inventory': 139},
    },
    'bulk' : {
        'bulk dried fruits vegetables' : {'price': 6.99, 'inventory': 350},
        'bulk grains rice dried goods' : {'price': 5.99, 'inventory': 350},
    },
    'dry goods pasta' : {
        'dry pasta' : {'price': 5.99, 'inventory': 250},
        'fresh pasta' : {'price': 7.99, 'inventory': 250},
        'grains rice dried goods' : {'price': 8.99, 'inventory': 120},
        'instant foods' : {'price': 1.99, 'inventory': 120},
        'pasta sauce' : {'price': 4.99, 'inventory': 120},
        
        
    },
    
    'other' : {
        'other': {'price': 1.99, 'inventory': 50},
    },
}


products = pd.read_csv('products.csv')

departments = pd.read_csv('departments.csv')

aisles = pd.read_csv('aisles.csv')

# merge products, departments and aisles
prod_dep_ais = products.merge(departments, on='department_id', how='inner').merge(aisles, on='aisle_id', how='inner')

# get price and inventory
prod_dep_ais['price'] = prod_dep_ais.apply(lambda x: aisles_by_department.get(x.department).get(x.aisle).get('price'), axis=1)
prod_dep_ais['inventory'] = prod_dep_ais.apply(lambda x: aisles_by_department.get(x.department).get(x.aisle).get('inventory'), axis=1)

# save products_final
prod_dep_ais[['product_id', 'product_name', 'aisle_id', 'department_id', 'price']].to_csv('products_price.csv', index=False)

# change to null
prod_dep_ais['last_updated'] = None

# save inventory 
prod_dep_ais[['product_id', 'aisle_id', 'department_id', 'inventory', 'last_updated']].to_csv('inventory.csv', index=False)

