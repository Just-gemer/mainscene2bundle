# mainscene2bundle 1.0 by Just gemer, credits:augustodoidin
# Original idea: Rama
import os, json, pathlib, subprocess, shutil
from random import randint
# enter info....
print('mainscene2bundle by Just gemer')
mapname = str(input('MapName?: '))
coachnum = int(input('Coach Count?: '))
mapnamelow=mapname.lower()
# making directories (credits:augstodoidin)
output = (os.getcwd() + "\\output\\" + mapnamelow + "_pc")
#Cache Folder
cache_path = (output + "\\cache\\itf_cooked\\pc\\world\\maps\\" + mapnamelow + "\\")
os.makedirs(cache_path, exist_ok=True)
cache_audio = (cache_path + "audio\\")
os.makedirs(cache_audio, exist_ok=True)
cache_amb = (cache_path + "audio\\amb")
os.makedirs(cache_amb, exist_ok=True)
cache_autodance = (cache_path + "autodance\\")
os.makedirs(cache_autodance, exist_ok=True)
cache_cinematics = (cache_path + "cinematics\\")
os.makedirs(cache_cinematics, exist_ok=True)
cache_graph = (cache_path + "graph\\")
os.makedirs(cache_graph, exist_ok=True)
cache_menuart = (cache_path + "menuart\\")
cache_tex_menuart = (cache_path + "menuart\\textures\\")
os.makedirs(cache_tex_menuart, exist_ok=True)
cache_act_menuart = (cache_path + "menuart\\actors\\")
os.makedirs(cache_act_menuart, exist_ok=True)
cache_timeline = (cache_path + "timeline\\")
cache_pictos = (cache_path + "timeline\\pictos\\")
os.makedirs(cache_pictos, exist_ok=True)
cache_videoscoach = (cache_path + "videoscoach\\")
os.makedirs(cache_videoscoach, exist_ok=True)
#Cache Folder

#World Folder
world_path = (output + "\\world\\maps\\" + mapnamelow + "\\")
os.makedirs(world_path, exist_ok=True)
world_audio = (world_path + "audio\\")
os.makedirs(world_audio, exist_ok=True)
world_autodance = (world_path + "autodance\\") 
os.makedirs(world_autodance, exist_ok=True)
world_moves = (world_path + "timeline\\moves\\wiiu\\")
os.makedirs(world_moves, exist_ok=True)
world_videoscoach = (world_path + "videoscoach\\")
os.makedirs(world_videoscoach, exist_ok=True)
#World Folder
# writing files (credits:augstodoidin)
stapefile = open(cache_audio + mapname.lower() + ".stape.ckd", "w", encoding="utf-8")
stapefile.write('{"__class":"Tape","Clips":[],"TapeClock":0,"TapeBarCount":1,"FreeResourcesAfterPlay":0,"MapName":"' + mapname + '"}')
stapefile.close()
##

##
audioisc = open(cache_audio + mapname.lower() + "_audio.isc.ckd", "w", encoding="utf-8")
audioisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_musictrack.tpl">
            <COMPONENTS NAME="MusicTrackComponent">
                <MusicTrackComponent />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_sequence.tpl">
            <COMPONENTS NAME="TapeCase_Component">
                <TapeCase_Component />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>
''')
audioisc.close()
##

##
audiosequence = open(cache_audio + mapname.lower() + "_sequence.tpl.ckd", "w", encoding="utf-8")
audiosequence.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"TapeCase_Template","TapesRack":[{"__class":"TapeGroup","Entries":[{"__class":"TapeEntry","Label":"TML_Sequence","Path":"world/maps/' + mapname.lower() + '/audio/' + mapname.lower() + '.stape"}]}]}]}')
audiosequence.close()
##

#Cinematic Files
##
cinetape = open(cache_cinematics + mapname.lower() + "_mainsequence.tape.ckd", "w", encoding="utf-8")
cinetape.write('{"__class":"Tape","Clips":[],"TapeClock":0,"TapeBarCount":1,"FreeResourcesAfterPlay":0,"MapName":"' + mapname + '"}')
cinetape.close()
##

##
cineisc = open(cache_cinematics + mapname.lower() + "_cine.isc.ckd", "w", encoding="utf-8")
cineisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/cinematics/''' + mapname.lower() + '''_mainsequence.tpl">
            <COMPONENTS NAME="MasterTape">
                <MasterTape />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>''')
cineisc.close()
##

##
cinesequence = open(cache_cinematics + mapname.lower() + "_mainsequence.tpl.ckd", "w", encoding="utf-8")
cinesequence.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"MasterTape_Template","TapesRack":[{"__class":"TapeGroup","Entries":[{"__class":"TapeEntry","Label":"master","Path":"world/maps/' + mapname.lower() + '/cinematics/' + mapname.lower() + '_mainsequence.tape"}]}]}]}')
cinesequence.close()
##

#GraphFile
graphisc = open(cache_graph + mapname.lower() + "_graph.isc.ckd", "w", encoding="utf-8")
graphisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>''')
graphisc.close()
#GraphFile

#Menuart ISC
menuartisc = open(cache_menuart + mapname.lower() + "_menuart.isc.ckd", "w", encoding="utf-8")
menuartisc_content = ""
if(coachnum == 1):
   menuartisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>''')
if(coachnum == 2):
    menuartisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_2" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>''')
if(coachnum == 3):
    menuartisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_2" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_3" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>''')
if(coachnum == 4):
    menuartisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_2" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_3" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_4" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="6" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_4.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="6" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
            <COMPONENTS NAME="MaterialGraphicComponent">
                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </MaterialGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>''')
menuartisc.write(menuartisc_content)
menuartisc.close()
#Menuart ISC

