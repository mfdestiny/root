/*
  utcsh - The UTCS Shell

  <Put your name and CS login ID here>
*/

/* Read the additional functions from util.h. They may be beneficial to you
in the future */
#include "util.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Global variables */
/* The array for holding shell paths. Can be edited by the functions in util.c*/
char shell_paths[MAX_ENTRIES_IN_SHELLPATH][MAX_CHARS_PER_CMDLINE];
static char prompt[] = "utcsh> "; /* Command line prompt */
static char *default_shell_path[2] = {"/bin", NULL};
/* End Global Variables */

/* Convenience struct for describing a command. Modify this struct as you see
 * fit--add extra members to help you write your code. */
struct Command {
  char **args;      /* Argument array for the command */
  char *outputFile; /* Redirect target for file (NULL means no redirect) */
};

/* Here are the functions we recommend you implement */

char **tokenize_command_line(char *cmdline);
struct Command parse_command(char **tokens);
void eval(struct Command *cmd);
int try_exec_builtin(struct Command *cmd);
void exec_external_cmd(struct Command *cmd);

/* Main REPL: read, evaluate, and print. This function should remain relatively
   short: if it grows beyond 60 lines, you're doing too much in main() and
   should try to move some of that work into other functions. */
int main(int argc, char **argv) {
  set_shell_path(default_shell_path);

  /* These two lines are just here to suppress certain warnings. You should
   * delete them when you implement Part 1.4 */
  (void)argc;
  (void)argv;
  char* buffer;
  size_t bufsize = MAX_CHARS_PER_CMDLINE;
  size_t bytes_read;
  
  
  while (1) {
    printf("%s", prompt);
    /* Read */
    buffer = (char *)malloc(sizeof(char) * bufsize);
    if (buffer == NULL) { //if malloc fails throw error and exit
    	perror("Unable to allocate buffer");
    	free(buffer);
    	exit(1);
    }
    bytes_read = getline(&buffer,&bufsize,stdin);
    if ((int)bytes_read == -1) {
    	perror("Error in getline"); //if getline throws an error
    	free(buffer);
    	exit(1);
    }
    if (strcmp(buffer,"exit\n") == 0) {
    	printf("exiting\n");
    	free(buffer); //release memory
    	exit(0);
    }
    
    /* Evaluate */
    //tokenize arguments
    char** tokens = tokenize_command_line(buffer);
    free(buffer);
    //parse tokens into command struct
    struct Command commands = parse_command(tokens);
    //pass command struct through eval
    eval(&commands);

    /* Print (optional) */
  }
  return 0;
}

/* NOTE: In the skeleton code, all function bodies below this line are dummy
implementations made to avoid warnings. You should delete them and replace them
with your own implementation. */

/** Turn a command line into tokens with strtok
 *
 * This function turns a command line into an array of arguments, making it
 * much easier to process. First, you should figure out how many arguments you
 * have, then allocate a char** of sufficient size and fill it using strtok()
 */
char **tokenize_command_line(char *cmdline) {
  
  char** buffer = malloc(sizeof(char*) * MAX_WORDS_PER_CMDLINE); //allocate for worst case.
  char* p = NULL;
  int index = 0;
  
  p = strtok(cmdline, " \n"); //tokenize
  
  if (buffer != NULL) {
	while (p != NULL) {
		buffer[index++] = p;
		p = strtok(NULL, " \n");	  
	}
  }
  
  return buffer;
}

/** Turn tokens into a command.
 *
 * The `struct Command` represents a command to execute. This is the preferred
 * format for storing information about a command, though you are free to change
 * it. This function takes a sequence of tokens and turns them into a struct
 * Command.
 */
struct Command parse_command(char **tokens) {
  int index = 0;
  while (tokens[index] != NULL) { //
  	if (tokens[index] == NULL) {
  		printf("end of token list\n");
  		break;
  	}
  	printf("tokens %s\n", tokens[index]);
  	index++;
  	
  }
  struct Command dummy = {.args = tokens, .outputFile = NULL};
  return dummy;
}

/** Evaluate a single command
 *
 * Both built-ins and external commands can be passed to this function--it
 * should work out what the correct type is and take the appropriate action.
 */
void eval(struct Command *cmd) {
  (void)cmd;
  //printf("attempting to evaluate\n");
  return;
}

/** Execute built-in commands
 *
 * If the command is a built-in command, immediately execute it and return 1
 * If the command is not a built-in command, do nothing and return 0
 */
int try_exec_builtin(struct Command *cmd) {
  (void)cmd;
  
  return 0;
}

/** Execute an external command
 *
 * Execute an external command by fork-and-exec. Should also take care of
 * output redirection, if any is requested
 */
void exec_external_cmd(struct Command *cmd) {
  (void)cmd;
  return;
}
