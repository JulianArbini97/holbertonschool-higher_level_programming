#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert node at right space
 *
 * @head: the head of the list
 * @number: the value of the node
 *
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new;
  listint_t *actual;

  current = *actual;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);

  new->n = number;

  if (*head == NULL)
    *head = new;
  else
    {
      if (number < actual->n)
	{
	  new->next = actual;
	  *head = new;
	}
      else
	{
	  while (actual->next && number > actual->next->n)
	    actual = actual->next;

	  new->next = actual->next;
	  actual->next = new;
	}
    }
  return (new);
 }
