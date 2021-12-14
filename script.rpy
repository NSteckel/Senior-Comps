# Complete Renpy Documentation: https://www.renpy.org/doc/html/

# "Defining all characters"



define E = Character("Emmy")
define M = Character("Molly")
define R = Character("Robin")
define K = Character("Mark")
define L = Character("Ms. Lodsworth")
define V = Character("Evan")

# "Declaring all images"
image molly = "Molly(F).png"
image robin = "Robin(F).png"
image qrno = "staticF.png"
image qrtop = "staticFTop.png"
image qrbottom = "staticFBottom.png"
image mbed = "MollyBed.png"
image rbed = "RobinBed.png"
image living = "livrm.png"
image tvcode = "tvtest.png"
image mark = "Mark(F)5.png"
image emmy = "Emmy(F).png"
image purny = "Purny(F).png"
image evan = "Evan(F)2.png"
image wide = "widehold.png"
image close1 = "CHold1(F).png"
image close2 = "CHold2(F).png"
image close3 = "CHold3(F).png"
image lodsworth = "Mslodsworth(F).png"
image namebox = "namebox.png"
image schoolwalk = "walk3.jpeg"
image middleschool = "middleschool.png"
image lockers = "lockers.png"
image office = "lodsworthoffice.png"
image mopps = "toystore.png"
image dadbed = "dadbed2.png"

