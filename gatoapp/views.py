import random
from django.shortcuts import render, HttpResponse, redirect
from .models import Pregunta, Respuesta
import django.contrib.messages as messages
from core.models import User_Data

#Variables Globales
User_F_Join= 1
numDePregunta = 1
resp_correctas = 0
nivel = 1
mensajes_chat = ['''Correo a las 09:36 hrs del 05/04 – springtrap.nachi0407@miahoot.jp
HOLA
Oye buenos días, la verdad es que de agradezco mucho que quieras venir a enseñarme algo para poder hacerle frente a esos imbéciles de la comisión, viejos que son como hablarle a una pared de ladrillos. Aunque sigue siendo un poco irónico que diga eso, siendo yo un gato ignorante, como puedes ver. Pero bueno, acudí a ti para solucionar eso (=^ ◡ ^=)
He preparado un poco de té y comprado galletitas para cuando llegues, poder conversar un poco para después meternos de lleno a lo que es el estudio.
La verdad no estoy seguro si debería haber tenido algo más preparado, como una pizarra o algunos libros, PDF, etc, pero supongo que lo iremos viendo durante la semana. 
Ay, tengo muchos nervios, tenemos hasta el Domingo de esta semana. PERO confío en ti, simplemente me das buena espina.
Así que, eso. Sorry que no escriba más, no quiero molestar porque de seguro vas en el metro, además de que estoy en un apuro limpiando.
Nos vemos, byeeee      ฅ(＾・ω・＾ฅ)

-Nachi
''', 
                 '''Correo a las 08:11 hrs del 06/04  – springtrap.nachi0407@miahoot.jp
BUENOS DÍAS /ᐠ｡ꞈ｡ᐟ\
Me he levantado bastante motivado hoy para seguir. No pensaba que iría tan bien como fue ayer dkjasjdk. He aprendido bastante… me siento más seguro de mi mismo. Obvio que sigue siendo muy temprano para cantar victoria, pero nunca sienta mal un poco de alegría.
Ah, de seguro te hayas preguntado ayer por el nombre de mi correo. Viene de mis hijos, la verdad. Les comenté que me iba a cambiar de correo y ellos querían escoger el nombre. Les di permiso y acá estamos, terminaron usando el nombre de su personaje favorito, mi nombre y los meses de nacimiento de cada uno de ellos. Pensé que tendrían un poco más de imaginación… así que como el buen padre que soy les dije que no, pero me molestaron tanto para que dejara el nombre que simplemente lo hice. Ugh, no me dejaron por 2 horas tranquilo.
Por cierto, se llaman Shizuku y Aidan. Ambos diablos tienen 6 años. Mira, acá una foto de ellos si quieres ver.

En fin, que pena que no los alcanzaste a ver. Están con su madre por, uh, vacaciones, sí. Vacaciones bastante largas, la verdad… Pero no importa, espero que disfruten. Les mando cartitas constantemente para que sepan que su padre aún se acuerda de ellos mientras “viajan” ajaja. ＾ዋ⋏ዋ＾
Ahem, volviendo al tema central, te espero acá en casa a la hora usual. Compré un poco de dulces para la ocasión, además de boba. Mientras llegas, intentaré repasar el contenido del que me hablaste ayer, tomé muchas notas y tengo que repasarlas todas, además de hacer flashcards. =＾• ⋏ •＾=
Nos vemos!!1 (^≗ω≗^)
PS: Sabías que las flashcards son bastante efectivas para este tipo de cosas?
PS2: mira me encontré un chanchito de tierra

-Nachi
''',
                 '''Correo a las 10:15 hrs del 07/04  – springtrap.nachi0407@miahoot.jp
TENGO SUEÑO
Good mormimg, me levanté ultra cansado hoy por la sesión de ayer!! Decidí continuar el estudio de forma personal, repasando todo el material que vimos ayer, con flashcards y todo, y me quedé dormido repasando!!! (≽^╥⩊╥^≼)
Siendo muy sincero, eran las 04:34 cuando ocurrió eso, así que tampoco me sorprende mucho.  En fin, nada que hacerle, voy a tomar café y darme una ducha rápida para así estar decente cuando llegues.
Hm, a todo esto, perdón por ser un poco más frío ayer. Aunque suene super de la nada, resulta que uh, el pololo de mi pareja me mandó un mensaje mientras leía el material y me dijo unas cosas um, no tan bonitas jaja. Uh, crees que lo que dice es verdad? Que soy un <Miahoot Mail ha bloquado esta sección porque tienes filtro de palabrotas activado>.
 
En fin, no debería pensar mucho en ello. Voy a simplemente pedir un poco de MiauDonald’s para que podamos comer algo antes de comenzar  ฅ^.ᆺ.^ฅ
Nos vemos!!!! ⋆｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆
-Nachi
''',
                 '''Correo a las 3:56 hrs del 08/04  – springtrap.nachi0407@miahoot.jp
TENGO SUEÑO OTRA VEZ PERO TENGO QUE CONTARTE ESTO
Quizás te preguntes qué hago despierto a esta hora. Ni yo sé. No me desvelé estudiando como la otra vez, simplemente me quedé viendo videos de cómo encontrar a los misterios en Grand Theft Miauto SA con el mod y acá estoy. Ni si quiera tengo el juego instalado y me ví las 5 horas que duraba el video. Tengo que admitir que es un videazo y recomiendo MUCHO que también lo veas. Mañana si hay tiempo te puedo contar los 193 misterios y como encontrarlos, es muy emocionante. /ᐠ｡ꞈ｡ᐟ\
Ahora tengo tnto sueñi y lamentablemte voy a tener  que dormir commo 2 horas siqueiro alcanza t a hacer aseo y dfkaasffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffzzzzzzzzzzzzzzzzzzzzzsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr! ૮ ˙Ⱉ˙ ა rawr!asfdfffffffffffffffffffffffffdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
<Límite de caracteres especiales detectado>
-Nachi
''',
                 '''Correo a las 8:07 hrs del 08/04  – springtrap.nachi0407@miahoot.jp
RE: TENGO SUEÑO OTRA VEZ PERO TENGO QUE CONTARTE ESTO
…Perdón. Me quedé dormido.
-Nachi.
''',
                 '''Correo a las 08:51 hrs del 09/04 – springtrap.nachi0407@miahoot.jp
DUDAS SOBRE LA PREGUNTA C391.19
Buenos díaaaas. Espero que estés bien en tu viaje para acá. Ahorita ya había terminado de limpiar y me puse a leer las preguntas del libro extra que me dejaste para estudiar, el fucsia titulado “Cambio climático y las funciones de Edward Schauwser: Teoría básica” y tenía una duda en la pregunta C391.19 del libro, en el apartado de “Espacios específicos”. Dice, "Considerando las interrelaciones complejas entre los ciclos biogeoquímicos, la influencia de los patrones de circulación atmosférica y oceánica, junto con las variaciones en la actividad solar y la influencia antropogénica, ¿podría identificarse y cuantificarse de manera precisa el porcentaje individual de contribución de cada factor en el aumento de la temperatura global durante las últimas cinco décadas, teniendo en cuenta las múltiples interacciones entre estos factores y su influencia en los cambios climáticos extremos a nivel regional en diferentes partes del mundo?" 𓆝 𓆟 𓆞 𓆝
Estuve intentando demostrar que la solución es “sí” con las ecuaciones y datos de Eiden-Schauwser que me diste pero no me resulta. Crees que podrías ayudarme mientras vienes en el tren? Es una pregunta de nivel básico así que dudo que sea muy larga.
En fin, muchas gracias!!! Ahora voy a seguir repasando mientras. Ah y voy a pedir Starbucks para comer hoy, espero que no te moleste el bobba de acai. (づ˶•༝•˶)づ♡
Ten un viaje seguro.
PS: Mira, me encontré esto en el closet ayer. No sé qué pensar, la verdad.
-Nachi
''',
                 '''Correo a las 10:01 hrs del 10/04 – springtrap.nachi0407@miahoot.jp
GRACIAS
Hey. Simplemente te quería dar las gracias por todo lo que has hecho para ayudarme últimamente. Te has esmerado MUCHO por un gato sin rumbo y lo aprecio bastante. Pese a que hablas raro y no te entiendo lo que dices a veces, no importa, porque termino aprendiendo de igual manera. Voy a comprar KFC para celebrar hoy, como es el penúltimo día de estudios y porque es tu comida favorita, según lo que ví en el fondo de pantalla de tu celular. ฅ^.ᆺ.^ฅ
Mañana posiblemente no envíe un correo, porque dormiré un poco más hasta tarde y así estar descansado correctamente para el debate de la noche. Por mucho que me apene no mandar correos extraños, es para mejor.
Nos vemos!! ⸜(｡˃ ᵕ ˂ )⸝♡
-Nachi
'''
                ]
