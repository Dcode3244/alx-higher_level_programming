#include "lists.h"

void free_ptr(listint_t *head);
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
 * free_ptr - frees malloced memory
 * @head: pointer to the memory to be freed
 */
void free_ptr(listint_t *head)
{
	listint_t *ptr;

	while (head != NULL)
	{
		ptr = head->next;
		free(head);
		head = ptr;
	}
}
/**
 * is_palindrome - checks whether a linked list is a palindrome or not
 * @head: pointer to the head of the linked list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int i;
	listint_t *head_ptr, *new, *new_ptr;

	if (head == NULL || *head == NULL)
		return (1);

	head_ptr = rev(head);
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
	*head = head_ptr;
	head_ptr = rev(head);

	new = new_ptr;
	while (*head != NULL)
	{
		if ((*head)->n != new_ptr->n)
		{
			*head = head_ptr;
			free_ptr(new);
			return (0);
		}
		*head = (*head)->next;
		new_ptr = new_ptr->next;
	}
	*head = head_ptr;
	free_ptr(new);

	return (1);
}
