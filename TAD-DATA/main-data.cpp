#include <stdio.h>
#include <stdlib.h>
#include "data.h"
#include <string.h>

int main() {
    Data *d1=dt_cria("01/01/2021");
    Data *d2=dt_cria(11,3,2021);
    int ret;
    
    ret=dt_comp (d2,d1);
    if(ret > 0)
        printf("A data %s é posterior a %s \n",dt_to_string (d2),dt_to_string (d1));
    else
        if(ret < 0)
            printf("A data %s é anterior a %s \n",dt_to_string (d2),dt_to_string (d1));
        else
            printf("As datas %s e %s são iguais\n",dt_to_string (d2),dt_to_string (d1));
    
    printf("A diferença entre as duas datas é de %d dias\n",dt_difData(d1,d2));
    
    dt_libera(d1);
    dt_libera(d2);

    return 0;
}