#Timeline Files
##
timelineisc = open(cache_timeline + mapname.lower() + "_tml.isc.ckd", "w", encoding="utf-8")
timelineisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_dance.tpl">
            <COMPONENTS NAME="TapeCase_Component">
                <TapeCase_Component />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_karaoke.tpl">
            <COMPONENTS NAME="TapeCase_Component">
                <TapeCase_Component />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>''')
timelineisc.close()
##

##
dancetape = open(cache_timeline + mapname.lower() + "_tml_dance.tpl.ckd", "w", encoding="utf-8")
dancetape.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"TapeCase_Template","TapesRack":[{"__class":"TapeGroup","Entries":[{"__class":"TapeEntry","Label":"TML_Motion","Path":"world/maps/' + mapname.lower() + '/timeline/' + mapname.lower() + '_tml_dance.dtape"}]}]}]}')
dancetape.close()
##

##
karaoketape = open(cache_timeline + mapname.lower() + "_tml_karaoke.tpl.ckd", "w", encoding="utf-8")
karaoketape.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"TapeCase_Template","TapesRack":[{"__class":"TapeGroup","Entries":[{"__class":"TapeEntry","Label":"TML_karaoke","Path":"world/maps/' + mapname.lower() + '/timeline/' + mapname.lower() + '_tml_karaoke.ktape"}]}]}]}')
karaoketape.close()
##
#Timeline Files

#VideosCoach ISC
videoisc = open(cache_videoscoach + mapname.lower() + "_video.isc.ckd", "w", encoding="utf-8")
videoisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
            <COMPONENTS NAME="PleoComponent">
                <PleoComponent video="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.webm" dashMPD="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.mpd" channelID="" />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
            <COMPONENTS NAME="PleoTextureGraphicComponent">
                <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                    <PrimitiveParameters>
                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                        </GFXPrimitiveParam>
                    </PrimitiveParameters>
                    <ENUM NAME="anchor" SEL="1" />
                    <material>
                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                            <textureSet>
                                <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                            </textureSet>
                            <materialParams>
                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                            </materialParams>
                        </GFXMaterialSerializable>
                    </material>
                    <ENUM NAME="oldAnchor" SEL="1" />
                </PleoTextureGraphicComponent>
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>''')
videoisc.close()
#VideosCoach ISC

