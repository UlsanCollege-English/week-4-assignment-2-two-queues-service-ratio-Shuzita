from collections import deque

class Gate:
    def __init__(self):
        self._pattern = ["fastpass", "regular", "regular", "regular"]
        self._idx = 0
        self._fast = deque()
        self._reg = deque()

    def arrive(self, line, person_id):
        if line == "fastpass":
            self._fast.append(person_id)
        else:
            self._reg.append(person_id)

    def serve(self):
        if not self._fast and not self._reg:
            raise IndexError("No one in line to serve")

        n = len(self._pattern)
        for _ in range(n):
            line_type = self._pattern[self._idx]
            self._idx = (self._idx + 1) % n
            if line_type == "fastpass" and self._fast:
                return self._fast.popleft()
            elif line_type == "regular" and self._reg:
                return self._reg.popleft()

        while self._fast or self._reg:
            line_type = self._pattern[self._idx]
            self._idx = (self._idx + 1) % n
            if line_type == "fastpass" and self._fast:
                return self._fast.popleft()
            elif line_type == "regular" and self._reg:
                return self._reg.popleft()


        raise IndexError("No one in line to serve")

    def peek_next_line(self):
        """Return which line would be served next, considering empties."""
        n = len(self._pattern)
        start_idx = self._idx
        for _ in range(n):
            line_type = self._pattern[start_idx]
            if line_type == "fastpass" and self._fast:
                return "fastpass"
            elif line_type == "regular" and self._reg:
                return "regular"
            start_idx = (start_idx + 1) % n
        return None
