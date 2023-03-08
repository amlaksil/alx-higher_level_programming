#include "lists.h"

/**
 * check_cycle - checks if a listint_t list has a cycle in it
 * @list: the head of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cylce
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;
	while (temp != NULL)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
	}

	return (0);
}
