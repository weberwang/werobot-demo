#coding='utf-8'
import werobot
robot = werobot.WeRoBot(token='gI2fYZGM2IUJ10a')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.run(port=9527)