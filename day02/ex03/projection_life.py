from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """Main function."""
    life_expectancy_year = load("life_expectancy_years.csv")
    come_per_person = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    if life_expectancy_year is None or come_per_person is None:
        exit(1)

    gdp_1900 = life_expectancy_year[
            ['country', '1900']
        ].rename(columns={'1900': 'gdp'})

    life_exp = come_per_person[
            ['country', '1900']
        ].rename(columns={'1900': 'life_exp'})

    merged_data = pd.merge(gdp_1900, life_exp, on='country')
    plt.figure(figsize=(6, 6))
    plt.scatter(
        merged_data['gdp'],
        merged_data['life_exp'],
        edgecolor='k', alpha=0.7)
    plt.title('1900')
    plt.xlabel('Gross domestic product ')
    plt.ylabel('Life expectancy')
    plt.show()


if __name__ == "__main__":
    main()
