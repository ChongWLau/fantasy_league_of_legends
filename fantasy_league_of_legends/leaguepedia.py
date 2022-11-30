import mwclient


site = mwclient.Site('lol.fandom.com', path='/')

def get_champions():
    response = site.api('cargoquery',
        limit = 'max',
        tables = "Champions=CH",
        fields = "CH.Name, CH.ReleaseDate, CH.Attributes"
    )
    print(response)
    return response