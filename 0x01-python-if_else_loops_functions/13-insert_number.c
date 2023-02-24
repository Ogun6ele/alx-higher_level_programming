#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list of numbers
 * singly linked list
 * @head: address of head to the list
 * @number: number to be added
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	
	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;
	
	return (new);
}
