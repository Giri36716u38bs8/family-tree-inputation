#input grandfathers  and grandmothers name:
PGF=input(("Enter name of your paternal grandfather:"))
MGF=input(("Enter name of your maternal grandfather:"))
PGM=input(("Enter name of your paternal grandmother:"))
MGM=input(("Enter name of your paternal grandmother:"))
#children of particular parent
l1=[]
l2=[]
l3=[]
l4=[]
#DETAILS OF SONS AND DAUGHTER OF GRANDPARENTS:
NMGP=int(input("Enter no of children to maternal Grandparents"))
NPGP=int(input("Enter no of children to paternal Grandparents"))
Father=""
Mother=""
Sons_of_maternalgrandparents=[]
wifes_of_Sons_of_maternalgrandparents=[]
Sons_of_paternalgrandparents=[]
wifes_of_Sons_of_paternalgrandparents=[]
daughters_of_maternalgrandparents=[]
husbands_of_daughters_of_maternalgrandparents=[]
daughters_of_paternalgrandparents=[]
husbands_of_daughters_of_paternalgrandparents=[]
for i in range (NMGP):
    s=input("Enter son or daughter:")
    if s=="son":
        E=input("Enter name of the Son: ")
        r =Sons_of_maternalgrandparents.append(E)
        d=input("Is he married or not")
        if d=="yes":
            o=input("Enter name of wife of  Son: ")
            O=wifes_of_Sons_of_maternalgrandparents.append( o)
            g=input("Is he ur father or uncle")
            k=int(input("enter no of children"))
            for i in range(k):
                P=input("enter name of the child")
                l1.append(P)
                Q=[]
                Q.extend(l1)
            if g=="father":
                Father=E
                Mother=o
            else:
                print()
            
        else:
           print()
            
    elif s=="daughter":
        P=input("Enter name of daughter: ")
        X=daughters_of_maternalgrandparents.append(P)
        q=input("Is she married or not")
        if q=="yes":
            F=input("Enter daughter's husband name:")
            f=husbands_of_daughters_of_maternalgrandparents.append(F)
            v=input("Is she ur mother or aunt")
            z=int(input("enter no of children"))
            for i in range(z):
                D=input("enter name of the child")
                l2.append(D)
                A=[]
                A.extend(l2)
            if v=="mother":
                Father=F
                Mother=P
                print()
            else:
                print()
        else:
            print()
print()
print()

for i in range (NPGP):
    s=input("Enter son or daughter:")
    if s=="son":
        B=input("Enter name of the Son: ")
        R=Sons_of_paternalgrandparents.append(B)
        d=input("Is he married or not")
        if d=="yes":
            N=input("Enter Son's wife name:")
            n=wifes_of_Sons_of_paternalgrandparents.append(N)
            L=input("Is he ur father or uncle")
            H=int(input("enter no of children"))
            for i in range(H):
                J=input("enter name of child")
                l3.append(J)
                S=[]
                S.extend(l3)
                
            if L=="father":
                Father=B
                Mother=N
                print()
            else:
                print()
            
        else:
           print()
            
    elif s=="daughter":
        Z=input("Enter name of daughter: ")
        t =daughters_of_paternalgrandparents.append(Z)
        c=input("Is she married or not")
        if c=="yes":
            U=input("Enter daughter's husband name:")
            f=husbands_of_daughters_of_paternalgrandparents.append(U)
            h=int(input("no of children"))
            v=input("Is she ur mother or aunt")
            for i in range(h):
                M=input("enter child name")
                l4.append(M)
                T=[]
                T.extend(l4)
            if v=="mother":
                Father=U
                Mother=Z
                print()
            else:
                print()
        else:
            print()
print(PGF,PGM,MGF,MGM)
print(Father,Mother)
print(Sons_of_maternalgrandparents)
print(wifes_of_Sons_of_maternalgrandparents)
print(Q)
print(daughters_of_maternalgrandparents)
print(husbands_of_daughters_of_maternalgrandparents)
print(A)
print(Sons_of_paternalgrandparents)
print(wifes_of_Sons_of_paternalgrandparents)
print(S)

print( daughters_of_paternalgrandparents)
print(husbands_of_daughters_of_paternalgrandparents)
print(T)