label start:

  # This menu is a table of contents to jump to specific puzzles/interactive elements. Get rid of it later. 
  #menu: 
  #  "start regular":
  #    jump storystart
  #  "go to puzzle 1":
  #    jump firstpuzzle
  #  "go to puzzle 2":
  #    jump secondpuzzle
  #  "go to puzzle 3":
  #    jump thirdpuzzle
  #  "accuse a suspect":
  #    jump accuse

  # The real (default) story starts here
  label storystart:
  scene rbed 
  show namebox zorder 100
  "It's a beautiful day in Berkeley, California. The sun is shining, the birds are chirping...but {i}something{/i} is missing."
  "Robin lies in bed in her room sleeping. Suddenly someone grabs her arm and shakes her awake."
  show robin
  R "What happened? What’s going on?"
  show molly

  M "Have you seen Purny? I can’t find him."
  hide molly
  show purny
  "{i}Purny was Molly's favorite stuffed animal. It looks a little like an alien teddy bear.{/i}"
  hide purny
  show molly
  "{i}Robin climbs out of bed and grabs clean clothes from her dresser.{/i}"
  R "I don’t know Molly, where was the last place you had him?"
  M "When we ate breakfast together yesterday!"
  R "Wait, what? It was just the two of us and dad at breakfast."
  M "But after that, Purny told me he was hungry, so I gave him a peanut butter and ham sandwich!!"
  R "A what? Molly, you shouldn’t eat stuff like that, you’ll make yourself sick."
  M "I didn’t, it was Purny!"
  "{i}Robin sighs and rolls her eyes.{/i}"
  R "Alright, where did Purny eat the sandwich?"
  M "He ate it in my room!"
  hide robin
  hide molly
  scene mbed
  show namebox zorder 100
  show robin
  show molly
  "{i}They walk out of Robin’s room and across the hall to Molly’s. There’s a little bit of banana and some ham on the floor.{/i}"
  M "{i}Loudly and upset{/i} \nSee, he’s not here!!"
  R "Alright I’ll go look for him, okay? Maybe dad moved him."
  R "And while I’m looking for him, I really need you to clean up the mess you made, okay?"
  M "{i}Even angrier{/i} \nI told you it was Purny, not me!!"
  R "Please just clean it up, okay?"
  M "...fine."
  hide molly
  scene living
  show namebox zorder 100
  show robin
  show mark
  # show mark
  "{i}Robin leaves her sister’s room, and goes downstairs. Their dad is sitting half asleep on the living room couch in front of the staticky tv."
  R "Hey, dad?"
  K "Yeah pumpkin?"
  R "Have you seen Purny?"
  "{i}Mark rubs his eyes.{/i}"
  K "…Have I seen what? "
  R "Purny. It’s Molly’s stuffed alien thing."
  K "Oh. Oh, right. Did something happen to it?"
  R "She can’t find it. I think she just left it somewhere, but she’s kind of freaking out about it."
  K "Alright, well I just saw an ad for a bunch of those guys, so maybe you should just get her a new one."
  "{i}He points towards the tv, which seems to be playing an ad.{/i}"
  hide robin
  hide mark
  hide namebox
  show qrbottom
  ''
  hide qrbottom
  show qrno
  ''
  hide qrno
  show qrtop
  ''
  hide qrtop
  show namebox zorder 100
  show robin
   
  R "That looks like it’s an ad for Nondosoft, that toy company. I bet I can buy a new Purny toy from there!" 
  hide namebox
  hide robin
  scene dadbed
  show robin 
  show namebox zorder 100
  "{i}Robin runs upstairs and grabs the family laptop. She goes to the Nondosoft website and begins scrolling through it.{/i}"
  R "Whoa, there’s a bunch of stuff here! Games, toys, characters… here we go, Purny! "
  R "Here’s a plushy that seems good, and it looks just like Molly’s old one!"
  "{i}Robin clicks on it.{/i}"
  R "Wait, $25 dollars?!?! That’s more than I thought, and I’ve only got 21.50! If only it were a little bit cheaper…"
  #hide robin

  label firstpuzzle:

  label safe:

  label code1:

  # The '$' symbol executes a python statement. Each line can be executed individually, or you can declare
  # declare a larger python section if the renpy project calls for a lot of python scripting. You don't 
  # need to download python or any extensions separately in order to write python in a renpy (.rpy) file.

  $ pass1 = "qtpurn20"

  $ code = renpy.input ("Input discount code:")
  $ code = code.lower()
  if code == pass1:
    "Code accepted, discount applied!"
    jump nextstory

  else:
    "Discount code invalid."
    jump safe

  # ^^^^ Password input code segment using python ^^^^ #  

  label nextstory:
  "{i}Robin is about to buy the toy when Molly walks in.{/i}"
  show molly
  M "Robin? What are you doing in Dad’s room? "
  R "Oh...I was just about to buy you a new Purny toy."
  M "What? Why?"
  R "Well, we haven’t been able to find your Purny anywhere, and I just don’t know where it would be. It might be better if we just get you a new one.  "
  M "No! I want {i}my{/i} Purny!"
  R "Come on Molly, please. I really need you to-"
  M "No no no! It has to be that one!!!"
  "{i}Robin takes a deep breath{/i}"
  R "Fine. I’ll help you look for Purny, but I need you to think really hard. Is there anywhere you took him after we had breakfast yesterday?"
  "{i}They sit for a moment. Molly’s face is scrunched up in thought.{/i}"
  M "Wait, I know where he is!"
  R "Alright, where?"
  "{i}Molly hesitates.{/i}"
  M "...I don’t want to tell you."
  R "Molly come on. I really need to know where you left Purny, otherwise I can’t help you find him."
  M "He was lonely, and he said he wanted to go to school with me."
  R "You took it to school?!?! How many times do we have to tell you, you can’t take that thing to school! It’s against the rules! "
  M "He's not an it, he's my friend! He was was sad, and said he wanted to come with me."
  R "He wasn’t- whatever. Let’s just go to school and go get him."

  #   ^^^ ALL GOOD ABOVE! ^^^

  label secondpuzzle:
  scene schoolwalk 

  show namebox zorder 100
  "{i}Molly and Robin step outside. They live in Berkeley, California at 1502 North St street. They're heading towards MLK Jr. Middle school, on 1781 Rose street.{/i}"
  label directions:
  show namebox zorder 100
  "{i}What is the best way for Molly and Robin to get to school?{/i}"
  hide namebox
  menu:

    "Go down North street and turn left Jaynes St.":
      jump routegood2
    "Go down North street and turn right Jaynes St.":
      jump routebad2
    "Go down North street and turn left on McGee Ave.":
      jump routebad2
    "Go down McGee Avenue and turn left on Jaynes St.":
      jump routebad2

  label routegood2:
  menu:
    "Then turn left onto Vine St.":
      jump routebad3
    "Then turn right onto Josephine St.":
      jump routebad3
    "Then turn left onto Edith St.":
      jump routegood3
    "Then turn right onto Cedar St.":
      jump routebad3

  label routebad2:
  menu:
    "Then turn left onto Vine St.":
      jump routebad3
    "Then turn right onto Josephine St.":
      jump routebad3
    "Then turn left onto Edith St.":
      jump routebad3
    "Then turn right onto Cedar St.":
      jump routebad3

  label routegood3:
  menu: 
    "Then turn left onto Vine St.":
      jump routebad4
    "Then turn right onto Vine St.":
      jump routegood4
    "Finally, turn left onto Vine St.":
      jump routebad4
    "Finally, turn right onto Vine St.":
      jump routebad4

  label routebad3:
  menu: 
    "Then turn left onto Vine St.":
      jump routebad4
    "Then turn right onto Vine St.":
      jump routebad4
    "Finally, turn left onto Vine St.":
      jump routebad4
    "Finally, turn right onto Vine St.":
      jump routebad4

  label routegood4:
  menu: 
    "Finally, turn left onto Grant St. and go straight.":
      jump directiondone
    "Finally, turn left onto Josephine St. and go straight.":
      "{i}It seems like Molly and Robin took a wrong turn.{/i}"
      jump directions
    "Finally, turn left onto McGee Ave. and go straight.":
      "{i}It seems like Molly and Robin took a wrong turn.{/i}"
      jump directions
    "Finally, turn right onto Josephine St. and go straight.":
      "{i}It seems like Molly and Robin took a wrong turn.{/i}"
      jump directions

  label routebad4:
  menu: 
    "Finally, turn left onto Grant St. and go straight.":
      show namebox zorder 100
      "{i}It seems like Molly and Robin took a wrong turn.{/i}"
      hide namebox
      jump directions
    "Finally, turn left onto Josephine St. and go straight.":
      show namebox zorder 100
      "{i}It seems like Molly and Robin took a wrong turn.{/i}"
      hide namebox
      jump directions
    "Finally, turn left onto McGee Ave. and go straight.":
      show namebox zorder 100
      "{i}It seems like Molly and Robin took a wrong turn.{/i}"
      hide namebox
      jump directions
    "Finally, turn right onto Josephine St. and go straight.":
      show namebox zorder 100
      "{i}It seems like Molly and Robin took a wrong turn.{/i}"
      hide namebox
      jump directions

  label directiondone:
  scene middleschool
  show robin
  show molly
  show namebox zorder 100

  R "Alright Molly, we’re here." 
  "{i}Molly’s on her phone, doesn’t seem to be listening.{/i}" 
  R "What are you doing?"
  M "I’m looking at my friend Emmy’s instagram, she just made a new account."
  "{i}Robin grabs Molly’s phone, glances at it.{/i}"
  R "emmy_again_81? Kind of a weird username. Why are you looking at this right now, where did you leave Purny?"
  M "I left Purny in Emmy’s locker because she thought I would get in trouble if he stayed in mine. "
  R "Fine, do you know where Emmy’s locker is? "
  M "Yeah, it’s number 130. Down this hallway."
  hide namebox
  hide robin
  hide molly
  scene lockers
  show molly
  show robin
  show namebox zorder 100
  "{i}They walk over to the locker.{/i}"
  R "Do you know what the code is?"
  M "I think it’s her birthday, but i’m not sure."
  R "Okay, and when is that?"
  M "I don’t know. Maybe she posted about it?"

  label thirdpuzzle:
  label password3:
    # "Input locker combo"
    jump safe3

  label safe3:

  
  $ pass3 = "12-06-09"
  $ code3 = renpy.input ("Input locker combo. {i}Format it as XX-XX-XX{/i}")
  if code3 == pass3:
    "{i}The lock clicks, and the door swings open.{/i}"
    jump nextstory3

  else:
    "{i}They input the code and pull at the door, but nothing happens.{/i}"
    R "That didn't work. Let's try a different combo."
    jump safe3

  label nextstory3:

  R "We got it!"
  "{i}They look inside, but the locker is empty except for a history textbook.{/i}"
  M "Where did he go?"
  R "I don’t know. Can you think of anywhere else--"
  hide molly
  show lodsworth
  L "Hey!!! What are you girls doing here?"
  "{i}It's Ms. Lodsworth, one of the school's guidance counselors. She walks swiftly towards the two girls.{/i}"
  R "Ms. Lodsworth? What are you doing here?"
  L "That’s none of your business! It’s a Saturday, what are {i}you two{/i} doing here looking through another student’s locker?"
  R "We’re just trying to find Molly’s doll. She knows it’s against the rules, but she brought it to school and then she lost it."
  L "A likely story. Come with me you two, we’ll figure this out in my office."
  hide lodsworth
  hide robin
  hide namebox
  scene office
  show namebox zorder 100
  show robin 
  show lodsworth
  "{i}The three of them walk upstairs to Ms. Lodsworth's office. She looks unhappy.{/i}"
  L "So, what were you doing here?"
  R "We were just trying to get Molly's toy back. She brought it to school a few days ago, and ended up leaving it here with one of her friends."
  L "So you brought {i} a toy{/} to school against the rules, and now you're trying to retreive it? A likely story."
  hide lodsworth
  show molly
  M "Purny's not some toy, he's my friend!"
  hide molly
  show lodsworth
  L "If you want it back so much, it must be very valuable. Let's have a look, shall we?"
  "{i}She turns to her computer.{/i}"
  R "It's called Purny, it looks like a three-eared bear with little dots on its cheecks."
  "{i}Ms. Lodsworth scrolls through a website, then stops. She looks shocked.{/i}"
  L "Did this doll happen to come out in the mid-90's?"
  R "I think so, but I'm not sure. Why does that matter?"
  L "That particular model has become somewhat of a collector's item. It's worth over ten thousand dollars."
  R "What?"
  L "Obviously there's no way that the two of you could have such a valuable item, and if you did it was clearly stolen." 
  L "I will escort you back home, although I'm afraid I will have to confiscate the doll once it has been found."
  R "Wait, that's so not fair!"
  L "I'm sorry young lady, but it must be done."
  hide lodsworth
  show molly
  M "Wait! Emmy's dad works at a toy store! He's seen Purny with me and he collects all sorts of valuable items, so he might know where Purny went."
  hide molly
  show lodsworth
  L "Evan Simmons? Well, how would you get in touch with him?"
  R "I should have the address for his shop in my contacts list!"

  label fourthpuzzle:
  #"!!Third puzzle here!!"
  label password4:
    # "store name"
    jump safe4
  label safe4:

  $ pass4 = "mr. mopps"
  $ code4 = renpy.input ("What is the name of Mr. Simmons' store?")
  $ code4 = code4.lower()
  if code4 == pass4:
    R "That's it! It's Mr. Mopps' Toy Shop! "
    jump nextstory4
  else:
    R "No, that's not the right one. Let's try something different."
    jump safe4
  label nextstory4:


  L "Alright then, let's go."

  scene mopps
  show namebox zorder 100
  show robin



