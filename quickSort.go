package main

import (
	"fmt"
)

func swap(x *int, y *int) {
	temp := *x
	*x = *y
	*y = temp
}
func median(nums []int, left, right int) int {
	center := (left + right) / 2
	if nums[left] > nums[center] {
		swap(&nums[left], &nums[center])
	}
	if nums[left] > nums[right] {
		swap(&nums[left], &nums[right])
	}
	if nums[right] < nums[center] {
		swap(&nums[right], &nums[center])
	}
	swap(&nums[center], &nums[right-1])
	return nums[right-1]
}

func QuickSort(nums []int, left, right int) {
	if left >= right {
		return
	}
	pivot := median(nums, left, right)
	low, high := left, right-1
	for {
		for ; nums[low] <= pivot && high > low; low++ {
		}
		for ; nums[high] >= pivot && high > low; high-- {
		}
		if low < high {
			swap(&nums[low], &nums[high])
		} else {
			break
		}
	}

	swap(&nums[low], &nums[right-1])
	QuickSort(nums, left, low-1)
	QuickSort(nums, low+1, right)
}

func main() {
	a := []int{4, 3, 2, 1}
	a = []int{4, 8, 3, 7, 1, 5, 6, 2}
	QuickSort(a, 0, len(a)-1)
	fmt.Println(a)
}
