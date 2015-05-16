alpha = "abcdefghijklmnopqrstuvwyxz"
cyphe = "boihgknhvtwyurxparemsldpfc"

'''
abchefghitklmroparetsvwyxc

q->a
a->b
t->m
l->y
y->p
e->g
v->l
f->k
c->i
g->n
o->x
w->d
k->w
b->o
i->v
x->f
m->u

n-->r
z-->c

jd->th <------
sn->er <------
su->es

jds->the <------

uu->ss
'''

text = raw_input("Text: ").lower()
out = ""
for c in text:
    if (alpha.find(c) != -1):
        if (c == cyphe[alpha.find(c)]):
            out += c.upper()
        else:
            out += cyphe[alpha.find(c)]
    elif (c != " "):
        out += c

print out
