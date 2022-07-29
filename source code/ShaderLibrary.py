bl_info = {
    "name": "ShaderLibrary",
    "author": "Cyrese Mills",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

import bpy

class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shader Library"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Select a Shader to be addded ")
        row.operator("shader.diamond_operator")
        
class SHADER_OT_DIAMOND(bpy.types.Operator):
    bl_label = "Diamond"
    bl_idname = "shader.diamond_operator"
    
    def execute(self, context):
        
        material_diamond = bpy.data.materials.new(name = "Diamond")
        material_diamond.use_nodes = True
        material_output.location = (-400,0)
        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
        material_output=material_diamond.node_tree.nodes.get('Material Output')
        
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass1_node.location = (-600,0)
        
        glass1_node.inputs[0].default_value=(1, 0, 0, 1)
        
        glass1_node.inputs[2].default_value = 1.446
        
        
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass2_node.location = (-600,-300)
        
        glass2_node.inputs[0].default_value=(0, 0, 1, 1)
        
        glass2_node.inputs[2].default_value = 1.450
        
        
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass3_node.location = (-600,0)
        glass3_node.inputs[0].default_value=(1, 0, 0, 1)
        glass3_node.inputs[2].default_value = 1.446
        
        add1_node= material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add1_node.location = (-100,0)
        add1_node.label = "Add 2"
        add1_node.hide = True
        add1_node.select = False
        
        add2_node= material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add2_node.location = (-400,-50)
        add2_node.label = "Add 1"
        add2_node.hide = True
        add2_node.select = False
        
        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass4_node.location = (-150,-150)
        glass4_node.inputs[0].default_value=(1, 1, 1, 1)
        glass4_node.inputs[2].default_value = 1.450
        glass4_node.select = False
        
        mix1_node= material_diamond.node_tree.nodes.new('ShaderNodeMixShader')
        mix1_node.location = (200,0)
        mix1_node.select = False
        
        material_diamond.node_tree.links(glass1_node.outputs[0], add1_node.inputs[0])
        material_diamond.node_tree.links(glass2_node.outputs[0], add1_node.inputs[1])
        material_diamond.node_tree.links(add1_node.outputs[0], add2_node.inputs[0])
        material_diamond.node_tree.links(glass3_node.outputs[0], add2_node.inputs[1])
        material_diamond.node_tree.links(add2_node.outputs[0], mix1_node.inputs[1])
        material_diamond.node_tree.links(glass4_node.outputs[0], mix1_node.inputs[2])
        material_diamond.node_tree.links(mix1_node.outputs[0], material_output.inputs[0])
        
        bpy.context.object.active_material = material_diamond
        
        return {'FINISHED'}
        
def register():
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(SHADER_OT_DIAMOND)

def unregister():
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(SHADER_OT_DIAMOND)

if __name__ == "__main__":
    register()
