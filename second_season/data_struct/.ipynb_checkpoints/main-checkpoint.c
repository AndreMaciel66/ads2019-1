#include <stdio.h>
typedef struct {
    int matricula;
    char nome[100];
    float nota;
} Aluno;
int main() {
  int N, i; // quantidade de alunos
  Aluno aluno[10];
  printf("Programa - Alunos\n");
  printf("Informe a quantidade de alunos:");
  scanf("%d", &N);
  i = 0;
  while (i < N) {
    printf("Matrícula do aluno: ");
    scanf("%d", &aluno[i].matricula);
    printf("Nome do aluno: ");
    scanf("%s", aluno[i].nome);    
    printf("Nota do aluno: ");
    scanf("%f", &aluno[i].nota);        
    i++;
  }
  printf("Alunos aprovados\n");
  i = 0;
  while (i < N) {
    if (aluno[i].nota > 60) 
      printf("Matrícula: %d, Nome: %s, Nota: %f\n",aluno[i].matricula, aluno[i].nome,aluno[i].nota); 
      i++;
  }

  return 0;
}