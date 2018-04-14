import unittest
import random
import pandas as pd
from moneypy.visual import utils


def set_up_dataframe(date, number_of_dates=3):
    df = pd.DataFrame()
    df['Date'] = pd.date_range(start=str(date),
                               periods=number_of_dates,
                               freq=str(random.randrange(10, 100)) + 'D')
    df = df.sample(frac=1)
    return df


# Set a random date
random_date = 2000 + random.randrange(0, 16)

# Setting up dataframes
df_one = set_up_dataframe(random_date)
df_two = set_up_dataframe(random_date + 1)
df_with_one_date = set_up_dataframe(random_date, 1)


# Create the lists of dataframes to pass to functions.
df_list = [df_one, df_two]
df_list_of_one = [df_one]
df_list_one_date = [df_with_one_date]


# Setting up tuples
single_tuple = (df_one['Date'].min(), df_one['Date'].max())

list_of_tuples = [(df_one['Date'].min(), df_one['Date'].max()),
                  (df_two['Date'].min(), df_two['Date'].max())]


class TestUtils(unittest.TestCase):

    """Unittest for utils.py"""

    def test_min_max_date(self):
        # Expected result is a list of tuples of dates
        self.assertEqual(utils.min_max_date(df_list),
                         [(df_one['Date'].min(), df_one['Date'].max()),
                          (df_two['Date'].min(), df_two['Date'].max())])
        # Edge case of only one dataframe in the list passed.
        self.assertEqual(utils.min_max_date(df_list_of_one),
                         [(df_one['Date'].min(), df_one['Date'].max())])
        # Edge case of only one date in one dataframe passed.
        self.assertEqual(utils.min_max_date(df_list_one_date),
                         [(df_with_one_date['Date'].min(),
                           df_with_one_date['Date'].max())])

    def test_min_max_date_format(self):
        # Expected result is a list of tuples of dates that are formatted.
        self.assertEqual(utils.min_max_date_format(df_list),
                         [(df_one['Date'].min().strftime('%y/%m/%d'),
                           df_one['Date'].max().strftime('%y/%m/%d')),
                          (df_two['Date'].min().strftime('%y/%m/%d'),
                           df_two['Date'].max().strftime('%y/%m/%d'))])
        # Edge case of only one dataframe in the list passed.
        self.assertEqual(utils.min_max_date_format(df_list_of_one),
                         [(df_one['Date'].min().strftime('%y/%m/%d'),
                           df_one['Date'].max().strftime('%y/%m/%d'))])
        # Edge case of only one date in one dataframe passed.
        self.assertEqual(utils.min_max_date_format(df_list_one_date),
                         [(df_with_one_date['Date'].min().strftime('%y/%m/%d'),
                           df_with_one_date['Date'].max().strftime('%y/%m/%d'))
                          ])

    def test_max_date_range(self):
        # Expected result is a tuple containing the min and max date from the
        # list of date tuples passed to this function.
        self.assertEqual(utils.max_date_range(list_of_tuples),
                         (df_one['Date'].min(), df_two['Date'].max()))

    def test_format_date_to_string(self):
        # Expected result is a tuple containing formatted dates.
        self.assertEqual(utils.format_date_to_string(single_tuple),
                         (df_one['Date'].min().strftime('%y/%m/%d'),
                          df_one['Date'].max().strftime('%y/%m/%d')))
        self.assertEqual(utils.format_date_to_string(single_tuple,
                                                     date_format='yymm'),
                         (df_one['Date'].min().strftime('%y/%m'),
                          df_one['Date'].max().strftime('%y/%m')))


if __name__ == '__main__':
    unittest.main()
