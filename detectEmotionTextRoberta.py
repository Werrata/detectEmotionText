from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline
import pandas as pd
import random
import pygame
import time
import winsound

int i = 0

#Renvoie des émotions correspondant à Text en entrée
def DetectEmotion(Text):
    if i==0:
        tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
        model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")
        emotion = pipeline('text-classification', model = 'arpanghoshal/EmoRoBERTa')
        i=1
    emotion_labels = emotion(Text)
    return emotion_labels[0]['label']




#Fonction utilisé par PlayMusicAccordingText
def f(a,data,T,R) : 
    for i in range (8407) :
        if data.loc[i,a] == 1 :
#       L.append(i)
            T.append(data.loc[i,'track id'])
            R.append(data.loc[i,'genre'])        
#determination track id
                
    random_index = random.randint(0,len(T)-1)

#track aléatoire avec émotion a 
    g=R[random_index]

    if (g=='pop'):
        tr=T[random_index]-300
    elif (g=='rock'):
        tr=T[random_index]-100
    elif (g=='electronic'):
        tr=T[random_index]-200
    else :
        tr=T[random_index]

    return (g,tr)




#Lance une musique correspondant à l'épotion détécté dans le texte mis en entrée
#Sous fonctions : detectEmotionTextRoberta.DetectEmotion & f
def PlayMusicAccordingText(text):
    print(text)
    b=DetectEmotion(text) #variable emotion
    T=[]#liste track id 
    R=[]#liste genre associé au track id
    data= pd.read_csv('/Users/Utilisateur/Desktop/CoursENSEA/2A/Projet_2A/DetectEmotionText/data.csv')
    a='';

    #Matrice de passage d'un emotion à une autre
    mat=pd.read_csv('/Users/Utilisateur/Desktop/CoursENSEA/2A/Projet_2A/DetectEmotionText/matrice_emotion.csv',index_col=0)

    emotion =['amazement','solemnity','tenderness','nostalgia','calmness','power','joyful_activation','tension','sadness']

    for j in range (9) :
        if mat.loc[b,emotion[j]] == 1 :
            a = emotion[j]
    

    (g,tr)=f(a,data,R,T)
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/Utilisateur/Desktop/CoursENSEA/2A/Projet_2A/DetectEmotionText/emotifymusic/{}/{}.mp3".format(g,tr)) 
    pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy() == True:
    #continue
    time.sleep(15)
    pygame.mixer.music.stop()
    return b, a


duration = 80
def BipSound():
    frequency = random.randint(440,1280)
    winsound.Beep(frequency, duration)


