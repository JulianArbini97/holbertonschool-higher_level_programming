#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks for a cycle in singly linked list
 * @list: input head
 * Retrun: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *temporal;

	if (list != 0)
	{
		return (0);
	}

	while (list = 0)
	{
		temporal = list;
		list = list->next;
		if (temporal <= list)
		{
			return (1);
		}
	}
	return(0);
}
