import time

import pygame
import math
import copy
from brain import Brain

ROT_ANGLE = 6
ACC = 3
MAX_VEL = 15
car_image = pygame.image.load("images/car.png")
START_POS = (800, 150)
MUTATION_RATE = 8
MAP = "images/easyTrack.png"
MAP_IMAGE = pygame.image.load(MAP)


def calcCounterClockwiseAngle(lineA, lineB):
    line1Y1 = lineA[0][1]
    line1X1 = lineA[0][0]
    line1Y2 = lineA[1][1]
    line1X2 = lineA[1][0]

    line2Y1 = lineB[0][1]
    line2X1 = lineB[0][0]
    line2Y2 = lineB[1][1]
    line2X2 = lineB[1][0]

    angle1 = math.atan2(line1Y1 - line1Y2, line1X1 - line1X2)
    angle2 = math.atan2(line2Y1 - line2Y2, line2X1 - line2X2)
    return (angle1 - angle2) * 360 / (2 * math.pi)


def calcClockwiseAngle(lineA, lineB):
    line1Y1 = lineA[0][1]
    line1X1 = lineA[0][0]
    line1Y2 = lineA[1][1]
    line1X2 = lineA[1][0]

    line2Y1 = lineB[0][1]
    line2X1 = lineB[0][0]
    line2Y2 = lineB[1][1]
    line2X2 = lineB[1][0]

    v1 = (line1X2 - line1X1, line1Y2 - line1Y1)
    v2 = (line2X2 - line2X1, line2Y2 - line2Y1)
    dotProduct = v1[0] * v2[0] + v1[1] * v2[1]
    crossProduct = v1[0] * v2[1] - v1[1] * v2[0]
    angle = math.atan2(abs(crossProduct), dotProduct) * 180 / math.pi
    if crossProduct < 0:
        angle = 360 - angle
    return angle


class Car(pygame.sprite.Sprite):
    def __init__(self, inputP, hddenP, outputP):
        pygame.sprite.Sprite.__init__(self)
        self.collision = False
        self.angle = 0
        self.original_image = car_image
        self.original_image = pygame.transform.scale(self.original_image, [40, 20])
        self.image = self.original_image
        self.rect = self.image.get_rect(center=START_POS)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = 0
        self.brain = Brain([inputP, hddenP, outputP])
        self.fitness = 0
        self.laps = 0
        self.previousAngle = 0
        self.aliveTime = 0
        self.direction = 1

    def update(self, window):
        if self.collision is False:
            self.trackCarProgress()
            self.rotate()
            predictions = self.feedBrain()
            self.brainDrive(predictions)

    def resetToDefault(self):
        self.collision = False
        self.angle = 0
        self.image = self.original_image
        self.rect = self.image.get_rect(center=START_POS)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = 0
        self.fitness = 0
        self.laps = 0
        self.previousAngle = 0
        self.aliveTime = 0
        self.direction = 1

    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, keyPressed):
        if self.collision is False:
            if keyPressed[pygame.K_a]:
                self.angle += ROT_ANGLE
            if keyPressed[pygame.K_d]:
                self.angle -= ROT_ANGLE
            if keyPressed[pygame.K_w]:
                if self.velocity < MAX_VEL:
                    self.velocity += ACC
                self.movePoints()
            else:
                if self.velocity > 0:
                    self.velocity -= 1
                self.movePoints()

    def movePoints(self):
        self.rect.centerx += math.cos(math.radians(360 - self.angle)) * self.velocity
        self.rect.centery += math.sin(math.radians(360 - self.angle)) * self.velocity

    def brainDrive(self, predictions):
        if self.collision is False:
            if predictions[0] > 0.4:
                self.angle += ROT_ANGLE
            if predictions[1] > 0.4:
                self.angle -= ROT_ANGLE
            if predictions[2] > 0.4:
                if self.velocity < MAX_VEL:
                    self.velocity += ACC
                self.movePoints()
            else:
                if self.velocity > 0:
                    self.velocity -= 1
                self.movePoints()

    def feedBrain(self):
        possibleCollisionsPoints = [
            self.calcDistance(self.findPossibleCollisionPoint(0)),
            self.calcDistance(self.findPossibleCollisionPoint(30)),
            self.calcDistance(self.findPossibleCollisionPoint(-30)),
            self.calcDistance(self.findPossibleCollisionPoint(90)),
            self.calcDistance(self.findPossibleCollisionPoint(-90))
        ]
        return self.brain.feedForward(possibleCollisionsPoints)

    def findPossibleCollisionPoint(self, angle):
        angle = self.angle + angle
        pointX = math.cos(math.radians(360 - angle)) * 10 + self.rect.centerx
        pointY = math.sin(math.radians(360 - angle)) * 10 + self.rect.centery
        while MAP_IMAGE.get_at((int(pointX), int(pointY))) != MAP_IMAGE.get_at((0, 0)):
            pointX += math.cos(math.radians(360 - angle)) * 10
            pointY += math.sin(math.radians(360 - angle)) * 10

        while MAP_IMAGE.get_at((int(pointX), int(pointY))) != (0, 0, 0, 0):
            pointX -= math.cos(math.radians(360 - angle)) * 1
            pointY -= math.sin(math.radians(360 - angle)) * 1

        return pointX, pointY

    def calcDistance(self, point):
        return math.sqrt(
            ((int(self.rect.centerx) - int(point[0])) ** 2) + ((int(self.rect.centery) - int(point[1])) ** 2))

    def trackCarProgress(self):
        reverseAngle = calcCounterClockwiseAngle(
            [[MAP_IMAGE.get_rect().centerx, MAP_IMAGE.get_rect().centery], list(START_POS)],
            [[MAP_IMAGE.get_rect().centerx, MAP_IMAGE.get_rect().centery],
             [self.rect.centerx, self.rect.centery]]) * (-1)
        if reverseAngle < 0 and self.previousAngle < 45:
            self.direction = -1

        actualAngle = calcClockwiseAngle(
            [[MAP_IMAGE.get_rect().centerx, MAP_IMAGE.get_rect().centery], list(START_POS)],
            [[MAP_IMAGE.get_rect().centerx, MAP_IMAGE.get_rect().centery],
             [self.rect.centerx, self.rect.centery]])

        if self.previousAngle > 350 and 360 - actualAngle > 10:
            self.laps += 1
        self.previousAngle = actualAngle

    def calculateFitness(self):
        self.fitness = (self.laps * 360 + self.previousAngle) * self.direction


