/*   GRUPO:
Daniel Peralta (1811442)
Felipe Meiga (2011460)
Rafaela Carneiro (2011483)
*/

#include <stdio.h>
#include <stdlib.h>
#include "UI.h"
#define MAX 10

struct lista
{
	int tam;
	void **vet;
	int ini, fin, corr;
};

Lista* lst_cria(void)
{
	Lista* lst = (Lista*)malloc(sizeof(Lista));

	if (lst == NULL)
	{
		printf("Error while dynamically allocating memory for \"lst\"!");
		exit(1);
	}
	
	lst->vet = (void*)malloc(MAX*sizeof(void));

	lst->tam = 0;
	lst->ini = 0;
	lst->fin = 0;
	lst->corr = -1;

	return lst;
}

int lst_vazia(Lista* list)
{
	if (list->tam == 0)
	{
		return 1;
	}

	return 0;
}

void lst_insIni(Lista* list, void* data)
{
	if (list->tam == MAX)
	{
		printf("Lista lotada\n");
		return;
	}
     if( lst_vazia(list) == 1)
    {
    	list->ini = MAX-1;
    	list->fin = 1;
        list->vet[0] = data;
	}
    
    else
    {		
		list->vet[list->ini] = data;
		list->ini = (list->ini-1)%MAX;
    }
        
    list->tam++;
}

void lst_insFin(Lista* list, void* data)
{
	if (list->tam == MAX)
	{
		printf("Lista lotada\n");
		return;
	}
	
    if( lst_vazia(list) == 1)
    {
    	list->ini = MAX-1;
    	list->fin = 1;
        list->vet[0] = data;
	}
    
    else
    {		
		list->vet[list->fin] = data;
		list->fin = (list->fin+1)%MAX;
    }
        
    list->tam++;
}

void *lst_retIni(Lista *list)
{

	if (lst_vazia(list) == 1)
		return NULL;
	
	list->ini = (list->ini+1)%MAX;
	list->tam--;
	
	return list->vet[list->ini];
}

void *lst_retFin(Lista *list)
{
	if (lst_vazia(list)==1)
		return NULL;
	
	list->fin = (list->fin-1)%MAX;
	list->tam--;
	
	return list->vet[list->fin];
}

void lst_posIni(Lista* list) 
{
	if (lst_vazia(list) == 1)
		list->corr = -1;
		
	else
		list->corr = (list->ini+1)%MAX;
}

void lst_posFin(Lista* list) 
{
	if (lst_vazia(list) == 1)
		list->corr = -1;

	else
		list->corr = (list->fin-1)%MAX;
}

void *lst_prox(Lista *list)
{	
	if (list->corr == -1)
		return NULL;
		
	void *elem = list->vet[list->corr];
		
	list->corr = (list->corr+1)%MAX;
	
	if (list->corr== list->fin)
		list->corr = -1;
		
	return elem;
}

void *lst_ant(Lista *list){
	if (list->corr==-1)
		return NULL;
	
	void *elem = list->vet[list->corr];
	
	list->corr = (list->corr-1)%MAX;
	
	if (list->corr == list->ini)
		list->corr = -1;
	
	return elem;
}

void lst_libera(Lista* list)
{
	lst_posIni(list);
	
	while(list->tam > 0)
	{
		free(list->vet[list->corr]);
		list->corr = (list->corr + 1)%MAX;
		list->tam--;
	}
	
	free(list->vet);
	free(list);
	
	printf("\n=== free success ===\n");
}
