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
	int i, nums[60];
	listint_t *ptr;

	ptr = rev(head);

	for (i = 0; *head != NULL; i++)
	{
		nums[i] = (*head)->n;
		*head = (*head)->next;
	}
	*head = ptr;
	rev(head);

	for (i = 0; *head != NULL; i++)
	{
		if ((*head)->n != nums[i])
			return (0);
		*head = (*head)->next;
	}
	return (1);
}
