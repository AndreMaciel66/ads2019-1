# %%
class Dogs:
    def __init__(self, name, race, color, age):
        self.name = name
        self.race = race
        self.color = color
        self.age = age

    def bark(self):
        print('Dog {name} is barking'.format(name=self.name))

    def walk(self):
        print('Dog {name} is walking'.format(name=self.name))

    def play(self):
        print('Dog {name} is playing'.format(name=self.name))


dog1 = Dogs('Jon', 'Spitz', 'white', 4)
dog2 = Dogs('Mel', 'vl', 'black', 2)
dog3 = Dogs('Bobby', 'Cofap', 'brown', 4)


class Cars:
    def __init__(self, brand, color, model, year):
        self.brand = brand
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        print("You're now driving a cool car model {model}".format(model=self.model))

    def to_fuel(self):
        print("You're now to fuel a cool car model {model}".format(model=self.model))

    def turn_on(self):
        print("Car model {model} is working".format(model=self.model))


car1 = Cars('Fiat', 'black', 'Uno', 1989)
car2 = Cars('Ford', 'Grey', 'Ka', 2004)
car3 = Cars('Volks', 'black', 'Gol', 2010)


class Students:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.student_id = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


student1 = Students('Andre', 3, 30, 1)
student2 = Students('Yasmin', 3, 30, 1)
student3 = Students('Ramon', 4, 20, 1)


class ContaBancaria:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.birth_date = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


cb1 = ContaBancaria('Andre', 3, 30, 1)
cb2 = ContaBancaria('Yasmin', 3, 30, 1)
cb3 = ContaBancaria('Ramon', 4, 20, 1)


class ContaCorrente:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.birth_date = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


cc1 = ContaCorrente('Andre', 3, 30, 1)
cc2 = ContaCorrente('Yasmin', 3, 30, 1)
cc3 = ContaCorrente('Ramon', 4, 20, 1)


class Casa:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.birth_date = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


casa1 = Casa('Andre', 3, 30, 1)
casa2 = Casa('Yasmin', 3, 30, 1)
casa3 = Casa('Ramon', 4, 20, 1)


class Apartamento:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.birth_date = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


apt1 = Apartamento('Andre', 3, 30, 1)
apt2 = Apartamento('Yasmin', 3, 30, 1)
apt3 = Apartamento('Ramon', 4, 20, 1)


class Edificio:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.birth_date = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


ed1 = Edificio('Andre', 3, 30, 1)
ed2 = Edificio('Yasmin', 3, 30, 1)
ed3 = Edificio('Ramon', 4, 20, 1)


class Carta:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.birth_date = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


ct1 = Carta('Andre', 3, 30, 1)
ct2 = Carta('Yasmin', 3, 30, 1)
ct3 = Carta('Ramon', 4, 20, 1)


class Emails:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.birth_date = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


em1 = Emails('Andre', 3, 30, 1)
em2 = Emails('Yasmin', 3, 30, 1)
em3 = Emails('Ramon', 4, 20, 1)


class Livro:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.birth_date = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


lv1 = Livro('Andre', 3, 30, 1)
lv2 = Livro('Yasmin', 3, 30, 1)
lv3 = Livro('Ramon', 4, 20, 1)


class Agenda:
    def __init__(self, name, class_num, age, student_id):
        self.name = name
        self.class_num = class_num
        self.age = age
        self.birth_date = student_id

    def salvar_presenca(self):
        print('presença lançada aluno: {name}'.format(name=self.name))

    def lancar_nota(self):
        print('lançar nota aluno: {name}'.format(name=self.name))

    def corrigir_trabalho(self):
        print('trabalho corrigido aluno: {name}'.format(name=self.name))


ag1 = Agenda('Andre', 3, 30, 1)
ag2 = Agenda('Yasmin', 3, 30, 1)
ag3 = Agenda('Ramon', 4, 20, 1)