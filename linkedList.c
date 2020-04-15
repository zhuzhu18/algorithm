#include<stdio.h>
#include<stdlib.h>

typedef struct node {
	int item;
	struct node* next;
} Node;

Node* create(Node* head){
	int num;
	scanf("%d", &num);
	while(num){         //创建一个链表，遇到0结束输入，0不作为最后一个数据
		Node *p = (Node *)malloc(sizeof(Node));
		p->item = num;
		p->next = head;
		head = p;
		scanf("%d", &num);
	}
	return head; 
}

void main(){
	Node *head = NULL;
	head = create(head);
	for(Node *p=head; p; p=p->next){
		printf("%4d", p->item);
	}
	printf("\n");
} 
