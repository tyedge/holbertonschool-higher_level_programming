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

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	while (ground != NULL && chaser != NULL && chaser->next != NULL &&
	       chaser->next->next != NULL)
	{
		ground = ground->next;
		chaser = chaser->next->next;
		if (chaser == ground)
			return (1);
	}
	return (0);
}
