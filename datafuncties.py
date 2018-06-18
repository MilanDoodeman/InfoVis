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
    nationality.append("Other")
    times.append(other)
    return nationality, times