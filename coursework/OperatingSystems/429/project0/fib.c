#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>

const int MAX = 13;

static void doFib(int n, int doPrint);


/*
 * unix_error - unix-style error routine.
 */
inline static void unix_error(char *msg)
{
    fprintf(stdout, "%s: %s\n", msg, strerror(errno));
    exit(1);
}


int main(int argc, char **argv)
{
    int arg;
    int print=1;

    if(argc != 2){
        fprintf(stderr, "Usage: fib <num>\n");
        exit(-1);
    }

    arg = atoi(argv[1]);
    if(arg < 0 || arg > MAX){
        fprintf(stderr, "number must be between 0 and %d\n", MAX);
        exit(-1);
    }

    doFib(arg, print);

    return 0;
}

/*
 * Recursively compute the specified number. If print is
 * true, print it. Otherwise, provide it to my parent process.
 *
 * NOTE: The solution must be recursive and it must fork
 * a new child for each call. Each process should call
 * doFib() exactly once.
 */
  static void doFib(int n, int doPrint)
{
  int result = 0;
  pid_t pid1;
  pid_t pid2;
  int status;

  //base case
  if ((n == 0) || (n==1)) {
  	if (doPrint) {
  		//printf("base: %d\n",n);
  		exit(0);
  	} else {
  		exit(n);
  	}
  }

  //creating child processes for recursion
  if ((pid1 = fork()) == 0) {
  	doFib(n-1,0);
  }
  if ((pid2 = fork()) == 0) {
  	doFib(n-2,0);
  }

  while (waitpid(pid1,&status,0) > 0) {
  	if (WIFEXITED(status)) {
  		//printf("reaping first child status %d\n",WEXITSTATUS(status));
  		result += WEXITSTATUS(status);

  	}
  }

  while (waitpid(pid2,&status,0) > 0) {
  	if (WIFEXITED(status)) {
  		//printf("reaping second child\n");
  		result += WEXITSTATUS(status);
  	}
  }

  if (doPrint) {//doPrint is only True for the original Parent
  	printf("%d\n",result);
  	exit(0);
  } else {
  	//printf("sending result to parent\n");
  	exit(result);
  }

}
