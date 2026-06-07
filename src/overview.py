def get_overview(df):
    overview = {
        'num_rows': df.shape[0],
        'num_columns': df.shape[1],
        'column_names': df.columns.tolist(),
        'data_types': df.dtypes.to_dict(),
    }
    return overview
    