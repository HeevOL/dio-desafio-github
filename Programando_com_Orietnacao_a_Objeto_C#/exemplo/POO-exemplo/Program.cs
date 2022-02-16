using System;
using POO_exemplo.Models;

namespace POO_exemplo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Pessoa p1 = new Pessoa();

            // p1.Nome = "Bob";
            // p1.Idade = 20;

            // p1.Apresentar();

            // Retangulo r = new Retangulo();
            // r.definirMedidas(30, 30);

            // System.Console.WriteLine($"Área: {r.ObterArea()}");

            Aluno a1 = new Aluno();
            a1.Idade = 15;
            a1.Nome = "Caio";
            a1.Nota = 8.5;
            a1.Documento = "575848-0";

            a1.Apresentar();

            Professor prof1 = new Professor();
            prof1.Idade = 40;
            prof1.Nome = "José";
            prof1.Salario = 3500.50;
            prof1.Documento = "987717-9";

            prof1.Apresentar();

            Calculadora calc = new Calculadora();
            System.Console.WriteLine("Resultado da primeira soma: " + calc.Somar(10, 10));
            System.Console.WriteLine("Resultado da segunda soma: " + calc.Somar(10, 10, 60));
        }
    }
}