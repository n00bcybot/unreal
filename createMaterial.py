import unreal

# Define the material name and folder path
asset_name = 'NewMaterial'
dest_path = '/Game/Materials'
material_path = dest_path + "/" + asset_name
texture_path = '/Game/Textures/bark07'

# Create new material - name, path, class, factory
new_mat = unreal.AssetToolsHelpers.get_asset_tools().create_asset(asset_name, dest_path, unreal.Material, unreal.MaterialFactoryNew())

# Load asset as object
texture = unreal.EditorAssetLibrary.load_asset(texture_path)

# Create texture sampler - point to material. Material expression is the actual node being created
texture_sampler = unreal.MaterialEditingLibrary.create_material_expression(new_mat, unreal.MaterialExpressionTextureSample, -200, -200)

# Connect texture to texture sampler
texture_sampler.texture = texture

# Connect texture sampler to base color of the material
unreal.MaterialEditingLibrary.connect_material_property(texture_sampler, 'RGB', unreal.MaterialProperty.MP_BASE_COLOR)

# Compile
unreal.MaterialEditingLibrary.recompile_material(new_mat)

# Save
unreal.EditorAssetLibrary.save_asset(material_path)
