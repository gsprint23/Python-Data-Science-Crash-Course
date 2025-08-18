import pandas as pd

# why pandas?
# major shortcomings of using a 2D list to store tabular data
# 1. lot of work to get a column
# 2. lack of label-based indexing

# 2 main data storage objects
# 1. Series: 1D data
# 2. DataFrame: 2D data

# lets start with Series
pops = [764753, 229608, 96619, 32868]
cities = ["Seattle", "Spokane", "Bellingham", "Pullman"]

pop_ser = pd.Series(pops, index=cities)
pop_ser.name = "Population"
print(pop_ser)

# indexing
print(pop_ser["Seattle"])
print(pop_ser["Seattle": "Bellingham"]) # inclusive of the stop because label-based
print(pop_ser[["Seattle", "Bellingham"]])

# use .iloc[ ] for position based indexing
print(pop_ser.iloc[0])
print(pop_ser.iloc[0:2]) # exclusive of the stop because position based
print(pop_ser.iloc[[0, 2]])

# summary stats
print(pop_ser.mean())
print(pop_ser.std())

# we can add a new value to the series
pop_ser["Bothell"] = 51575
print(pop_ser)

# we can also make an empty Series
pop_ser2 = pd.Series(dtype=int)
pop_ser2["Bothell"] = 51575
print(pop_ser2)

# on to DataFrames!
twod_list = [["a", 3], ["b", 7], ["c", -5]]
df = pd.DataFrame(twod_list, index=["row1", "row2", "row3"], columns=["col1", "col2"])
print(df)

# task: make a DataFarme for our city population data
# columns: "City", "Population", "Size"
pop_data = [
    ["Seattle", 764753, "Large"],
    ["Spokane", 229608, "Large"],
    ["Bellingham", 96619, "Medium"],
    ["Pullman", 32868, "Small"]
]
pop_df = pd.DataFrame(pop_data, columns=["City", "Population", "Size"])
pop_df = pop_df.set_index("City")
print(pop_df)

# indexing
pop_ser = pop_df["Population"]
print(pop_ser)
# use .loc[ ] to do label based row indexing
seattle_ser = pop_df.loc["Seattle"]
print(seattle_ser)
# use .iloc[ ] to do position based row or column indexing
seattle_ser = pop_df.iloc[0]
print(seattle_ser)
pop_ser = pop_df.iloc[:, 0]
print(pop_ser)
seattle_pop = pop_df.iloc[0, 0]
print(seattle_pop)

regions_df = pd.read_csv("regions.csv", index_col=0)
print(regions_df)

# now lets join pop_df and regions_df on "City"
merged_df = pop_df.merge(regions_df, on=["City"], how="outer")
print(merged_df)

# lets write the merged_df to a file
merged_df.to_csv("merged.csv")

# data aggregation: gathering and presenting data in a summarized form
# split apply combine
# 1. split merged_df by Size
grouped_by_size = merged_df.groupby("Size")
print(grouped_by_size)

# lets grab a single "group" (a subtable)
large_df = grouped_by_size.get_group("Large")
print(large_df)
print(grouped_by_size.groups.keys())

# lets iterate over all the groups
mean_pop_ser = pd.Series(dtype=float)
for group_name, group_df in grouped_by_size:
    print(group_name)
    print(group_df)

    # 2. apply a mean to each subtable's population
    group_pop_ser = group_df["Population"]
    group_pop_mean = group_pop_ser.mean()
    print(group_pop_mean)

    # 3. combine
    mean_pop_ser[group_name] = group_pop_mean
    print()

print(mean_pop_ser)
# another much shorter way!
mean_pop_ser = grouped_by_size["Population"].mean()
print(mean_pop_ser)