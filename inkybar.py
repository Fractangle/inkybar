import re

import inkyphat

_c39 = {
    'A': [1,1,0,1,0,1,0,0,1,0,1,1,0],
    'B': [1,0,1,1,0,1,0,0,1,0,1,1,0],
    'C': [1,1,0,1,1,0,1,0,0,1,0,1,0],
    'D': [1,0,1,0,1,1,0,0,1,0,1,1,0],
    'E': [1,1,0,1,0,1,1,0,0,1,0,1,0],
    'F': [1,0,1,1,0,1,1,0,0,1,0,1,0],
    'G': [1,0,1,0,1,0,0,1,1,0,1,1,0],
    'H': [1,1,0,1,0,1,0,0,1,1,0,1,0],
    'I': [1,0,1,1,0,1,0,0,1,1,0,1,0],
    'J': [1,0,1,0,1,1,0,0,1,1,0,1,0],
    'K': [1,1,0,1,0,1,0,1,0,0,1,1,0],
    'L': [1,0,1,1,0,1,0,1,0,0,1,1,0],
    'M': [1,1,0,1,1,0,1,0,1,0,0,1,0],
    'N': [1,0,1,0,1,1,0,1,0,0,1,1,0],
    'O': [1,1,0,1,0,1,1,0,1,0,0,1,0],
    'P': [1,0,1,1,0,1,1,0,1,0,0,1,0],
    'Q': [1,0,1,0,1,0,1,1,0,0,1,1,0],
    'R': [1,1,0,1,0,1,0,1,1,0,0,1,0],
    'S': [1,0,1,1,0,1,0,1,1,0,0,1,0],
    'T': [1,0,1,0,1,1,0,1,1,0,0,1,0],
    'U': [1,1,0,0,1,0,1,0,1,0,1,1,0],
    'V': [1,0,0,1,1,0,1,0,1,0,1,1,0],
    'W': [1,1,0,0,1,1,0,1,0,1,0,1,0],
    'X': [1,0,0,1,0,1,1,0,1,0,1,1,0],
    'Y': [1,1,0,0,1,0,1,1,0,1,0,1,0],
    'Z': [1,0,0,1,1,0,1,1,0,1,0,1,0],
    ' ': [1,0,0,1,1,0,1,0,1,1,0,1,0],
    '0': [1,0,1,0,0,1,1,0,1,1,0,1,0],
    '1': [1,1,0,1,0,0,1,0,1,0,1,1,0],
    '2': [1,0,1,1,0,0,1,0,1,0,1,1,0],
    '3': [1,1,0,1,1,0,0,1,0,1,0,1,0],
    '4': [1,0,1,0,0,1,1,0,1,0,1,1,0],
    '5': [1,1,0,1,0,0,1,1,0,1,0,1,0],
    '6': [1,0,1,1,0,0,1,1,0,1,0,1,0],
    '7': [1,0,1,0,0,1,0,1,1,0,1,1,0],
    '8': [1,1,0,1,0,0,1,0,1,1,0,1,0],
    '9': [1,0,1,1,0,0,1,0,1,1,0,1,0],
    '-': [1,0,0,1,0,1,0,1,1,0,1,1,0],
    '$': [1,0,0,1,0,0,1,0,0,1,0,1,0],
    '%': [1,0,1,0,0,1,0,0,1,0,0,1,0],
    '.': [1,1,0,0,1,0,1,0,1,1,0,1,0],
    '/': [1,0,0,1,0,0,1,0,1,0,0,1,0],
    '+': [1,0,0,1,0,1,0,0,1,0,0,1,0],
    'START': [1,0,0,1,0,1,1,0,1,1,0,1,0],
    'STOP': [1,0,0,1,0,1,1,0,1,1,0,1],
    'PAD': [0,0,0,0,0,0,0,0,0,0,0,0],
}