class BG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.original_image = MAP_IMAGE
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(800, 510))
        self.mask = pygame.mask.from_surface(self.image)


def runGame(carsNum, neuronsNum):
    pygame.init()
    global MAP_IMAGE
    MAP_IMAGE = pygame.image.load(MAP)
    window = pygame.display.set_mode((1600, 1020))
    movingObjects = [Car(5, neuronsNum, 3) for _ in range(carsNum)]
    staticObjects = [BG()]
    static_sprites = pygame.sprite.Group(staticObjects)
    moving_objects_copy = list(movingObjects)
    moving_sprites = pygame.sprite.Group(moving_objects_copy)
    run = True
    genNumber = 1

    myFont = pygame.font.SysFont('Comic Sans MS', 30)
    angleTitle = myFont.render("Actual angle:", False, (0, 0, 0))
    lapsTitle = myFont.render("Laps:", False, (0, 0, 0))
    aliveTitle = myFont.render("Alive:", False, (0, 0, 0))
    instruction = myFont.render("Press n to generate new generation", False, (0, 0, 0))
    actualCar = myFont.render("Highlighted car stats", False, (0, 0, 0))
    clock = pygame.time.Clock()


    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return

        window.fill((0, 0, 0))
        static_sprites.draw(window)

        for car in moving_objects_copy:
            car.update(window)
            collide = pygame.sprite.spritecollide(car, static_sprites, False, pygame.sprite.collide_mask)
            if collide:
                car.collision = True
                car.enableLine = False
                moving_objects_copy.remove(car)

        pygame.draw.circle(window, (0, 255, 255), movingObjects[0].rect.center, 20)

        if pygame.key.get_pressed()[pygame.K_n]:
            for car in movingObjects:
                car.calculateFitness()
            moving_objects_copy = prepareNextGen(window, movingObjects)
            genNumber += 1

        moving_sprites.draw(window)

        angle = myFont.render(str(int(movingObjects[0].previousAngle)), False, (0, 0, 0))
        laps = myFont.render(str(movingObjects[0].laps), False, (0, 0, 0))
        alive = myFont.render(str(len(moving_objects_copy)), False, (0, 0, 0))
        genNum = myFont.render("Generation number: " + str(genNumber), False, (0, 0, 0))

        window.blit(angle, (870, 420))
        window.blit(laps, (870, 460))
        window.blit(alive, (870, 500))
        window.blit(angleTitle, (670, 420))
        window.blit(lapsTitle, (670, 460))
        window.blit(aliveTitle, (670, 500))
        window.blit(lapsTitle, (670, 460))
        window.blit(instruction, (550, 550))
        window.blit(actualCar, (635, 370))
        window.blit(genNum, (635, 600))
        pygame.display.update()


def prepareNextGen(window, moving_objects):
    moving_objects.sort(key=lambda car: car.fitness, reverse=True)
    pygame.draw.circle(window, (0, 255, 0), moving_objects[0].rect.center, 20)
    pygame.display.update()
    time.sleep(2)
    bestCar = moving_objects[0]
    for car in moving_objects[1:]:
        car.brain = copy.deepcopy(bestCar.brain)
        car.brain.mutate(MUTATION_RATE)
        car.resetToDefault()
    bestCar.resetToDefault()
    return list(moving_objects)


if __name__ == "__main__":
    runGame(50, 15)
