Chiffrement rotatif
===

Principe
---
A chaque caractère, le script génère un alphabet de subsitution (principe qui s'inspire de la machine Enigma)

Pour l'instant il se contente d'effectuer une rotation d'un caractère vers la droite. Ce chiffrement n'a rien à voir avec le ROT.


Exemple
---

On veut chiffrer le mot suivant : `kayak`

L'alphabet initial est le suivant : `abcdefghijklmnopqrstuvwxyz`


```code
#lettre k
abcdefghijklmnopqrstuvwxyz

#lettre a
zabcdefghijklmnopqrstuvwxy
z étant la 1ère lettre on substitue 'a' par 'z'

#lettre y
yzabcdefghijklmnopqrstuvwx
y étant la 25ème lettre on substitue 'y' par 'w'

#lettre a
xyzabcdefghijklmnopqrstuvw
a étant la 1ère lettre on substitue 'a' par 'x'

#lettre y
wxyzabcdefghijklmnopqrstuv
k étant la 11ème lettre on substitue 'k' par 'g'

```

Fonctions futures
---

* Avoir un motif de rotation différent (eg : rotation 1 fois à droite, puis 2 fois à gauche)
* Avoir un motif non prévisible 
* Génération d'un jeton de communication
* Etablir la communication avec une autre machine
* Sécuriser la connexion
* Fiabiliser l'échange de données de telle sorte que l'interception des données ne compromette pas les messages.
