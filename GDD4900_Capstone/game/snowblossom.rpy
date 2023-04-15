# Snow Blossom

init python:
    
    import random
    
    random.seed()
    
    def clamp(num, min_value, max_value):
        return max(min(num, max_value), min_value)

    #################################################################
    # Snow particles
    # ----------------
    def Snow(image, max_particles=50, speed=150, wind=100, gravity=100, xborder=(0,100), yborder=(50,400), start=50, **kwargs):
        """
        This creates the snow effect. You should use this function instead of instancing
        the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
        using the default values =D)
        
        @parm {image} image:
            The image used as the snowflakes. This should always be a image file or an im object,
            since we'll apply im transformations in it.
        
        @parm {int} max_particles:
            The maximum number of particles at once in the screen.
            
        @parm {float} speed:
            The base vertical speed of the particles. The higher the value, the faster particles will fall.
            Values below 1 will be changed to 1
            
        @parm {float} wind:
            The max wind force that'll be applyed to the particles.
            
        @parm {Tuple ({int} min, {int} max)} xborder:
            The horizontal border range. A random value between those two will be applyed when creating particles.
            
        @parm {Tuple ({int} min, {int} max)} yborder:
            The vertical border range. A random value between those two will be applyed when creating particles.
            The higher the values, the fartest from the screen they will be created.

        @parm {int} start:
            The number of particles to start with on screen so the don't all start from the top of the screen
            only new particles after the scene starts will be added from the top/sides/etc.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, gravity, xborder, yborder, start, **kwargs))
    
    # ---------------------------------------------------------------
    class SnowFactory(object):
        """
        The factory that creates the particles we use in the snow effect.
        """
        def __init__(self, image, max_particles, speed, wind, gravity, xborder, yborder, start, **kwargs):
            """
            Initialize the factory. Parameters are the same as the Snow function.
            """            
            self.max_particles = max_particles
            
            self.speed = speed
            self.gravity = gravity
            
            self.wind = wind
            
            self.xborder = xborder
            self.yborder = yborder
            
            self.depth = kwargs.get("depth", 10)
            
            self.image = self.image_init(image)

            self.start = start
            

        def create(self, particles, st):
            """
            This is internally called every frame by the Particles object to create new particles.
            We'll just create new particles if the number of particles on the screen is
            lower than the max number of particles we can have.
            """

            # If this is the first time create is called, create a bunch of particles
            if particles is None or len(particles) == 0:

                particles = []
                
                for i in range(0, self.start):
                
                    depth = random.randint(1, self.depth)
                    
                    depth_speed = 1.5-depth/(self.depth+0.0)                    #print("adding a particle")
                    particles.append( SnowParticle(self.image[depth-1],      # the image used by the particle 
                                        random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                        self.speed*depth_speed,
                                        self.gravity,  # the vertical speed of the particle
                                        random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                        -random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                        ) )
                return particles

            # If this is not the first time create is called, just create the max particles
            elif len(particles) < self.max_particles:
                
                depth = random.randint(1, self.depth)
                
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # the image used by the particle 
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                      self.speed*depth_speed,
                                      self.gravity,  # the vertical speed of the particle
                                      random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                      random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                      ) ]
        
        
        def image_init(self, image):
            """
            This is called internally to initialize the images.
            will create a list of images with different sizes, so we
            can predict them all and use the cached versions to make it more memory efficient.            
            """
            rv = [ ]
            
            for depth in range(self.depth):
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv
        
        
        def predict(self):
            """
            This is called internally by the Particles object to predict the images the particles
            are using. It's expected to return a list of images to predict.
            """ 
            return self.image
            
    # ---------------------------------------------------------------
    class SnowParticle(object):
        """
        Represents every particle in the screen.
        """
        def __init__(self, image, wind, speed, gravity, xborder, yborder):
            """
            Initializes the snow particle. This is called automatically when the object is created.
            """
            
            self.image = image
            
            if speed <= 0:
                speed = 1
                
            self.wind = wind
            
            self.speed = speed
            self.gravity = gravity

            self.oldst = None

            # Set up the random movement for dust particles
            self.velocity = [random.uniform(-self.speed, self.speed), random.uniform(-self.speed, self.speed)]
            self.counter = random.uniform(20, 100)
            #print(self.velocity, self.counter)

            #print("xborder", xborder, "yborder", yborder)
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            """
            Called internally in every frame to update the particle.
            """
            
            # calculate lag
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            self.xpos += lag * (self.wind + self.velocity[0])
            self.ypos += lag * (self.gravity + self.velocity[1])
            self.counter -= 1
            #print(self.counter)
            scale = .50
            counterMin = 10
            if self.counter <= counterMin:
                self.velocity[0] += random.uniform(-self.speed * scale, self.speed * scale)
                self.velocity[0] = clamp(self.velocity[0], -self.speed, self.speed)
                self.velocity[1] += random.uniform(-self.speed * scale, self.speed * scale)
                self.velocity[1] = clamp(self.velocity[1], -self.speed, self.speed)
                self.counter = random.uniform(counterMin, 50)
                #print(self.velocity, self.counter)
               
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                return None
                
            return int(self.xpos), int(self.ypos), st, self.image