#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>

/**
  * insert_node - function that inserts a number to a sorted list
  * @head: the linked list
  * @number: the number that will be inserted at the end of the list.
  * Return: the new node.
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}
		temp->next = new;
		new->next = current;
	}
	return (new);
}
