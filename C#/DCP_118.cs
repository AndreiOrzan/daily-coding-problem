using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dcp_118
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] initial = new int[5] { -9, -2, 0, 2, 3 };
            int helper = 0;

            for (int i = 0; i < initial.Length; i++)
            {
                helper = initial[i] * initial[i];
                initial[i] = initial[i] * initial[i];
                
            }
            Array.Sort(initial);
            foreach (var item in initial)
            {
                Console.WriteLine(item);
            }
        }
    }
}
