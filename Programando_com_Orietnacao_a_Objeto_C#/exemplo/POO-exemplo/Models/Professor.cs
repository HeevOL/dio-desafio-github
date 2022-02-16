namespace POO_exemplo.Models
{
    public class Professor : Pessoa
    {
        public double Salario { get; set; }
        public override void Apresentar()
        {
            System.Console.WriteLine($"Olá meu nome é {Nome}, sou Profesor e tenho um sálario de {Salario}");
        }
    }
}