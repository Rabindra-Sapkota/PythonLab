import pandas as pd
import matplotlib.pyplot as plt

usr_df = pd.read_csv("test.csv")

usr_df.plot(x="id", y="student", kind="scatter", color="red")
plt.title("Plot of Course and Student")
plt.xticks(rotation=0)
plt.show()
