#include <stdio.h>
#include "lists.h"

/**
* check_cycle - This code checks if a singly linked list has a cycle within it.
* @list:This is a singly linked list.
* Return: 0 is there is no cycle within, 1 if there is a cycle within.
*/

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tail;

	if (list == NULL)
		return (0);

	head = list;

	tail = list;

	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;

		tail = tail->next->next;

		if (head == tail)
			return (1);

	}
	return (0);
}
