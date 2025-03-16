# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class ListNode:
    def __init__(self, val, forward=None, backward=None):
        self.val = val
        self.forward = forward   
        self.backward = backward   
class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr_node = ListNode(homepage)

    def visit(self, url: str) -> None:
        forward_node = ListNode(url, None, self.curr_node)
        self.curr_node.forward = forward_node
        self.curr_node = forward_node

    def back(self, steps: int) -> str:
        while steps and self.curr_node.backward is not None:
            self.curr_node = self.curr_node.backward
            steps -= 1
        return self.curr_node.val

    def forward(self, steps: int) -> str:
        while steps and self.curr_node.forward is not None:
            self.curr_node = self.curr_node.forward
            steps -= 1
        return self.curr_node.val
