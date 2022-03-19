#include <stdio.h>
#include <stdlib.h>
#include "UI.h"

typedef struct no
{
	void* info;
	struct no* prox;
	struct no* ant;
}No;

struct lista
{
	int tam;
	No* ini;
	No* fin;
	No* corr;
};

Lista* lst_cria(void)
{
	Lista* lst = (Lista*)malloc(sizeof(Lista));

	if (lst == NULL)
	{
		printf("Error while dynamically allocating memory for \"lst\"!");
		exit(1);
	}

	lst->tam = 0;
	lst->ini = NULL;
	lst->fin = NULL;
	lst->corr = NULL;

	return lst;
}

int lst_vazia(Lista* list)
{
	if (list->ini == NULL)
	{
		return 1;
	}

	return 0;
}

void lst_insIni(Lista* list, void* data)
{
	No* temp = (No*)malloc(sizeof(No));
	temp->info = data;
	temp->prox = NULL;
	temp->ant = NULL;

	if (lst_vazia(list) == 1)
	{
		list->ini = temp;
		list->fin = temp;
	}
	else
	{
		list->corr = list->ini;
		temp->prox = list->corr;
		list->corr->ant = temp;
		list->ini = temp;
	}
	list->tam++;
}

void lst_insFin(Lista* list, void* data) {
	No* temp = (No*)malloc(sizeof(No));
	temp->info = data;
	temp->prox = NULL;
	temp->ant = NULL;

	if (list->ini == NULL) {
		list->ini = temp;
		list->fin = temp;
	}
	else {
		list->corr = list->fin;
		temp->ant = list->corr;
		list->corr->prox = temp;
		list->fin = temp;
	}
	list->tam++;
}

void* lst_retIni(Lista* list)
{
	if (lst_vazia(list) == 1)
	{
		return NULL;
	}

	void* elem = list->ini->info;
	
	if (list->fin == list->ini)
	{
		free (list->fin);
		list->ini = NULL;
		list->fin = NULL;
	}
	else{
	list->corr = list->ini;
	list->ini = list->corr->prox;

	free(list->corr);

	list->corr = list->ini;
	list->ini->ant = NULL;
	}

	list->tam--;

	return elem;
}

void* lst_retFin(Lista* list)
{
	if (lst_vazia(list) == 1)
	{
		return NULL;
	}

	void* elem = list->fin->info;
	
	if (list->fin == list->ini)
	{
		free(list->ini);
		list->ini = NULL;
		list->fin = NULL;
	}
	
	else{
		
		list->corr = list->fin;
		list->fin = list->corr->ant;
	
		free(list->corr);
	
		list->corr = list->fin;
		list->fin->prox = NULL;
	}

	list->tam--;

	return elem;
}

void lst_posIni(Lista*list){
	if (lst_vazia(list) == 1)
		list->corr = NULL;
	else
		list->corr = list->ini;
	return;
}

void lst_posFin(Lista*list){
	if (lst_vazia(list) == 1)
		list->corr = NULL;
	else
		list->corr = list->fin;
}

void *lst_prox(Lista*list){
	if (list->corr == NULL)
		return NULL;
	void *el = list->corr->info;
	list->corr = list->corr->prox;
	return el;
}

void *lst_ant(Lista *list){
	 if (list->corr == NULL)
		return NULL;
	void *el = list->corr->info;
	list->corr = list->corr->ant;
	return el;
}

void lst_libera(Lista *list){
	lst_posFin(list);	

	No * aux;
	while (list->corr != list->ini){
			aux = list->corr;
			list->corr = list->corr->ant;
			list->corr->prox = NULL;

			free(aux);
	}
	free(list->corr);
	free(list);
	
	if(list) 
		printf("\n !!! lista liberada !!! \n");
	else printf("\n!!! ainda existe lista !!!!\n");
}
