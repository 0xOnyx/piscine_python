from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Main function."""
    data = load("life_expectancy_years.csv")

    if data is None:
        exit(1)

    switzerland_data = data[
           data['country'] == 'Switzerland'
        ].iloc[0, 1:].astype(float)

    plt.figure(figsize=(8, 8))
    plt.plot(switzerland_data.index, switzerland_data.values, color='blue')
    plt.title('Switzerland life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.xticks([
        str(year) if int(year) % 40 == 0 else '' for year
        in range(1800, 2101, 10)
    ], rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
