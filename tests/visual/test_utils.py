import unittest
import random
import pandas as pd
from moneypy.visual import utils


# Set up two empty dataframes.
df_one = pd.DataFrame()
df_two = pd.DataFrame()

# Generate a random year between 2000 and 2016.
random_date = 2000 + random.randrange(0, 16)

# Create a date column and add 3 dates to it, based on the random_date above.
df_one['Date'] = pd.date_range(start=str(random_date),
                               periods=3,
                               freq=str(random.randrange(10, 100)) + 'D')

random_date = 2000 + random.randrange(0, 16)
df_two['Date'] = pd.date_range(start=str(random_date),
                               periods=3,
                               freq=str(random.randrange(10, 100)) + 'D')

# Saves the min and max dates of each dataframe, to test against.
df_one_start_date = df_one['Date'].min()
df_one_end_date = df_one['Date'].max()

df_two_start_date = df_two['Date'].min()
df_two_end_date = df_two['Date'].max()

# Randomize the order of the dates.
df_one = df_one.sample(frac=1)
df_two = df_two.sample(frac=1)

# Create the list of dataframes to pass to functions.
df_list = [df_one, df_two]


class TestUtils(unittest.TestCase):

    """Unittest for utils.py"""

    def test_min_max_date(self):
        # Expected result is a list of tuples of dates
        self.assertEqual(utils.min_max_date(df_list),
                         [(df_one_start_date, df_one_end_date),
                          (df_two_start_date, df_two_end_date)])

    def test_min_max_date_format(self):
        # Expected result is a list of tuples of dates that are formatted.
        self.assertEqual(utils.min_max_date_format(df_list),
                         [(df_one_start_date.strftime('%y/%m/%d'),
                           df_one_end_date.strftime('%y/%m/%d')),
                          (df_two_start_date.strftime('%y/%m/%d'),
                           df_two_end_date.strftime('%y/%m/%d'))])


if __name__ == '__main__':
    unittest.main()
