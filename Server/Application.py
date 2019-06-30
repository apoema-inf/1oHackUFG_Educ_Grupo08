from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from io import BytesIO

class Request(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.processRequest()
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


    def do_POST(self):
        db = GraphDatabase("http://localhost:7474", username="neo4j", password="wbdss")
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        string =json.loads(body)
        print("POST: ",string)
        if string["function"] == "cadastro":
            q1 = 'MATCH(b) WHERE b.nome = "'+string["perfil"]+'" RETURN b;'
            result = db.query(q1,returns = (client.Node))
            q =  'CREATE (a:Alunos{usuario:"'+string["matricula"]+'",senha:"'+string["senha"]+'",nome:"'+string["nome"].replace(':','',5).replace('í','i',10).replace('ê','e',10).replace('ã','a',10).replace('ú','u',10).replace('á','a',10).replace('ç','c',10).replace('/','',10).replace('ó','o',10)+'"}) RETURN a'
            result2 = db.query(q,returns = (client.Node))
            for r in result:
                for z in result2:
                    z[0].relationships.create("tem",r[0])
        else:
            if string["function"] == "getcurso":
                varj = '{"nome":['
                print("Curso")
                q = 'MATCH(a:Cursos) RETURN a'
                result = db.query(q,returns = (client.Node))
                for x in result:
                    varj = varj+'"'+str(x[0]["nome"])+'"'+','
                varj = varj[:-1]
                varj = varj+']}'
                response.write(varj.encode("utf8"))
                

            else:
                   if string["function"] == "getdados":
                        varj = '{"nome":['
                        print("Curso")
                        q = 'match(a:Materias)-[]->(b:Conteudo),(c:Personalidades)-[]->(b) where c.nome="'+string["perfil"].lower()+'" and a.nome= "'+string["disciplina"].lower().replace(':','',5).replace('í','i',10).replace('ê','e',10).replace('ã','a',10).replace('ú','u',10).replace('á','a',10).replace('ç','c',10).replace('/','',10).replace('ó','o',10)+'" return b;'
                        result = db.query(q,returns = (client.Node))
                        for x in result:
                            varj = varj+'"'+str(x[0]["nome"])+'"'+','
                        varj = varj[:-1]
                        varj = varj+'],"tipo":['
                        for y in result:
                            varj = varj+'"'+str(y[0]["tipo"])+'"'+','
                        varj = varj[:-1]
                        varj += ']}'
                        response.write(varj.encode("utf8"))

                   else:
                        if string["function"] == "login":
                            response.write('{"response":"sucesso"}'.encode("utf8"))
                        else:
                            if string["function"] == "getdisciplina":
                                varj = '{"nome":['
                                print("Curso")
                                q = 'MATCH(a:Cursos)-[b]->(c) WHERE a.nome = "'+string["curso"].lower().replace(':','',5).replace('í','i',10).replace('ê','e',10).replace('ã','a',10).replace('ú','u',10).replace('á','a',10).replace('ç','c',10).replace('/','',10).replace('ó','o',10)+'" RETURN c'
                                result = db.query(q,returns = (client.Node))
                                for x in result:
                                    varj = varj+'"'+str(x[0]["nome"])+'"'+','
                                varj = varj[:-1]
                                varj = varj+']}'
                                response.write(varj.encode("utf8"))
                                
        self.wfile.write(response.getvalue())
httpd = HTTPServer(('localhost', 8080), Request)
httpd.serve_forever()
