import pandas as pd

def _filter_by_column(df, value, columns):
    """Filtra o DataFrame por qualquer uma das colunas possíveis, suporta listas e case-insensitive."""
    for col in columns:
        if col in df.columns:
            if isinstance(value, (list, tuple, set)):
                if df[col].dtype == object:
                    return df[df[col].str.lower().isin([str(v).lower() for v in value])]
                else:
                    return df[df[col].isin(value)]
            else:
                if isinstance(value, str):
                    return df[df[col].str.lower().str.contains(value.lower(), na=False)]
                else:
                    return df[df[col] == value]
    return df

def load_merge_master(
    path,
    split=None,
    split_type='split_70_15_15',
    quadrant=None,
    year=None,
    artist=None,
    title=None,
    genres=None,
    return_cols=None,
    as_copy=True
):
    """
    Loader flexível para os masters do MERGE Dataset.
    """
    df = pd.read_csv(path)
    df.columns = [c.lower() for c in df.columns]

    if split is not None and split_type in df.columns:
        df = df[df[split_type] == split]
    if quadrant is not None and 'quadrant' in df.columns:
        if isinstance(quadrant, (list, tuple, set)):
            df = df[df['quadrant'].isin(quadrant)]
        else:
            df = df[df['quadrant'] == quadrant]
    if year is not None:
        df = _filter_by_column(df, year, ['year', 'actualyear'])
    if artist is not None:
        df = _filter_by_column(df, artist, ['artist'])
    if title is not None:
        df = _filter_by_column(df, title, ['title'])
    if genres is not None:
        df = _filter_by_column(df, genres, ['genres'])
    if return_cols:
        existing_cols = [col for col in return_cols if col in df.columns]
        df = df[existing_cols]
    return df.copy() if as_copy else df