# Explicação do Código - Auditoria e Segurança de Sistemas.

-> A fuunção "caesar_cipher" tem alguns parâmetros como text (texto a ser criptografado ou descriptografado) e o shift (quantidade de posições a serem deslocadas). Dentro dela, a função interna "shift_char", ela verifica se o caractere é uma letra (char.isalpha()), calcula o deslocamento efetivo (shift_amount), garantindo que ele esteja dentro do intervalo de 0 a 25 (shift % 26), determina a base ASCII (65 para letras maiúsculas e 97 para letras minúsculas), desloca o caractere e o converte de volta para o valor ASCII correto e retorna o caractere deslocado. Se o caractere não for uma letra, retorna o próprio caractere e aplica "shift_char" a cada caractere do texto e retorna o texto resultante.

-> A função "shuffle_text" tem três parâmetros, que são o text (texto a ser embaralhado ou desembaralhado) e a key (chave para inicializar o gerador de números aleatórios), encrypt (booleano indicando se é para embaralhar ou desembaralhar). Essa funcão inicializa o gerador de números aleatórios com a chave (random.seed(key)), converte o texto em uma lista de caracteres (text_list) e se encrypt é True, embaralha a lista de caracteres (random.shuffle(text_list)). Se encrypt é False, cria uma lista de índices e a embaralha e usa os índices embaralhados para reordenar os caracteres de volta às suas posições originais. Ela ainda retorna a lista de caracteres convertida de volta para string.


-> Na função "encrypt", como parâetros há o text (texto a ser criptografado) e key (chave de criptografia). Essa função calcula o deslocamento somando os valores ASCII dos caracteres da chave e pegando o resto da divisão por 26 (shift = sum(ord(char) for char in key) % 26), criptografa o texto usando a cifra de César (caesar_cipher(text, shift)), embaralha o texto criptografado usando a chave (shuffle_text(encrypted_text, key)) e retorna o texto criptografado e embaralhado.

-> Função "decrypt", tem os parâmetros text (texto a ser descriptografado) e key (chave de criptografia), calcula o deslocamento de forma similar à função encrypt, desembaralha o texto usando a chave (shuffle_text(text, key, encrypt=False)), descriptografa o texto desembaralhado usando a cifra de César com o deslocamento negativo (caesar_cipher(shuffled_text, -shift)) e retorna o texto original.


Por fim, apenaws para uso de testes/exemplos, foi adicionado os seguintes passos:

(mensagem_original = "David Goncalves Maia") e (chave = "mysecretkey") define uma mensagem original e uma chave, criptografa a mensagem original usando a função encrypt, imprime a mensagem criptografada, descriptografa a mensagem criptografada usando a função decrypt e por fim imprime a mensagem descriptografada.
