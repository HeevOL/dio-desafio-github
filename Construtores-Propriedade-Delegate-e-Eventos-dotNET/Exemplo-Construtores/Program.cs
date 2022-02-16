using Exemplo_Construtores.Models;

namespace Exemplo_Construtores
{
    class Program
    {
        public delegate void Operacao(int x, int y);
        static void Main(string[] args)
        {
            Matematica m = new Matematica(10, 20);
            m.Somar();
            // Operacao op = new Operacao(Calculadora.Somar);
            // op += Calculadora.Subtrair;

            // op.Invoke(10, 10);

            // Data data = new Data();
            // //data.SetMes(20);
            
            // data.Mes = 12;
            // System.Console.WriteLine(data.Mes);

            // data.ApresentarMes();

            // Aluno p1 = new Aluno("Heverton", "Lourenço", "Teste");
            // p1.Apresentar();

            // Log log = Log.GetInstance();

            // log.PropriedadeLog = "Teste instancia";
            
            // Log log2 = Log.GetInstance();
            // System.Console.WriteLine(log2.PropriedadeLog);

            // Pessoa p1 = new Pessoa("Heverton", "Lourenço");
            // p1.Apresentar();
        }
    }
}