# Value, A-meaning, B-meaning, C-meaning, pattern
_c128table = [
    [0,' ',' ','00','212222'],
    [1,'!','!','01','222122'],
    [2,'"','"','02','222221'],
    [3,'#','#','03','121223'],
    [4,'$','$','04','121322'],
    [5,'%','%','05','131222'],
    [6,'&','&','06','122213'],
    [7,'\'','\'','07','122312'],
    [8,'(','(','08','132212'],
    [9,')',')','09','221213'],
    [10,'*','*','10','221312'],
    [11,'+','+','11','231212'],
    [12,',',',','12','112232'],
    [13,'-','-','13','122132'],
    [14,'.','.','14','122231'],
    [15,'/','/','15','113222'],
    [16,'0','0','16','123122'],
    [17,'1','1','17','123221'],
    [18,'2','2','18','223211'],
    [19,'3','3','19','221132'],
    [20,'4','4','20','221231'],
    [21,'5','5','21','213212'],
    [22,'6','6','22','223112'],
    [23,'7','7','23','312131'],
    [24,'8','8','24','311222'],
    [25,'9','9','25','321122'],
    [26,':',':','26','321221'],
    [27,';',';','27','312212'],
    [28,'<','<','28','322112'],
    [29,'=','=','29','322211'],
    [30,'>','>','30','212123'],
    [31,'?','?','31','212321'],
    [32,'@','@','32','232121'],
    [33,'A','A','33','111323'],
    [34,'B','B','34','131123'],
    [35,'C','C','35','131321'],
    [36,'D','D','36','112313'],
    [37,'E','E','37','132113'],
    [38,'F','F','38','132311'],
    [39,'G','G','39','211313'],
    [40,'H','H','40','231113'],
    [41,'I','I','41','231311'],
    [42,'J','J','42','112133'],
    [43,'K','K','43','112331'],
    [44,'L','L','44','132131'],
    [45,'M','M','45','113123'],
    [46,'N','N','46','113321'],
    [47,'O','O','47','133121'],
    [48,'P','P','48','313121'],
    [49,'Q','Q','49','211331'],
    [50,'R','R','50','231131'],
    [51,'S','S','51','213113'],
    [52,'T','T','52','213311'],
    [53,'U','U','53','213131'],
    [54,'V','V','54','311123'],
    [55,'W','W','55','311321'],
    [56,'X','X','56','331121'],
    [57,'Y','Y','57','312113'],
    [58,'Z','Z','58','312311'],
    [59,'[','[','59','332111'],
    [60,'\\','\\','60','314111'],
    [61,']',']','61','221411'],
    [62,'^','^','62','431111'],
    [63,'_','_','63','111224'],
    [64,'\x00','`','64','111422'],
    [65,'\x01','a','65','121124'],
    [66,'\x02','b','66','121421'],
    [67,'\x03','c','67','141122'],
    [68,'\x04','d','68','141221'],
    [69,'\x05','e','69','112214'],
    [70,'\x06','f','70','112412'],
    [71,'\x07','g','71','122114'],
    [72,'\x08','h','72','122411'],
    [73,'\x09','i','73','142112'],
    [74,'\x0A','j','74','142211'],
    [75,'\x0B','k','75','241211'],
    [76,'\x0C','l','76','221114'],
    [77,'\x0D','m','77','413111'],
    [78,'\x0E','n','78','241112'],
    [79,'\x0F','o','79','134111'],
    [80,'\x10','p','80','111242'],
    [81,'\x11','q','81','121142'],
    [82,'\x12','r','82','121241'],
    [83,'\x13','s','83','114212'],
    [84,'\x14','t','84','124112'],
    [85,'\x15','u','85','124211'],
    [86,'\x16','v','86','411212'],
    [87,'\x17','w','87','421112'],
    [88,'\x18','x','88','421211'],
    [89,'\x19','y','89','212141'],
    [90,'\x1A','z','90','214121'],
    [91,'\x1B','{','91','412121'],
    [92,'\x1C','|','92','111143'],
    [93,'\x1D','}','93','111341'],
    [94,'\x1E','~','94','131141'],
    [95,'\x1F','\x7F','95','114113'],
    [96,'FNC_3','FNC_3','96','114311'],
    [97,'FNC_2','FNC_2','97','411113'],
    [98,'SHIFT_B','SHIFT_A','98','411311'],
    [99,'CODE_C','CODE_C','99','113141'],
    [100,'CODE_B','FNC_4','CODE_B','114131'],
    [101,'FNC_4','CODE_A','CODE_A','311141'],
    [102,'FNC_1','FNC_1','FNC_1','411131'],
    [103,'START_A','START_A','START_A','211412'],
    [104,'START_B','START_B','START_B','211214'],
    [105,'START_C','START_C','START_C','211232'],
    [106,'STOP','STOP','STOP','2331112'],   # 7 widths because it's the end
]

_c128 = {
    'START_A': 103,
    'START_B': 104,
    'START_C': 105,
    'START': {'A': 103,
              'B': 104,
              'C': 105,},
    'STOP': 106,  
    'A': {'WIDTH': 1},
    'B': {'WIDTH': 1},
    'C': {'WIDTH': 2},
}

for i in range(0, len(_c128table)):
    _c128["A"][_c128table[i][1]] = _c128table[i][0]
    _c128["B"][_c128table[i][2]] = _c128table[i][0]
    _c128["C"][_c128table[i][3]] = _c128table[i][0]

################################################################################

def _bitsFromWidths(widths):
    result = []
    onesMode = False
    for width in widths:
        for i in range(0,int(width)):
            result += [1] if onesMode else [0]
        onesMode = not onesMode
    return result

def _bitsRect(bits, xy=(None, None), height=inkyphat.HEIGHT):
    origX, origY = xy
    if origX == None:
        origX = int((inkyphat.WIDTH - len(bits))/2)
    if origY == None:
        origY = int((inkyphat.HEIGHT - height)/2)
    
    x = origX
    for bit in bits:
        inkyphat.line((x, origY, x, origY+height), bit)
        x+=1

