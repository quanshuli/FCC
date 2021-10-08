import copy
import random
# Consider using the modules imported above.

class Hat:
    balls = {}
    contents = []

    
    def __init__(self, **balls):
        if len(balls) < 1:
            return 'Not enough balls'
        else:
            self.balls = balls 

            for key, value in balls.items():
                if value > 0:
                    for i in range(value):
                        self.contents.append(key)
                     
            
    
    def draw(self, draws):
        if draws > len(self.contents):
            return self.contents
        
        num_draws = []
        ball_picked = []
        
        for i in range(draws):
            num_draws.append(random.randint(0, len(self.contents)-1))
        
        #print(num_draws)
        #print(self.contents)
                
        for i in range(draws):
            ball_picked.append(self.contents[num_draws[i]])
                    
        #print(ball_picked)
        return ball_picked
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #hat_loc = copy.deepcopy(hat)
    from collections import Counter 
    
    draw_result = []
    count = 0
    
    for i in range(10):
     
        draw_result = hat.draw(num_balls_drawn)  
        #print(draw_result)
        count_draw = dict(Counter(draw_result)) 
        comn_dict = count_draw.items() & expected_balls.items()
        #print(count_draw.items(),expected_balls.items())
        #print(comn_dict)
        
        if len(comn_dict) == len(expected_balls):
            count += 1
            
            
    return count / num_experiments
                    
        
'''                        
hat = Hat(red=3,blue=2)
print(hat.contents)

hat = Hat(blue=4, red=2, green=6)
#print(hat.draw(4))


probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
'''








































