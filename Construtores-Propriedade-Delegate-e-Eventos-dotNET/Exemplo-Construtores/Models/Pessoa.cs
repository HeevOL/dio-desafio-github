namespace Exemplo_Construtores.Models
{
    public class Pessoa
    {
        private readonly string nome = "Heverton";
        private readonly string sobrenome;
        public Pessoa()
        {
            nome = string.Empty;
            sobrenome = string.Empty;
        }
        public Pessoa(string nome, string sobrenome)
        {
            this.nome = nome;
            this.sobrenome = sobrenome;
        }
        public void Apresentar()
        {
            Console.WriteLine($"Olá meu nome é {nome} {sobrenome}");
        }

    }
}