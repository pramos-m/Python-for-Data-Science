import matplotlib.pyplot as plt
from load_csv import load
import numpy as np

if __name__ == "__main__":
    df = load("./life_expectancy_years.csv")

    afghanistan = df.loc[df['country'] == 'Afghanistan']
    years = afghanistan.columns[1:]
    values = afghanistan.values[0][1:]
    
    plt.xticks(np.arange(0, 300, 40))
    plt.plot(np.array(years), np.array(values), label='Morocco')
    plt.title('Morocco Life expectancy Projections')
    plt.show()
