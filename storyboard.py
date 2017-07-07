Print ("A girl is at home when she suddenly realizes her new dog is gone. The dog, being new and young, does not have a sense of direction and cannot find its way home. The girl runs outside to her sidewalk, panicked, and begins looking for her dog.")
answer= str (input("Where does she head towards first? Type right to go right and left to go left"))
if answer in ['right']:
    print ("She walks a few blocks and encounters a neighborhood dog park. She looks around and sees a man nearby sitting on a bench with his dog.")
    answer= str (input("Type ask man to ask him if he has seen her dog or type ignore to continue looking for her dog herself at the dog park."))
    if answer in ['ask man']:
            print ("The man has seen her dog! He points her in the direction of her dog and she and her dog are reunited again.")
    else:
            print ("She continues to walk around the park and out of the corner of her eye, she sees a glimpse of her dogs brown fur and finds her dog playing catch with another dog. She is very happy to have found her dog.")
else:
    print ("She turns left and she approaches an intersection. There, she sees a house with a few kids playing on their lawn.")
    answer= str (input("Type ask kids to ask the kids if they have been her dog or type leave to turn onto the intersection."))
    if answer in ['ask kids']:
        print ("The kids tell her that her dog is actually playing with their dog in their backyard. They lead her to her dog and they are both happy to be reunited.")
    else:
        print ("She turns the corner and walks for a few minutes. Then she hears a bark for behind and turns around to see her dog running up to her. They are both happy to be reunited.")
print ("end game")
