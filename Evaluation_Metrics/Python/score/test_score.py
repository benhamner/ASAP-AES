import unittest
import score

class TestQuadraticWeightedKappa(unittest.TestCase):

    def setUp(self):
        self.qwk = score.QuadraticWeightedKappa()

    def test_confusion_matrix(self):
        conf_mat = self.qwk.confusion_matrix([1,2],[1,2])
        self.assertEqual(conf_mat,[[1,0],[0,1]])
        
        conf_mat = self.qwk.confusion_matrix([1,2],[1,2],0,2)
        self.assertEqual(conf_mat,[[0,0,0],[0,1,0],[0,0,1]])
        
        conf_mat = self.qwk.confusion_matrix([1,1,2,2,4],[1,1,3,3,5])
        self.assertEqual(conf_mat,[[2,0,0,0,0],[0,0,2,0,0],[0,0,0,0,0],
                                   [0,0,0,0,1],[0,0,0,0,0]])
        
        conf_mat = self.qwk.confusion_matrix([1,2],[1,2],1,4)
        self.assertEqual(conf_mat,[[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]])

    def test_score(self):
        score = self.qwk.score([1,2,3],[1,2,3])
        self.assertAlmostEqual(score, 1.0)

        score = self.qwk.score([1,2,1],[1,2,2],1,2)
        self.assertAlmostEqual(score, 0.4)

        score = self.qwk.score([1,2,3,1,2,2,3],[1,2,3,1,2,3,2])
        self.assertAlmostEqual(score, 0.75)

if __name__ == '__main__':
    unittest.main()
