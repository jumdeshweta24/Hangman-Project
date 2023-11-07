class HangmanVisuals:
    def get_visual(self, attempts):
        hangman_visuals = [
            """
              -----
              |   |
                  |
                  |
                  |
                  |
            """,
            """
              -----
              |   |
              O   |
                  |
                  |
                  |
            """,
            """
              -----
              |   |
              O   |
              |   |
                  |
                  |
            """,
            """
              -----
              |   |
              O   |
             /|   |
                  |
                  |
            """,
            """
              -----
              |   |
              O   |
             /|\\  |
                  |
                  |
            """,
            """
              -----
              |   |
              O   |
             /|\\  |
             /    |
                  |
            """,
            """
              -----
              |   |
              O   |
             /|\\  |
             / \\  |
                  |
            """
        ]

        return hangman_visuals[6 - attempts]
