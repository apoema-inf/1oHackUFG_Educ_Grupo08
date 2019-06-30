from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="wbdss")
q = 'MATCH(a)-[b]->(c) delete b,a,c'
results = db.query(q)
q = 'MATCH(a) delete a'
results = db.query(q)


aluno = db.labels.create("Alunos")

personalidade = db.labels.create("Personalidades")
u1 = db.nodes.create(nome = "visual",descricao = "A pessoa com predominância do aprendizado VISUAL valoriza a beleza e estética, em formas e detalhes. Tem uma postura corporal rígida e sua respiração é torácica. Ela fala muito rapidamente porque as imagens se sucedem em sua mente como um filme.  Aprende pela visão; observa demonstrações; gosta de ler e imaginar as cenas no livro; tem boa concentração;  é rápido na compreensão.")
personalidade.add(u1)
u2 = db.nodes.create(nome = "cinestésico",descricao = "Para esta pessoa, todas as experiências são físicas. Esta pessoa prefere conforto à beleza e busca sempre o bem-estar, o prazer e o aconchego. Aprende fazendo, por envolvimento direto; prefere ir logo para a ação; não é bom leitor.")
personalidade.add(u2)
u3 = db.nodes.create(nome = "auditivo",descricao = "A pessoa com predominância auditiva não dá grande valor às aparências, mas sim ao bom papo, bom senso e inteligência. Aprende por instruções verbais; gosta de diálogos; evita descrições longas; não presta atenção nas ilustrações; move os lábios quando lê; subvaloriza.")
personalidade.add(u3)

cursos = db.labels.create("Cursos")
cursosV = ["Administração","Agronomia","Arquitetura e Urbanismo","Artes Visuais","Biblioteconomia","Biomedicina","Biotecnologia","Ciências Ambientais","Ciências Biológicas","Ciências Biológicas","Ciências da Computação","Ciências Contábeis","Ciências Econômicas","Ciências Sociais","Ciências Sociais: Políticas Públicas","Comunicação Social: Publicidade e Propaganda","Dança","Design de Ambientes","Design de Moda","Design Gráfico","Direção de Arte","Direito","Ecologia e Análise Ambiental","Educação Física","Educação Intercultural","Educação no Campo","Enfermagem","Engenharia Ambiental e Sanitária","Engenharia Civil","Engenharia de Alimentos","Engenharia da Computação","Engenharia de Minas","Engenharia de Produção","Engenharia de Software","Engenharia de Transportes","Engenharia Elétrica","Engenharia Física","Engenharia Florestal","Engenharia Mecânica","Engenharia Química","Estatística","Farmácia","Filosofia","Física","Física Médica","Fisioterapia","Geografia","Geologia","Gestão da Informação","História","Jornalismo","Letras: Espanhol","Letras: Linguística","Letras: Estudos Literários","Letras: Francês","Letras: Inglês","Letras: Libras","Letras: Português","Letras: Português/Inglês","Letras: Tradução e Interpretação em Libras/Português","Matemática","Matemática Industrial","Medicina","Medicina Veterinária","Museologia","Música: Canto","Música: Composição","Música: Educação Musical","Música: Ensino do Instrumento Musical","Música: Instrumento Musica","Musicoterapia","Nutrição","Odontologia","Pedagogia","Psicologia"]

materias = db.labels.create("Materias")
materiasV = ["Álgebra Linear","Algoritmos e Programação de Computadores 1","Algoritmos e Programação de Computadores 2","Análise e Projeto de Algoritmos","Arquitetura de Computadores","Banco de Dados 1","Banco de Dados 2","Cálculo 1","Cálculo 2","Compiladores","Computação Gráfica","Direito em Informática","Empreendedorismo","Engenharia de Software 1","Estrutura de dados 1","Estrutura de dados 2","Fábrica de Software","Inteligência Artificial","Introdução a Computação","Laboratório de Programação 1","Laboratório de Programação 2","Linguagens Formais e Autômatos","Lógica Matemática","Pesquisa Operacional","PFC1","PFC2","Probabilidade e Estatística","Produção de Texto","Programação Funcional e Lógica","Programação Orientada a Objetos","Redes de Computadores 1","Redes de Computadores 2","Sistemas Distribuídos","Sistemas Operacionais 1","Sistemas Operacionais 2","Sistemas Digitais","Teoria da Computação","Teoria dos Grafos","Tópicos 1","Tópicos 2","Tópicos 3"]

