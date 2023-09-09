class Pessoa:
    def __init__(self, name, birthday, cpf):
        self._nome = name
        self._nascimento = birthday
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nascimento(self):
        # Formato mm/dd/aaaa
        data = f'{self._nascimento[3:5]}/{self._nascimento[0:2]}/{self._nascimento[6:10]}'
        return data
    
    @property
    def cpf(self):
        cpf = f'{self._cpf[0:3]}.{self._cpf[3:6]}.{self._cpf[6:9]}-{self._cpf[9:11]}'
        return cpf