def draw_compact_architecture_diagram():
    diagram = """
    +-------------------------+
    |    User Interface       |
    +-------------+-----------+
                  |
    +-------------v-----------+   +-------------------+
    | Define Total Network   |   | Assign Cloud      |
    | Camera                |---| Instances         |
    +------------------------+   +-------------------+
                  |                         |
    +-------------v-----------+             |
    | Calculate Low Cost     |             |
    | Cloud                   |             |
    +------------------------+             |
                  |                         |
    +-------------------------+            |
    | Run Simulation         |            |
    +-------------+-----------+            |
                  |                         |
    +-------------v-----------+            |
    | Start Video Analysis   |            |
    +------------------------+            |
                  |                         |
    +-------------------------+            |
    | Start Simulation       |            |
    +-------------+-----------+            |
                  |                         |
    +-------------------------+            |
    | Cost Graph              |            |
    +-------------+-----------+            |
                  |                         |
    +-------------------------+            |
    | Frames Folder           |            |
    +-------------+-----------+            |
                  |                         |
    +-------------------------+            |
    | Adaptive Resource      |            |
    | Management              |            |
    +-------------------------+            |
    """

    print(diagram)

# Call the function to draw the compact architecture diagram
draw_compact_architecture_diagram()
