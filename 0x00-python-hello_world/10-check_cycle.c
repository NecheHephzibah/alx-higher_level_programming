#include "lists.h"

/**
  * check_cycle - function that checks if a singly linked list
  * contain a cycle
  * @list: the linked list to check
  * Return: 1 if there is a cycle and 0 otherwise
  */

int check_cycle(listint_t *list)
{
	listint_t *forward = list;
	listint_t *backward = list;

	if (!list)
		return (0);

	while (backward && forward && forward->next)
	{
		backward = backward->next;
		forward = forward->next->next;
		if (backward == forward)
			return (1);
	}
	return (0);
}
