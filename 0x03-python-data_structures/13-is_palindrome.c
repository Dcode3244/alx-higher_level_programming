#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first linked list item
 * Return: 0 if it is not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	int i = 1, j, k = 1, len = 0;
	listint_t *front, *back, *start;

	front = back = start = *head;

	while ((*head) != NULL)
	{
		len++;
		*head = (*head)->next;
	}

	j = len;
	while (i <= j)
	{
		back = start;
		while (k < j)
		{
			back = back->next;
			k++;
		}
		if (front->n != back->n)
			return (0);
		front = front->next;
		k = 1;
		j--;
		i++;
	}

	return (1);
}
