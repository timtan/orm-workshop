import pandas as pd


def table(queryset):
    data = list(queryset.values())
    df = pd.DataFrame(data)
    del df['id']
    return df