"""Add your solution to the problem 'print_medals' here."""

space = " "


def print_medals(medal_counts):
    """Takes the a dictionary of medal counts and prints
    a nicely formatted table with totals for each country
    as described in the pset 5 problem.
    """
    # Add your code here.

    country_sort = sorted(medal_counts)

    print(f"{space:18}  Gold   Silver   Bronze   Total")

    for i in range(len(country_sort)):
        print(f"{country_sort[i]:>15}", end=" ")

        sum = 0

        for j in range(3):
            print(f"{medal_counts[country_sort[i]][j]:8}", end=" ")
            sum += medal_counts[country_sort[i]][j]

        print(f"{sum:7}")


def main():
    # Add your solution to the problem that makes use of the above.
    MEDAL_COUNTS = {
        "Canada": [0, 3, 0],
        "Italy": [0, 0, 1],
        "Germany": [0, 0, 1],
        "Japan": [1, 0, 0],
        "Kazakhstan": [0, 0, 1],
        "Russia": [3, 1, 1],
        "South Korea": [0, 1, 0],
        "United States": [1, 0, 1],
    }

    print_medals(MEDAL_COUNTS)


if __name__ == "__main__":
    main()
