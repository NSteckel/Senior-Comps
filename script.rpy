# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# "Defining all characters"
define E = Character("Emmy")
define M = Character("Molly")
define R = Character("Robin")
define K = Character("Mark")
define L = Character("Ms. Lodsworth")
define V = Character("Evan")

# "Declaring all images"
image molly = "Molly.png"
image robin = "Robin.png"
image qrno = "staticF.png"
image qrtop = "staticFTop.png"
image qrbottom = "staticFBottom.png"
image mbed = "MollyBed.png"
image rbed = "RobinBed.png"
image living = "livrm.png"
image tvcode = "tvtest.png"
image mark = "Mark.png" # ???

label start:

  # This menu is a table of contents to jump to specific puzzles/interactive elements. 
  menu: 
    "start regular":
      jump storystart
    "go to puzzle 1":
      jump firstpuzzle
    "go to puzzle 2":
      jump secondpuzzle
    "go to puzzle 3":
      jump thirdpuzzle
    "accuse a suspect":
      jump accuse

  # The real (default) story starts here
  label storystart:
  scene rbed 
  "Robin lies in bed in her room sleeping. Suddenly someone grabs her arm and shakes her awake."
  show robin
  R "What happened? What’s going on?"
  show molly
  M "Have you seen Purny? I can’t find him."
  "{i}Robin climbs out of bed and grabs clean clothes from her dresser.{/i}"
  R "I don’t know Molly, where was the last place you had him?"
  M "When we ate breakfast together yesterday!"
  R "Wait what? It was just the two of us and dad at breakfast."
  M "But after that, Purny told me he was hungry, so I gave him a peanut butter and ham sandwich!!"
  R "A what? Molly, you shouldn’t eat stuff like that, you’ll make yourself sick."
  M "I didn’t, it was Purny!"
  "{i}Robin sighs and rolls her eyes.{/i}"
  R "Alright, where did Purny eat the sandwich?"
  M "He ate it in my room!"
  scene mbed
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
  # show mark
  "{i}Robin leaves her sister’s room, and goes downstairs. Their dad is sitting half awake on the living room couch in front of the staticy tv. He’s been sleeping there a lot lately.{/i}"
  R "Hey, dad?"
  K "Yeah pumpkin?"
  R "Have you seen Purny?"
  "Mark rubs his eyes"
  K "…Have I seen what? "
  R "Purny. It’s Molly’s stuffed alien thing."
  K "Oh. Oh, right. Did something happen to it?"
  R "She can’t find it. I think she just left it somewhere, but she’s kind of freaking out about it."
  K "Alright well I just saw an ad for a bunch of those guys, so maybe you should just get her a new one."
  "{i}He points towards the staticky tv, which seems to be playing an ad.{/i}"
  hide robin
  hide molly
  show qrbottom
  ''
  hide qrbottom
  show qrno
  ''
  hide qrno
  show qrtop
  
  #

  hide qrtop
  show robin
  R "That looks like it’s an ad for Nondosoft, that toy company. I bet I can buy a new Purny toy from there!" 
  "{i}Robin runs upstairs and grabs the family laptop. She goes to the Nondosoft website and begins scrolling through it.{/i}"
  R "Whoa, there’s a bunch of stuff here! Games, toys, characters… here we go, Purny! "
  R "Here’s a plushy that seems good, and it looks just like Molly’s old one!"
  "{i}Robin clicks on it.{/i}"
  R "Wait, $25 dollars?!?! That’s more than I thought, and I’ve only got 21.50! If only it were a little bit cheaper…"
  hide robin

  #
  label firstpuzzle:

  label password:
    # "Insert discount code"
    jump safe

  label safe:

  
  #menu:
  #  "Try again.":
  #    jump code
  #  "No":
  #    return
  

  label code:

  $ pass1 = "qtpurn20"

  $ code = renpy.input ("Input discount code.")

  if code == pass1:
    "Code accepted, discount applied!"
    jump nextstory

  else:
    "Discount code invalid."
    jump safe


  label nextstory:
  "{i}Robin is about to buy the toy when Molly walks in.{/i}"
  show molly
  M "Robin? What are you doing in Dad’s room? "
  R "Oh...I was just about to buy you a new Purny toy."
  M "what? Why?"
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
  M "he was lonely, and he said he wanted to go to school with me."
  R "You took him to school?!?! How many times do we have to tell you, you can’t take that thing to school! It’s against the rules! "
  M "But Purny was sad, and he wanted to come with me."
  R "He wasn’t- whatever. Let’s just go to school and go get him."

  label secondpuzzle:
  "!!Second puzzle Here!!"

  R "Alright Molly, we’re here. Molly’s on her phone, doesn’t seem to be listening. What are you doing?"
  M "I’m looking at my friend Emmy’s instagram, she just made a new account."
  "{i}Robin grabs Molly’s phone, glances at it.{/i}"
  R "Emmy_Again_85? Kind of a weird username. (Turns to Molly) Why are you looking at this right now? "
  M "I left Purny in Emmy’s locker, because she thought I would get in trouble if Purny stayed in mine. "
  R "fine, do you know where emmy’s locker is? "
  M "Yeah, it’s number 1282. Down the hall."
  "{i}They walk over to the locker{/i}"
  R "Do you know what the code is?"
  M "I think it’s her birthday, but i’m not sure."
  R "and when is that?"
  M "I don’t know. Maybe she posted about it?"

  label thirdpuzzle:
  "!!Third puzzle here!!"

  R "We got it!"
  "{i}The door swings open, but the locker is empty except for a history textbook.{/i}"
  M "Where did he go?"
  R "I don’t know. Listen can you think of anywhere else--"
  L "Hey!!! What are you girls doing here?"
  "{i}Ms. Lodsworth, a math teacher enters. She walks swiftly towards the two girls.{/i}"
  R "Ms. Lodsworth? What are you doing here?"
  L "That’s none of your business! It’s a Saturday, what are {i}you two{/i} doing here looking through another student’s locker?"
  R "We’re just trying to find Molly’s doll. She knows it’s against the rules, but she brought it to school and then she lost it."
  L "A likely story. Come with me you two, we’ll figure this out in my office with your parents on the phone."


  label accuse:
  "Who is the person wqho took Molly's doll?"
  menu:
    "It was Nathan, Robin and Molly's dad.":
      R "It was you, dad!!"
      R "you didn't even try to look for Purny after I told you it was missing, and immediately offered to buy Molly a new one, as if you new it wouldn’t be returned!"
      K "Come on Robin, I wouldn't do something like that. Especially not to my two favorite girls."
      R "Hmm... A likely story. Who could it be then?"   
      jump accuse

    "It was Ms. Lodsworth, a math teacher.":
      R "It was you, Ms. Lodsworth!!"
      R "You were at school on a Saturday, and then refused to explain what you were doing there."
      R "Also, you were shocked at how expensive the purny doll was, and you only makes a teacher’s salary."
      L "Oh come on, you can't seriously think that I was the one who took that silly doll. I would never steal from my students!"
      R "Don't give us that! You have Emmy in your class and you knew her dad would pay a fortune for it!"
      R "You just waited for the right moment and then you must've confiscated it after Molly brought it to school!"
      L "This is rediculous, I don't have to stand here and listen to these rediculous accusations!"
      K "Maybe not now, but you'll have to listen to them at the next PTA meeting."
      L "I didn't do it, I swear!!"
      K "Yeah, right."
      L "Hmph!"
      "{i}Ms. Lodsworth turns around and runs out of the store.{/i}"
      M "Wow, I can't believe that Ms. Lodsworth was the one who took Purny."
      jump awakenending

    "It was Emmy Simmons, Molly's best friend.":
      R "It was you, Emmy!!"
      R "You were jealous of Molly for having such a rare and valuble toy. Also, Purny went missing from inside your locker, most other people wouldn’t know the locker combo."
      E "How can you say that?!?! Molly is my best friend, I would never do that to her."
      R "You're obsessed with instagram, you only use Molly for a prop!" 
      E "I can't believe you!"
      V "Emmy, is this true?"
      E "No, it's not!!"
      R "Yes, it is!!"
      V "You know what? You're grounded for a week."
      E "I told you, it wasn't me!!"
      V "Are you trying for two weeks?"
      E "This is so unfair! I told you, I didn't do it!"
      "{i}She runs out of the store.{/i}"
      M "Wow, I can't believe that Emmy was the one who took Purny."
      jump awakenending

    "It was Evan Simmons, Emmy's dad.":
      R "It was you, Mr. Simmons!!"
      R "You knew how valuable the doll was before anyone else and you run a toy store, so you collect a lot of rare items."
      V "Wait what?! You can't seriously be suggesting that I stole a stupid doll from my daughter's best friend just so I could make a few bucks!"
      M "Hey! Purny's not just some stupid doll, he's my friend!"
      K "Seriously, Evan? This isn't cool. Just give her back the doll."
      V "I didn't {i}take{/i} the doll. I don't have to listen to this, just get out of my shop."
      "{i}He storms out to the back room of the store.{/i}"
      M "Wow, I can't believe that Emmy's dad was the one who took Purny."
      jump awakenending
  
  label awakenending:

  "The End"
  ""
  "Thanks for playing! --Nate"
    # "{i}{/i}"

    # This ends the game.

  return
