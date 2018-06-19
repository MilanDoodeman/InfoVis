def terroristnationality(country, df):
    final = {}
    landdata = df[df["country_txt"] == country]
    length = len(landdata)
    for land in landdata["natlty1_txt"]:
        if land in final:
            final[land] += 1
        else:
            final[land] = 1
    nationality = []
    times = []
    other = 0
    for keys, values in final.items():
        if keys !=".":
            if values > (0.01*length):
                nationality.append(keys)
                times.append(values)
            else:
                other += values
    if other > 0:
        nationality.append("Other")
        times.append(other)
    return nationality, times

def attacktype(df, country):
    everything = []
    types = []
    for type_attack in df["attacktype1_txt"].unique():
        years = []
        values = []
        for year in df["iyear"].unique():
            yearcheck = df[df["iyear"] == year]
            countrycheck = yearcheck[df["country_txt"] == country]
            attackcheck = countrycheck[df["attacktype1_txt"] == type_attack]
            killcount = attackcheck["nkill"].sum()
            years.append(year)
            values.append(killcount)
        everything.append(values)
        types.append(type_attack)
    return years, everything, types 