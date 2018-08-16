import pandas as pd


def table(queryset):
    data = list(queryset)
    df = pd.DataFrame(data)
    if 'id' in df:
        del df['id']
    return df