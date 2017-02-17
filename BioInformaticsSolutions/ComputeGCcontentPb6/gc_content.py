dna_file = open('C:/Users/Rajesh/PycharmProjects/ComputeGCcontentPb6/rosalind_gc.txt','r')

gc_dict = {}
gc_key = ''

for dna_data in dna_file:
    if dna_data[0] =='>':
        gc_key = dna_data[1:].rstrip()
        gc_dict[gc_key] = ''
    else:
        gc_dict[gc_key] += dna_data.rstrip()

for string_id, gc_content in gc_dict.iteritems():
    gc_dict[string_id] = (float(gc_content.count('G') + gc_content.count('C'))/len(gc_content)) * 100

(maxim_id,gc_maxim) = max(list(gc_dict.iteritems()),key = lambda item :item[1])

print maxim_id
print("%f" %gc_maxim)



