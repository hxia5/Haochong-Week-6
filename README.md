# Haochong-week6-mini-repo [![CI](https://github.com/hxia5/Haochong-Week-6/actions/workflows/cicd.yml/badge.svg)](https://github.com/hxia5/Haochong-Week-6/actions/workflows/cicd.yml)
This is a repo template for course 706_Data_Engineering Week 6 Mini Project. Since we need to perform join this week, I need to find two new datasets that fit this project. In this case, I found two datsets about the prediction of the world cup. First of all, I define functions called `extract` to get data from url. Then, use `load` to connect Databricks database. After that, I create afunction called `complex_query` to fulfill our requirement. Consequently, I use `main.py` to use my function in `lib.py`, and use the output of `main.py` and `test_main.py` to test my `main.py`. And also, I create a function called `query_record` to save my query history. Finally, I use Action to run `Makefile` and got a 100% pass. 

Important file:
* `Makefile`
*`cicd.yml`
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
1. open codespaces and vscode
2. wait for container to be built with requiremnts.txt installed

## Check format and test errors
1. Format code with Python black by using `make format`

2. Lint code with Ruff by using `make lint`. 

3. Test code by using `make test`

In this project, I got the first failure while import my csv file. Panda can't read it. After checking the error message and my csv file, I found out that it's not raw. After putting `?raw=True` after the url, I fix this problem. 

I was confused at first, and you can see I create several ways but all failed. After google this I noticed that it was because I use the number as the fisrt letter of my database, which is not allowed. I fixed this by delete "25".


I didn't meet too many trouble for other parts.



### result:




For the test, I didn't test for function like `connect`, since they are just for the connection. If they can't work, all other part won't be able to run, which means they are definitely fine.

I write test in `test_main.py` for CRUD functions. I use function`fetchone()` to fetch the row I want, and then compare the result with `None` to see whether the operation happened. I got them all pass:



![Alt text](<截屏2023-09-28 下午1.15.28.png>)


