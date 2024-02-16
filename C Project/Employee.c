#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

struct employee{
    char id[10];
    char name[20];
    char surname[20];
    char position[20];
    float salary;
}emp;

void insert_data();
void delete_data();
void search_data();

int main(){
    int choice;
    char tmp[20];
    do{
        system("cls");
        printf("####################################\n");
        printf("###  Welcome to employee system  ###\n");
        printf("####################################\n");
        printf("###     Please select choice     ###\n");
        printf("###        1. Insert Data        ###\n");
        printf("###        2. Delete Data        ###\n");
        printf("###        3. Search Data        ###\n");
        printf("###        4. Exit               ###\n");
        printf("####################################\n");
        printf("Please select choice(1-4 only): ");
        gets(tmp);
        choice = atoi(tmp);
        if(choice==1)insert_data();
        else if(choice==2)delete_data();
        else if(choice==3)search_data();
    }while(choice!=4);
    system("cls");
    printf("#########################\n");
    printf("## End of the program! ##\n");
    printf("#########################\n");
    return 0;
}

void insert_data(){
    FILE *fp;
    char ans;
    char tmp[20];

    if((fp=fopen("employee.txt","ab"))==NULL){
        printf("Can't open file for insert data\n");
        getch();
        exit(1);
    }
    do{
        printf("\nPlease insert employee data\n");
        printf("Employee ID : "); gets(emp.id);
        printf("Name        : "); gets(emp.name);
        printf("Surname     : "); gets(emp.surname);
        printf("Position    : "); gets(emp.position);
        printf("Salary      : "); gets(tmp);
        emp.salary = atof(tmp);
        fwrite(&emp,sizeof(emp),1,fp);
        if(ferror(fp)){
            printf("Error for insert data\n");
            getch();
            exit(1);
        }
        printf("Continue(press C) or Exit(press E) : ");
        ans = getche();
        while(ans!='C'){
            if(ans=='E'){
                break;
            }else if(ans!='C'){
                system("cls");
                printf("\nPlease enter only C and E\n");
                printf("Continue(press C) or Exit(press E) : ");
                ans = getche();
            }
        }
    }while(ans!='E');
    fclose(fp);
}

void delete_data(){
    FILE *fp;
    char ans;
    char rec[10];
    if((fp=fopen("employee.txt","rb+"))==NULL){
        printf("Can't open file for delete data\n");
        getch();
        exit(1);
    }
    printf("\nThis is employee for delete\n");
    do{
        int i=0;
        while(1){
            fread(&emp,sizeof(emp),1,fp);
            if(ferror(fp)){
                printf("\nError to read data for delete\n");
                exit(1);
            }
            if(feof(fp)){
                break;
            }
            ++i;
            printf("%d.%s\t\t",i,emp.id);
        }
        printf("\nDo you want to delete data(Y or N) : ");
        ans = getche();
        if(ans=='N'){
            break;
        }
        else if(ans=='Y'){
            printf("\nEnter record number : ");
            gets(rec);
            fseek(fp,((atoi(rec)-1)*sizeof(emp)),SEEK_SET);
            strcpy(emp.id,"\0");
            fwrite(&emp,sizeof(emp),1,fp);
            if(ferror(fp)){
                printf("Error for delete data\n");
                getch();
                exit(1);
            }
            printf("Delete data complete!\n");
            printf("\nPlease press any button to return to the home page.");
            getch();
            break;
        }
        else{
            printf("\nPlease enter only Y and N\n");
        }
    }while(1);
    fclose(fp);
}

void search_data(){
    FILE *fp;
    char ans;
    char id[10];
    if((fp=fopen("employee.txt","rb"))==NULL){
        printf("Can't open file for search data\n");
        getch();
        exit(1);
    }
    do{
        printf("\nPlease enter employee id for search : ");
        scanf("%s",id);

        while(1){
            fread(&emp,sizeof(emp),1,fp);
            if(ferror(fp)){
                printf("Error for search data\n");
                getch();
                exit(1);
            }
            if(feof(fp)){
                break;
            }
            if(strcmp(id,emp.id)==0){
                printf("Data Found!!\n");
                printf("Employee ID : %s\n",emp.id);
                printf("Name        : %s\n",emp.name);
                printf("Surname     : %s\n",emp.surname);
                printf("Position    : %s\n",emp.position);
                printf("Salary      : %.2f\n\n",emp.salary);
                break;
            }
        }
        if(strcmp(id,emp.id)!=0){
            printf("No employee in employee id %s\n\n",id);
        }
        printf("Continue(press C) or Exit(press E) : ");
        ans = getche();
        rewind(fp);
        while(ans!='C'){
            if(ans=='E'){
                break;
            }else if(ans!='C'){
                system("cls");
                printf("\nPlease enter only C and E\n");
                printf("Continue(press C) or Exit(press E) : ");
                ans = getche();
            }
        }
        printf("\n");
    }while(ans!='E');
    fclose(fp);
}