#MAINSCENE ISC
#MAINSCENE ISC
#MAINSCENE ISC
mainsceneisc = open(cache_path + mapname.lower() + "_main_scene.isc.ckd", "w", encoding="utf-8")
mainsceneisc_content = ""
if(coachnum == 1):
   mainsceneisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="2.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <PLATFORM_FILTER>
        <TargetFilterList platform="WII">
            <objects VAL="''' + mapname + '''_AUTODANCE" />
        </TargetFilterList>
    </PLATFORM_FILTER>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_AUDIO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_audio.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_musictrack.tpl">
                            <COMPONENTS NAME="MusicTrackComponent">
                                <MusicTrackComponent />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_sequence.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_CINE" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/cinematics/''' + mapname.lower() + '''_cine.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/cinematics/''' + mapname.lower() + '''_mainsequence.tpl">
                            <COMPONENTS NAME="MasterTape">
                                <MasterTape />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_GRAPH" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/graph/''' + mapname.lower() + '''_graph.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_TML" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_dance.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_karaoke.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_VIDEO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''_video.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
                            <COMPONENTS NAME="PleoComponent">
                                <PleoComponent video="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.webm" dashMPD="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.mpd" channelID="" />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
                            <COMPONENTS NAME="PleoTextureGraphicComponent">
                                <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </PleoTextureGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + ''' : Template Artist - Template Title&#10;JDVer = 5, ID = 842776738, Type = 1 (Flags 0x00000000), NbCoach = 2, Difficulty = 2" MARKER="" POS2D="-3.531976 -1.485322" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/songdesc.tpl">
            <COMPONENTS NAME="JD_SongDescComponent">
                <JD_SongDescComponent />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_menuart" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/menuart/''' + mapname.lower() + '''_menuart.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="3" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_AUTODANCE" MARKER="" POS2D="0.000000 -0.033823" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/autodance/''' + mapname.lower() + '''_autodance.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/autodance/''' + mapname.lower() + '''_autodance.tpl">
                            <COMPONENTS NAME="JD_AutodanceComponent">
                                <JD_AutodanceComponent />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0">
            <sceneConfigs NAME="JD_MapSceneConfig">
                <JD_MapSceneConfig name="" soundContext="" hud="0" phoneTitleLocId="4294967295" phoneImage="">
                    <ENUM NAME="Pause_Level" SEL="6" />
                    <ENUM NAME="type" SEL="1" />
                    <ENUM NAME="musicscore" SEL="2" />
                </JD_MapSceneConfig>
            </sceneConfigs>
        </SceneConfigs>
    </sceneConfigs>
</Scene>
</root>''')
if(coachnum == 2):
    mainsceneisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="2.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <PLATFORM_FILTER>
        <TargetFilterList platform="WII">
            <objects VAL="''' + mapname + '''_AUTODANCE" />
        </TargetFilterList>
    </PLATFORM_FILTER>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_AUDIO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_audio.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_musictrack.tpl">
                            <COMPONENTS NAME="MusicTrackComponent">
                                <MusicTrackComponent />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_sequence.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_CINE" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/cinematics/''' + mapname.lower() + '''_cine.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/cinematics/''' + mapname.lower() + '''_mainsequence.tpl">
                            <COMPONENTS NAME="MasterTape">
                                <MasterTape />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_GRAPH" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/graph/''' + mapname.lower() + '''_graph.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_TML" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_dance.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_karaoke.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_VIDEO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''_video.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
                            <COMPONENTS NAME="PleoComponent">
                                <PleoComponent video="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.webm" dashMPD="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.mpd" channelID="" />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
                            <COMPONENTS NAME="PleoTextureGraphicComponent">
                                <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </PleoTextureGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + ''' : Template Artist - Template Title&#10;JDVer = 5, ID = 842776738, Type = 1 (Flags 0x00000000), NbCoach = 2, Difficulty = 2" MARKER="" POS2D="-3.531976 -1.485322" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/songdesc.tpl">
            <COMPONENTS NAME="JD_SongDescComponent">
                <JD_SongDescComponent />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_menuart" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/menuart/''' + mapname.lower() + '''_menuart.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="3" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_2" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_AUTODANCE" MARKER="" POS2D="0.000000 -0.033823" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/autodance/''' + mapname.lower() + '''_autodance.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/autodance/''' + mapname.lower() + '''_autodance.tpl">
                            <COMPONENTS NAME="JD_AutodanceComponent">
                                <JD_AutodanceComponent />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0">
            <sceneConfigs NAME="JD_MapSceneConfig">
                <JD_MapSceneConfig name="" soundContext="" hud="0" phoneTitleLocId="4294967295" phoneImage="">
                    <ENUM NAME="Pause_Level" SEL="6" />
                    <ENUM NAME="type" SEL="1" />
                    <ENUM NAME="musicscore" SEL="2" />
                </JD_MapSceneConfig>
            </sceneConfigs>
        </SceneConfigs>
    </sceneConfigs>
</Scene>
</root>''')
if(coachnum == 3):
    mainsceneisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="2.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <PLATFORM_FILTER>
        <TargetFilterList platform="WII">
            <objects VAL="''' + mapname + '''_AUTODANCE" />
        </TargetFilterList>
    </PLATFORM_FILTER>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_AUDIO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_audio.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_musictrack.tpl">
                            <COMPONENTS NAME="MusicTrackComponent">
                                <MusicTrackComponent />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_sequence.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_CINE" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/cinematics/''' + mapname.lower() + '''_cine.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/cinematics/''' + mapname.lower() + '''_mainsequence.tpl">
                            <COMPONENTS NAME="MasterTape">
                                <MasterTape />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_GRAPH" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/graph/''' + mapname.lower() + '''_graph.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_TML" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_dance.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_karaoke.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_VIDEO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''_video.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
                            <COMPONENTS NAME="PleoComponent">
                                <PleoComponent video="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.webm" dashMPD="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.mpd" channelID="" />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
                            <COMPONENTS NAME="PleoTextureGraphicComponent">
                                <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </PleoTextureGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + ''' : Template Artist - Template Title&#10;JDVer = 5, ID = 842776738, Type = 1 (Flags 0x00000000), NbCoach = 2, Difficulty = 2" MARKER="" POS2D="-3.531976 -1.485322" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/songdesc.tpl">
            <COMPONENTS NAME="JD_SongDescComponent">
                <JD_SongDescComponent />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_menuart" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/menuart/''' + mapname.lower() + '''_menuart.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="3" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_2" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_3" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_AUTODANCE" MARKER="" POS2D="0.000000 -0.033823" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/autodance/''' + mapname.lower() + '''_autodance.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/autodance/''' + mapname.lower() + '''_autodance.tpl">
                            <COMPONENTS NAME="JD_AutodanceComponent">
                                <JD_AutodanceComponent />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0">
            <sceneConfigs NAME="JD_MapSceneConfig">
                <JD_MapSceneConfig name="" soundContext="" hud="0" phoneTitleLocId="4294967295" phoneImage="">
                    <ENUM NAME="Pause_Level" SEL="6" />
                    <ENUM NAME="type" SEL="1" />
                    <ENUM NAME="musicscore" SEL="2" />
                </JD_MapSceneConfig>
            </sceneConfigs>
        </SceneConfigs>
    </sceneConfigs>
</Scene>
</root>''')
if(coachnum == 4):
    mainsceneisc_content = ('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="2.000000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <PLATFORM_FILTER>
        <TargetFilterList platform="WII">
            <objects VAL="''' + mapname + '''_AUTODANCE" />
        </TargetFilterList>
    </PLATFORM_FILTER>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_AUDIO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_audio.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="MusicTrack" MARKER="" POS2D="1.125962 -0.418641" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_musictrack.tpl">
                            <COMPONENTS NAME="MusicTrackComponent">
                                <MusicTrackComponent />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_sequence" MARKER="" POS2D="-0.006158 -0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/audio/''' + mapname.lower() + '''_sequence.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_CINE" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/cinematics/''' + mapname.lower() + '''_cine.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_MainSequence" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/cinematics/''' + mapname.lower() + '''_mainsequence.tpl">
                            <COMPONENTS NAME="MasterTape">
                                <MasterTape />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_GRAPH" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/graph/''' + mapname.lower() + '''_graph.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="10.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="Camera_JD_Dummy" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_emptyactor.tpl" />
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_TML" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_dance" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_dance.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000001" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_tml_karaoke" MARKER="" POS2D="-1.157740 0.006158" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/timeline/''' + mapname.lower() + '''_tml_karaoke.tpl">
                            <COMPONENTS NAME="TapeCase_Component">
                                <TapeCase_Component />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_VIDEO" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''_video.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="-1.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="VideoScreen" MARKER="" POS2D="0.000000 -4.500000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_player_main.tpl">
                            <COMPONENTS NAME="PleoComponent">
                                <PleoComponent video="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.webm" dashMPD="world/maps/''' + mapname.lower() + '''/videoscoach/''' + mapname.lower() + '''.mpd" channelID="" />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="3.941238 2.220000" xFLIPPED="0" USERFRIENDLY="VideoOutput" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/_common/videoscreen/video_output_main.tpl">
                            <COMPONENTS NAME="PleoTextureGraphicComponent">
                                <PleoTextureGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000" channelID="">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/pleofullscreen.msh" stencilTest="0" alphaTest="0" alphaRef="0">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </PleoTextureGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + ''' : Template Artist - Template Title&#10;JDVer = 5, ID = 842776738, Type = 1 (Flags 0x00000000), NbCoach = 2, Difficulty = 2" MARKER="" POS2D="-3.531976 -1.485322" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/songdesc.tpl">
            <COMPONENTS NAME="JD_SongDescComponent">
                <JD_SongDescComponent />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_menuart" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/menuart/''' + mapname.lower() + '''_menuart.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="3" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="1">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_generic" MARKER="" POS2D="266.087555 197.629959" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_generic.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_online" MARKER="" POS2D="-150.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_online.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumcoach" MARKER="" POS2D="738.106323 359.612030" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumcoach.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.300000 0.300000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_cover_albumbkg" MARKER="" POS2D="1067.972168 201.986328" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha_mul_b.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_cover_albumbkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="world/ui/textures/mask_square.tga" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_1" MARKER="" POS2D="212.784500 663.680176" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_1.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_2" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_2.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_3" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_3.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="0.290211 0.290211" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_coach_4" MARKER="" POS2D="524.381104 670.829834" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="4294967295" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="6" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/ui/materials/alpha.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_coach_4.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="6" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="256.000000 128.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_banner_bkg" MARKER="" POS2D="1487.410156 -32.732918" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/tpl_materialgraphiccomponent2d.tpl">
                            <COMPONENTS NAME="MaterialGraphicComponent">
                                <MaterialGraphicComponent colorComputerTagId="0" renderInTarget="0" disableLight="0" disableShadow="1" AtlasIndex="0" customAnchor="0.000000 0.000000" SinusAmplitude="0.000000 0.000000 0.000000" SinusSpeed="1.000000" AngleX="0.000000" AngleY="0.000000">
                                    <PrimitiveParameters>
                                        <GFXPrimitiveParam colorFactor="1.000000 1.000000 1.000000 1.000000">
                                            <ENUM NAME="gfxOccludeInfo" SEL="0" />
                                        </GFXPrimitiveParam>
                                    </PrimitiveParameters>
                                    <ENUM NAME="anchor" SEL="1" />
                                    <material>
                                        <GFXMaterialSerializable ATL_Channel="0" ATL_Path="" shaderPath="world/_common/matshader/multitexture_1layer.msh" stencilTest="0" alphaTest="4294967295" alphaRef="4294967295">
                                            <textureSet>
                                                <GFXMaterialTexturePathSet diffuse="world/maps/''' + mapname.lower() + '''/menuart/textures/''' + mapname.lower() + '''_banner_bkg.tga" back_light="" normal="" separateAlpha="" diffuse_2="" back_light_2="" anim_impostor="" diffuse_3="" diffuse_4="" />
                                            </textureSet>
                                            <materialParams>
                                                <GFXMaterialSerializableParam Reflector_factor="0.000000" />
                                            </materialParams>
                                        </GFXMaterialSerializable>
                                    </material>
                                    <ENUM NAME="oldAnchor" SEL="1" />
                                </MaterialGraphicComponent>
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <ACTORS NAME="SubSceneActor">
        <SubSceneActor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_AUTODANCE" MARKER="" POS2D="0.000000 -0.033823" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="enginedata/actortemplates/subscene.tpl" RELATIVEPATH="world/maps/''' + mapname.lower() + '''/autodance/''' + mapname.lower() + '''_autodance.isc" EMBED_SCENE="1" IS_SINGLE_PIECE="0" ZFORCED="1" DIRECT_PICKING="1" IGNORE_SAVE="0">
            <ENUM NAME="viewType" SEL="2" />
            <SCENE>
                <Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
                    <ACTORS NAME="Actor">
                        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/autodance/''' + mapname.lower() + '''_autodance.tpl">
                            <COMPONENTS NAME="JD_AutodanceComponent">
                                <JD_AutodanceComponent />
                            </COMPONENTS>
                        </Actor>
                    </ACTORS>
                    <sceneConfigs>
                        <SceneConfigs activeSceneConfig="0" />
                    </sceneConfigs>
                </Scene>
            </SCENE>
        </SubSceneActor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0">
            <sceneConfigs NAME="JD_MapSceneConfig">
                <JD_MapSceneConfig name="" soundContext="" hud="0" phoneTitleLocId="4294967295" phoneImage="">
                    <ENUM NAME="Pause_Level" SEL="6" />
                    <ENUM NAME="type" SEL="1" />
                    <ENUM NAME="musicscore" SEL="2" />
                </JD_MapSceneConfig>
            </sceneConfigs>
        </SceneConfigs>
    </sceneConfigs>
</Scene>
</root>''')
mainsceneisc.write(mainsceneisc_content)
mainsceneisc.close()
#MAINSCENE ISC
#MAINSCENE ISC
#MAINSCENE ISC

