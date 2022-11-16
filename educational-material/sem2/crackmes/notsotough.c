#include <stdio.h>
#include <string.h>
#include <stdbool.h>
int main(){
     char password[200];

     printf("Enter the password: \n");
     scanf("%s",&password);
     //printf("P: %s\n", password);
     //printf("%d",strlen(password));
    bool flag1 = false;
    bool flag2 = true;
    if (strlen(password) >= 8){
        
        int i = 0;
        while(password[i]){
            //printf("%c",password[i]);
            switch(password[i]){

                case '@':
                    flag1 = !(flag1);
                    //printf("f1");
                    break;
                case 't':
                    flag2 = !(flag2);
                    //printf("f2");

            }
            i++;
        }
        if ((flag1 && flag2) == false){
            printf("Invalid password. You have been detained. Await your sentence at the end of time.\n");
            return 1;
        

        }
    }
    else{
        printf("Invalid password. You have been detained. Await your sentence at the end of time.\n");
        return 1;
    }
        //printf("%d",i);
    printf("Victory!");

    return 0;
}