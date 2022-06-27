import math

def deg2rad(angle) :
    '''Conversion en degré d'un angle exprimé en degré
    - param : angle en degré (float)
    - retour : angle en radian (float)
    '''
    return angle * 2 * math.pi / 360

def rad2deg(angle) :
    '''Conversion en degré d'un angle exprimé en radian
    - param : angle en radian (float)
    - retour : angle en degré (float)
    '''
    return angle * 360 / (2 * math.pi)

def wrap_radian(angle) :
    '''Exprime un angle en radian dans [0, 2*pi]
    - param : angle en radian (float)
    - retour : angle en radian dans l'intervalle [0, 2*pi] (float)
    '''
    return (angle + 2 * math.pi) % (2 * math.pi)

def wrap_degre(angle) :
    '''Exprime un angle en degré dans [0, 360]
    - param : angle en degré (float)
    - retour : angle en degré dans l'intervalle [0, 360] (float)
    '''
    return (angle + 360) % 360

def norme(v) :
    '''renvoie la norme du vecteur v
    - param : v : tuple de deux valeurs x, y
    - retour : norme du vecteur (float)
    '''
    x, y = v
    return math.sqrt(x**2 + y**2)

def angle(v) :
    '''renvoie l'angle du vecteur v
    - param : v : tuple de deux valeurs x, y
    - retour : angle du vecteur en degré (float)
    '''
    x, y = v
    angle = math.atan2(y, x)
    return wrap_radian(angle)


def add_vect(v1, v2) :
    '''Additionne les vecteurs v1 et v2
    - param : v1/v2 : Tuple de coordonnées (x, y)
    - retour : tuple de coordonnées (x, y)
    '''
    x1, y1 = v1
    x2, y2 = v2
    return (x1 + x2, y1 + y2)

def coord_vect(norme, angle) :
    '''Calcul les coordonnées d'un vecteur exprimé par sa norme et son angle
    - param :   norme : norme du vecteur (float)
                angle : angle du vecteur exprimé en degré (float)
    - Retour : coordonnées du vecteur -> tuple (x, y)
    '''
    x = norme * math.cos(angle)
    y = norme * math.sin(angle)
    return (x, y)

def soust_vect(v1, v2) :
    '''Soustrait deux vecteurs
    - param : v1/v2 : coordonnées des vecteurs -> tuple (x, y)
    - Retour : v12 : coordonnées du vecteur v1 - v2-> tuple (x, y)
    '''
    x1, y1 = v1
    x2, y2 = v2
    return (x1 - x2, y1 - y2)


    