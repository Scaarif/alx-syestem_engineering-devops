#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infite_while - infinite loop
 * Return: 0
 */
int infite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: 0 (success) always
 */
int main(void)
{
	pid_t child_pid;
	int i;

	/* create 5 child processes */
	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		/* if child successfully created, print as such */
		if (child_pid > 0) /* child pid returned to process */
			sleep(1);
		else
			exit(0); /* failed to create child */
		printf("Zombie process created, PID: %d\n", child_pid);
	}
	/* indefinitely put the program to sleep */
	infite_while();

	return (0);
}
