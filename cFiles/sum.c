#include<stdio.h>

int sum(int a, int b){
	
	if(b>INT_MAX-a){
		return ;
	}else{
		return a+b;
	}
}

int main(){
	
	return 0;
}
