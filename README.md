# Proyecto_squid

Limitaciones para alumnos:
<pre>
- No puede bajar ficheros que se puedan instalar.
- Sin acceso los fines de semanas
- Sin ver contenido multimedia
- Sólo tienen conexión de 8:00 a 14:00 h.
</pre>
Limitaciones para profesores:
- No puede bajar ficheros que se puedan instalar.
- Sin acceso los fines de semanas
- Comenzamos descomentando:

Comenzamos comentando la acl que permite entrar a la red local:

#http_access allow localnet 
#http_access allow localhost 

Creamos el listado de acls:

#Para profesores y alumnos: 
#--------------------------------- 
acl profesores proxy_auth profesor 
acl alumnos proxy_auth alumno 
#--------------------------------- 
#Lista de limitaciones: 
#----------------------------------------- 
#Indicamos que podemos bajar ficheros ejecutables: 
#----------------------------------------- 
acl no_instalar url_regex -i exe$ zip$ rar$ iso$ msi$ bin$ 
#----------------------------------------- 
#Indiccamos que la hora accesible es un dia 
#----------------------------------------- 
acl fin_de_semana time AS 00:00-23:59 
#----------------------------------------- 
#Indicamos que podemos ver contenido multimedia: 
#----------------------------------------- 
acl multimedia url_regex -i avi$ mp3$ mp4$ mpeg$ wav$ wmv$ wma$ flv$ 
#----------------------------------------- 
#Indicamos el horario de clase: 
#----------------------------------------- 
acl horario_clase time MTWHF 8:00-14:00 
#----------------------------------------- 

Ahora aplicamos nuestras reglas acl mediante la directiva http_access y http_reply_access. Es importante el orden, ya que se recomienda el menor número posible de directivas:

#Reglas http_access 
http_access allow alumnos localnet horario_clase !fin_de_semana !multimedia !multimedia2 !no_instalar 
http_access allow profesores localnet !fin_de_semana !no_instalar 
