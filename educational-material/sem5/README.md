# Semester 5 of SigMal

**Projects + Tips in Security**

## Resources 

|Icon   | Title  | Description
| :---: | :--:   | :----
| :new: | [Projects](#projects) |
| :new: | [F-OOP](#f-oop) | OOP is stupid
| :new: | [Agile](#agile) | Agile Fundamentals 
| :new: | [PM](#pm) | PM Approaches 


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



<div id="agile"><div>

## Agile
  
Built for change and flexibility
  
 - Able to move quickly and easily
 - Willing to change and adapt
 - Done in pieces (More iterative)

 - Agile projects phases overlap and tasks are completed in iterations, (Scrum -> Sprints)
  
 - Great for a not concrete project, just ideas.

## PM 
  
  **Waterfall** is a traditional methodology in which tasks and phases are completed in a linear, sequential manner, and each stage of the project must be completed before the next begins. The project manager is responsible for prioritizing and assigning tasks to team members. In Waterfall, the criteria used to measure quality is clearly defined at the beginning of the project.

**Agile** involves short phases of collaborative, iterative work with frequent testing and regularly-implemented improvements. Some phases and tasks happen at the same time as others. In Agile projects, teams share responsibility for managing their own work. Scrum and Kanban are examples of Agile frameworks, which are specific development approaches based on the Agile philosophy.

**Scrum** is an Agile framework that focuses on developing, delivering, and sustaining complex projects and products through collaboration, accountability, and an iterative process. Work is completed by small, cross-functional teams led by a Scrum Master and is divided into short Sprints with a set list of deliverables.

**Kanban** is both an Agile approach and a tool that provides visual feedback about the status of the work in progress through the use of Kanban boards or charts. With Kanban, project managers use sticky notes or note cards on a physical or digital Kanban board to represent the team’s tasks with categories like “To do,” “In progress,” and “Done.”

**Lean** uses the 5S quality tool to eliminate eight areas of waste, save money, improve quality, and streamline processes. Lean’s principles state that you can do more with less by addressing dysfunctions that create waste. Lean implements a Kanban scheduling system to manage production.

**Six** Sigma involves reducing variations by ensuring that quality processes are followed every time. The Six Sigma method follows a process-improvement approach called DMAIC, which stands for define, measure, analyze, improve, and control.

**Lean Six Sigma** is a combination of Lean and Six Sigma approaches. It is often used in projects that aim to save money, improve quality, and move through processes quickly. Lean Six Sigma is also ideal for solving complex or high-risk problems. The 5S quality tool, the DMAIC process, and the use of Kanban boards are all components of this approach. 

Despite their differences, all of these project management methodologies require communication and collaboration among various teams and aim to deliver projects on time and within budget. 
































