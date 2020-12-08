#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node to linked list
 * @head: head of singly linked list
 * @number: input value
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insertnode, *temporal;

	temporal = *head;
	if (!head)
		return (NULL);
	insertnode = malloc(sizeof(listint_t));
	if (!insertnode)
		return (NULL);
	insertnode->n = number;
	if (!temporal || temporal->n >= number)
	{
		insertnode->next = temporal;
		*head = insertnode;
		return (insertnode);
	}
	return (insertnode);
}
