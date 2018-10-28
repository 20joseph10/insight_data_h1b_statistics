import sys



def main(args):
    infile, out_occu, out_state = args
    total_num_cert = 0                 # used for calculating percentage
    occu_dict = {}
    state_dict = {}

    # data reading
    with open(infile) as f:
        header = f.readline()
        header = header.strip('\n').split(';')
        status_idx, state_idx, soc_idx = -1, -1, -1
        for i, col in enumerate(header):
            if 'STATUS' in col:
                status_idx = i
            elif 'SOC' in col and 'NAME' in col:
                soc_idx = i
            elif 'WORK' in col and 'STATE' in col and state_idx == -1:
                state_idx = i
            if status_idx != -1 and state_idx != -1 and soc_idx != -1:
                break                  # found all indices
        for line in f:
            line = line.split(';')

            # only look at certified applications
            if line[status_idx].upper() == 'CERTIFIED':
                total_num_cert += 1
                if line[soc_idx].strip('"') not in occu_dict:
                    occu_dict[line[soc_idx].strip('"')] = 0
                occu_dict[line[soc_idx].strip('"')] += 1
                if line[state_idx] not in state_dict:
                    state_dict[line[state_idx]] = 0
                state_dict[line[state_idx]] += 1
    
    # sorting by decreasing number and increasing alphabet
    occu_list = sorted(occu_dict.items(), key=lambda x: (-x[1], x[0]))
    state_list = sorted(state_dict.items(), key=lambda x: (-x[1], x[0]))

    # taking top 10
    occu_list_res = occu_list[:10]
    state_list_res = state_list[:10]

    occu_header = 'TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n'
    state_header = 'TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n'
    
    with open(out_occu, 'w') as f:
        f.write(occu_header)
        for item in occu_list_res:
            to_write = item[0] + ';' + str(item[1])
            to_write += ';{0:.1f}%\n'.format(item[1]/total_num_cert*100)
            f.write(to_write)

    with open(out_state, 'w') as f:
        f.write(state_header)
        for item in state_list_res:
            to_write = item[0] + ';' + str(item[1])
            to_write += ';{0:.1f}%\n'.format(item[1]/total_num_cert*100)
            f.write(to_write)


if __name__ == '__main__':
    assert len(sys.argv) == 4
    main(sys.argv[1:])
