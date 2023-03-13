#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: pointer to pointer holds the address of the head of a list
 *
 * Return: 0 if it is not a palindrome
 * 1 if it is a palindrome and empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int k = 0, len = 0;
	int a[1024];

	if (*head == NULL)
		return (1);
	ptr = *head;
	while (ptr != NULL)
	{
		a[len] = ptr->n;
		ptr = ptr->next;
		len++;
	}
	while (a[k] == a[len - 1])
	{
		k++;
		len--;
		if (k == len)
			return (1);
		continue;
	}
	return (0);
}