#MAINSCENE SGS
#MAINSCENE SGS
#MAINSCENE SGS
mainscenesgs = open(cache_path + mapname.lower() + "_main_scene.sgs.ckd", "w", encoding="utf-8")
mainscenesgs.write('S{"settings":{"__class":"JD_MapSceneConfig","Pause_Level":6,"name":"","type":1,"musicscore":2,"soundContext":"","hud":0,"phoneTitleLocId":4294967295,"phoneImage":""}}')
mainscenesgs.close()
#MAINSCENE SGS
#MAINSCENE SGS
#MAINSCENE SGS

#AutoDance Files
##
autodancetpl = open(cache_autodance + mapname.lower() + "_autodance.tpl.ckd", "w", encoding="utf-8")
autodancetpl.write('{"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"JD_AutodanceComponent_Template","song":"' + mapname + '","autodanceData":{"__class":"JD_AutodanceData","recording_structure":{"__class":"JD_AutodanceRecordingStructure","records":[{"__class":"Record","Start":88,"Duration":16},{"__class":"Record","Start":136,"Duration":8},{"__class":"Record","Start":188,"Duration":8},{"__class":"Record","Start":252,"Duration":16}]},"video_structure":{"__class":"JD_AutodanceVideoStructure","SongStartPosition":244,"Duration":32,"ThumbnailTime":0,"FadeOutDuration":3,"GroundPlanePath":"invalid ","FirstLayerTripleBackgroundPath":"invalid ","SecondLayerTripleBackgroundPath":"invalid ","ThirdLayerTripleBackgroundPath":"invalid ","playback_events":[{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":244,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":245,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":246,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":247,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":3,"StartTime":248,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":3,"StartTime":248.500000,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":3,"StartTime":249,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":3,"StartTime":249.500000,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":0,"StartTime":250,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":1,"StartTime":251,"Duration":1,"Speed":4},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":5,"StartTime":252,"Duration":1,"Speed":1.500000},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":5,"StartTime":253,"Duration":1,"Speed":1.500000},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":254,"Duration":2,"Speed":1.800000},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":256,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":256.500000,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":257,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":257.500000,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":6,"StartTime":258,"Duration":0.500000,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":7,"StartTime":258.500000,"Duration":1.500000,"Speed":1.500000},{"__class":"PlaybackEvent","ClipNumber":2,"StartClip":0,"StartTime":260,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":2,"StartTime":261,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":2,"StartTime":262,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":1,"StartClip":2,"StartTime":263,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":0,"StartTime":264,"Duration":1.500000,"Speed":3},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":3,"StartTime":265.500000,"Duration":1.500000,"Speed":-3},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":1.500000,"StartTime":267,"Duration":1,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":2.200000,"StartTime":268,"Duration":1,"Speed":3},{"__class":"PlaybackEvent","ClipNumber":2,"StartClip":0,"StartTime":269,"Duration":2,"Speed":3},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":271,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":4,"StartTime":272,"Duration":2,"Speed":2},{"__class":"PlaybackEvent","ClipNumber":0,"StartClip":0,"StartTime":274,"Duration":1,"Speed":1},{"__class":"PlaybackEvent","ClipNumber":3,"StartClip":3,"StartTime":275,"Duration":1,"Speed":5}],"background_effect":{"__class":"AutoDanceFxDesc","Opacity":1,"ColorLow":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"ColorMid":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"ColorHigh":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"LowToMid":0.333000,"LowToMidWidth":0.150000,"MidToHigh":0.666000,"MidToHighWidth":0.150000,"SobColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"OutColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":0},"ThickMiddle":0.400000,"ThickInner":0.100000,"ThickSmooth":0.100000,"ShvNbFrames":0,"PartsScale":[0,0,0,0,0],"HalftoneFactor":0,"HalftoneCutoutLevels":256,"UVBlackoutFactor":0,"UVBlackoutDesaturation":0.200000,"UVBlackoutContrast":4,"UVBlackoutBrightness":0,"UVBlackoutColor":{"__class":"GFX_Vector4","x":0.549020,"y":0.549020,"z":1,"w":1},"ToonFactor":0,"ToonCutoutLevels":8,"RefractionFactor":0,"RefractionTint":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"RefractionScale":{"__class":"GFX_Vector4","x":0.030000,"y":0.030000,"z":0.030000,"w":0.030000},"RefractionOpacity":0.200000,"ColoredShivaThresholds":{"__class":"GFX_Vector4","x":0.100000,"y":0.300000,"z":0.600000,"w":0.950000},"ColoredShivaColor0":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"ColoredShivaColor1":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"ColoredShivaColor2":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"SaturationModifier":0,"SlimeFactor":0,"SlimeColor":{"__class":"GFX_Vector4","x":0.499020,"y":0.629176,"z":0.136039,"w":1},"SlimeOpacity":0.200000,"SlimeAmbient":0.200000,"SlimeNormalTiling":7,"SlimeLightAngle":0,"SlimeRefraction":0.091300,"SlimeRefractionIndex":1.083700,"SlimeSpecular":1,"SlimeSpecularPower":10,"OverlayBlendFactor":0,"OverlayBlendColor":{"__class":"GFX_Vector4","x":0.721569,"y":0.639216,"z":0.756863,"w":1},"BackgroundSobelFactor":0,"BackgroundSobelColor":{"__class":"GFX_Vector4","x":0,"y":1,"z":1,"w":1},"PlayerGlowFactor":0,"PlayerGlowColor":{"__class":"GFX_Vector4","x":0,"y":1,"z":1,"w":1},"SwapHeadWithPlayer":[0,1,2,3,4,5],"AnimatePlayerHead":[0,0,0,0,0,0],"AnimatedHeadTotalTime":20,"AnimatedHeadRestTime":16,"AnimatedHeadFrameTime":0.600000,"AnimatedHeadMaxDistance":1.250000,"AnimatedHeadMaxAngle":1.200000,"ScreenBlendInverseAlphaFactor":0,"ScreenBlendInverseAlphaScaleX":0,"ScreenBlendInverseAlphaScaleY":0,"ScreenBlendInverseAlphaTransX":0,"ScreenBlendInverseAlphaTransY":0,"TintMulColorFactor":0,"TintMulColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"FloorPlaneFactor":0,"FloorPlaneTiles":{"__class":"GFX_Vector4","x":8,"y":8,"z":0,"w":0},"FloorSpeedX":0,"FloorSpeedY":0,"FloorWaveSpeed":0,"FloorBlendMode":0,"FloorPlaneImageID":0,"StartRadius":3,"EndRadius":2,"RadiusVariance":0.500000,"RadiusNoiseRate":0,"RadiusNoiseAmp":0,"MinSpin":-4,"MaxSpin":4,"DirAngle":0,"MinWanderRate":2,"MaxWanderRate":3,"MinWanderAmp":0.100000,"MaxWanderAmp":0.200000,"MinSpeed":0.200000,"MaxSpeed":0.400000,"MotionPower":1.500000,"Amount":0,"ImageID":7,"StartR":1,"StartG":0.100000,"StartB":0.100000,"EndR":0.100000,"EndG":0.200000,"EndB":1,"StartAlpha":1,"EndAlpha":1,"TexturedOutlineFactor":0,"TexturedOutlineTiling":1,"TripleLayerBackgroundFactor":0,"TripleLayerBackgroundTintColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":0},"TripleLayerBackgroundSpeedX":0,"TripleLayerBackgroundSpeedY":0,"TrailEffectId":0},"player_effect":{"__class":"AutoDanceFxDesc","Opacity":1,"ColorLow":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"ColorMid":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"ColorHigh":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"LowToMid":0.333000,"LowToMidWidth":0.150000,"MidToHigh":0.666000,"MidToHighWidth":0.150000,"SobColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"OutColor":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":0},"ThickMiddle":0.400000,"ThickInner":0.100000,"ThickSmooth":0.100000,"ShvNbFrames":0,"PartsScale":[0,0,0,0,0],"HalftoneFactor":0,"HalftoneCutoutLevels":256,"UVBlackoutFactor":0,"UVBlackoutDesaturation":0.200000,"UVBlackoutContrast":4,"UVBlackoutBrightness":0,"UVBlackoutColor":{"__class":"GFX_Vector4","x":0.549020,"y":0.549020,"z":1,"w":1},"ToonFactor":0,"ToonCutoutLevels":256,"RefractionFactor":0,"RefractionTint":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"RefractionScale":{"__class":"GFX_Vector4","x":0.030000,"y":0.030000,"z":0.030000,"w":0.030000},"RefractionOpacity":0.200000,"ColoredShivaThresholds":{"__class":"GFX_Vector4","x":0.100000,"y":0.300000,"z":0.600000,"w":0.950000},"ColoredShivaColor0":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"ColoredShivaColor1":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"ColoredShivaColor2":{"__class":"GFX_Vector4","x":1,"y":1,"z":1,"w":1},"SaturationModifier":0,"SlimeFactor":0,"SlimeColor":{"__class":"GFX_Vector4","x":0.894118,"y":0.294118,"z":1,"w":0.549020},"SlimeOpacity":0.200000,"SlimeAmbient":0.200000,"SlimeNormalTiling":7,"SlimeLightAngle":0,"SlimeRefraction":0.100000,"SlimeRefractionIndex":1.100000,"SlimeSpecular":1.100000,"SlimeSpecularPower":2,"OverlayBlendFactor":0,"OverlayBlendColor":{"__class":"GFX_Vector4","x":0.721569,"y":0.639216,"z":0.756863,"w":1},"BackgroundSobelFactor":0,"BackgroundSobelColor":{"__class":"GFX_Vector4","x":0,"y":1,"z":1,"w":1},"PlayerGlowFactor":0,"PlayerGlowColor":{"__class":"GFX_Vector4","x":0,"y":1,"z":1,"w":1},"SwapHeadWithPlayer":[0,1,2,3,4,5],"AnimatePlayerHead":[0,0,0,0,0,0],"AnimatedHeadTotalTime":20,"AnimatedHeadRestTime":16,"AnimatedHeadFrameTime":0.600000,"AnimatedHeadMaxDistance":1.250000,"AnimatedHeadMaxAngle":1.200000,"ScreenBlendInverseAlphaFactor":0,"ScreenBlendInverseAlphaScaleX":0,"ScreenBlendInverseAlphaScaleY":0,"ScreenBlendInverseAlphaTransX":0,"ScreenBlendInverseAlphaTransY":0,"TintMulColorFactor":0,"TintMulColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":1},"FloorPlaneFactor":0,"FloorPlaneTiles":{"__class":"GFX_Vector4","x":8,"y":8,"z":0,"w":0},"FloorSpeedX":0,"FloorSpeedY":0,"FloorWaveSpeed":0,"FloorBlendMode":0,"FloorPlaneImageID":0,"StartRadius":0,"EndRadius":2,"RadiusVariance":0,"RadiusNoiseRate":0,"RadiusNoiseAmp":0,"MinSpin":0,"MaxSpin":0,"DirAngle":0,"MinWanderRate":0,"MaxWanderRate":0,"MinWanderAmp":0,"MaxWanderAmp":0,"MinSpeed":2,"MaxSpeed":4,"MotionPower":1,"Amount":0,"ImageID":0,"StartR":0,"StartG":0,"StartB":0,"EndR":1,"EndG":1,"EndB":1,"StartAlpha":1,"EndAlpha":1,"TexturedOutlineFactor":0,"TexturedOutlineTiling":0,"TripleLayerBackgroundFactor":0,"TripleLayerBackgroundTintColor":{"__class":"GFX_Vector4","x":0,"y":0,"z":0,"w":0},"TripleLayerBackgroundSpeedX":0,"TripleLayerBackgroundSpeedY":0,"TrailEffectId":0}},"autodanceSoundPath":"world/maps/' + mapname.lower() + '/autodance/' + mapname.lower() + '.ogg"}}]}')
autodancetpl.close()
##

