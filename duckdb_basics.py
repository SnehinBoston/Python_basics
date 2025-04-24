data = {"a": [1, 3, -1, 8]}

# import pandas as pd

# df_pd = pd.DataFrame(data)
# df_pd["a_centered"] = df_pd["a"] - df_pd["a"].mean()

# import polars as pl

# df_pl = pl.DataFrame(data)
# df_pl.with_columns(a_centered=pl.col("a") - pl.col("a").mean())

# import duckdb

# print(duckdb.sql(
#     """
#         SELECT
#         *,
#         a - MEAN(a) over () as a_centered
#         from df_pl
#     """
# ).fetchall())

# from datetime import datetime

# dates = [
#     datetime(2025, 1, 1),
#     datetime(2025, 1, 7),
#     datetime(2025, 1, 8),
#     datetime(2025, 1, 9),
#     datetime(2025, 1, 16),
#     datetime(2025, 1, 17),
# ]
# sales = [1, 5, 0, 4, 3, 6]
# data = {"date": dates, "sales": sales}

# import pandas as pd
# df_pd = pd.DataFrame(data)
# df_pd.resample("1W-Wed", on="date", closed="left", label="left")["sales"].mean()

# import polars as pl

# df_pl = pl.DataFrame(data)
# print((
#     df_pl.group_by_dynamic(
#         pl.col("date").alias("week_start"), every="1w", start_by="wednesday"
#     ).agg(pl.col("sales").mean())
# ))

# import duckdb

# print(duckdb.sql(
#     """
#     SELECT
#         DATE_TRUNC('week', date - INTERVAL 2 DAYS) + INTERVAL 2 DAYS AS week_start,
#         AVG(sales) AS sales
#     FROM df_pl
#     GROUP BY week_start
#     ORDER BY week_start
# """
# ).fetchall())

from datetime import datetime

dates = [
    datetime(2025, 1, 1),
    datetime(2025, 1, 2),
    datetime(2025, 1, 3),
    datetime(2025, 1, 4),
    datetime(2025, 1, 5),
    datetime(2025, 1, 7),
]

sales = [2.0, 4.6, 1.32, 1.11, 9, 8]
data = {"date": dates, "sales": sales}

import pandas as pd

df_pd = pd.DataFrame(data)
df_pd["sales_smoothed"] = df_pd["sales"].rolling(3).mean()

import polars as pl

df_pl = pl.DataFrame(data)
df_pl.with_columns(sales_smoothed=pl.col("sales").rolling_mean(3))

import duckdb
import pprint
pprint.pp(duckdb.sql("""
    SELECT
           *,
           MEAN(sales) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS sales_smoothed
    FROM df_pl           
""").fetchall())

pprint.pp(duckdb.sql(
    """
    SELECT
        *,
        CASE WHEN (COUNT(sales) OVER w) >= 3
             THEN MEAN(sales) OVER w
             ELSE NULL
             END AS sales_smoothed
    FROM df_pl
    window w as (order by date rows between 2 preceding and current row)
    """
).fetchall())