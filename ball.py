import helper

class Ball():
    def __init__(self, pong):
        self.radius  = 5
        self.dt = pong.dt
        self.minX    = self.radius;
        self.maxX    = pong.width - self.radius
        self.minY    = pong.wall_width + self.radius
        self.maxY    = pong.height - pong.wall_width - self.radius
        self.speed   = (self.maxX - self.minX) / 4;
        self.accel   = 8;

    def update(self, left_pad, right_pad):

        pos = helper.accelerate(self.x, self.y, 
                            self.dx, self.dy, 
                            self.accel, self.dt);

        if ((pos.dy > 0) and (pos.y > self.maxY)):
            pos.y = self.maxY
            pos.dy = -pos.dy
        elif ((pos.dy < 0) and (pos.y < self.minY)):
            pos.y = self.minY
            pos.dy = -pos.dy

        paddle = left_pad if (pos.dx < 0) else right_pad;
        pt = helper.ballIntercept(self, paddle, pos.nx, pos.ny);

        if pt:
            if pt.d == 'left' or pt.d == 'right':
                pos.x = pt.x
                pos.dx = -pos.dx
            elif pt.d == 'top' or pt.d == 'bottom':
                pos.y = pt.y
                pos.dy = -pos.dy

        if paddle.up:
            pos.dy = pos.dy * (0.5 if pos.dy < 0 else 1.5)
        elif paddle.down:
          pos.dy = pos.dy * (0.5 if pos.dy > 0 else 1.5)

        self.set_position(pos.x,  pos.y);
        self.set_direction(pos.dx, pos.dy);

