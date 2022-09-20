#include "lists.h"

/**
 * insert_node - insertsa number into a sorted singly linked list
 * @head: pointer to first node of the list
 * @number:the number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *fptr, *sptr;

	if (head == NULL || *head == NULL)
		return (NULL);

	sptr = *head;
	fptr = (*head)->next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (number < sptr->n)
	{
		new->next = sptr;
		*head = new;
		return (*head);
	}
	while (fptr != NULL)
	{
		if (number < fptr->n)
		{
			new->next = fptr;
			sptr->next = new;
			break;
		}
		sptr = sptr->next;
		fptr = fptr->next;

		if (fptr == NULL && sptr->n < number)
		{
			sptr->next = new;
			new->next = NULL;
		}
	}

	return (*head);
}
