namespace POO_exemplo.Models
{
    public class Aluno : Pessoa
    {
        public double Nota { get; set; }
        public override void Apresentar()
        {
            System.Console.WriteLine($"Olá, sou o aluno {Nome} de nota {Nota}");
        }
    }
}