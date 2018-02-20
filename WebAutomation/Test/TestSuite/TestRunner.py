from unittest import TestLoader, TestSuite, TestCase, TextTestRunner
from WebAutomation.Test.Scripts.MercuryTour_HomePage import MercuryTours_HomePage
from WebAutomation.Test.Scripts.MercuryTour_Registration import MercuryTour_Registration
from WebAutomation.Test.Scripts.test_MerciryTour_SignOn import MercuryTours_SignOn


# IMPORT TEST TOOLS AS TEST TOOLS

if  __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(MercuryTours_HomePage),
        loader.loadTestsFromTestCase(MercuryTour_Registration),
        loader.loadTestsFromTestCase(MercuryTours_SignOn)
         ))


# run tests sequentially using simple TextTestRunner

runner = TextTestRunner(verbosity=2)
runner.run(suite)

# #run test parallel using concurrent_suite
#concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
#concurrent_suite.run(testtools.StreamResult())