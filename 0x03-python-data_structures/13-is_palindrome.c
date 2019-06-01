#include "lists.h"
#include <stdio.h>

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
	listint_t *trav = *head;
	int store[2048];
	int len, i = 0, start = 0, end;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	len = get_len(*getter);
	end = len - 1;
	if (len == 1)
		return (1);
	while (trav->next != NULL)
	{
		store[i] = trav->n;
		trav = trav->next;
		i++;
	}
	store[i++] = '\0';
	while (start < len && end >= 0)
	{
		if (start >= end)
			return (1);
		if (store[start] != store[end])
			return (0);
		start++;
		end--;
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
