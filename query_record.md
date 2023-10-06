```sql
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

```response from databricks
[Row(group='b', avg_soccer_power_in_group=81.5, win_possibility_0609=4, win_possibility_0613=4), Row(group='e', avg_soccer_power_in_group=78.25, win_possibility_0609=4, win_possibility_0613=4), Row(group='d', avg_soccer_power_in_group=79.75, win_possibility_0609=4, win_possibility_0613=4)]
```

```sql
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

```response from databricks
[Row(group='b', avg_soccer_power_in_group=81.5, win_possibility_0609=4, win_possibility_0613=4), Row(group='e', avg_soccer_power_in_group=78.25, win_possibility_0609=4, win_possibility_0613=4), Row(group='d', avg_soccer_power_in_group=79.75, win_possibility_0609=4, win_possibility_0613=4)]
```

```sql
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

```response from databricks
[Row(group='b', avg_soccer_power_in_group=81.5, win_possibility_0609=4, win_possibility_0613=4), Row(group='e', avg_soccer_power_in_group=78.25, win_possibility_0609=4, win_possibility_0613=4), Row(group='d', avg_soccer_power_in_group=79.75, win_possibility_0609=4, win_possibility_0613=4)]
```

```sql
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

```response from databricks
[Row(group='b', avg_soccer_power_in_group=81.5, win_possibility_0609=4, win_possibility_0613=4), Row(group='e', avg_soccer_power_in_group=78.25, win_possibility_0609=4, win_possibility_0613=4), Row(group='d', avg_soccer_power_in_group=79.75, win_possibility_0609=4, win_possibility_0613=4)]
```

