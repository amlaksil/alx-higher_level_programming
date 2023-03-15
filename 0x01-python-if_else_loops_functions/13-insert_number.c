#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: points to the first element on the list
 * @number: the number to be inserted
 *
 * Return: the address of the new node
 * or NUll if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *prev;
	listint_t *temp = *head;
	int k = 0;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (temp == NULL)
	{
		*head = new;
		return (new);
	}
	while (temp != NULL)
	{
		if (temp->n >= number)
		{
			new->next = temp;
			if (k != 0)
				prev->next = new;
			temp = new;
			if (k == 0)
				*head = temp;
			return (temp);
		}
		k++;
		prev = temp;
		temp = temp->next;
	}
	if (temp == NULL)
		prev->next = new;

	return (new);
}
