from typing import List, Dict, Any

from Loaders.ILoader import ILoader


def get_options() -> Dict[str, str]:
    return {
        "python": \
"""if __name__ == "__main__":
    print("Hello World!")
""",

        "java": \
"""class Test
{
    public static void main(String []args)
    {
        System.out.println("My First Java Program.");
    }
};
""",
        "c#": \
"""public class Program
{
    public static void Main(string[]   args)
    {
        System.Console.WriteLine("Hello, World!");
    }
}
""",
    }


class TextLoader(ILoader):

    def to_string(self, attr: Dict[str, Any] = None) -> str:
        return get_options()[attr["language"]]