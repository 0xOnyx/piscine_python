from load_csv import load
import matplotlib.pyplot as plt


def main():
    data = load("population_total.csv")

    switzerland_data = data[data['country'] == 'Switzerland'].iloc[0, 1:]
    germany_data = data[data['country'] == 'Germany'].iloc[0, 1:]

    print(switzerland_data)
    print(germany_data)
    plt.figure(figsize=(8, 8))
    plt.plot(
        switzerland_data.index,
        switzerland_data.values,
        label="Switzerland", color='blue')
    plt.plot(germany_data.index,
             germany_data.values,
             label="Germany", color='green')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks([
        str(year) if int(year) % 40 == 0 else '' for year
        in range(1800, 2150, 10)
    ], rotation=45)
    plt.tight_layout()

    max_pop = max(max(switzerland_data.values), max(germany_data.values))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
