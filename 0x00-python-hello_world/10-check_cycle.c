#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tmp;

	head = list;
	tmp = list;

	while(tmp != NULL && head->next != NULL && head->next->next != NULL)
	{
		head = head->next->next;
		tmp = tmp->next;

		if (head == tmp)
			return (1);
	}
	return (0);
}
