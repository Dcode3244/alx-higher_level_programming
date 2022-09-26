#include "lists.h"

/**
 * rev - reverses a linked list
 * @head: pointer to the first item of the list
 * Return: pointer to the head of the reversed list
 */

listint_t *rev(listint_t **head)
{
	listint_t *temp, *next;

	temp = *head;
	*head = NULL;

	while (temp != NULL)
	{
		next = temp->next;
		temp->next = *head;
		*head = temp;
		temp = next;
	}

	return (*head);
}

/**
 * is_palindrome - checks whether a linked list is a palindrome or not
 * @head: pointer to the head of the linked list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int i;
	listint_t *ptr, *new, *new_ptr;

	ptr = rev(head);
	new = malloc(sizeof(listint_t));
	new_ptr = new;
	for (i = 0; *head != NULL; i++)
	{
		new->n = (*head)->n;
		*head = (*head)->next;
		if (*head != NULL)
		{
			new->next = malloc(sizeof(listint_t));
			new = new->next;
		}
		else
			new->next = NULL;
	}
	*head = ptr;
	rev(head);

	new = new_ptr;
	while (*head != NULL)
	{
		if ((*head)->n != new_ptr->n)
			return (0);
		*head = (*head)->next;
		new_ptr = new_ptr->next;
	}

	new_ptr = new;
	while (new != NULL)
	{
		new_ptr = new_ptr->next;
		free(new);
		new = new_ptr;
	}

	return (1);
}
