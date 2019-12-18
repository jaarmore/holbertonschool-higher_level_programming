#include "lists.h"
/**
 * is_palindrome - function that check if singly list is palindrome.
 * @head: first element of the list
 * Return: 1 if is palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *node_aux = *head;
	int sum = 0;

	if (*head == NULL)
		return (1);

	while (node_aux->next != NULL)
	{
		sum += node_aux->n;
		node_aux = node_aux->next;
	}

	if ((sum % 2) == 0)
		return (1);
	else
		return (0);
}