#   VVV  ALL GOOD!  VVV

  "{i}Molly, Robin and Ms. Lodsworth walk into the toy store. Evan and his daughter Emmy Simmons are behind the counter, Mark is on the other side talking to them.{/i}"
  show mark
  K "Molly, Robin! It's good to see you two. Look what i found!"
  hide mark 
  show purny
  M "Purny!"
  hide purny
  show evan
  V "Yes, your father pointed it out on one of my shelves, and once I took a closer look, we realized it was yours."
  hide evan 
  show molly
  M "How did he get all the way over here?"
  hide molly 
  show evan
  V "Well, I think that someone found it and sold it to me in bulk with a bunch of other toys. They probably didn't realize it was so valuble."
  hide evan 
  show molly
  M "But who took him?"
  hide molly 
  show evan
  V "I'm sorry, but I really can't say. I don't really keep records of who gives me toys to sell." 
  hide evan 
  show molly
  M "I don't believe you! Someone here must have taken Purny!"
  hide molly
  hide robin

  label accuse:
  "Who is the person who took Molly's doll?"
  hide molly
  hide robin
  menu:
    "It was Mark, Robin and Molly's dad.":
      show molly
      show robin
      M "It was you, dad!! You told Robin to buy me a new one because you new it wouldn’t be returned!"
      hide molly
      show mark
      K "Come on, I wouldn't do something like that. Especially not to my daughter."
      hide mark 
      show molly
      M "Hmm... A likely story. Who could it be then?"   
      hide molly
      jump accuse

    "It was Ms. Lodsworth, a math teacher.":
      show molly
      show robin
      M "It was you, Ms. Lodsworth!!"
      
      R "Of course! You were at school on a Saturday, and then refused to explain what you were doing there. You only took us here to get the doll back for yourself."
      R "Also, you were shocked at how expensive the purny doll was, and you don't make a lot of money as a school aministrator."
      hide molly
      show lodsworth
      L "Oh come on, you can't seriously think that I was the one who took that silly doll. I would never steal from my students!"
      R "Don't give us that! You have Emmy in your class and you knew her dad would pay a fortune for it!"
      R "You just waited for the right moment and then you must've confiscated it after Molly brought it to school!"
      L "This is rediculous, I don't have to stand here and listen to these rediculous accusations!"
      hide lodsworth
      show mark
      K "Maybe not now, but you'll have to listen to them at the next PTA meeting."
      hide mark
      show lodsworth
      L "I didn't do it, I swear!!"
      hide lodsworth
      show mark
      K "Yeah, right."
      hide mark
      show lodsworth
      L "Hmph!"
      hide lodsworth
      show molly
      "{i}Ms. Lodsworth turns around and runs out of the store.{/i}"
      M "Wow, I can't believe that Ms. Lodsworth was the one who took Purny."
      hide molly
      show mark
      K "Do you really think she was the reason Purny went missing? You shouldn't just accuse people if you don't have all the facts."
      
      R "Who knows, it's just a good thing we got him back."
      hide robin
      hide molly
      hide mark
      jump awakenending

    "It was Emmy Simmons, Molly's best friend.":
      show molly
      show robin
      M "It was you, Emmy!!"
      R "Of course! You were jealous of Molly for having such a rare and valuble toy. Also, Purny went missing from inside your locker, most other people wouldn’t know the locker combo."
      hide molly
      show emmy
      E "How can you say that?!?! Molly is my best friend, I would never do that to her."
      R "You're obsessed with instagram, you only use Molly for a prop!" 
      E "I can't believe you!"
      hide emmy
      show evan
      V "Emmy, is this true?"
      hide evan
      show emmy
      E "No, it's not!!"
      R "Yes, it is!!"
      hide emmy
      show evan
      V "You know what? You're grounded for a week."
      hide evan
      show emmy
      E "I told you, it wasn't me!!"
      hide emmy
      show evan
      V "Are you trying for two weeks?"
      hide evan
      show emmy
      E "This is so unfair! I told you, I didn't do it!"
      hide emmy
      "{i}She runs out of the store.{/i}"
      show molly
      M "Wow, I can't believe that Emmy was the one who took Purny."
      hide molly
      show mark
      K "Do you really think she was the reason Purny went missing? You shouldn't just accuse people if you don't have all the facts."
      R "Who knows, it's just a good thing we got him back."
      hide robin
      jump awakenending

    "It was Evan Simmons, Emmy's dad.":
      show molly
      show robin
      M "It was you, Mr. Simmons!!"
      R "Of Course! You knew how valuable the doll was before anyone else and you run a toy store, so you collect a lot of rare items."
      hide molly
      show evan
      V "Wait what?! You can't seriously be suggesting that I stole a stupid doll from my daughter's best friend just so I could make a few bucks!"
      hide evan
      show molly
      M "Hey! Purny's not just some stupid doll, he's my friend!"
      hide molly
      show mark
      K "Seriously, Evan? This isn't cool. Just give her back the doll."
      hide mark
      show evan
      V "I didn't {i}take{/i} the doll. I don't have to listen to this, just get out of my shop."
      hide evan
      "{i}He storms out to the back room of the store.{/i}"
      show molly
      M "Wow, I can't believe that Emmy's dad was the one who took Purny."
      hide molly
      show mark
      K "Do you really think he was the reason Purny went missing? You shouldn't just accuse people if you don't have all the facts."
      R "Who knows, it's just a good thing we got him back."
      hide mark 
      hide robin
      jump awakenending
  
  label awakenending:
  show mark
  K "Come on girls, let's go home."
  hide mark
  hide namebox
  show wide
  ""
  hide wide
  show close1
  ""
  ""
  hide close1
  show close2
  ""
  hide close2
  show close3
  ""
  show namebox zorder 100
  "The End"
  "Thanks for playing! --Nate"
  return