#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - this function checks to see if
 * a linked list contains a cycle
 * @list: pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *ground = list;
	listint_t *chaser = list;

	while (ground != NULL)
	{
		while (chaser != NULL)
		{
			chaser = chaser->next;
			chaser = chaser->next;
			if (chaser == ground)
				return (1);
		}
		ground = ground->next;
	}
	return (0);
}
