typedef struct vetor Vetor;

Vetor *vet_cria(float, float);
Vetor *vet_soma(Vetor *, Vetor *);
float vet_norma(Vetor *);
float vet_prod_int(Vetor *,Vetor *);
char *vet_format(Vetor *,char *);
void vet_libera(Vetor *);
