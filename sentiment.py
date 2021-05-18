#Code to clean and assign sentiment to message
from textblob import TextBlob
import re

def get_sentiment(message):
    
    lis= ' '.join(re.sub("( me | my | myself | we | our | ours | ourselves | you | your | yours | yourself |yourselves | he | him | his | himself | she | her | hers | herself | it | its | itself | they | them | their | theirs | themselves | what | which | who | whom | this | that | these | those | am | is | are | was | were | be | been | being | have | has | had | having | do | does | did | doing | an | the | a | and | but | if | or | because | as | until | while | of | at | by | for | with | about | against | between | into | through | during | before | after | above | below | to | from | up | down | in | out | on | off | over | under | again | further | then | once | here | there | when | where | why | how | all | any | both | each | few | more | most | other | some | such | no | nor | only | own | same | so | than | too | very | can | will | just | don | should | now | ain | aren | couldn | didn | doesn | hadn | hasn | haven | isn | ma | mightn | mustn | needn | shan | shouldn | wasn | weren | won | wouldn | I |RT )"," ",message).split())
    lis.lower()
    lis=' '.join(re.sub(":\) |:-\) | \^.\^ |\^_\^ | :p | :-p | : \)"," happy ",lis).split())
    lis=' '.join(re.sub(":\( |:-\( | :/ "," sad ",lis).split())
    lis=' '.join(re.sub(" xd | :d |:-d | x-d"," funny ",lis).split())
    lis=' '.join(re.sub("\*_\* "," amazing ",lis).split())
    lis=' '.join(re.sub("-.- |-_- | x-\( | x\( "," angry ",lis).split())
    analysis = TextBlob(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", lis).split()))
    return analysis.sentiment.polarity