def perimeter(s1,s2,s3):
    return s1+s2+s3 if s1>0 and s2>0 and s3>0 and s1+s2>s3 and s2+s3>s1 and s1+s3>s2 else None



#role 1+2 - represent object and its behaviors
class Triangle:

    def create(s1,s2,s3):
        t=Triangle()
        t.s1=s1
        t.s2=s2
        t.s3=s3
        t.validate() #Triangle.validate(t)
        return t
        
    def validate(self):
        self.valid= self.s1>0 and self.s2>0 and self.s3>0 and self.s1+self.s2>self.s3 and self.s1+self.s3>self.s2 and self.s2+self.s3>self.s1
        
    def is_valid(self):
        return isinstance(self,Triangle) and self.valid
    
    def perimeter(self):
        return self.s1+self.s2+self.s3 if self.is_valid() else None
    
    def info(self):
        if self.is_valid():
            return f'Triangle<{self.s1},{self.s2},{self.s3}>'
        else:
            return '<invalid triangle>'
        
    def draw(self,surface):
        if self.is_valid():
            print(f'{Triangle.info(self)} drawn on {surface}')
