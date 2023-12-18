from unittest import TestCase
from src.katas.ContainsDuplicates import Numbers


class TestSolution(TestCase):
    def test_check_duplicate_in_array1With4Items(self):
        # Given
        
        solution = Numbers()
        # When
        result = solution.containsDuplicateBySort([1, 2, 3, 1])
        # Then
        self.assertEqual(result, True)
        # When
    def test_check_duplicate_in_array1With4ItemsMatchLastTwo(self):
        # Given
        
        solution = Numbers()
    #     # When
        result = solution.containsDuplicateBySort([1, 2, 3, 3])
    #     # Then
        self.assertEqual(result, True)
    #     # When

    def test_check_duplicate_in_array2(self):
        
        solution = Numbers()
        result = solution.containsDuplicateBySort([1, 2, 3, 4])
    #     # # Then
        self.assertEqual(result, False)
    #     # # When

    def test_check_duplicate_in_array3(self):
            
        solution = Numbers() 

        result = solution.containsDuplicateByHashSet([1, 3, 4, 4, 2])
    #     # # Then
        self.assertEqual(result, True)

    def test_check_duplicate_in_array4(self):
        solution = Numbers()
        result = solution.containsDuplicateByHashMap([1, 2, 3, 4, 5, 4, 7, 8, 9, 10,5,5,6,7,4,656765,688,3,5,7,9])
       # # Then
        self.assertEqual(result, True)
    #     # # When
    def test_check_duplicate_in_arrayWith10Items(self):
        solution = Numbers() 
        result = solution.containsDuplicateByHashMap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #     # # Then
        self.assertEqual(result, False)
        #HashSet:45000,HashMap:41000,Sort:42000,BruteForce:128000


    def test_check_duplicate_in_arrayWith25Items(self):
        solution = Numbers() 
        result = solution.containsDuplicateBySort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,23,13,14,15,16,17,28,19,20,21,22,24])
    #     # # Then
        self.assertEqual(result, False)

    # def test_check_duplicate_in_array1With4ItemsWithSort(self):
    #     # Given
        
    #     solution = Numbers()
    #     # When
    #     result = solution.containsDuplicateByBruteForce([1, 2, 3, 1])
    #     # Then
    #     self.assertEqual(result, True)
    #     # When


       

    