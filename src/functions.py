def welcome_message():
    print('*' * 50)
    for i in range(30):
        if i == 15:
            print('*           Welcome to the MovieRec!             *')
        else:
            print('*' + ' ' * 48 + '*')
    print('*' * 50)


def enter_input():
    return input('Please enter a genre of your choice: ').lower()


def lcs(s1, s2, m, n):
    R = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                R[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                R[i][j] = R[i - 1][j - 1] + 1
            else:
                R[i][j] = max(R[i - 1][j], R[i][j - 1])

    return R[m][n]


def search_algorithm(movies, user_choice):
    if user_choice in movies:
        return movies[user_choice]
    else:
        most_likely = {} #a dictionary that stores the resemblance between user input and available genres
        for genre in movies:
            most_likely[genre] = lcs(genre, user_choice, len(genre), len(user_choice))
        most_likely = sorted(most_likely.items(), key=lambda x:-x[1])
        user_prompt = input(f'The genre {user_choice} is not currently available in our database - the closest match is'
                            f' {most_likely[0][0]}. Did you mean to write that? Enter y/n: ').lower()
        if user_prompt == 'y':
            return movies[most_likely[0][0]]
        else:
            return search_algorithm(movies, enter_input())


def sorting_algorithm():
    # sort all the movies in the inputted genre
    pass


def show_movies(movies, linked_list):
    print(linked_list.stringify_list())
    user_prompt = input('Do you want to see another genre? Enter y/n: ').lower()
    if user_prompt == 'n':
        return
    else:
        show_movies(movies, search_algorithm(movies, enter_input()))


def goodbye():
    print('Thank you for using our recommendation program!')

def run(movies):
    welcome_message()
    show_movies(movies, search_algorithm(movies, enter_input()))
    goodbye()
