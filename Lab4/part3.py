from summa.summarizer import summarize
from summa import keywords

text = "En kvinna i 60-årsåldern från Oskarshamn har blivit av med cirka 200 000 kronor efter att ha lurats av en person som uppgivit sig för att vara amerikanske skådespelaren Keanu Reeves, rapporterar Barometern. Kvinnan hade först fått flera vänförfrågningar på sociala medier från konton som uppgav sig för att vara skådespelaren. Hon tog då kontakt med kontot som hon trodde tillhörde den riktiga Keanu Reeves för att varna honom. De började sedan skriva till varandra och en träff mellan de två planerades i Oskarshamn. Men kontot som uppgav sig för att vara Reeves hade pengaproblem. Hans pengar var låsta. Kvinnan betalade då både hans resa och covidintyg. När han skulle resa till Oskarshamn blev han kidnappad på flygplatsen. Kvinnan betalade då en lösensumma för att han skulle släppas fri och ta sig till henne med en privat buss. Vid det tillfället hade kvinnan skickat cirka 200 000 kronor och när han aldrig kom förstod kvinnan att hon utsatts för ett bedrägeri. Vårt råd är att aldrig godkänna vänförfrågningar på sociala medier från personer man inte känner, oavsett om de är kändisar eller inte. De är oerhört skickliga och manipulerande. Det är en stor kränkning mot personen som drabbas, säger polisens presstalesperson Robert Loeffel till Barometern."
# Define length of the summary as a proportion of the text
print(summarize(text, ratio=1))

# summarize(text, words=7)

print("Keywords:\n",keywords.keywords(text))
# to print the top 3 keywords
print("Top 3 Keywords:\n",keywords.keywords(text,words=3))