##
autodanceisc = open(cache_autodance + mapname.lower() + "_autodance.isc.ckd", "w", encoding="utf-8")
autodanceisc.write('''<?xml version="1.0" encoding="ISO-8859-1"?>
<root>
<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">
    <ACTORS NAME="Actor">
        <Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="''' + mapname + '''_autodance" MARKER="" POS2D="-0.006150 -0.003075" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/''' + mapname.lower() + '''/autodance/''' + mapname.lower() + '''_autodance.tpl">
            <COMPONENTS NAME="JD_AutodanceComponent">
                <JD_AutodanceComponent />
            </COMPONENTS>
        </Actor>
    </ACTORS>
    <sceneConfigs>
        <SceneConfigs activeSceneConfig="0" />
    </sceneConfigs>
</Scene>
</root>''')
autodanceisc.close()
##
#AutoDance Files

#ACT FILES
#ACT FILES
#ACT FILES
autodanceact = open(cache_autodance + mapname.lower() + "_autodance.act.ckd", "wb")
ByteFileName = (mapname.lower() + "_autodance.tpl").encode()
ByteFileName_Length = (len(ByteFileName).to_bytes(4, 'big'))
BytePathFile = ("world/maps/" + mapname.lower() + "/autodance/").encode()
BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
autodanceact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00')
autodanceact.write(ByteFileName_Length)
autodanceact.write(ByteFileName)
autodanceact.write(BytePathFile_Length)
autodanceact.write(BytePathFile)
autodanceact.write(fileHash)
autodanceact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x67\xB8\xBB\x77')
autodanceact.close

