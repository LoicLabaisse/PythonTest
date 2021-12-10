class Persona:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        
        self._address_street = ""       # address_street sera une chaine de caractères vide
        self._address_number = 0        #address_number sera un integer égal à 0
        self._city = ""                 #city sera une chaine de caractères vide
        self._postcode = ('')            #postcode sera une chaine de caractères vide ('')
        
    def __str__(self):
        return f"Hi ! I'm {self._first_name} {self._last_name}"
    
    def set_address(self,address_street, address_number, city, postcode):
        self._address_street = address_street
        self._address_number = address_number
        self._city = city
        self._postcode = postcode
    
    
    def show_address(self):
        return f"My full address is : {self._address_number} {self._address_street} {self._city} {self._postcode}"
    
    def test(self):
        self._postcode = "sa devrait pas marcher si c'est un int"
    
#p1= Persona(first_name="Francois", last_name="Saura") 
#print(p1.show_address())

data = [{
"first_name":"Ilyès",
"last_name":"Fleury",
"address_street":"Rue Paul Bert",
"address_number":73,
"city":"Dunkerque",
"postcode":12681
},{
"first_name":"Lia",
"last_name":"Dumont",
"address_street":"Rue Louis-Blanqui",
"address_number":30,
"city":"Lille",
"postcode":63996
},{
"first_name":"Eléonore",
"last_name":"Caron",
"address_street":"Avenue du Château",
"address_number":87,
"city":"Rennes",
"postcode":78482
},{
"first_name":"Eva",
"last_name":"Girard",
"address_street":"Rue du Bon-Pasteur",
"address_number":9,
"city":"Rueil-Malmaison",
"postcode":23879
}]

for personne in data:
    p1 = Persona(personne['first_name'], personne['last_name'])
    p1.set_address(personne['address_street'], personne['address_number'], personne['postcode'] ,personne['city'])
    print(p1)
    print(p1.show_address())
    print("--")
  
