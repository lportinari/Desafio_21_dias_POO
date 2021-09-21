<?php
# Exercício em PHP

class Cachorro {
    public $nome;
    public $raça;
    public $cor;

    public function getNome(){
        return $this->nome;
    }

    public function setNome($nome){
        $this->nome = $nome;
    }

    public function getRaça(){
        return $this->raça;
    }

    public function setRaça($raça){
        $this->raça = $raça;
    }

    public function getCor(){
        return $this->cor;
    }

    public function setCor($cor){
        $this->cor = $cor;
    }
}

?>