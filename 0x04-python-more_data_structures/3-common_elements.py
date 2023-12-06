#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing common elements in both input sets.
    """
    # Use the intersection operator (&) to find common elements
    common_set = set_1 & set_2

    return common_set

# Example usage:
if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}

    # Find and print the common elements
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))

