using System;
namespace Pessoas
{
    public class Fisica: Pessoa
    {
        publick Fisica(string nome)
        {
            this.Nome = nome;
            this.NomePersonalizado;
        }

        public string CPF { get; set; }

        public new string NomePersonalizado()
        {
            return $"{this.NomePersonalizado()} - Polimorfismo";
        }
    }
}