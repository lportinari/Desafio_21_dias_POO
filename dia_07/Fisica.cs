using System;
using System.Collections.Generic;

namespace Pessoas
{
    public class Fisica: Pessoa
    {
        public Fisica(string nome)
        {
            this.Nome = nome;
            this.NomePersonalizado;
        }

        public void Salvar()
        {
            Fisica.BancoEmMemoriaDePessoasFisicas.Add(this);
        }

        public string CPF { get; set; }

        public new string NomePersonalizado()
        {
            return $"Teste = {this.Nome()}";
        }

        public new string NomePersonalizado(string dado)
        {
            return $"{this.NomePersonalizado()} - Polimorfismo";
        }

        public static List<Fisica> BancoEmMemoriaDePessoasFisicas = new List<Fisica>();

        public static List<Fisica> Todas()
        {
            return Fisica.BancoEmMemoriaDePessoasFisicas;
        }

        public static void SalvarInstancia(Fisica obj)
        {
            Fisica.BancoEmMemoriaDePessoasFisicas.Add(obj);
        }

        public static List<Fisica> BuscaPorNome(string nome)
        {
            var novaLista = new List<Fisica>();
            foreach(var inst in Fisica.BancoEmMemoriaDePessoasFisicas)
            {
                if(inst.Nome.ToLower().Constains(nome.ToLower()))
                {
                    novaLista.Add(inst);
                }

                return novaLista;
            }
        }
    }
}