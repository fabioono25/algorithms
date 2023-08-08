namespace Algorithms.CodeChallenges
{
    /***
    * given a string containing the characters ( ) { } [ ] determine if the string is valid
    * (){}[] -> true
    * (] -> false
    ***/
    public static class ValidParenthesis
    {
        public static void Execute(){
            Console.WriteLine($"Is ()[]{{}} valid? : {isValid("()[]{}")}");            
            Console.WriteLine($"Is (] valid? : {isValid("(]")}");            
            Console.WriteLine($"Is ([)] valid? : {isValid("([)]")}");            
        }

        private static bool isValid(string s) {
            var temp = new Stack<char>();

            foreach (var item in s) {
                switch (item)
                {
                    case '(' or '{' or '[':
                        temp.Push(item);
                        break;
                    case ')':
                        if (temp.Pop() != '(')
                            return false;
                        break;
                    case ']':
                        if (temp.Pop() != '[')
                            return false;
                        break;
                    case '}':
                        if (temp.Pop() != '{')
                            return false;
                        break;
                }
            }

            return true;
        }
    }
}