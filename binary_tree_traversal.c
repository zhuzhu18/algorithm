#include<stdio.h>
#include<stdlib.h>

typedef struct node{
	int val;
	struct node* left;
	struct node* right;
} Node;

Node* init(int a){
	Node* node = (Node*)malloc(sizeof(Node));
	node->val = a;
	node->left = NULL;
	node->right = NULL;
	return node;
}

Node* insert_left(Node* root, Node* child){
	root->left = child;
	return root;
}
Node* insert_right(Node* root, Node* child){
	root->right = child;
	return root;
}

/****** 递归实现的三种遍历方式  ********/
void print_preorder(Node* tree){     // 先序遍历 
	if(tree){
		printf("%4d", tree->val);
		print_preorder(tree->left);
		print_preorder(tree->right);
	}
}
void print_inorder(Node* tree){     // 中序遍历 
	if(tree){
		print_inorder(tree->left);
		printf("%4d", tree->val);
		print_inorder(tree->right);
	}
}
void print_postorder(Node* tree){     // 后序遍历 
	if(tree){
		print_postorder(tree->left);
		print_postorder(tree->right);
		printf("%4d", tree->val);
	}
}
int main(){
    Node* tree = init(0);
    Node* node_1 = init(1);
    Node* node_2 = init(2);
    tree = insert_left(tree, node_1);
    tree = insert_right(tree, node_2);
    
    Node* node_3 = init(3);
    Node* node_4 = init(4);
    node_1 = insert_left(node_1, node_3);
    node_1 = insert_right(node_1, node_4);
    
    Node* node_5 = init(5);
    Node* node_6 = init(6);
    node_2 = insert_left(node_2, node_5);
    node_2 = insert_right(node_2, node_6);
    
    print_preorder(tree);
    printf("\n");
    print_inorder(tree);
    printf("\n");
    print_postorder(tree);
}
