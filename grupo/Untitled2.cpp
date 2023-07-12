#include <stdio.h>
#include "lista.h"
#include <stdlib.h>

void exibeLista(Lista *f) {
	int *aux;
	puts("=== Elementos da Lista ***");
	lst_posIni(f);
	aux=(int*)lst_prox(f);
	while(aux) {
		printf("%d\n",*aux);
		aux=(int*)lst_prox(f);
	}
}

int main(){
	
	Lista *f=lst_cria();
	int *a=(int*) malloc(sizeof(int));
	int *b=(int*) malloc(sizeof(int));
	int *c=(int*) malloc(sizeof(int));
	int *d=(int*) malloc(sizeof(int));
	int *aux;
	*a=10;
	*b=20;
	*c=30;
	*d=40;
	lst_insFin(f,a);
	lst_insFin(f,b);
	lst_insFin(f,c);
	lst_insFin(f,d);
	exibeLista(f);

	
	/*Lista *lst = lst_cria();
	int b=5;
	int *a = &b;
	lst_insFin(lst, (void*) a);
	No* tmp;
	tmp = (No*) malloc(sizeof(No));
	tmp = lst->ini;
	printf("%d\n%d",lst->tam, tmp->info);*/
	
	return 0;
}
