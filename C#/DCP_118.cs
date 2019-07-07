using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given[-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].*/

namespace dcp_118
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] initial = new int[5] { -9, -2, 0, 2, 3 };

            for (int i = 0; i < initial.Length; i++)
            {

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
