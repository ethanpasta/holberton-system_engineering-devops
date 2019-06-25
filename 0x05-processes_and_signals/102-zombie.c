#include <stdio.h>
#include <stdlib.h>

/**
 * main - entry point
 *
 * Return: exit status
 */
int main(void)
{
	int i;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (1);
}

/**
 * infinite_while - function runs an infinite loop
 *
 * Return: returns 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
