class Televisao
    attr_reader :marca, :modelo, :preco

    def marca=(valor)
        if valor == ""
            raise "A marca não pode estar em branco!"
        end
        @nome = valor
    end

    def modelo=(valor)
        @modelo = valor
    end

    def preco=(valor)
        @preco = valor
    end

    def mostrar
        puts "#{marca}, #{modelo}, #{preco}"
    end
end