def makeTexAct(texturename, output):
    file = open(output, 'wb')
    SongTextureName = (texturename).encode()
    SongTextureName_Length = (len(SongTextureName).to_bytes(4, 'big'))
    PathToSongTexture = ("world/maps/" + mapname.lower() + "/menuart/textures/").encode()
    PathToSongTexture_Length = (len(PathToSongTexture).to_bytes(4, 'big'))
    fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
    file.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x22\x74\x70\x6C\x5F\x6D\x61\x74\x65\x72\x69\x61\x6C\x67\x72\x61\x70\x68\x69\x63\x63\x6F\x6D\x70\x6F\x6E\x65\x6E\x74\x32\x64\x2E\x74\x70\x6C\x00\x00\x00\x1A\x65\x6E\x67\x69\x6E\x65\x64\x61\x74\x61\x2F\x61\x63\x74\x6F\x72\x74\x65\x6D\x70\x6C\x61\x74\x65\x73\x2F\xB4\xA8\x17\xA8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x72\xB6\x1F\xC5\x3F\x80\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00')
    file.write(SongTextureName_Length)
    file.write(SongTextureName)
    file.write(PathToSongTexture_Length)
    file.write(PathToSongTexture)
    file.write(fileHash)
    file.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x17\x6D\x75\x6C\x74\x69\x74\x65\x78\x74\x75\x72\x65\x5F\x31\x6C\x61\x79\x65\x72\x2E\x6D\x73\x68\x00\x00\x00\x18\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x6D\x61\x74\x73\x68\x61\x64\x65\x72\x2F\xD7\xE7\xD9\xC7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')
    file.close
    
