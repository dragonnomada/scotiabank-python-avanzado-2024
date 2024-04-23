class Particle:

    def __init__(self, x, y, vel_ang):
        self.x = x
        self.y = y
        self.vel_ang = vel_ang

    def __str__(self):
        return "({:6.2f}, {:6.2f}) [{:6.2f}]".format(self.x, self.y, self.vel_ang)

class ParticleSimulator:

    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.000001
        nsteps = int(dt / timestep)

        for i in range(nsteps):
            for p in self.particles:

                r = (p.x ** 2 + p.y ** 2) ** 0.5

                vx = -p.y / r
                vy = p.x / r

                dx = timestep * p.vel_ang * vx
                dy = timestep * p.vel_ang * vy

                p.x += dx
                p.y += dy

def visualize(simulator):
    from matplotlib import pyplot as plt
    from matplotlib import animation

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)

    # It will be run when the animation starts
    def init():
        line.set_data([], [])
        return line, # The comma is important!

    def animate(i):
        # We let the particle evolve for 0.01 time units
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]
        line.set_data(X, Y)
        return line,

    # Call the animate function each 10 ms
    anim = animation.FuncAnimation(fig,
        animate, init_func=init, blit=True,
        interval=10)

    plt.show()

def test_1():
    p1 = Particle(2, 2, -1)
    p2 = Particle(1, 1, 10)

    sim = ParticleSimulator([p1, p2])
    
    sim.evolve(1)

def test_2():
    import random
    particles = []

    for i in range(10):
        p = Particle(random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-10, 10))
        particles.append(p)

    sim = ParticleSimulator(particles)
    
    sim.evolve(1)

# if __name__ == "__main__":
#     p1 = Particle(2, 2, -1)
#     p2 = Particle(1, 1, 10)

#     print(p1)
#     print(p2)

#     sim = ParticleSimulator([p1, p2])

#     sim.evolve(2)

#     print(p1)
#     print(p2)

#     visualize(sim)
