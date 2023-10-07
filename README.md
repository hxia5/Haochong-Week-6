# Haochong-week6-mini-repo [![CI](https://github.com/hxia5/Haochong-Week-6/actions/workflows/cicd.yml/badge.svg)](https://github.com/hxia5/Haochong-Week-6/actions/workflows/cicd.yml)
This is a repo template for course 706_Data_Engineering Week 6 Mini Project. Since we need to perform join this week, I need to find two new datasets that fit this project. In this case, I found two datsets about the prediction of the world cup. First of all, I define functions called `extract` to get data from url. Then, use `load` to connect Databricks database. After that, I create afunction called `complex_query` to fulfill our requirement. Consequently, I use `main.py` to use my function in `lib.py`, and use the output of `main.py` and `test_main.py` to test my `main.py`. And also, I create a function called `query_record` to save my query history. Finally, I use Action to run `Makefile` and got a 100% pass. 

Important file:
* `Makefile`
* `cicd.yml`
* `lib.py`
* `main.py`
* `.env`(which is hidden)
* `query_record.md`
* `dataset`
* `test_main.py`

# Purpose
- Connect to a SQL Databricks database
- Design a complex SQL query involving joins, aggregation, and sorting
- Provide an explanation for what the query is doing and the expected results

## Preparation 
1. Open codespaces and vscode
2. Wait for container to be built with requiremnts.txt installed

## Set up for Databricks
After logging in Azure Education, I create a Azure Databricks. After launching the 
workspace, I got a database called "default". Then I found the information I need: server hostname, http path and my token. I put them in `.env` and use those three variables in my `load` function to build connection with Databricks. In addition, I also put those three variables in the `Action` under the `Secrets and variables` in the `Setting` of the repo. I create two table in the database. 
## Check format and test errors
1. Format code with Python black by using `make format`

2. Lint code with Ruff by using `make lint`. 

3. Test code by using `make test`

In this project, I got the first failure while import my csv file. Panda can't read it. After checking the error message and my csv file, I found out that it's not raw. After putting `?raw=True` after the url, I fix this problem. 

![Alt text](<截屏2023-10-07 下午3.06.14.png>)

I didn't meet too many trouble for other parts. I write test in `test_main.py` for three functions, and I got them all pass:.

![Alt text](<截屏2023-10-07 下午3.23.45.png>)

### query and result(you can also see in query_record):
Here is my query:

```
SELECT t1.group,
                AVG(t1.spi) as avg_soccer_power_in_group,
                COUNT(t1.win) as win_possibility_0609,
                COUNT(t2.win) as win_possibility_0613
            FROM default.wc609 t1
            JOIN default.wc613 t2 ON t1.id = t2.id
            GROUP BY t1.group, t2.group
            ORDER BY win_possibility_0609 DESC
            LIMIT 3
```

The purpose is to find out which group has the largest possibility to win the cup base on the prediction of Jun.9th and check if there is any change on Jun.13th. Hence, I joined two days' prediction, group them by the group of world cup, sum the possibility of win for all teams in the group and ordered by the possibility of Jun.9th. I also output the possibility od Jun.13th as comparison and the average soccer power as additional information.

Here is the result:

```response from databricks
[Row(group='b', avg_soccer_power_in_group=81.5, win_possibility_0609=4, win_possibility_0613=4), Row(group='c', avg_soccer_power_in_group=78.0, win_possibility_0609=4, win_possibility_0613=4), Row(group='f', avg_soccer_power_in_group=78.75, win_possibility_0609=4, win_possibility_0613=4)]
```


