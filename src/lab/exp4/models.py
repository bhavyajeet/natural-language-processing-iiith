from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/corpus.db'
corpusdb = SQLAlchemy(app)

class BigramTable (corpusdb.Model):
    id = corpusdb.Column(corpusdb.Integer,primary_key=True)
    formid = corpusdb.Column (corpusdb.Integer(),unique=False,nullable=False)
    corpus = corpusdb.Column (corpusdb.Integer(),unique=False , nullable=False  )
    answer = corpusdb.Column (corpusdb.String(4),unique=False ,nullable=False )

    def __init__ (self,corpus,formid,answer):
        self.corpus= corpus
        self.formid = formid 
        self.answer= answer 

#    def __repr__(self) :
#        return '<User %r>' % self.formid % self.answer



# def create ():
#     sentence1= "(eos) Can I sit near you (eos) You can sit (eos) Sit near him (eos) I can sit you (eos)"
#     sentence1=sentence1.split()
#     sentence=[]
#     for i in sentence1:
#         if i not in sentence:
#             sentence.append(i)
#     count=0
#     corpus=0
#     for i in range(len(sentence)):
#         for j in range(len(sentence)):
#             formid=count
#             count+=1
#             counti=0
#             countt=0
#             for k in range(len(sentence1)):
#                 if sentence1[k]==sentence[i]:
#                     counti+=1
#                     if sentence[j]==sentence1[i+1]:
#                         countt+=1
#             answer=float(countt)/counti
#             corpusdb.create_all()
#             newentry=BigramTable(corpus,formid,answer)
#             corpusdb.session.add(newentry)
#             corpusdb.session.commit()

# corpusdb.create_all()

print ("exec complete")




