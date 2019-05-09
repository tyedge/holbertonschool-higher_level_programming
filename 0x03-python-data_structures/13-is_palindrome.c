#include "lists.h"
#include <stdio.h>

listint_t *curr_trav(listint_t *curr, int c_idx);
listint_t *prev_trav(listint_t *prev, int p_idx);
int get_len(listint_t *h);

/**
 * is_palindrome - checks if a singly linked list is a
 * palindrome
 * @head: pointer to a pointer of the first element of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 *
 */



int is_palindrome(listint_t **head)
{
	listint_t **getter = head;
	listint_t *pretrav = *head;
	listint_t *curtrav = *head;
	listint_t *previous = NULL;
	listint_t *current = NULL;
	int prev_idx, curr_idx;
	int half, len = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	len = get_len(*getter);
	if (len % 2 == 0)
	{
		half = len / 2;
		prev_idx = half - 1;
		curr_idx = half;
	}
	else
	{
		half = (len - 1) / 2;
		prev_idx = half - 1;
		curr_idx = half + 1;
	}
	while (prev_idx >= 0 && curr_idx < len)
	{
		previous = prev_trav(pretrav, prev_idx);
		current = curr_trav(curtrav, curr_idx);
		if (previous->n != current->n)
			return (0);
		prev_idx -= 1;
		curr_idx += 1;
	}
	return (1);
}



/**
 * get_len - counts the elements in a linked
 * list
 * @h: pointer to the first element of the list
 *
 * Return: the number of nodes in the list
 *
 */

int get_len(listint_t *h)
{
	listint_t *numnode = h;
	int count = 0;


	while (numnode != NULL)
	{
		count++;
		numnode = numnode->next;
	}
	return (count);
}


/**
 * prev_trav - counts the elements in a linked
 * list
 * @prev: pointer to the first element of the list
 * @p_idx: desired index
 *
 * Return: pointer to node stored at desired index
 *
 */

listint_t *prev_trav(listint_t *prev, int p_idx)
{
	listint_t *pre = prev;
	int i = 0;

	while (i != p_idx)
	{
		if (pre->next != NULL)
		{
			pre = pre->next;
			i++;
		}
	}
	return (pre);

}


/**
 * curr_trav - counts the elements in a linked
 * list
 * @curr: pointer to the first element of the list
 * @c_idx: desired index
 *
 * Return: pointer to node stored at desired index
 *
 */

listint_t *curr_trav(listint_t *curr, int c_idx)
{
	listint_t *cur = curr;
	int i = 0;

	while (i != c_idx)
	{
		if (cur->next != NULL)
		{
			cur = cur->next;
			i++;
		}
	}
	return (cur);
}
