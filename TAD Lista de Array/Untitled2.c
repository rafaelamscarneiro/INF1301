#include <stdio.h>
#include <stdlib.h>
#include "lista.h"

#define TAM = 10

struct lista{
	int tam;
	void **vet;
	int ini, fin, corr;
};

Lista *lst_cria(void){
	Lista *novo = (Lista*) malloc(sizeof(Lista));
	if (novo==NULL){
		printf("Erro na alocacao de memoria\n");
		exit(1);
	}
	novo->vet = (void**) malloc(TAM*sizeof(void*));
	if (novo->vet==NULL){
		printf("Erro na alocacao de memoria\n");
		exit(1);
	}
	novo->tam=0;
	novo->ini=0;
	novo->fin=0;
	novo->corr=-1;
	
	return novo;
}

int lst_vazia
