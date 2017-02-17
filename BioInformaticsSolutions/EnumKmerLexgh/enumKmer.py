def kmer_lexogh(chars, str_len, next='', result=[]):
    if str_len > 0:
        for c in chars:
            kmer_lexogh(chars, str_len - 1, next + c, result)
    elif str_len == 0:
        result.append(next)
    return result


if __name__ == "__main__":

    symbol_file = open('C:/Users/Rajesh/PycharmProjects/EnumKmerLexgh/enum_kmer.txt').read()

    symbols_data = symbol_file.split()
    symbols = symbols_data[:-1]
    n = int(symbols_data[-1])
    symbols.sort()
    for k in kmer_lexogh(symbols,n):
        print k