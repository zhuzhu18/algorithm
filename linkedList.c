#include<stdio.h>
#include<stdlib.h>

typedef struct LNode{
	int data;
	struct LNode *next;
} List;

// 求链表的长度 
int len(List *ptrl){
	int l = 0;
	List *p = ptrl;
	while(p){
		l += 1;
		p = p->next;
	}
	return l;
}
// 查找第 k 个元素的地址
List * findKth(List *ptrl, int k){
	List *p = ptrl;
	int i = 0;
	while(p && i<k){
		i += 1;
		p = p->next;
	}
	if(i==k)
		return p;
	else
		return NULL;
}
// 查找元素 X 的地址
List *find(List *ptrl, int x){
	List *p = ptrl;
	while(p && p->data != x){
		p = p->next;
	}
	return p;
}
// 在第 i 个位置处插入元素 x
List *insert(List *ptrl, int i, int v) {
	List *p = (List *)malloc(sizeof(List));
	p->data = v;
	if (i==0){
		p->next = ptrl;
		return p;
	}
	else{
		List *prior = findKth(ptrl, i-1);
		if(prior == NULL){
			printf("参数出错!");
			return NULL;
		}
		p->next = prior->next;
		prior->next = p;
		return ptrl;
	}
}
// 删除第 i 个节点
List *delete(List *ptrl, int i){
	if(i==0){
		if(ptrl){
			ptrl = ptrl->next;
		}
		return ptrl;
	}
	else{
		List *p = findKth(ptrl, i-1);
		if(p==NULL | p->next == NULL){
			printf("第%d个节点不存在！", i);
			return NULL;
			}
		else{
			List *s = p->next;
			p->next = s->next;
			free(s);
			return ptrl;
		}
	}
} 

void output(List *ptrl){
	List *p = ptrl;
	while(p){
		printf("%4d", p->data);
		p = p->next;
	}
	printf("\n");
}

List *create(){
	int num;
	List *ptrl = NULL;
	scanf("%d", &num);
	while(num != 0){
		List *node = (List *)malloc(sizeof(List));
		node->data = num;
		node->next = ptrl;
		ptrl = node;
		scanf("%d", &num);
	}
	return ptrl;
}

void main(){
	List *head = create(), *new;
	output(head);
	new = delete(head, 0);
	output(new);
//	printf("%d", findKth(head, 3)->data);
}
