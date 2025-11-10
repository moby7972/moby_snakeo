def move_snake(snake):
    j = len(snake)
    while j > 0:
        for i in range(j-1):
            temp = snake[i]
            snake[i] = snake[i+1]
            snake[i+1] = temp
        j -= 1

snakey = [0, 1, 2, 3, 4, 8., 666, 642, 221, 74, 1, 9]
print (snakey)

move_snake(snakey)
print (snakey)