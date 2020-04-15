#include<stdio.h>

void insertSort(int* array, int len){
	for(int i=1; i<len; i++){
		for(int j=0; j<i; j++){
			if(array[i] <= array[j]){
				int temp = array[i];
				for(int k=i; k>j; k--){
					array[k] = array[k-1];
				}
				array[j] = temp;
			}
		}
	}
}
void main(){
	int a[] = {125, 130, 132, 123, 127, 129, 117, 121, 126, 116, 120, 122};
	insertSort(a, 12);
	for(int m=0; m<12; m++)
		printf("%4d", a[m]);
} 
