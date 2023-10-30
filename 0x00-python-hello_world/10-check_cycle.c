#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle
 * @list: Pointer to the head of the linked list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (slow != NULL && fast != NULL && fast->next != NULL)
    {
        slow = slow->next;      // Move slow one step
        fast = fast->next->next; // Move fast two steps

        // If they meet, there is a cycle
        if (slow == fast)
            return 1;
    }

    // If they don't meet, there is no cycle
    return 0;
}

