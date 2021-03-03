from konlpy.tag import Komoran

komo = Komoran(userdic='./user_dic.tsv')
text = "우리 챗봇은 엔엘피를 좋아해."
pos = komo.pos(text)
print(pos)

# 사용자 사전 적용 전 :
# [('우리', 'NP'), ('챗봇은', 'NA'), ('엔', 'NNB'), ('엘', 'NNP'), ('피', 'NNG'), ('를', 'JKO'), ('좋아하', 'VV'), ('아', 'EF'), ('.', 'SF')]