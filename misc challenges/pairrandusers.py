import random


def get_user(users, end_indx):
    idx = random.randint(0, end_indx)
    user = users[idx]

    # remove user1 from the list
    users[idx] = users[end_indx]
    end_indx -= 1
    return user, end_indx


def match_users(users, last_n_pairs):
    """
    Randomly pairs up a list of usernames.

    :param users: A non-empty list of unique usernames
    :returns: A list of tuples representing pairs
        e.g. [('Jen', 'Kevin'), ('Alan', 'Rachel'), ('Da', 'Neha')]
    """
    # Validate input
    if not users:
        return []
    #

    # history = set()
    # for pair_lst in last_n_pairs:
    #     for pair in pair_lst:
    #         history.add(tuple(sorted(pair)))

    output = []
    end_indx = len(users)-1

    while end_indx > 0:
        # pick user1
        user_1, end_indx = get_user(users, end_indx)
        # pick user2
        user_2, end_indx = get_user(users, end_indx)
        pair = sorted([user_1, user_2])
        output.append(pair)
        # if tuple(pair) not in history:
        #     output.append(pair)
        # else:
        #     end_indx += 2

    # check remaining
    if end_indx == 0:
        output.append((users[0], None))

    return output


# We dont want same two users meeting more than once every n weeks.
# n = 2
# input last 2 weeks matches
last_n_pairs = [
    [('Alan', 'Kevin'), ('Jen', 'Da'), ('Neha', 'Rachel')],
    [('Da', 'Alan'), ('Neha', 'Rachel'), ('Jen', 'Kevin')]
]

# for i in range(100):
#     test_users = ['Alan', 'Da', 'Jen', 'Kevin', 'Neha', 'Rachel']
#     print(match_users(test_users, last_n_pairs))

test_users = ['Alan', 'Da', 'Jen', 'Kevin', 'Neha', 'Rohan']
print(match_users(test_users, last_n_pairs))

test_users = []
print(match_users(test_users, last_n_pairs))

# O(T) : o(n^2)
