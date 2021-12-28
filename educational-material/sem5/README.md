# Semester 5 of SigMal

**Projects + Tips in Security**

## Resources 

|Icon   | Title  | Description
| :---: | :--:   | :----
| :new: | [Projects](#projects) |
| :new: | [F-OOP](#f-oop) | OOP is stupid



<!-- So everything is on one README -->
<div id="projects"></div>

## Projects 


<div id="f-oop"></div>

## F-OOP

### OOP 
```python
class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['name']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
```

### Not OOP

