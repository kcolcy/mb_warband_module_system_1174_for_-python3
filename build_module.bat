@echo off
python process_init.py
python process_global_variables.py

python process_strings.py
python process_skills.py
python process_music.py
python process_animations.py
python process_meshes.py
python process_sounds.py
python process_skins.py
python process_factions.py
python process_particle_sys.py
python process_quests.py
python process_info_pages.py
python process_postfx.py

python process_map_icons.py
python process_items.py
python process_scenes.py
python process_troops.py
python process_scene_props.py
python process_tableau_materials.py
python process_presentations.py
python process_party_tmps.py
python process_parties.py
python process_scripts.py
python process_mission_tmps.py
python process_game_menus.py
python process_simple_triggers.py
python process_dialogs.py

python process_global_variables_unused.py


@REM 原版编译顺序(存在依赖矛盾，不建议使用)
@REM python process_init.py
@REM python process_global_variables.py
@REM python process_strings.py
@REM python process_skills.py
@REM python process_music.py
@REM python process_animations.py
@REM python process_meshes.py
@REM python process_sounds.py
@REM python process_skins.py
@REM python process_map_icons.py
@REM python process_factions.py
@REM python process_items.py
@REM python process_scenes.py
@REM python process_troops.py
@REM python process_particle_sys.py
@REM python process_scene_props.py
@REM python process_tableau_materials.py
@REM python process_presentations.py
@REM python process_party_tmps.py
@REM python process_parties.py
@REM python process_quests.py
@REM python process_info_pages.py
@REM python process_scripts.py
@REM python process_mission_tmps.py
@REM python process_game_menus.py
@REM python process_simple_triggers.py
@REM python process_dialogs.py
@REM python process_global_variables_unused.py
@REM python process_postfx.py

echo Deleting __pycache__ directories...
rd /s /q "__pycache__" 2>nul
for /d /r %%i in (__pycache__) do rd /s /q "%%i" 2>nul
echo Done.

echo.
echo ______________________________
echo.
echo Script processing has ended.
echo Press any key to exit. . .
pause>nul