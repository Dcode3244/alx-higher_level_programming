#include "lists.h"

/**
 * check_cycle - checks if a linked list has a loop or not
 * @list: pointer to the head of the linked list
 * Return: 0 if no loop, or 1 if there is a loop
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = slow = list;

	do {
		fast = fast->next->next;
		slow = slow->next;

		if (fast == NULL)
			return (0);
	} while (fast != slow);

	return (1);
}
