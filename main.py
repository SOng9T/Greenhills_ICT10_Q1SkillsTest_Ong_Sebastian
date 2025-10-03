# working with strings
'''
from pyscript import display, document

def sample_function(e):
    data1 = document.getElementById('input1').value 
    data2 = document.getElementById('input2').value

    display(f'Welcome {data1}, Are you {data2} years old?')
    '''

'''
    same_multilinestring = This is a
    asdmoaskdoamd 
    sodoskdoas
    msdkms
    chiwawa
    

print(same_multilinestring)

sample_string = "This is a sample string"

print(sample_string * 5)

longest = 'supercalifragilisticexpialidocious'

print(longest[0:5]) 
print(len(longest))

sample_string4 = "Sebastian Chilli Ong"
print(sample_string4)

section - ["Emerald Hill", "Bukit Timah", "Orchard Road", "Marina Bay Sands", "Sentosa"]
join = 'the Junior High School section are'
print(join, ',' join(section))]

sample_string6 = 'romeo and juliet by william shakespeare'
print(sample_string6.title())
print(sample_string6.upper())
print(sample_string6.lower())  
print(sample_string6.swapcase())
'''

#sorry sir for the messy notes on top, I kept them there for my references when I was researching for python, I kept them there during class ;v;
from js import document

def process_order(event=None):
    menu = {
        "Spicy Szechuan Nuggets": 70.00,
        "Mapo Tofu Curry": 60.00,
        "Dim Sum Platter": 50.00,
        "Peking Duck": 40.00,
        "Lechon Macau": 60.00
    }

    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    selected = []
    total = 0
    for item in menu:
        checkbox_id = item.replace(" ", "_")
        checkbox = document.getElementById(checkbox_id)
        if checkbox.checked:
            selected.append(item)
            total += menu[item]

    summary = f"""
    <h3>Order Summary</h3>
    <p><strong>Order for:</strong> {name}<br>
    <strong>Address:</strong> {address}<br>
    <strong>Contact:</strong> {contact}<br>
    <strong>Items Ordered:</strong> {', '.join(selected)}<br>
    <strong>Total:</strong> ₱{total:.2f}</p>
    """

    document.getElementById("output").innerHTML = summary