Conteudo = db.labels.create("Conteudo")
c1 = db.nodes.create(nome="artigo exemplo 1",tipo="artigo")
c2 = db.nodes.create(nome="artigo exemplo 2",tipo="artigo")
c3 = db.nodes.create(nome="artigo exemplo 3",tipo="artigo")
c4 = db.nodes.create(nome="artigo exemplo 4",tipo="artigo")
c5 = db.nodes.create(nome="artigo exemplo 5",tipo="artigo")
c6 = db.nodes.create(nome="artigo exemplo 6",tipo="artigo")
c7 = db.nodes.create(nome="artigo exemplo 5",tipo="video")
c8 = db.nodes.create(nome="artigo exemplo 6",tipo="video")
Conteudo.add(c1,c2,c3,c4,c5,c6,c7,c8)

u1.relationships.create("Contem",c1)
u1.relationships.create("Contem",c2)
u2.relationships.create("Contem",c3)
u2.relationships.create("Contem",c4)
u3.relationships.create("Contem",c5)
u3.relationships.create("Contem",c6)
u1.relationships.create("Contem",c7)
u2.relationships.create("Contem",c8)


#QUERY AUXILIARES
"""
MATCH(a),(b) where a.nome = "visual" and b.nome = "computacao grafica" return a,b; CREATE (b:Conteudo{nome:"artigo exemplo1",tipo:"artigo"})-->(a)
MATCH(a),(b) where a.nome = "visual" and b.nome = "computacao grafica"; CREATE (b:Conteudo{nome:"artigo exemplo2",tipo:"artigo"})-->(a)
MATCH(a),(b) where a.nome = "cinestésico" and b.nome = "computacao grafica"; CREATE (b:Conteudo{nome:"artigo exemplo1",tipo:"artigo"})-->(a)
MATCH(a),(b) where a.nome = "cinestésico" and b.nome = "computacao grafica"; CREATE (b:Conteudo{nome:"artigo exemplo2",tipo:"artigo"})-->(a)
MATCH(a),(b) where a.nome = "auditivo" and b.nome = "computacao grafica"; CREATE (b:Conteudo{nome:"artigo exemplo1",tipo:"artigo"})-->(a)
MATCH(a),(b) where a.nome = "auditivo" and b.nome = "computacao grafica"; CREATE (b:Conteudo{nome:"artigo exemplo2",tipo:"artigo"})-->(a)
MATCH(a),(b) where a.nome = "auditivo" and b.nome = "computacao grafica"; CREATE (b:Conteudo{nome:"https://www.youtube.com/watch?v=-JjQalcnvkc",tipo:"video"})-->(a)
MATCH(a),(b) where a.nome = "visual" and b.nome = "computacao grafica"; CREATE (b:Conteudo{nome:"https://www.youtube.com/watch?v=-JjQalcnvkc",tipo:"video"})-->(a)
"""

for x in cursosV:
	x = x.lower()
	
	x = x.replace('','',5).replace(':','',5).replace('í','i',10).replace('ê','e',10).replace('ã','a',10).replace('ú','u',10).replace('á','',10).replace('ç','c',10).replace('/','',10).replace('ó','o',10)
	u = db.nodes.create(nome = x)
	if x== "Ciências da Computação".lower().replace('','',5).replace(':','',5).replace('í','i',10).replace('ê','e',10).replace('ã','a',10).replace('ú','u',10).replace('á','a',10).replace('ç','c',10).replace('/','',10).replace('ó','o',10):
		for k in materiasV:
			curso = db.nodes.create(nome=k.lower().replace('','',5).replace(':','',5).replace('í','i',10).replace('ê','e',10).replace('ã','a',10).replace('ú','u',10).replace('á','a',10).replace('ç','c',10).replace('/','',10).replace('ó','o',10))
			materias.add(curso)
			u.relationships.create("possui",curso)
			if k == "Computação Gráfica":
				curso.relationships.create("Contem",c1)
				curso.relationships.create("Contem",c2)
				curso.relationships.create("Contem",c3)
				curso.relationships.create("Contem",c4)
				curso.relationships.create("Contem",c5)
				curso.relationships.create("Contem",c6)
				curso.relationships.create("Contem",c7)
				curso.relationships.create("Contem",c8)
	cursos.add(u)
