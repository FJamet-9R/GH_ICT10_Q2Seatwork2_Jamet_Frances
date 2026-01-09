from pyscript import document, display


subjects = ["Math", "Science", "English", "Filipino", "Social Studies", "ICT"]
units = ('5', '5', '5', '3', '3', '2')
total_units = 5 + 5 + 5 + 3 + 3 + 2

def calculate(e):
    FName = document.getElementById('inputFName').value
    LName = document.getElementById('inputLName').value
    Math = float(document.getElementById('InputM').value)
    Science = float(document.getElementById('InputS').value)
    English = float(document.getElementById('InputE').value)
    Filipino = float(document.getElementById('InputF').value)
    Social_Studies = float(document.getElementById('InputSS').value)
    ICT = float(document.getElementById('InputICT').value)
    Cal = (Math*5 + Science*5 + English*5 + Filipino*3 + Social_Studies*3 + ICT*2) / total_units
    display(f"Student Name: {FName} {LName}", target="result")
    display(f"Math: {Math}", target="result")
    display(f"Science: {Science}", target="result")
    display(f"English: {English}", target="result")
    display(f"Filipino: {Filipino}", target="result")
    display(f"Social Studies: {Social_Studies}", target="result")
    display(f"ICT: {ICT}", target="result")
    display(f"Your General Average is: {Cal}", target="result")


    if Cal < 74:
        display(f'you got a FAILING grade', target="result")
    else:
        display(f'you got a PASSING grade', target='result')
    
 
 

 



