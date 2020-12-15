#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 *
 * @head: the head address of the linked list
 *
 * Return: 1 if it's a palindrome, 0 else
 */

int is_palindrome(listint_t **head)
{

	listint_t *temp = *head;
	listint_t *temp2 = *head;
	int array[5000], i = 0, len = 0;

	if (!head)
		return (0);
	if (!*head || (*head)->next == NULL)
		return (1);

	for (len = 0; temp2->next != NULL; len++)
	{
		temp2 = temp2->next;
	}

	for (i = 0; i <= len; i++)
	{
		array[i] = temp->n;
		temp = temp->next;
	}

	for (i = 0, len; i < len; i++, len--)
	{
		if (array[len] != array[i])
		{
			return (0);
		}
	}
	return (1);
}
