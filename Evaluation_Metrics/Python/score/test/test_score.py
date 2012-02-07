import unittest
import score

class Testquadratic_weighted_kappa(unittest.TestCase):


    def test_confusion_matrix(self):
        conf_mat = score.confusion_matrix([1,2],[1,2])
        self.assertEqual(conf_mat,[[1,0],[0,1]])
        
        conf_mat = score.confusion_matrix([1,2],[1,2],0,2)
        self.assertEqual(conf_mat,[[0,0,0],[0,1,0],[0,0,1]])
        
        conf_mat = score.confusion_matrix([1,1,2,2,4],[1,1,3,3,5])
        self.assertEqual(conf_mat,[[2,0,0,0,0],[0,0,2,0,0],[0,0,0,0,0],
                                   [0,0,0,0,1],[0,0,0,0,0]])
        
        conf_mat = score.confusion_matrix([1,2],[1,2],1,4)
        self.assertEqual(conf_mat,[[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]])

    def test_quadratic_weighted_kappa(self):
        kappa = score.quadratic_weighted_kappa([1,2,3],[1,2,3])
        self.assertAlmostEqual(kappa, 1.0)

        kappa = score.quadratic_weighted_kappa([1,2,1],[1,2,2],1,2)
        self.assertAlmostEqual(kappa, 0.4)

        kappa = score.quadratic_weighted_kappa([1,2,3,1,2,2,3],[1,2,3,1,2,3,2])
        self.assertAlmostEqual(kappa, 0.75)

if __name__ == '__main__':
    unittest.main()
