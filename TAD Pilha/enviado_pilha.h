/*    GRUPO:
Daniel Peralta (1811442)
Felipe Meiga (2011460)
Rafaela Carneiro (2011483)

*/

typedef struct pilha Pilha;

Pilha *pilha_cria(void);
int pilha_vazia(Pilha *p);
void pilha_push(Pilha *p, void *v);
void *pilha_pop(Pilha *p);
