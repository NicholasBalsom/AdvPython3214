import numpy as np
import pandas as pd
from matplotlib import axes
from matplotlib import pyplot as plt


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Handle missing data
    # Filled in some missing data with the mode because these values are not nessasary for our calcuaktions
    df = df.fillna(
        {
            "director": df["director"].mode()[0],
            "cast": df["cast"].mode()[0],
            "country": df["country"].mode()[0],
        }
    )
    # Droped any other rows with missing data that had valuable data missing
    df = df.dropna()
    return df


def movies_vs_shows(df: pd.DataFrame) -> None:
    # Number of Movies vs. Shows
    # Count the number of movies/shows for each type
    grouped_types = df.groupby(["type"])["type"].count()
    # Plot the data onto a bar graph
    plt.bar(grouped_types.index, grouped_types.values, color=["darkblue", "skyblue"])
    plt.title("Number of Movies vs Shows")
    plt.ylabel("Count")


def content_added_over_years(df: pd.DataFrame) -> None:
    # Line graph: Trend of content added over the years

    group = df.groupby(["year_added"])["year_added"].count()
    plt.figure(figsize=(10, 8))
    plt.plot(group.index, group.values)
    plt.title("Content added each year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.show()


def histogram(df: pd.DataFrame) -> None:
    plt.hist(df["release_year"])
    plt.show()


def ratings_piechart(df: pd.DataFrame) -> None:
    group = df.groupby(["rating"])["rating"].count()

    plt.pie(group, labels=group.index, autopct="%1.2f%%")
    plt.show()


def duration_movies(df: pd.DataFrame) -> None:
    df_movies = df[df["type"] == "Movie"]
    plt.scatter(df_movies["release_year"], df_movies["duration"])
    plt.show()


def duration_shows(df: pd.DataFrame) -> None:
    df_shows = df[df["type"] == "TV Show"]
    plt.scatter(df_shows["release_year"], df_shows["duration"])
    plt.show()


def main():
    # Load data into dataframe
    df = pd.read_csv("csv/netflix_titles.csv")
    df = df.set_index("show_id")
    df = clean_data(df)
    df["year_added"] = df["date_added"].map(lambda x: x[-4:])
    duration_movies(df)
    duration_shows(df)


if __name__ == "__main__":
    main()
