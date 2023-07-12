#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "vetor.h"

struct vetor{
	float x,y;
};

Vetor * vet_cria(float a, float b){
	Vetor *vet;
	vet = (Vetor*) malloc(sizeof(struct vetor));
	if (vet == NULL){
		printf("Erro ao alocar memoria");
		exit(1);
	}
	vet->x=a;
	vet->y=b;
	return vet;
}

Vetor * vet_soma(Vetor *u, Vetor *v){
	Vetor *w = vet_cria(0.0,0.0);
	w->x = u->x + v->x;
	w->y = u->y + v->y;
	return w;
}

float vet_norma(Vetor *u){
	return sqrt(pow(u->x,2)+pow(u->y,2));
}

float vet_prod_int(Vetor *u, Vetor *v){
	return u->x*v->x+u->y*v->y;
}

char * vet_format(Vetor *u, char *str){
	sprintf(str, "(%.1f,%.1f)", u->x, u->y);
	return str;
}

void vet_libera(Vetor *u){
	free(u);
}
