#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

void reversal(listint_t **head);
int list_compare(listint_t *head, listint_t *middle, int length);

/**
  * is_palindrome - function that checks if a singly linked
  * lists is a palindrome.
  * @head: pointer to the pointer of the first node in the lists passed
  * Return: 1 if palindrom exists, 0 otherwise.
  */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *middle;
	int length, i;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	middle = *head;

	for (length = 0; temp != NULL; length++)
		temp = temp->next;

	length = length / 2;

	for (i = 1; i < length; i++)
		middle = middle->next;

	if (length % 2 != 0 && length != 1)
	{
		middle = middle->next;
		length = length - 1;
	}
	reversal(&middle);
	i = list_compare(*head, middle, length);
	return (i);

}

/**
  * list_compare - compares two lists
  * @head: pointer to the head node
  * @middle: pointer to the middle node
  * @length: length of the list
  * Return: 1 if they're the same, 0 if they're not
  */

int list_compare(listint_t *head, listint_t *middle, int length)
{
	int i;

	if (head == NULL || middle == NULL)
		return (1);
	for (i = 0; i < length; i++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);

}


/**
  * reversal - function to reverse a list
  * @head: pointer to the head node to reverse
  * Return: void.
  */

void reversal(listint_t **head)
{
	listint_t *current, *next, *prev;

	if (head == NULL || *head == NULL)
		return;
	prev = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
