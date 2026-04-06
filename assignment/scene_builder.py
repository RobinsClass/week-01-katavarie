
#DIGM 131 - Assignment 1: Procedural Scene Builder


import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

#Create Sphere
building = cmds.polySphere(
    name="building_sphere",
    radius=3,
)[0]

cmds.move(3, building_height / 2.0, 3, building)

#Create Cylinder
building = cmds.polyCylinder(
    name="building_cylinder",
    radius=0.5,
    height=10,
)[0]

cmds.move(-5, 10 / 2.0, -10, building)

#Create Pyramid
building = cmds.polyPyramid(
    name="building_pyramid",
    sideLength=5,
    numberOfSides=3,
)[0]

cmds.move(-5, 12, -10, building)

#Create Torus
building = cmds.polyTorus(
    name="building_donut",
    heightBaseline=0,
    radius=5,
    sectionRadius=2,
    twist=10,
    subdivisionsAxis=20,
    subdivisionsHeight=20,
)[0]

cmds.move(3, 3, 3, building)


# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
