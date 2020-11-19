import requests
from diff_piv import Diff_priv

req = requests.get("http://localhost:5000/api/query", params={"query": "SELECT AVG(age) FROM table1 WHERE year = 2005"})
req = requests.get("http://localhost:5000/api/query", params={"query": "SELECT MEDIAN(age) FROM table1 WHERE year = 2020"})