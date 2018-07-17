import bpy
import math
sce = bpy.context.scene
# number of uavs in our scene
number_of_uavs = 2
# treshold distance in centimeters
d_treshold = 250
# length of animations in frames
frames_count = 1080
# scale
scale = 1.0

for i in range(0, number_of_uavs-1):
    ob = bpy.data.objects['Sphere.00' + str(i)]
    for f in range(sce.frame_start, frames_count):
        if ((f-1) % 3 == 0):
            sce.frame_set(f)
            x = int(ob.matrix_world.to_translation().x*100 * scale)
            y = int(ob.matrix_world.to_translation().y*100 * scale)
            z = int(ob.matrix_world.to_translation().z*100 * scale)
            for k in range(i+1, number_of_uavs):
                if (k != i):
                    ob2 = bpy.data.objects['Sphere.00' + str(k)]
                    x2 = int(ob2.matrix_world.to_translation().x*100 * scale)
                    y2 = int(ob2.matrix_world.to_translation().y*100 * scale)
                    z2 = int(ob2.matrix_world.to_translation().z*100 * scale)
                    dx = x2 - x
                    dy = y2 - y
                    dz = z2 - z
                    d = math.sqrt(dx*dx + dy*dy + dz*dz)
                    if (d < d_treshold):
                        print("Danger! Distance = " + str(d) + " between " + str(i) + " and " + str(k) + " on " + str(f) + " frame")
