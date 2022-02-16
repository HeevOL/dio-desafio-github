using Colecoes.Helper;

OperacoesArray array = new OperacoesArray();
int[] Array = new int[5] {5, 3, 2, 1, 4};

array.OrdenarBubbleSort(ref Array);
array.ImprimirArray(Array);

// int[,] matriz = new int[4, 2]
// {
//     {8, 8},
//     {10, 20},
//     {50, 100},
//     {120, 240}
// };

// for (int i = 0; i < matriz.GetLength(0); i++)
// {
//     for (int j = 0; j < matriz.GetLength(1); j++)
//     {
//         System.Console.WriteLine(matriz[i, j]);
//     }
// }

// int[] arrayInteiros = new int[3];
// arrayInteiros[0] = 10;
// arrayInteiros[1] = 20;
// arrayInteiros[2] = 30;

// //erro->
// arrayInteiros[3] = 40;

// for (int i = 0; i < arrayInteiros.Length; i++)
// {
//     System.Console.WriteLine(arrayInteiros[i]);
// }
// foreach (int item in arrayInteiros)
// {
//     System.Console.WriteLine(item);
// }