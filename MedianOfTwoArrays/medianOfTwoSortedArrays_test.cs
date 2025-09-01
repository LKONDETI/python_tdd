using NUnit.Framework;
using System; 

namespace Tests
{
    public class MedianOfTwoSortedArraysTests
    {
        [Test]
        public void Test_EvenTotalLength()
        {
            int[] nums1 = {1, 3};
            int[] nums2 = {2, 4};
            double expected = 2.5;
            var solution = new Solution();
            Assert.That(solution.FindMedianSortedArrays(nums1, nums2), Is.EqualTo(expected));
        }

        [Test]
        public void Test_OddTotalLength()
        {
            int[] nums1 = {1, 2};
            int[] nums2 = {3};
            double expected = 2.0;
            var solution = new Solution();
            Assert.That(solution.FindMedianSortedArrays(nums1, nums2), Is.EqualTo(expected));
        }

        [Test]
        public void Test_OneEmptyArray()
        {
            int[] nums1 = {};
            int[] nums2 = {2, 3};
            double expected = 2.5;
            var solution = new Solution();
            Assert.That(solution.FindMedianSortedArrays(nums1, nums2), Is.EqualTo(expected));
        }
    }
}
