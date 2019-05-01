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
	listint_t *chaser = list->next;

	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	while (ground != NULL && chaser != NULL && chaser->next != NULL &&
	       chaser->next->next != NULL)
	{
		if (chaser == ground)
			return (1);
		ground = ground->next;
		if (ground->next == NULL)
			return (1);
		chaser = chaser->next->next;
	}
	return (0);
}
