<?xml version="1.0" encoding="UTF-8"?>
<MetaResultFile version="20200629" creator="Solver HFTD - Field 3DFD Monitor">
  <MetaGeometryFile filename="model.gex" lod="1"/>
  <SimulationProperties fieldname="h-field (f=12.6) [1]" fieldtype="H-Field" frequency="12.600000381469727" encoded_unit="&amp;U:A^1.:m^-1" fieldscaling="PEAK" dB_Amplitude="20"/>
  <ResultDataType vector="1" complex="1" timedomain="0"/>
  <SimulationDomain min="-30.6179619 -27.9623032 -5.99584913" max="30.6179619 27.9623032 9.30084896"/>
  <PlotSettings Plot="4" ignore_symmetry="0" deformation="0" enforce_culling="0" default_arrow_type="ARROWS"/>
  <Source type="SOLVER"/>
  <SpecialMaterials>
    <Background type="NORMAL"/>
    <Material name="Copper (annealed)" type="FIELDFREE"/>
  </SpecialMaterials>
  <AuxGeometryFile/>
  <AuxResultFile/>
  <FieldFreeNodes/>
  <SurfaceFieldCoefficients/>
  <UnitCell/>
  <SubVolume/>
  <Units/>
  <ResultGroups num_steps="1" transformation="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1">
    <SharedDataWith treepath="2D/3D Results\Surface Current\surface current (f=12.6) [1]" rexname="h-field (f=12.6)_1,1_m3d_sct.rex"/>
    <Frame index="0">
      <FieldResultFile filename="h-field (f=12.6)_1,1.m3d" type="m3d"/>
    </Frame>
  </ResultGroups>
</MetaResultFile>
