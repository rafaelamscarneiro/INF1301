#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "data.h"

struct data {
   int dd,mm,aa;	// formato dd/mm/aaaa
};

Data* dt_cria (int dia, int mes, int ano) {

Data* dt_cria (const char *d) {
    char aux[5];
    int dia, mes, ano;
    
    dia=atoi(strncpy(aux,d,2));



    
    return dt_cria (dia, mes, ano);
}

void dt_libera (Data* d) {
   free(d);
}

char *dt_to_string (Data* d) {
   char* str = (char*) malloc(11*sizeof(char));
   if (str == NULL) {
      printf("Memória insuficiente!\n");
      exit(1);
   }
   
   sprintf(str,"%02d/%02d/%04d",d->dd,d->mm,d->aa);
   
   return str;
}

int dt_difData(Data *dt1,Data *dt2) {
    int days1, days2;
    Data date1=*dt1,date2=*dt2;
 
    date1.mm = (date1.mm + 9)%12;
    date1.aa = date1.aa - date1.mm/10;
 
    date2.mm = (date2.mm + 9)%12;
    date2.aa = date2.aa - date2.mm/10;
 
    days1 = 365*date1.aa + date1.aa/4 - date1.aa/100 + date1.aa/400 + (date1.mm*306 + 5)/10 + ( date1.dd - 1 );
    days2 = 365*date2.aa + date2.aa/4 - date2.aa/100 + date2.aa/400 + (date2.mm*306 + 5)/10 + ( date2.dd - 1 );
 
    return days2 - days1;
}

// retorna o inteiro x
// se dt1 > dt2 então x > 0
// se dt1 < dt2 então x < 0
// se dt1 = dt2 então x = 0

// o mesmo comportamento da função strcmp()

int dt_comp (Data *dt1,Data *dt2) {

}