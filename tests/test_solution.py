from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        import numpy as np

        dic = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
                        'Jonas'], 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
               'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
               'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        res = solution(dic)
        resshape = res.shape
        self.assertEqual(resshape, (2,4))
        self.assertEqual(str(res['score'][3]), 'nan')
        self.assertEqual(str(res['score'][7]), 'nan')
