import numpy as np

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

def attacktype(df, country, choice):
    if choice == "Doden":
        everything = []
        years = []
        types = []
        countrycheck = df[df["country_txt"] == country]
        for type_attack in df["attacktype1_txt"].unique():
            attackcheck = countrycheck[df["attacktype1_txt"] == type_attack]
            years = []
            values = []
            for year in df["iyear"].unique():
                yearcheck = attackcheck[df["iyear"] == year]
                killcount = yearcheck["nkill"].sum()
                years.append(year)
                values.append(killcount)
            everything.append(values)
            types.append(type_attack)
    elif choice == "Aanslagen":
        everything = []`
        years = []
        types = []
        countrycheck = df[df["country_txt"] == country]
        for type_attack in df["attacktype1_txt"].unique():
            attackcheck = countrycheck[df["attacktype1_txt"] == type_attack]
            years = []
            values = []
            for year in df["iyear"].unique():
                yearcheck = attackcheck[df["iyear"] == year]
                years.append(year)
                values.append(len(yearcheck))
            everything.append(values)
            types.append(type_attack)
    return years, everything, types 

def worldmap(df, year, choice, display):
    if choice == "Aanslagen":
        countryattacks = {i: {} for i in set(df[(df['iyear']==year)]['country_txt'])}
        for i in countryattacks.keys():
            countryattacks[i]['meanlongitude'] = np.mean(list(df[df['country_txt']==i]['longitude'].fillna(0)))
            countryattacks[i]['meanlatitude'] = np.mean(list(df[df['country_txt']==i]['latitude'].fillna(0)))
            countryattacks[i]['amount'] = len(df[(df['iyear']==year) & (df['country_txt']==i)])

        limits = [(1,10),(11,20),(21,30),(31,40),(41,3000)]
        colors = ["rgb(0,223,255)","rgb(51,255,51)","rgb(255,255,51)","rgb(255,153,51)","rgb(255,0,0)"]
        data = []

        for i in range(len(limits)):
            lim = limits[i]
            df_sub = [c for c in countryattacks.items() if c[1]['amount']>=lim[0] and c[1]['amount']<=lim[1]]
            if display == 'Locatie':
                displaytext = [i[0] for i in df_sub]
            elif display == 'Aantal':
                displaytext = [i[1]['amount'] for i in df_sub]
            trace = dict(
                type = 'scattergeo',
                lon = [float(i[1]['meanlongitude']) for i in df_sub],
                lat = [float(i[1]['meanlatitude']) for i in df_sub],
                text = displaytext,
                marker = dict(
                    size = [float(i[1]['amount']) ** 0.35 * 10 for i in df_sub],
                    color = colors[i],
                    line = dict(width=0.5, color='rgb(40,40,40)'),
                    sizemode = 'area'
                ),
                name = '{0} - {1}'.format(lim[0],lim[1])
            )
            data.append(trace)

        layout = dict(
                title = 'Amount of attacks per country in {}<br>(Scales in legend, click legend to toggle)' .format(year),
                showlegend = True,
                geo = dict(
                    scope='world',
                    projection=dict( type='equirectangular' ),
                    showland = True,
                    showocean = True,
                    landcolor = 'white',
                    countrycolor= 'rgb(255, 255, 255)'
                )
            )
    elif choice == "Doden":
        limits = [(5,20),(21,50),(51,100),(101,3000)]
        colors = ["rgb(51,255,51)","rgb(255,255,51)","rgb(255,153,51)","rgb(255,0,0)"]
        data = []

        for i in range(len(limits)):
            lim = limits[i]
            df_sub = df[(df['iyear']==year) & (df['nkill']>=lim[0]) & (df['nkill']<=lim[1])]
            if display == 'Locatie':
                displaytext = df_sub['city']+', '+df_sub['country_txt']
            elif display == 'Aantal':
                displaytext = df_sub['nkill'].astype(int)
            trace = dict(
                type = 'scattergeo',
                lon = df_sub['longitude'],
                lat = df_sub['latitude'],
                text = displaytext,
                marker = dict(
                    size = df_sub['nkill'] * 1.5,
                    color = colors[i],
                    opacity = 0.4,
                    line = dict(width=0.5, color='rgb(0,0,0)'),
                    sizemode = 'area'
                ),
                name = '{0} - {1}'.format(lim[0],lim[1])
            )
            data.append(trace)

        layout = dict(
                title = 'Casualties per terrorist attack in {}<br>(Scales in legend, click legend to toggle)'.format(year),
                showlegend = True,
                geo = dict(
                    scope='world',
                    projection=dict( type='equirectangular' ),
                    showland = True,
                    showocean = True,
                    landcolor = 'white',
                    countrycolor= 'rgb(255, 255, 255)'
                )
            )
    else:
        layout = {}
        data =[]
    return layout, data
