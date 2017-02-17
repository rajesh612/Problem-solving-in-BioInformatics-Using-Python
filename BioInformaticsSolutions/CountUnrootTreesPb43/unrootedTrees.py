def unrootedTreeCount(taxa):
    if taxa <=0:
        return 1
    else:
        return taxa * unrootedTreeCount(taxa-2)

taxafile = open('C:/Users/Rajesh/PycharmProjects/CountUnrootTreesPb43/rosalind_cunr.txt', 'r')
for n in taxafile:
    unrootedTrees = unrootedTreeCount(2*int(n)-5)%1000000
    print("Distinct Unrooted Trees {}".format(unrootedTrees))