abname = (mapname.lower() + "_cover_albumcoach")
makeTexAct(abname + ".tga", cache_act_menuart + abname + ".act.ckd")

bannername = (mapname.lower() + "_banner_bkg")
makeTexAct(bannername + ".tga", cache_act_menuart + bannername + ".act.ckd")

covergenericname = (mapname.lower() + "_cover_generic")
makeTexAct(covergenericname + ".tga", cache_act_menuart + covergenericname + ".act.ckd")

coveronlinename = (mapname.lower() + "_cover_online")
makeTexAct(coveronlinename + ".tga", cache_act_menuart + coveronlinename + ".act.ckd")

albumbkgname = (mapname.lower() + "_cover_albumbkg")
makeTexAct(albumbkgname + ".tga", cache_act_menuart + albumbkgname + ".act.ckd")

if(coachnum >= 1):
    c1name = (mapname.lower() + "_coach_1")
    makeTexAct(c1name + ".tga", cache_act_menuart + c1name + ".act.ckd")
    
if(coachnum >= 2):
    c2name = (mapname.lower() + "_coach_2")
    makeTexAct(c2name + ".tga", cache_act_menuart + c2name + ".act.ckd")

if(coachnum >= 3):
    c3name = (mapname.lower() + "_coach_3")
    makeTexAct(c3name + ".tga", cache_act_menuart + c3name + ".act.ckd")

if(coachnum >= 4):
    c4name = (mapname.lower() + "_coach_4")
    makeTexAct(c4name + ".tga", cache_act_menuart + c4name + ".act.ckd")

danceact = open(cache_timeline + mapname.lower() + "_tml_dance.act.ckd", "wb")
ByteFileName = (mapname.lower() + "_tml_dance.tpl").encode()
ByteFileName_Length = (len(ByteFileName).to_bytes(4, 'big'))
BytePathFile = ("world/maps/" + mapname.lower() + "/timeline/").encode()
BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
danceact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00')
danceact.write(ByteFileName_Length)
danceact.write(ByteFileName)
danceact.write(BytePathFile_Length)
danceact.write(BytePathFile)
danceact.write(fileHash)
danceact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x23\x1F\x27\xDE')
danceact.close

karaokeact = open(cache_timeline + mapname.lower() + "_tml_karaoke.act.ckd", "wb")
ByteFileName = (mapname.lower() + "_tml_karaoke.tpl").encode()
ByteFileName_Length = (len(ByteFileName).to_bytes(4, 'big'))
BytePathFile = ("world/maps/" + mapname.lower() + "/timeline/").encode()
BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
karaokeact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00')
karaokeact.write(ByteFileName_Length)
karaokeact.write(ByteFileName)
karaokeact.write(BytePathFile_Length)
karaokeact.write(BytePathFile)
karaokeact.write(fileHash)
karaokeact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x23\x1F\x27\xDE')
karaokeact.close

videoscoachact = open(cache_videoscoach + "video_player_main.act.ckd", "wb")
ByteFileName = (mapname.lower() + ".webm").encode()
ByteFileName_Length = (len(ByteFileName).to_bytes(4, 'big'))
ByteMpdFileName = (mapname.lower() + ".mpd").encode()
ByteMpdFileName_Length = (len(ByteMpdFileName).to_bytes(4, 'big'))
fileHash1 = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
BytePathFile = ("world/maps/" + mapname.lower() + "/videoscoach/").encode()
BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
fileHash2 = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
videoscoachact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x15\x76\x69\x64\x65\x6F\x5F\x70\x6C\x61\x79\x65\x72\x5F\x6D\x61\x69\x6E\x2E\x74\x70\x6C\x00\x00\x00\x1A\x77\x6F\x72\x6C\x64\x2F\x5F\x63\x6F\x6D\x6D\x6F\x6E\x2F\x76\x69\x64\x65\x6F\x73\x63\x72\x65\x65\x6E\x2F\xF5\xD5\xE8\xF2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x12\x63\xDA\xD9')
videoscoachact.write(ByteFileName_Length)
videoscoachact.write(ByteFileName)
videoscoachact.write(BytePathFile_Length)
videoscoachact.write(BytePathFile)
videoscoachact.write(fileHash1)
videoscoachact.write(b'\x00\x00\x00\x00')
videoscoachact.write(ByteMpdFileName_Length)
videoscoachact.write(ByteMpdFileName)
videoscoachact.write(BytePathFile_Length)
videoscoachact.write(BytePathFile)
videoscoachact.write(fileHash2)
videoscoachact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
videoscoachact.close

