label ch1:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "Well time for my first day of, High School!"
    "Can't wait!"
    "Man i think im gonna join a club..."
    "Im kinda a reader so maybe theres a club for that."
    "I guess i should get to my class."
    "Lets see my classes are..."
    "History, Chemistry (Ha it's kinda just science)"
    "Oh then lunch... Kinda lucky."
    "Wait. suddenly a student, rushes past me almost knocking me to the floor"
    show mcc 1s1 zorder 2 at t11
    s "S-sorry! Im runing late to class!"
    $ s_name = "MonaCha"
    hide mcc
    "He droped his card.... hm"
    "His name is MonaCha?"
    "Weird name..."
    mc "Wait!"
    show mcc 1s1 zorder 2 at t11
    s "Huh?"
    mc "You forgot your card!"
    show mcc 1s2
    s "Oh.. How silly of me thanks for picking it up!"
    mc "No.. Problem... MonaCha"
    show mcc 1s
    s "W-What?"
    s "How do you know my name?"
    mc "It's on the card..."
    show mcc 1s2
    s "Oh... Haha"
    show mcc 1j
    s "I'l see you around ok?"
    mc "Okay..."
    hide mcc
    "Hes kinda cute..."
    "Oh right i better get to class too"

    scene bg class_day
    with wipeleft_scene

    "I let out a very loud yawn..."
    "Its time to go check out a club!"
    "I get my things and i head out"
    "Im so tired"
    "Oh. I bumped right into someone"
    show monika 1k zorder 2 at t31
    $ m_name = "???"
    m "Oh sorry.."
    mc "Ah.. Its fine i wasen't paying attention"
    "Ow.. Who walks in a classroom when the school day is technically over"
    m 1b "Sorry i was about to hang up Flyers for my club"
    mc "Hm? What club?"
    m 5 "Oh its the Literature Club!"
    "I love literature!"
    mc "Oh i love literature, can i join?"
    m 1b "Of course!"
    mc "Were is it?"
    m 5 "Well its kinda in the back of the school. Why don't you follow me after i get these flyers up!"
    mc "Alright. Sounds reasonable"

    with wipeleft_scene

    m 1b "And done that wasen't too long"
    "It was 2 minutes"
    "So she isn't wrong"
    mc "Alright ready to go then?"
    m "Yep!"
    mc "Oh wait is it funny that we havent told each other our names?"
    m "Oh right..."
    $ m_name = "Monika"
    m 5 "Im Monika."
    mc "Im [player]"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    hide monika
    "We walk really far into the school. Seems like a far walk."
    "Its been 1 minute"
    "Im still walking"
    "Im alwase like that..."
    "Alwase complaning"
    "Even though i have a decent life."
    "Monika opens the door with alot. When i say Alot i mean ALOT! of energy"

    scene bg club_day
    with wipeleft
    play music t3

    show monika 1b at l41
    m "We have a new member!"
    show mcc 1s1 zorder 2 at t32
    s "Oh."
    "Wait he's here....."
    hide mcc
    hide monika
    show yuri 1a zorder 2 at t11
    $ y_name = "Girl 1"
    y "Welcome to the Literature Club. It's a pleasure meeting you."
    show mcc 1j at l41
    s "Yeah welcome!"
    hide yuri
    show natsuki 4c zorder 2 at t32
    $ n_name = "Girl 2"
    n "Oh. Hey!"
    "Seems like quite a crowd..."
    "Not really, it's not crowd"
    n "Heh, atleast it's not another boy.."
    show mcc 1a
    s "What?"
    show natsuki zorder 3 at f32
    n "Well i mean...."
    s "Huh what is it?"
    show natsuki zorder 3 at f32
    n "I don't want to ruin this with boys!"
    show mcc 1s
    s "T-that's a little un-called for!"
    hide mcc
    show yuri 1a zorder 2 at t33
    y "Natsuki, be a little nice for one time in your life."
    $ n_name = "Natsuki"
    hide yuri
    hide natsuki
    show monika 1b zorder 3 at f31
    m "Don't worry, Natsuki is a little fussy sometimes."
    m "Anywase this is Yuri, and this is Natsuki."
    $ y_name = "Yuri"
    mc "Erm, Nice to meet you all!"
    m "It also sounds like you met MonaCha Already"
    mc "Yeah we keep meeting"
    show mcc 1s2 zorder 2 at t32
    s "Heh..."
    hide mcc
    m "Well anyway welcome!"
    mc "Thanks~!"
    show mcc 1j zorder 2 at t32
    s "Hey why don't you sit down next to me at the table!"
    "Huh they have a little table made out of desk's..... Kinda cute."
    mc "O-Okay!"
    hide mcc
    hide monika
    "i take a seat at the table"
    show natsuki 4c zorder 2 at t32
    n "Man, you should have told me monika!"
    show monika 1b zorder 3 at f31
    m "Hm?"
    n "I would have made cupcakes!"
    m "Oh sorry~!"
    hide monika
    n "Ugh.."
    hide natsuki
    show yuri 1a zorder 2 at t32
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "Oh well.."
    mc "I kinda like chapter books like novels, More or less like The Rings Of The Lords, Or Potter Of Harry's Magic."
    "Those were some good books"
    y 3u "O-Oh... Those were s-some good books..."
    "Okay...."
    hide yuri
    show monika 1b zorder 3 at f31
    m "Anyway let's rap this up, Im hungry!"
    show mcc 1 zorder 2 at t32
    s "Y-You just ate!"
    m "Eh, only like 4 hours ago"
    show mcc 1s1
    s "More like 4 minutes ago"
    m "Heh..."
    s "Anyway i got to go too"
    m "Alright i guess that rap's it up!"
    hide mcc
    m "Oh right make sure to write a poem for the next meeting!"
    m "Alright now we can go"

    scene bg residential_day
    with wipeleft_scene

    "Some day..."
    "I guess i have to make a poem"
    "Hm, what should it be about?"

    stop music fadeout 2.0
    call screen dialog("Thanks For Playing My Demo\nOf My Mod!", ok_action=Return())
    play music audio.t4
    show end
    m "I guess that's it huh"
    m "See you in the full version~!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
