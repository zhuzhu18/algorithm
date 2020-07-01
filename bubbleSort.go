package main

import (
	"fmt"
)

func BubbleSort(nums []int) int {
	// 复杂度为O(N^2)，即(N-1)N/2
	count := 0
	flag := false
	for p := len(nums); p > 0; p-- {
		for i := 0; i < p-1; i++ {
			// count++                需要比较的次数，等于从数组中选出二元组的组合数
			if nums[i] > nums[i+1] {
				flag = true
				count++ // 需要交换的次数等于逆序对数
				temp := nums[i]
				nums[i] = nums[i+1]
				nums[i+1] = temp
			}
		}
		if !flag {
			break
		}
	}
	return count
}

func main() {
	a := [6]int{34, 8, 64, 51, 32, 21}
	count := BubbleSort(a[:])
	fmt.Println(a)
	fmt.Println(count)
}