#Función reinicia preguntas
def Reset_Questions(request):
    for pregunta in Pregunta.objects.filter(pregunta_Usada = True):
            pregunta.pregunta_Usada = False
            pregunta.save()

#Función que reinicia el juego
def clean_data(request):
    global numDePregunta, resp_correctas
    numDePregunta = 1; resp_correctas = 0; 

#Función que carga la información del usuario
def load_user(request):
    global nivel
    nivel = User_Data.objects.filter(nombre = request.user).values_list("nivel")[0][0]

# Función main de la pagina gatoapp
def gatoapp(request):
    #variables
    global numDePregunta, resp_correctas, nivel, User_F_Join
    resp_correctas_alert = resp_correctas
    nivel_completo = 0
    #Si se llega recien a la pagina o si recarga parte de 0 
    if request.method == "GET":
        clean_data(request)
        nivel_completo = -1
        if request.user.is_authenticated: #Si hay un usuario logueado carga su información
            load_user(request)
    #Para cambiar de nivel o repetirlo dependiendo de las buenas
    if numDePregunta == 6:
        if resp_correctas >= 3:
            nivel+=1
            nivel_completo = 1
            try: #Guarda el nivel logrado en la información del usuario logueado
                user_playing = User_Data.objects.get(nombre = request.user)
                user_playing.nivel = nivel
                user_playing.save()
            except:
                pass
        else:
            nivel_completo = 0
            Reset_Questions(request)
        clean_data(request)
    if nivel == 8:
        nivel = 1
        User_F_Join = -1
        return redirect("lobby")
        
    #Si responde una alternativa y es correcta se suma una respuesta correcta
    if request.method == "POST":
        if Respuesta.objects.filter(id = request.POST["respuesta"]).values_list("respuesta_Correcto")[0][0] == True:
            resp_correctas += 1
    #Saca todas las preguntas que no hayan sido usadas antes.
    preguntasDisponibles = Pregunta.objects.filter(pregunta_Usada=False)
    
    #Sortea las preguntas.
    preguntasElegidas = random.sample(list(preguntasDisponibles), 1)
    
    for preguntaElegida in preguntasElegidas:
        preguntaElegida.pregunta_Usada = True 
        preguntaElegida.save()

    respuestasPorPregunta = {}
    for pregunta in preguntasElegidas:

        respuestasTexto = Respuesta.objects.filter(pregunta_Origen=pregunta)

        respuestasPorPregunta[pregunta] = respuestasTexto

    context = {
        'preguntasElegidas': preguntasElegidas,
        'respuestasPorPregunta': respuestasPorPregunta,
        'numDePregunta' : numDePregunta,
        'nivel' : nivel,
        'resp_correctas_alert' : resp_correctas_alert,
        'nivel_completo' : nivel_completo,
    }

    numDePregunta+=1
    return render(request, "gatoapp.html", context)

def lobby(request):
    global nivel, mensajes_chat, User_F_Join
    if User_F_Join == 1:
        Reset_Questions(request)
        User_F_Join = 0
        return render(request, "Inicio.html")
    if User_F_Join == -1:
        User_F_Join = 1
        return render(request, "Final.html")
    if request.user.is_authenticated: #Si hay un usuario logueado carga su información
        load_user(request)
    return render(request, "lobby.html", {"nivel" : nivel, "mensajes_chat" : mensajes_chat[nivel-1]})