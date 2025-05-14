"""
Alice has two queues, Q and R, which can store integers. Bob gives alice 50 odd integers and 50 evens and
insists that she store all 100 in tegers in Q and R. They then play a game where Bob picks Q or R at random
and then applies the round-robin scheduler, described in the chapter to the chosen queue a random number
of times. If the last number to be processed at the end of this game was odd, Bob wins. Otherwise, Alice wins.
How can Alice allocate integers to queues to optimize her chances of winning? what is her chance of winning?
"""