def c39bits(text, smashCase=False):
    """
    Returns an array of 0s and 1s representing the (padded) code 39 barcode.
    If smashCase is true, it ignores case in doing so.
    Raises a ValueError if the text cannot be converted to code 39.
    """
    result = []
    result += _c39["PAD"]
    result += _c39["START"]
    
    _text = text
    
    if smashCase:
        _text = _text.upper()
        
    for c in _text:
        if c not in _c39.keys():
            raise ValueError("Character '" + c + "' is invalid in code 39")
        result += _c39[c]
    
    result += _c39["STOP"]
    result += _c39["PAD"]
    return result

def c39rect(text, xy=(None, None), height=inkyphat.HEIGHT, smashCase=False):
    """
    Draws a code-39 barcode. Set x or y to None to center on that axis.
    """
    bits = c39bits(text, smashCase)
    _bitsRect(bits, xy, height)

def _c128widthsFromValues(values):
    WIDTHS = 4
    QUIET='901'
    result = ''
    result += QUIET
    
    for value in values:
        result += _c128table[value][WIDTHS]
    
    result += QUIET
    return result

def _c128chooseMode(text, currMode):
    nextA = re.search("[\x00-\x1F]", text)
    nextB = re.search("[\x60-\x7F]", text)
    
    # If we don't have a mode, pick one
    if currMode == "?":
        if re.match("[0-9]{4}", text):
            return "C", True
        else:
            if re.match("^[\x20-\x5F]*[\x00-\x1F]", text):
                return "A", True
            else:
                return "B", True
    
    # If we're not in mode C, should we change to it?
    if currMode != "C":
        if re.match(".*[^0-9]", text):
            if re.match("^[0-9]{6}", text):
                return "C", True
        else:
            if re.match("^([0-9]{2}){2,}$", text):
                return "C", True
    
    # If we're in mode C, what should we do?
    if currMode == "C":
        if re.match("^[0-9]{2}", text):
            return "C", None
        else:
            if nextA and nextB:
                if nextA.start() < nextB.start():
                    return "A", True
                else:
                    return "B", True
            else:
                if nextA: # "not nextB" is implicit
                    return "A", True
                # If we don't explicitly need A, default to B
                return "B", True
    
    # At this point, we should have nothing to do with mode C.
    
    if nextA and nextB:
        if nextA.start() < nextB.start():
            if currMode == "A":
                return "A", None
            if re.match("^([\x20-\x5F]*[\x00-\x1F]){3}", text):
                return "A", True
            else:
                if re.match("^[\x00-\x1F]", text):
                    return "A", False
                else:
                    return "B", None
        else:
            if currMode == "B":
                return "B", None
            if re.match("^([\x20-\x5F]*[\x60-\x7F]){3}", text):
                return "B", True
            else:
                if re.match("^[\x60-\x7F]", text):
                    return "B", False
                else:
                    return "A", None
    
    if nextA:
        if currMode == "B":
            return "A", True
        return "A", None
    
    if nextB:
        if currMode == "A":
            return "B", True
        return "B", None
    
    return currMode, None
    
    raise RuntimeError("Failed to choose a mode, yell at github.com/Fractangle")

def _c128values(text):
    result = []
    
    baseMode = "?"
    baseMode, junk = _c128chooseMode(text, baseMode)
    result += [_c128["START"][baseMode]]
    
    index = 0
    while index < len(text):
        currMode = baseMode
        newMode, isPerm = _c128chooseMode(text[index:len(text)], baseMode)
        if newMode != baseMode:
            if isPerm is False:
                currMode = newMode
                result += [_c128[baseMode]["SHIFT_"+newMode]]
            else:
                if isPerm is True:
                    result += [_c128[baseMode]["CODE_"+newMode]]
                    baseMode = newMode
                    currMode = baseMode
        
        width = _c128[currMode]["WIDTH"]
        chunk = text[index:index+width]
        if chunk in _c128[currMode].keys():
            result += [_c128[currMode][chunk]]
            index += width
        else:
            # Something went wrong
            raise ValueError("Can't encode '" + chunk + "' in mode " + currMode)
    
    # Weights go 1, 1, 2, 3, ..., so we start at 0 and use max(n, 1)
    checksum = 0
    checkweight = 0
    for value in result:
        checksum += value * max(checkweight, 1)
        checkweight += 1
    checksum = checksum % 103
    result += [checksum]
    result += [_c128table[_c128["STOP"]][0]]
    return result

def c128bits(text):
    values = _c128values(text)
    widths = _c128widthsFromValues(values)
    return _bitsFromWidths(widths)

def c128rect(text, xy=(None, None), height=inkyphat.HEIGHT):
    """
    Draws a code-128 barcode. Set x or y to None to center on that axis.
    Currently only uses mode B due to programmer laziness. TODO: ensmarten it
    """
    bits = c128bits(text)
    _bitsRect(bits, xy, height)
















