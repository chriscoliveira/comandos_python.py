import re


class CalcIPv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        """define o inicializador da classe"""
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()


    ################ inicio dos getters e setters ################
    # getter do atributo ip
    @property
    def ip(self):
        return self._ip

    # getter do atributo mascara
    @property
    def mascara(self):
        return self._mascara

    # getter do atributo prefixo
    @property
    def prefixo(self):
        return self._prefixo

    # setter do atributo ip
    @ip.setter
    def ip(self, valor):

        # verifica se o ip e valido
        if not self._valida_ip(valor):
            raise ValueError('IP invalido')
        # fim da verificacao

        self._ip = valor

        # converte o ip em binario
        self._ip_bin = self._ip_to_bin(valor)

    # setter do atributo mascara
    @mascara.setter
    def mascara(self, valor):
        # verifica se a mascara foi enviada
        if not valor:
            return
            # fim da verificacao

        # verifica se o mascara e valida
        if not self._valida_ip(valor):
            raise ValueError('Mascara invalido')
        # fim da verificacao
        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')
        # print(self._mascara_bin)

    # setter do atributo prefixo
    @prefixo.setter
    def prefixo(self, valor):
        # verifica se o prefixo foi enviado
        if not valor:
            return
        # fim da verificacao

        # verifica se o prefixo e inteiro
        if not isinstance(valor, int):
            raise TypeError('Prefixo precisa ser inteiro')
        # fim da verificacao

        # verifica se o prefixo tem 32 bits
        if valor > 32:
            raise TypeError('Prefixo precisa ter 32 bits')
        # fim da verificacao

        self._prefixo = valor
        # converte o prefixo em binario e completa com zeros a direita
        self._mascara_bin = (valor * '1').ljust(32, '0')

        # envia a mascara para converter em ip
        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)
        # print(self._mascara_bin)

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numero_ips()

    ################ fim dos getters e setters ################

    # valida se o ip e valido
    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )
        if regexp.search(ip):
            return True

    # converte o ip em binario
    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        # print(blocos)
        # octeto recebe a list comprehension de blocos convertendo para binario e retirando os
        # 2 primeiros digitos da funcao bin() e com o .zfill(8) para completar os digitos
        # faltantes em 8 digitos
        octeto = [bin(int(x))[2:].zfill(8) for x in blocos]
        return ''.join(octeto)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        # separa a mascara em 8 octetos e converte para a mascara decimal
        bloco = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]
        # junta os blocos
        return '.'.join(bloco)

    def _set_broadcast(self):
        # verifica o numero de hosts disponiveis em bits
        host_bits = 32 - self.prefixo

        # pega o binario do broadcast
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        # pega o ip do broadcast
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        # verifica o numero de hosts disponiveis em bits
        host_bits = 32 - self.prefixo

        # pega o binario do broadcast
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        # pega o ip do broadcast
        self._rede = self._bin_to_ip(self._rede_bin)

        return self._rede

    def _get_numero_ips(self):
        #calcula o numero total de ips dentro da rede
        return 2 ** (32 - self.prefixo)

    def exibe_info_rede(self):
        print(f'End IP:\t\t{self.ip}\n'
              f'Masc:\t\t{self.mascara}\n'
              f'Rede:\t\t{self.rede}\n'
              f'Broad:\t\t{self.broadcast}\n'
              f'Cidr:\t\t{self.prefixo}\n'
              f'Subnet:\t\t{self.numero_ips}\n'
              f'Ip Max:\t\t{self.numero_ips-2}')