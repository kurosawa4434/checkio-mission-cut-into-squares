"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [4, 4],
            "answer": 0,
            "explanation": [
                [0, 0, 4],
            ],
        },
        {
            "input": [4, 2],
            "answer": 1,
            "explanation": [
                [0, 0, 2],
                [2, 0, 2],
            ],
        },
        {
            "input": [7, 6],
            "answer": 4,
            "explanation": [
                [0, 0, 4],
                [0, 4, 2],
                [2, 4, 2],
                [4, 0, 3],
                [4, 3, 3],
            ],
        },
    ],
    "Extra": [
        # {
        #     "input": [91, 31],
        #     "answer": 10,
        # },
        {
            "input": [149, 139],
            "answer": 19,
            "explanation": [
                [0, 0, 139],
                [139, 0, 10],
                [139, 10, 10],
                [139, 20, 10],
                [139, 30, 10],
                [139, 40, 10],
                [139, 50, 10],
                [139, 60, 10],
                [139, 70, 10],
                [139, 80, 10],
                [139, 90, 10],
                [139, 100, 10],
                [139, 110, 10],
                [139, 120, 10],
                [139, 130, 5],
                [144, 130, 5],
                [139, 135, 4],
                [143, 135, 4],
                [147, 135, 2],
                [147, 137, 2],
            ],
        },
        {
            "input": [25, 23],
            "answer": 11,
            "explanation": [
                [0, 0, 13],
                [13, 0, 9],
                [22, 0, 3],
                [22, 3, 3],
                [22, 6, 3],
                [13, 9, 4],
                [17, 9, 4],
                [21, 9, 4],
                [0, 13, 10],
                [10, 13, 10],
                [20, 13, 5],
                [20, 18, 5],
            ],
        },
        {
            "input": [27, 25],
            "answer": 10,
            "explanation": [
                [0, 0, 18],
                [18, 0, 9],
                [18, 9, 9],
                [0, 18, 7],
                [7, 18, 7],
                [14, 18, 7],
                [21, 18, 4],
                [25, 18, 2],
                [25, 20, 2],
                [21, 22, 3],
                [24, 22, 3],
            ],
        },
        {
            "input": [31, 29],
            "answer": 15,
            "explanation": [
                [0, 0, 19],
                [19, 0, 12],
                [19, 12, 7],
                [26, 12, 5],
                [26, 17, 2],
                [28, 17, 2],
                [30, 17, 1],
                [30, 18, 1],

                [0, 19, 10],
                [10, 19, 10],
                [20, 19, 5],
                [20, 24, 5],
                [25, 19, 6],
                [25, 25, 4],
                [29, 25, 2],
                [29, 27, 2],

            ],
        },
        {
            "input": [139, 137],
            "answer": 21,
            "explanation": [
                [0, 0, 84],
                [84, 0, 55],
                [84, 55, 29],
                [113, 55, 13],
                [126, 55, 13],
                [113, 68, 16],
                [129, 68, 10],
                [129, 78, 6],
                [135, 78, 4],
                [135, 82, 2],
                [137, 82, 2],
                [0, 84, 53],
                [53, 84, 53],
                [106, 84, 33],
                [106, 117, 20],
                [126, 117, 13],
                [126, 130, 7],
                [133, 130, 4],
                [137, 130, 2],
                [137, 132, 2],
                [133, 134, 3],
                [136, 134, 3],
            ],
        },
    ]
}
