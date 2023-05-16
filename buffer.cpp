#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char *gets(char *);

int main(int argc, char **argv)
{
  struct
  {
    char buffer[4];
    volatile int changeme;
  } locals;

  printf("%s\n", "Start");

  locals.changeme = 0;
  gets(locals.buffer);

  if (locals.changeme != 0)
  {
    puts("Buffer overflowed and 'changeme' variable has been changed!");
  }
  else
  {
    puts(
        "No buffer overflow & 'changeme' has not yet been changed. Would you like to try "
        "again?");
  }
  exit(0);
}

// #include <stdio.h>
// int main()
// {
//   struct
//   {
//     char text[5];
//     short int code;
//   } local;
//   local.code = 0;
//   gets(local.text);
//   if (local.code == 97)
//   {
//     puts("Buffer overflow successful");
//   }
//   else
//   {
//     puts("Buffer overflow unsuccessful");
//   }
//   return 0;
// }