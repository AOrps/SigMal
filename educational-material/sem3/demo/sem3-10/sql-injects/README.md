# General SQL Injection Vulnerability

* You need to gather information from your database and also need your database to authenticate that some person has an account with your company or your thing. 

* Picture below is what a database looks like from a practical and high-level view.
![](https://live.staticflickr.com/8744/16909119497_7c884617b8_b.jpg)

## Beginner View of Python Code

```python
import sqlite3
userInput = "Cassian"
con = sqlite3.connect('example.db')
cur = con.cursor()
cursor.execute(f"SELECT * FROM users WHERE name = '{userInput}'")
con.close()
```

## Problem
* There is no inherit problem with fetching data from a database (querying). The problem arises when one can manipulate the query and it goes to the database unchecked. 

```sql
SELECT * FROM users WHERE name = <User Input>;
```
* (Nothing is wrong with this!*)

`* Assuming you have a "wholesome" and good intentioned defintion for user input`

```python
import sqlite3

# userInput = input()
userInput = "Cassian"

with sqlite3.connect('bruh.db') as conn:
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{userInput}'")

# Congratulations you have wrote vulnerable code that people can exploit
```

## Solution

### How to Exploit

> "Totes Cool, Brotendo" - Steve Ballmer
```sql
-- Input: Cassian
SELECT * FROM users WHERE name = 'Cassian';
```

---

> "Totes not chill, dog" - Steve Ballmer
```sql
-- Input: l33thacker'; SELECT * FROM users;
SELECT * FROM users WHERE name = 'l33thacker'; SELECT * FROM users;--';
```

---

> "Bro....." - Steve Ballmer
```sql
-- Input: ' or 1=1;--
SELECT * FROM users WHERE name = '' or 1=1;--';
```

---

### Mitigation
* On the sqlite3 documentation btw, so you don't have to think about it too much but you can do your own individual thonk and see how you would go about it.


```python 
import sqlite3

# userInput = input()
userInput = ('Cassian', )

with sqlite3.connect('bruh.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name =?", userInput)

```

1. Use the `?` Placeholder
1. Provide a tuple of values as the second argument to the cursor's execute() method


## Sources
* [sqlite3-python3](https://docs.python.org/3/library/sqlite3.html)