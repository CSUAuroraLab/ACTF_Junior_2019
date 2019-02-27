#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

char adminps[16];
char flag[30];
char user[10][16] = {0};
char passwd[10][16] = {0};
char *current_user = "NULL";
int usercnt = 0;

void admin_login();
void user_login();
void regist();
void getflag();
void show_user();
void gets(char *a);

int main()
{
  int fd = open("/dev/urandom", O_RDONLY);
  if (fd < 0)
  {
    puts("Something goes wrong, tell admin...");
    exit(1);
  }
  else
  {
    ssize_t result = read(fd, adminps, 16);
    if (result < 0)
    {
      puts("Something goes wrong, tell admin...");
      exit(1);
    }
  }
  fd = open("flag", O_RDONLY);
  if (fd < 0)
  {
    puts("Something goes wrong, tell admin...");
    exit(1);
  }
  else
  {
    ssize_t result = read(fd, flag, 30);
    if (result < 0)
    {
      puts("Something goes wrong, tell admin...");
      exit(1);
    }
  }
  // puts(adminps);
  while (1)
  {
    int option;
    puts("What you want to do?\n"
         "1) Login as admin\n"
         "2) Login as user\n"
         "3) Register(max 10 account)\n"
         "4) Getflag(admin only)\n"
         "5) Who am I\n"
         "6) Exit");
    scanf("%d", &option);
    getchar();
    switch (option)
    {
      case 1:
        admin_login();
        break;
      case 2:
        user_login();
        break;
      case 3:
        regist();
        break;
      case 4:
        getflag();
        break;
      case 5:
        show_user();
        break;
      case 6:
        goto END;
      default:
        printf("What do you mean by %d", option);
        break;
    }
  }
  END:
  puts("You're welcome~");
  return 0;
}

void admin_login()
{
  char passwdbuf[16];
  printf("Input admin's password:");
  gets(passwdbuf);
  puts(passwdbuf);
  if (!memcmp(adminps, passwdbuf, 16)){
    current_user = "admin";
  } else {
    puts("Wrong password!!!");
  }
}

void user_login()
{
  char namebuf[16], passwdbuf[20];
  puts("Input username:");
  gets(namebuf);
  puts("Input password:");
  gets(passwdbuf);
  for (int i = 0; i < usercnt; ++i) {
    // printf("%s %s %s %s\n",namebuf,passwdbuf,user[i],passwd[i]);
    if (!strcmp(namebuf, user[i]) && !strncmp(passwdbuf, passwd[i], 16)){
      current_user = user[i];
      printf("Login success! Welcome, %s!\n", current_user);
      return;
    }
  }
  printf("You probably input wrong username or password...\n");
}

void regist()
{
  char namebuf[16], passwdbuf[16];
  if (usercnt < 10) {
    puts("Input your name");
    gets(namebuf);
    if (!strcmp(namebuf, "admin")) {
      puts("You can not register as admin!!!");
      return;
    }
    puts("Input your password");
    // printf("%p\n%p", namebuf, passwdbuf);
    gets(passwdbuf);
    // puts(namebuf);
    strncpy(user[usercnt], namebuf, 16);
    strncpy(passwd[usercnt], passwdbuf, 16);
    // puts(user[usercnt]);
    // puts(passwd[usercnt]);
    printf("Registered %s\n", namebuf);
    ++usercnt;
  } else {
    puts("Too many account...");
  }
}

void getflag()
{
  if (!strcmp(current_user, "admin")) {
    puts(flag);
  } else {
    puts("Ops...\nYou're not admin!!!");
  }
}

void show_user()
{
  printf("You're %s\n", current_user);
}