def print_tree():
    W = 100

    def print_side(side_label, gp1, gp2, members):
        print(f"\n  [ {side_label} ]")
        print()
        print(f"{gp1}  ==*==  {gp2}".center(W))
        print("||".center(W))

        if not members:
            return

        COL = 24
        GAP = 2
        total       = len(members)
        total_width = total * COL + (total - 1) * GAP
        start       = (W - total_width) // 2

        # horizontal connector
        bar = ""
        for i in range(total):
            mid = COL // 2
            if total == 1:
                bar += " " * mid + "|" + " " * (COL - mid - 1)
            elif i == 0:
                bar += " " * mid + "+" + "-" * (COL - mid - 1 + GAP)
            elif i == total - 1:
                bar += "-" * mid + "+" + " " * (COL - mid - 1)
            else:
                bar += "-" * mid + "+" + "-" * (COL - mid - 1 + GAP)
        print(" " * start + bar)

        # tick lines
        tick = ""
        for i in range(total):
            mid = COL // 2
            tick += " " * mid + "|" + " " * (COL - mid - 1 + GAP)
        print(" " * start + tick)

        # parent + spouse
        prow = ""
        for gender, name, spouse, kids in members:
            label = f"{name}+{spouse}" if spouse else name
            prow += label.center(COL) + " " * GAP
        print(" " * start + prow)

        # role
        rrow = ""
        for gender, name, spouse, kids in members:
            if name == Father:
                role = "(Father)"
            elif name == Mother:
                role = "(Mother)"
            elif gender == "son":
                role = "(Uncle)"
            else:
                role = "(Aunt)"
            rrow += role.center(COL) + " " * GAP
        print(" " * start + rrow)

        # tick to children
        ctick = ""
        for gender, name, spouse, kids in members:
            mid = COL // 2
            if kids:
                ctick += " " * mid + "|" + " " * (COL - mid - 1 + GAP)
            else:
                ctick += " " * (COL + GAP)
        print(" " * start + ctick)

        # children
        col_lines = []
        max_lines = 0

        for gender, name, spouse, kids in members:
            lines = []
            is_your_parent = (name == Father or name == Mother)

            if not kids:
                lines.append(" " * COL)
            elif len(kids) == 1:
                you = " <YOU" if is_your_parent else ""
                lines.append("|".center(COL))
                lines.append(f"{kids[0]}{you}".center(COL))
            else:
                nk  = len(kids)
                cw  = COL // nk
                cbar = ""
                for j in range(nk):
                    cmid = cw // 2
                    if j == 0:
                        cbar += " " * cmid + "+" + "-" * (cw - cmid - 1)
                    elif j == nk - 1:
                        cbar += "-" * cmid + "+" + " " * (cw - cmid - 1)
                    else:
                        cbar += "-" * cmid + "+" + "-" * (cw - cmid - 1)
                lines.append(cbar)

                ctk = ""
                for j in range(nk):
                    cmid = cw // 2
                    ctk += " " * cmid + "|" + " " * (cw - cmid - 1)
                lines.append(ctk)

                crow = ""
                for kid in kids:
                    you = "<YOU" if is_your_parent else ""
                    crow += f"{kid}{you}".center(cw)
                lines.append(crow)

            col_lines.append(lines)
            if len(lines) > max_lines:
                max_lines = len(lines)

        for lines in col_lines:
            while len(lines) < max_lines:
                lines.append(" " * COL)

        for li in range(max_lines):
            row = ""
            for lines in col_lines:
                row += lines[li] + " " * GAP
            print(" " * start + row)

    print("\n" + "=" * W)
    print("F A M I L Y   T R E E".center(W))
    print("=" * W)

    # paternal side
    paternal = []
    for i, name in enumerate(Sons_of_paternalgrandparents):
        sp = wifes_of_Sons_of_paternalgrandparents[i] if i < len(wifes_of_Sons_of_paternalgrandparents) else ""
        paternal.append(("son", name, sp, l3))
    for i, name in enumerate(daughters_of_paternalgrandparents):
        sp = husbands_of_daughters_of_paternalgrandparents[i] if i < len(husbands_of_daughters_of_paternalgrandparents) else ""
        paternal.append(("daughter", name, sp, l4))

    print_side("PATERNAL SIDE", PGF, PGM, paternal)

    # maternal side
    maternal = []
    for i, name in enumerate(Sons_of_maternalgrandparents):
        sp = wifes_of_Sons_of_maternalgrandparents[i] if i < len(wifes_of_Sons_of_maternalgrandparents) else ""
        maternal.append(("son", name, sp, l1))
    for i, name in enumerate(daughters_of_maternalgrandparents):
        sp = husbands_of_daughters_of_maternalgrandparents[i] if i < len(husbands_of_daughters_of_maternalgrandparents) else ""
        maternal.append(("daughter", name, sp, l2))

    print_side("MATERNAL SIDE", MGF, MGM, maternal)

    print("\n" + "-" * W)
    print(f"  Your Father : {Father}     Your Mother : {Mother}")
    print("=" * W)

print_tree()






        
        
        

                              
                          
