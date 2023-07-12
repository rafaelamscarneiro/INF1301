/*    GRUPO:
Daniel Peralta (1811442)
Felipe Meiga (2011460)
Rafaela Carneiro (2011483)

*/
#include <stdio.h>
#include <stdlib.h>
#include "UI.h"
#include "pilha.h"

struct pilha{
	Lista *lst;
};

Pilha *pilha_cria(){
	Pilha *p = (Pilha*) malloc(sizeof(Pilha));
	if (p == NULL){
		printf("Erro ao alocar memoria para a pilha");
		exit(1);
	}
	p->lst = lst_cria();
	
	return p;
}

int pilha_vazia(Pilha *p){
	return (lst_vazia(p->lst));
}

void pilha_push(Pilha *p, void *v){
	lst_insIni(p->lst, v);
	return;
}

void *pilha_pop(Pilha *p){
	if (pilha_vazia(p) == 1)
		return NULL;	
	void *v = lst_retIni(p->lst);
	return v;
}

void pilha_libera(Pilha *p){
	lst_libera(p->lst);
	free(p);
}
