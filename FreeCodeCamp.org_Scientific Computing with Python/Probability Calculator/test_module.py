import unittest
import prob_calculator

prob_calculator.random.seed(95)
class UnitTests(unittest.TestCase):
    def test_hat_class_contents(self):
        hat = prob_calculator.Hat(red=3, blue=2)
        command = hat.contents
        answer = ["red","red","red","blue","blue"]
        self.assertEqual(command, answer)

    def test_hat_draw(self):
        hat = prob_calculator.Hat(red=5, blue=2)
        command = hat.draw(2)
        answer = ['blue', 'red']
        self.assertEqual(command, answer, 'answer hat draw to return two random items from hat contents.')
        command = len(hat.contents)
        answer = 5
        self.assertEqual(command, answer, 'answer hat draw to reduce number of items in contents.')
        
    def test_prob_experiment1(self):
        hat = prob_calculator.Hat(blue=3,red=2,green=6)
        command = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
        answer = 0.272
        self.assertAlmostEqual(command, answer, delta = 0.01, msg = 'answer experiment method to return a different probability.')

    def test_prob_experiment2(self):
        hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
        command = prob_calculator.experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
        answer = 1.0
        self.assertAlmostEqual(command, answer, delta = 0.01, msg = 'answer experiment method to return a different probability.')

if __name__ == "__main__":
    unittest.main()
