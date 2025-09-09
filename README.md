## Building and Running

```cmd
cd CxxFullExample
```
Configure the project with CMake (update catalyst_DIR as needed)

```cmd
cmake -S . -B bin -G "Visual Studio 17 2022" ^
    -Dcatalyst_DIR=D:\Repositories\Visualization\catalyst\catalyst-build\lib\cmake\catalyst-2.0
```
Build the project in Release mode
```
cmake --build bin --config Release
```

Set environment variables for Catalyst implementation
```
set CATALYST_IMPLEMENTATION_PATHS=D:\Repositories\Visualization\ParaView\ParaView-build\bin\catalyst
set CATALYST_IMPLEMENTATION_NAME=paraview
```
Run the example with the pipeline
```
release\bin\Release\CxxFullExampleV2.exe catalyst_pipeline.py
```

