#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - function that inserts a number into a sorted linked list.
 * @head: firs element of the list.
 * @number: the value of node.
 * Return: the address of the new node or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *current;

	current = *head;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (*head == NULL)
		*head = node;
	else if (node->n < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	else
	{
		while ((current->next != NULL) &&
		       (current->next->n < node->n))
		{
			current = current->next;
		}
		node->next = current->next;
		current->next = node;
	}
	return (node);
}
