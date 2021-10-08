class Rectangle():
    width = 0
    height = 0
    
    def __init__(self, width, height):
        '''
        if type(width) == str:
            width = float(width.split('=')[2])
        
        if type(height) == str:
            height = float(height.split('=')[2])
        '''
        self.width = width
        self.height = height
        
    def __repr__(self):
        return 'Rectangle(width=' + str(self.width) \
                + ', height=' + str(self.height) + ')'
                
    def set_width(self, width):
        self.width = width
        
        
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height 
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ''
            
            
            for i in range(self.height):
                picture += '*' * self.width + '\n'
            
            return picture 
        
    def get_amount_inside(self,obj):
        fits = int(self.width / obj.width) * int(self.height / obj.height)
        
        return fits
            
        
class Square(Rectangle):
    side = 0
    
    def __init__(self, side):           
        self.side = side
        self.width = side
        self.height = side
        
    def __repr__(self):
        return 'Square(side=' + str(self.side) +')' 
        
    def set_side(self, side):            
        self.side = side
        self.width = side
        self.height = side
            
    def set_width(self, width):
        self.width = width
        self.heitht = width
        self.side = width
        
        
    def set_height(self, height):
        self.height = height
        self.width = height
        self.side = height
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        