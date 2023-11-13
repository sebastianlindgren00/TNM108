from summa.summarizer import summarize
from summa import keywords

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras gravida hendrerit metus, ac faucibus ipsum egestas quis. Vivamus facilisis eros id tellus cursus tempus. Mauris sapien lectus, auctor id metus ut, lacinia fermentum lorem. Donec suscipit dolor sed sem auctor congue. Nam tristique ultricies ullamcorper. Nulla tincidunt mi ut purus lacinia maximus porta et nisi. Donec ultrices, dui non mollis rutrum, magna diam condimentum elit, eu laoreet lectus nulla a nunc. Nulla quis diam posuere, finibus nunc ac, sagittis tellus. Aliquam posuere ac ex ut tincidunt. Cras velit justo, sagittis sit amet volutpat id, ultrices et justo. Etiam maximus, metus at mollis pretium, sapien mauris bibendum lorem, quis semper nunc ipsum non ligula. Cras diam dui, efficitur a purus eu, placerat efficitur lacus. Curabitur vulputate ornare commodo. Etiam commodo lorem a pharetra maximus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam ultricies, purus vel sodales pharetra, quam turpis dapibus neque, et tristique nunc lorem sed elit. Nam vitae sagittis diam. Morbi eget orci eleifend, vehicula mi posuere, fringilla orci. Etiam dignissim porta ante et congue. In mauris velit, lobortis nec dapibus sed, mattis vel velit. Nullam tempor ligula eu sodales laoreet. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac metus dignissim, tristique nisl eget, viverra enim. Nam tincidunt dui ac arcu accumsan, non dictum massa feugiat. Nam tincidunt mi pretium diam commodo cursus. Vivamus et elementum massa. Donec tincidunt magna non lorem semper auctor. Proin ac metus vitae metus venenatis dapibus. Praesent cursus turpis dignissim mauris egestas sodales. Phasellus sit amet velit at nisi vulputate finibus. Curabitur ornare nisi eu erat elementum, ac suscipit lacus cursus. Sed ut augue fringilla, maximus lectus vitae, maximus ante. Morbi hendrerit nulla vel elementum dignissim. Nulla vehicula, ligula sit amet accumsan tristique, metus elit fermentum dui, non bibendum nunc metus ut sem. Pellentesque sed felis ornare, porta elit et, tincidunt nunc. Ut consequat mauris eget convallis rhoncus. Aliquam erat volutpat. Donec auctor faucibus tristique. Phasellus pharetra nibh nec consequat fermentum. Sed at quam nec neque hendrerit sollicitudin id id libero. Aliquam dictum nibh vel erat luctus, vel porttitor urna porttitor. Sed rutrum metus fermentum, congue est in, pellentesque urna. Mauris ac quam dolor. Fusce et euismod dui. Suspendisse potenti. Mauris a nunc ligula. Donec a quam at ex elementum lobortis. Donec sed felis pulvinar, imperdiet elit cursus, cursus justo. Maecenas semper elit a quam ullamcorper, id hendrerit sem sagittis. Donec neque purus, tincidunt ut ex at, tempus tempus arcu. Morbi tempor condimentum neque, eget aliquam lectus placerat facilisis. Quisque at condimentum lorem, ac convallis dolor. Nunc scelerisque sem odio, ac aliquet massa lacinia et. Etiam dictum congue lectus, eu ultricies nulla blandit feugiat. Sed blandit dolor eu metus viverra iaculis."

# Define length of the summary as a proportion of the text
print(summarize(text, ratio=0.2))

summarize(text, words=50)

print("Keywords:\n",keywords.keywords(text))
# to print the top 3 keywords
print("Top 3 Keywords:\n",keywords.keywords(text,words=3))



