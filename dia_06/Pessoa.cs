using System;
namespace Pessoas
{
    public class Pessoa
    {
        public Pessoa()
        {

        }

        public int Id { get; set; }
        public string Nome { get; set; }
        public string Endereco { get; set; }

        // protected: Funciona somente dentro da herança
        protected virtual string NomePersonalizado()
        {
            return $"{this.nome}";
        }

    }
}