def getVideoInf(qualidade):
    nome = ("jmcs://jd-contents/" + mapname + "/" + mapname + "_" + qualidade + ".webm").encode()
    tamanho = (len(nome).to_bytes(4, 'big'))
    return tamanho, nome

videoscoachmpd = open(cache_videoscoach + mapname.lower() + ".mpd.ckd", "wb")
videoscoachmpd.write(b'\x00\x00\x00\x01\x00\x43\x29\x47\xAE\x3F\x80\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x43\x29\x47\xAE\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0A\x76\x69\x64\x65\x6F\x2F\x77\x65\x62\x6D\x00\x00\x00\x03\x76\x70\x38\x00\x00\x04\xC0\x00\x00\x02\xD0\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x00\x04\x00\x00\x00\x00\x00\x07\x39\x64')
LowWebm = getVideoInf("LOW")
MidWebm = getVideoInf("MID")
HighWebm = getVideoInf("HIGH")
UltraWebm = getVideoInf("ULTRA")
videoscoachmpd.write(LowWebm[0])
videoscoachmpd.write(LowWebm[1])
videoscoachmpd.write(b'\x00\x00\x00\x00\x00\x00\x02\x4B\x00\x00\x02\x4B\x00\x00\x0D\x5B\x00\x00\x00\x01\x00\x1C\x76\x0E')
videoscoachmpd.write(MidWebm[0])
videoscoachmpd.write(MidWebm[1])
videoscoachmpd.write(b'\x00\x00\x00\x00\x00\x00\x02\x4B\x00\x00\x02\x4B\x00\x00\x0D\xBF\x00\x00\x00\x02\x00\x38\xFF\x8E')
videoscoachmpd.write(HighWebm[0])
videoscoachmpd.write(HighWebm[1])
videoscoachmpd.write(b'\x00\x00\x00\x00\x00\x00\x02\x4B\x00\x00\x02\x4B\x00\x00\x0D\xE1\x00\x00\x00\x03\x00\x70\x94\x6D')
videoscoachmpd.write(UltraWebm[0])
videoscoachmpd.write(UltraWebm[1])
videoscoachmpd.write(b'\x00\x00\x00\x00\x00\x00\x02\x4B\x00\x00\x02\x4B\x00\x00\x0D\xF2')
videoscoachmpd.close()

songdescact = open(cache_path + "songdesc.act.ckd", "wb")
BytePathFile = ("world/maps/" + mapname.lower() + "/").encode()
BytePathFile_Length = (len(BytePathFile).to_bytes(4, 'big'))
fileHash = (randint(1000000000, 4000000000).to_bytes(4, 'big'))
songdescact.write(b'\x00\x00\x00\x01\x00\x00\x00\x00\x3F\x80\x00\x00\x3F\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x0C\x73\x6F\x6E\x67\x64\x65\x73\x63\x2E\x74\x70\x6C')
songdescact.write(BytePathFile_Length)
songdescact.write(BytePathFile)
songdescact.write(fileHash)
songdescact.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xE0\x7F\xCC\x3F')
songdescact.close
# unpacking jdu bundle
os.makedirs('output//temp', exist_ok=True)
subprocess.call('bin\\quickbms "bin\\scriptIPKextract.bms" "input\\'+mapnamelow+'_main_scene_pc.ipk" "output\\temp\\')
# importing files
src_files= os.listdir('output//temp//world//maps//'+mapnamelow+'//timeline//moves//wiiu')
for file_name in src_files:
    full_file_name= os.path.join('output//temp//world//maps//'+mapnamelow+'//timeline//moves//wiiu', file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, 'output//'+mapnamelow+'_pc//world//maps//'+mapnamelow+'//timeline//moves//wiiu')
src_files= os.listdir('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//timeline//pictos')
for file_name in src_files:
    full_file_name= os.path.join('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//timeline//pictos', file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, 'output//'+mapnamelow+'_pc//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//timeline//pictos')
src_files= os.listdir('input//textures')
for file_name in src_files:
    full_file_name= os.path.join('input//textures', file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, 'output//'+mapnamelow+'_pc//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//menuart//textures')
shutil.copy('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//audio//'+mapnamelow+'_musictrack.tpl.ckd', 'output//'+mapnamelow+'_pc//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//audio//')
shutil.copy('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//timeline//' + mapname.lower() + '_tml_dance.dtape.ckd', 'output//'+mapnamelow+'_pc//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//timeline//')
shutil.copy('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//songdesc.tpl.ckd', 'output//'+mapnamelow+'_pc//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//songdesc.tpl.ckd')
shutil.copy('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//timeline//'+mapnamelow+'_tml_karaoke.ktape.ckd', 'output//'+mapnamelow+'_pc//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//timeline//')
shutil.copy('input//'+mapnamelow+'_main_scene_pc.ipk', 'output//'+mapnamelow+'_pc.ipk')
shutil.copy('input//'+mapnamelow+'.webm', 'output//'+mapnamelow+'_pc//world//maps//'+mapnamelow+'//videoscoach//'+mapnamelow+'.webm')
shutil.copy('input//'+mapnamelow+'.ogg', 'output//'+mapnamelow+'_pc//world//maps//'+mapnamelow+'//audio//'+mapnamelow+'.ogg')
# removing temp
os.rmdir('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//audio')
os.rmdir('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//autodance')
os.rmdir('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//cinematics')
os.rmdir('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//graph')
os.rmdir('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//menuart//actors')
os.rmdir('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//menuart//textures')
os.rmdir('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//timeline//pictos')
os.rmdir('output//temp//cache//itf_cooked//pc//world//maps//'+mapnamelow+'//videoscoach')


