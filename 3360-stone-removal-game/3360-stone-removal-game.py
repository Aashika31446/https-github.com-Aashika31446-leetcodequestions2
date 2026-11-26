class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        alice_turn = True

        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            alice_turn = not alice_turn

        # If it is now Alice's turn, she cannot make a move and loses.
        # If it is Bob's turn, Bob cannot make a move and Alice wins.
        return not alice_turn