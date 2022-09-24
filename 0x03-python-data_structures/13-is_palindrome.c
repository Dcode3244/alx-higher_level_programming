#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the first linked list item
 * Return: 0 if it is not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	int i, j = 0, k;
	listint_t *front, *back;

	front = back = *head;
	while ((*head) != NULL)
	{
		j++;
		*head = (*head)->next;
	}
	*head = front;

	for (i = 1; i <= j; j--, i++)
	{
		back = *head;
		for (k = 1; k < j; k++)
			back = back->next;

		if (front->n != back->n)
			return (0);

		front = front->next;
	}
	return (1);
}
