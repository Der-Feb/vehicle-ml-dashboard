import pandas as pd


def frequency_table(df):
    manufacturer_counts = df["manufacturer"].value_counts().reset_index()
    manufacturer_counts.columns = ["Manufacturer", "Count"]
    return manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm mb-0",
        index=False,
        justify="center",
    )

