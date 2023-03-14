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
	listint_t *current = *head, *prev = *head, *slow = *head, *fast = *head;
	listint_t *midnode = NULL, *second_half;
	int status;

	if (current == NULL && current->next == NULL)
		return (1);
	/*
	 * Get the middle of the list. Move slow by 1 and  fast by 2 slow will
	 * have the middle node
	*/

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow, slow = slow->next;
	}
	/*
	 * fast would become NULL for enven number node and for odd we need
	 * to skip the middle node and store it somewhere so that we can restore
	 * the original list
	*/
	if (fast != NULL)
		midnode = slow, slow = slow->next;

	second_half = slow, prev->next = NULL; /* terminate first half */
	reverse(&second_half);
	status = compare_list(current, second_half);
	/* Restore the original list */
	reverse(&second_half);
	if (midnode != NULL)
		prev->next = midnode, midnode->next = second_half;
	else
		prev->next = second_half;

	if (status != 0)
		return (1);
	else
		return (0);
}

/**
 * reverse - listint_t singlylinked list
 * @head: pointer to pointer which points to the first item in the list
 *
 * Return: void
 */
void reverse(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL, *temp;

	while (current != NULL)
	{
		temp = current->next;
		current->next = prev;
		prev = current;
		current = temp;
	}
	*head = prev;
}

/**
 * compare_list - compares the two list given
 * @head1: pointer to the first list
 * @head2: pointer to the second list
 *
 * Return: 0 if the list contain the same element if not 1
 */
int compare_list(listint_t *head1, listint_t *head2)
{
	listint_t *current = head1;
	listint_t *second_half = head2;

	while (current && second_half)
	{
		if (current->n == second_half->n)
		{
			current = current->next;
			second_half = second_half->next;
		}
		else
			return (0);
	}
	if (current == NULL && second_half == NULL)
		return (1);

       /* will reach here when one is NULL and other is not */
	return (0);
}
