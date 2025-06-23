import unittest
from app import hello_world


class TestHelloWorld(unittest.TestCase):
    """Test cases for hello_world function."""

    def test_hello_world(self):
        """Test that hello_world returns the correct message."""
        self.assertEqual(hello_world(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
