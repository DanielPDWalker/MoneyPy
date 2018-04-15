import unittest
import random
import pandas as pd
from moneypy.visual import utils


def set_up_dataframe(date, number_of_dates=3):
    df = pd.DataFrame()
    df['Date'] = pd.date_range(start=str(date),
                               periods=number_of_dates,
                               freq=str(random.randrange(10, 100)) + 'D')
    # Randomize order of dates in the dataframe(s).
    df = df.sample(frac=1)
    return df


class TestUtils(unittest.TestCase):

    """Unittest for utils.py"""

    def setUp(self):
        # Set a random date
        self.random_date = 2000 + random.randrange(0, 16)

        # Setting up dataframes
        self.df_one = set_up_dataframe(self.random_date)
        self.df_two = set_up_dataframe(self.random_date + 1)
        self.df_with_one_date = set_up_dataframe(self.random_date, 1)

        # Create the lists of dataframes to pass to functions.
        self.df_list = [self.df_one, self.df_two]
        self.df_list_of_one = [self.df_one]
        self.df_list_one_date = [self.df_with_one_date]

        # Setting up tuples
        self.single_tuple = (self.df_one['Date'].min(),
                             self.df_one['Date'].max())
        self.list_single_tuple = [(self.df_one['Date'].min(),
                                   self.df_one['Date'].max())]
        self.list_of_tuples = [(self.df_one['Date'].min(),
                                self.df_one['Date'].max()),
                               (self.df_two['Date'].min(),
                                self.df_two['Date'].max())]

    def test_min_max_date(self):
        # Expected result is a list of tuples of dates
        self.assertEqual(utils.min_max_date(self.df_list),
                         [(self.df_one['Date'].min(),
                           self.df_one['Date'].max()),
                          (self.df_two['Date'].min(),
                           self.df_two['Date'].max())])
        # Edge case of only one dataframe in the list passed.
        self.assertEqual(utils.min_max_date(self.df_list_of_one),
                         [(self.df_one['Date'].min(),
                           self.df_one['Date'].max())])
        # Edge case of only one date in one dataframe passed.
        self.assertEqual(utils.min_max_date(self.df_list_one_date),
                         [(self.df_with_one_date['Date'].min(),
                           self.df_with_one_date['Date'].max())])

    def test_min_max_date_format(self):
        # Expected result is a list of tuples of dates that are formatted.
        self.assertEqual(utils.min_max_date_format(self.df_list),
                         [(self.df_one['Date'].min().strftime('%y/%m/%d'),
                           self.df_one['Date'].max().strftime('%y/%m/%d')),
                          (self.df_two['Date'].min().strftime('%y/%m/%d'),
                           self.df_two['Date'].max().strftime('%y/%m/%d'))])
        # Edge case of only one dataframe in the list passed.
        self.assertEqual(utils.min_max_date_format(self.df_list_of_one),
                         [(self.df_one['Date'].min().strftime('%y/%m/%d'),
                           self.df_one['Date'].max().strftime('%y/%m/%d'))])
        # Edge case of only one date in one dataframe passed.
        self.assertEqual(utils.min_max_date_format(self.df_list_one_date),
                         [(self.df_with_one_date['Date'].min()
                           .strftime('%y/%m/%d'),
                           self.df_with_one_date['Date'].max()
                           .strftime('%y/%m/%d'))])

    def test_max_date_range(self):
        # Expected result is a tuple containing the min and max date from the
        # list of date tuples passed to this function.
        self.assertEqual(utils.max_date_range(self.list_of_tuples),
                         (self.df_one['Date'].min(),
                          self.df_two['Date'].max()))
        # Edge case of only one tuple in a list passed.
        self.assertEqual(utils.max_date_range(self.list_single_tuple),
                         (self.df_one['Date'].min(),
                          self.df_one['Date'].max()))

    def test_format_date_to_string(self):
        # Expected result is a tuple containing formatted dates.
        self.assertEqual(utils.format_date_to_string(self.single_tuple),
                         (self.df_one['Date'].min().strftime('%y/%m/%d'),
                          self.df_one['Date'].max().strftime('%y/%m/%d')))
        # Test with different date_format passed.
        self.assertEqual(utils.format_date_to_string(self.single_tuple,
                                                     date_format='yymm'),
                         (self.df_one['Date'].min().strftime('%y/%m'),
                          self.df_one['Date'].max().strftime('%y/%m')))


if __name__ == '__main__':
    unittest.main()
