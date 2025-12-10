@echo off
:: 激活 Conda 环境（需替换为你的 Conda 安装路径）
call "D:\Code Environment\anaconda3\Scripts\activate.bat" "D:\Code Environment\anaconda3\envs\houdini"

:: 强制设置环境变量（覆盖 Houdini 内置）
set PYTHONHOME=D:\Code Environment\anaconda3\envs\houdini
set PYTHONPATH=D:\Code Environment\anaconda3\envs\houdini\Lib\site-packages
set HOUDINI_DISABLE_FORCED_SITE_PACKAGES=1
set HOUDINI_DISABLE_BUILTIN_PYTHON_PACKAGES=1
set HOUDINI_PYTHON_VERSION=3.11
set PATH=D:\Code Environment\anaconda3\envs\houdini;D:\Code Environment\anaconda3\envs\houdini\Library\bin;D:\Code Environment\anaconda3\envs\houdini\Scripts;%PATH%

:: 启动 Houdini（替换为你的 Houdini 启动路径）
start "" "D:\MyApps\Houdini 20.5.654\bin\houdinifx.exe"