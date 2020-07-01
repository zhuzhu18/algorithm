package main

import (
	"fmt"
)

func InsertSort(nums []int) int {
	// 复杂度为O(N^2)，最坏情况为(N-1)N/2，最好情况为O(N)，即遍历N-1次
	count := 0
	for p := 1; p < len(nums); p++ {
		i := 0
		temp := nums[p]
		for i = p; i > 0; i-- {
			count++ // 需要比较的次数，从后往前插入，遇到比插入元素小的就停止遍历内层循环
			if nums[i-1] <= temp {
				break
			}
			nums[i] = nums[i-1]
			// count++            需要交换的次数，等于逆序对数
		}
		nums[i] = temp
	}
	return count
}

func main() {
	a := [6]int{34, 8, 64, 51, 32, 21}
	count := InsertSort(a[:])
	fmt.Println(a)
	fmt.Println(count)
}
