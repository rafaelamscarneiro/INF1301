/* TAD: Data */

typedef struct data Data;

Data* dt_cria (int dia, int mes, int ano);
Data* dt_cria (const char *d);
void dt_libera (Data* d);
char *dt_to_string (Data* d);
int dt_difData (Data *dt1,Data *dt2);
int dt_comp (Data *dt1,Data *dt2);