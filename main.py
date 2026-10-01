normal = {
    "ATGC" : "Baseline human cellular metabolism",
    "TATA" : "Standard DNA transcription initiator (TATA box)",
    "CGTA" : "Typical human immune system response",
    "GCGC" : "Standard cognitive neural pathway development",
    "GGAT" : "Baseline human bone density and muscle synthesis"
}

extra = {
       "X" : "Mutant",
    "ASTR" : "Astrophage mitochondrial replacement (Extreme heat resistance and light-consumption)",
    "ERID" : "Eridanian heavy-metal carapace signature (Ammonia-based biology and advanced acoustic sensory traits)",
    "CHIT" : "Chitauri neural sequence (Cybernetic hive-mind biological integration)",
    "KLYN" : "Klyntar amorphous bonding sequence (Parasitic symbiosis and shape-alteration)",
    "PZSB" : "Hachimoji synthetic DNA (Lab-created artificial nucleobases)"
}

print("Input genetic sequence here(uppercase letters only): ")
gene = "abc"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
gene = input()
print("Checking input")
counter = 0
testerrr = 0

for i in range (len(gene)):
    counter = 0
    for j in range (26):
       if gene[i] == letters[j]:
           counter += 1
    if counter == 0:
        print("Invalid input, try again")
        testerrr += 1
        break

if testerrr < 1:
    res = []

    for ans in normal.keys():
       if ans in gene:
          res.append(normal[ans])

    for ans in extra.keys():
       if ans in gene:
          res.append(extra[ans])

    res2 = set(res)
    res = list(res2)
    if len(res2) == 0:
       print("No matching data found")

    elif len(res2) > 0:
       coun = 1
       for i in range (len(res)):
          print(coun, res[i])
          coun += 1



        


    