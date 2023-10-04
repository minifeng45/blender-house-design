import bpy
import bmesh

# House dimensions
length = 10
height = 3
width = 4
roof_height = 6  # Adjusted height

roof_width = 5
second_floor_height = 3  # Adjusted height
bathroom_length = 2
bathroom_width = 3.9

second_floor_length_offset = 0.7

room1_length = 2.72
room1_width = 3.9

room1_bathroom_gap = 0.3

room1_extension_length = 3
room1_extension_width = 1.5
third_floor_height = 2.7  # Adjusted height

chapel_offset = 1


# Create the existing cube
bpy.ops.mesh.primitive_cube_add(size=1, location=(width/2, length/2, height / 2))
cube = bpy.context.object
cube.scale.x = width
cube.scale.y = length
cube.scale.z = height
cube.name = "House_Cube"


# Create the existing cube
bpy.ops.mesh.primitive_cube_add(size=1, location=(width - bathroom_width/2 ,  room1_length+bathroom_length/2 + second_floor_length_offset + room1_bathroom_gap,  height + second_floor_height/2))
cube = bpy.context.object
cube.scale.x = bathroom_width
cube.scale.y = bathroom_length
cube.scale.z = second_floor_height
cube.name = "bathroom"

# Create the existing cube
bpy.ops.mesh.primitive_cube_add(size=1, location=(width - room1_width/2 , room1_length/2 + second_floor_length_offset,  height + second_floor_height/2))
cube = bpy.context.object
cube.scale.x = room1_width
cube.scale.y = room1_length
cube.scale.z = second_floor_height
cube.name = "room1"

# Create the existing cube
bpy.ops.mesh.primitive_cube_add(size=1, location=(room1_extension_width/2, room1_length+room1_extension_length/2 + second_floor_length_offset + room1_bathroom_gap,  height + second_floor_height  + third_floor_height/2))
cube = bpy.context.object
cube.scale.x = room1_extension_width
cube.scale.y = room1_extension_length
cube.scale.z = third_floor_height
cube.name = "room1_extension"


# Create the new cube on top with adjusted height
bpy.ops.mesh.primitive_cube_add(size=1, location=(roof_width/2, length/2, height + roof_height / 2))
roof = bpy.context.object
roof.scale.x = roof_width
roof.scale.y = length
roof.scale.z = roof_height
roof.name = "roof"


# Select the object you want to work with
roof = bpy.context.object 

# Assuming you have a specific vertex index you want to delete (e.g., vertex index 0)
vertex_index_to_delete = 0

# Switch to Edit Mode and create a Bmesh
bpy.ops.object.mode_set(mode='EDIT')
bm = bmesh.from_edit_mesh(roof.data)

# Deselect all vertices
for v in bm.verts:
    v.select = False

bm.verts.ensure_lookup_table()
# Get the vertex you want to dissolve
vertex_to_dissolve = bm.verts[5]
# Dissolve the selected vertex
bmesh.ops.dissolve_verts(bm, verts=[vertex_to_dissolve])

bm.verts.ensure_lookup_table()
# Get the vertex you want to dissolve
vertex_to_dissolve = bm.verts[6]
# Dissolve the selected vertex
bmesh.ops.dissolve_verts(bm, verts=[vertex_to_dissolve])

# Update the Bmesh and switch back to Object Mode
bmesh.update_edit_mesh(roof.data)
bpy.ops.object.mode_set(mode='OBJECT')

# Select the object (in this case, the "roof") you want to change the material of
obj = bpy.data.objects["roof"]

# Create a new material for the roof
roof_material = bpy.data.materials.new(name="Roof_Material")
roof_material.diffuse_color = (0.8, 0.2, 0.2, 1.0)  # Set the color to red (for example)
roof_material.specular_intensity = 0.5  # Adjust material properties as needed


# Assign the new material to the object
obj.data.materials.append(roof_material)

# Update the object to reflect the material changes
obj.data.update()

# Exit Edit Mode
#bpy.ops.object.mode_set(mode='OBJECT')
