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

	while (ground != NULL && list != NULL)
	{
		ground = ground->next;
		list = list->next->next;
		if (list == ground)
			return (1);
	}
	return (0);
}
