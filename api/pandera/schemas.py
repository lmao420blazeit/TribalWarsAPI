import pandas as pd
import datetime
from pandera import DataFrameSchema, Column, Check

# Assuming you have the Pydantic models defined as mentioned in the question

# Create Pandera schema for VillageData
village_data_schema = DataFrameSchema({
    "village_id": Column(int),
    "name": Column(str, nullable = True),
    "x": Column(int, nullable = True),
    "y": Column(int, nullable = True),
    "continent": Column(int, nullable = True),
    "player_id": Column(int, nullable = True),
    "points": Column(int, nullable = True),
    "datetime": Column(datetime.datetime),
    "server": Column(str),
}, 
add_missing_columns = True, 
coerce = True,
drop_invalid_rows = True)

# Create Pandera schema for AllyData
ally_data_schema = DataFrameSchema({
    "ally_id": Column(int),
    "name": Column(str, nullable = True),
    "tag": Column(str, nullable = True),
    "members": Column(int, nullable = True),
    "num_vill": Column(int, nullable = True),
    "points": Column(int, nullable = True),
    "total_points": Column(int, nullable = True),
    "rank": Column(int, nullable = True),
    "datetime": Column(datetime.datetime),
    "server": Column(str),
}, 
add_missing_columns = True, 
coerce = True,
drop_invalid_rows = True)

# Create Pandera schema for PlayerData
player_data_schema = DataFrameSchema({
    "player_id": Column(int),
    "name": Column(str, nullable = True),
    "ally_id": Column(int, nullable = True),
    "num_vill": Column(int, nullable = True),
    "points": Column(int, nullable = True),
    "rank": Column(int, nullable = True),
    "datetime": Column(datetime.datetime),
    "server": Column(str),
}, 
add_missing_columns = True, 
coerce = True,
drop_invalid_rows = True)

# Create Pandera schema for AttackData
attack_data_schema = DataFrameSchema({
    "player_id": Column(int),
    "rank": Column(int, nullable = True),
    "points": Column(int, nullable = True),
    "datetime": Column(datetime.datetime),
    "server": Column(str),
}, 
add_missing_columns = True, 
coerce = True,
drop_invalid_rows = True)

# Create Pandera schema for DefenseData
defense_data_schema = DataFrameSchema({
    "player_id": Column(int),
    "rank": Column(int, nullable = True),
    "points": Column(int, nullable = True),
    "datetime": Column(datetime.datetime),
    "server": Column(str),
}, 
add_missing_columns = True, 
coerce = True,
drop_invalid_rows = True)