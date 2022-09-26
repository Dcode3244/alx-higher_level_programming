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
 * is_palindrome - checks whether a linked list is a palindrome or not
 * @head: pointer to the head of the linked list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int i, len = 0;
	listint_t *new, *temp;

	temp = new = *head;
	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < len / 2; i++)
		temp = temp->next;

	rev(&temp);

	while (temp != NULL)
	{
		if (new->n != temp->n)
			return (0);
		new = new->next;
		temp = temp->next;
	}
	return (1);
}
