'''
Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

The figure illustrates the rule used by the builders:
D:\my_python_journey\11_problem_based_on_these_topics\height of pyramid.png

Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

Test your code using the data we've provided.

Sample Data:
Expected Output:

6
The height of the pyramid: 3

20
The height of the pyramid: 5

1000
The height of the pyramid: 44

2
The height of the pyramid: 1
'''


blocks = int(input("Enter the number of blocks: "))
height = 0
blocks_for_next_layer = 1
while blocks >= blocks_for_next_layer:
    blocks -= blocks_for_next_layer
    height += 1
    blocks_for_next_layer += 1

print("The height of the pyramid:", height)