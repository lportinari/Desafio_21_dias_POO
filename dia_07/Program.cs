using System.Collections.Generic;
using Alunos;

namespace Desafio21DiasPOO
{
    class Program
    {
        static void Main(string[] args)
        {
            Fisica usuario = new Fisica("Luciano")
            Console.WriteLine(usuario.NomePersonalizado());

            new Fisica("Luciano Celinski").Salvar();

            Fisica.SalvarInstancia(usuario);

            var lista = Fisica.BuscaPorNome("luciano");
            foreach(var pessoa in lista)
            {
                Console.WriteLine(usuario.Nome);
            }
            
            Console.WriteLine(usuario.Nome);
        }
    }
}