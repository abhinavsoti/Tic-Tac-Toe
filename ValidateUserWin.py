import os

v_dict = {}

def validatetictactoe(v_dict, chkmark):
    if (v_dict[1] == v_dict[4] == v_dict[7] == chkmark) or (v_dict[1] == v_dict[2] == v_dict[3] == chkmark) or (v_dict[1] == v_dict[5] == v_dict[9] == chkmark):
        return 'Winner'
    elif (v_dict[2] == v_dict[5] == v_dict[8] == chkmark) or (v_dict[3] == v_dict[5] == v_dict[7] == chkmark):
        return 'Winner'
    elif (v_dict[3] == v_dict[6] == v_dict[9] == chkmark) or (v_dict[4] == v_dict[5] == v_dict[6] == chkmark):
        return 'Winner'
    elif (v_dict[7] == v_dict[8] == v_dict[9] == chkmark):
        return 'Winner'
    else:
        return 'No Winner Yet'