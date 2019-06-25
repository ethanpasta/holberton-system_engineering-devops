#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - function runs an infinite loop
 *
 * Return: random value
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

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
			exit(1);
		else
			printf("Zombie process created, PID: %d\n", child);
	}
	infinite_while();
	return (1);
}
