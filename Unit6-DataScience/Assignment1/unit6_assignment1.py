import numpy as np
import pandas as pd

# Importing axes to beable to use the object type of an axis
# (Used for defining a data type in function arguments)
from matplotlib import axes
from matplotlib import pyplot as plt


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Task 1: Data Cleaning"""

    # Fill values with meadian year and mean sales respectivily
    df = df.fillna({"Year": df["Year"].median(), "Global_Sales": df["Global_Sales"].mean()})
    # Drop any rows with no name
    df["Name"] = df["Name"].dropna()
    # Fill na values with most common Platform and Genre respectivly
    df = df.fillna({"Platform": df["Platform"].mode(), "Genre": df["Genre"].mode()})
    # Drop any dupelicate rows
    df = df.drop_duplicates()
    return df


def yearly_game_releases(df: pd.DataFrame, ax: axes._axes.Axes) -> None:
    """Task: Yearly Game Releases"""

    # Count the number of games for each year
    group = df.groupby(["Year"])["Name"].agg({"count"})

    # Plot the data on the first axis using a line graph
    ax.plot(group.index, group["count"], marker="o", linestyle="--")
    ax.set_title("Number of Games per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Games")


def platform_popularity(df: pd.DataFrame, ax: axes._axes.Axes) -> None:
    """Task: Platform Popularity"""

    # Count the number of games for each game platform
    group = df.groupby(["Platform"])["Name"].agg({"count"})

    # Create a bar graph with collected data - zorder is used to control the order of layers
    ax.bar(group.index, group["count"], color=("black", "Blue", "red", "Green"), zorder=3)
    ax.set_title("Number of Games per Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Number of Games")
    # Create a grid (behind the bars: zorder) for easy viewing of values
    ax.grid(color="black", linestyle="--", linewidth=1, axis="y", zorder=0)


def top_selling_games(df: pd.DataFrame, ax: axes._axes.Axes) -> None:
    """Task: Top Selling Games"""

    # Find the top 5 rows with the largest Global Sales value
    top5 = df.nlargest(5, "Global_Sales")

    # Create a table to display values
    table = ax.table(cellText=top5.values, colLabels=top5.columns, rowLabels=[1, 2, 3, 4, 5], loc="center")
    # Increase the scale of the table (default=(1,1))
    table.scale(1, 1.5)
    ax.set_title("Top 5 selling games")
    # Used to hide the x and y axis
    ax.axis("off")


def annual_sales_trends(df: pd.DataFrame, ax: axes._axes.Axes) -> None:
    """Task: Annual Sales Trends"""

    # Calculate the total Global Sales for each year
    group = df.groupby(["Year"])["Global_Sales"].agg({"sum"})
    # Plot the data on a line graph
    ax.plot(group.index, group["sum"], marker="o", linestyle="-.")
    ax.set_title("Totoal Global Sales per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Global Sales (in millions)")


def genre_popularity(df: pd.DataFrame, ax: axes._axes.Axes) -> None:
    """Task: Genre Popularity"""

    # Calculate total global sales for each genre
    group = df.groupby(["Genre"])["Global_Sales"].agg({"sum"})
    # Create a pie chart for percentage of global sales per genre
    ax.pie(group["sum"], labels=group.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Poularity of Game Genres")


def sales_year_scatter(df: pd.DataFrame, ax: axes._axes.Axes) -> None:
    """Task: Sales vs. Year Scatter Plot"""

    # Calculate total Global Sales for each year
    group = df.groupby(["Year"])["Global_Sales"].agg({"sum"})
    # Create a scatter plot of the data
    ax.scatter(group.index, group["sum"])
    ax.set_title("Global Sales per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Global Sales (in millions)")

    # Creating a trend line
    z = np.polyfit(group.index, group["sum"], 1)
    p = np.poly1d(z)
    # Plotting the trend line
    ax.plot(group.index, p(group.index), "--", color="red")


def sales_dist_by_platform(df: pd.DataFrame, ax: axes._axes.Axes) -> None:
    """Task: Sales Distribution by Platform"""

    # Create a boxplot of individual global sales for each platform
    df.boxplot(column="Global_Sales", by="Platform", ax=ax)
    ax.set_title("Sales per Platform")
    ax.set_ylabel("Global Sales (in millions)")


def main():
    # Create DataFrame from csv
    df = pd.read_csv("csv/videogames.csv")
    df = clean_data(df)

    plt.figure(figsize=(14, 7))
    # Create axis' -- subplot(rows, columns, plot #)
    ax1, ax2, ax3 = plt.subplot(3, 3, 1), plt.subplot(3, 3, 2), plt.subplot(3, 3, 3)
    ax4, ax5, ax6 = plt.subplot(3, 3, 4), plt.subplot(3, 3, 5), plt.subplot(3, 3, 6)
    # This last plot will span across all columns of the bottom row
    ax7 = plt.subplot(3, 1, 3)

    # Creating plots
    yearly_game_releases(df, ax1)
    platform_popularity(df, ax2)
    top_selling_games(df, ax7)
    annual_sales_trends(df, ax3)
    genre_popularity(df, ax4)
    sales_year_scatter(df, ax5)
    sales_dist_by_platform(df, ax6)

    # Adding a "super title"
    plt.suptitle("Unit 6 - Assignment 1")
    # Format the graphs to fit without overlapping and adding padding
    plt.tight_layout(pad=1)
    # Display plots
    plt.show()


if __name__ == "__main__":
    main()
