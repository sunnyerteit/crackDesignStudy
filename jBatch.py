# Creates a simulation batch of a cracked half-plane with constant crack length a = 30 mm
# The load is applied a remote diplacement = 0.1 mm, normal to the crack plane
# Outputs the J-integral
# Author : Sunny Islam, 2017
# Abaqus version 6.14-1
#
# Run as script in Abaqus
#
#!/usr/bin/python
# -*- coding: utf-8 -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
from abaqus import *
from abaqusConstants import *

# importing time to delay printing of results

import time

# import math and numpy for basic operations

import numpy as np
import math

# some constant

f = 60.0

# parameters

b = 100.0
w = 100.0
n = 10

i = np.linspace(f, b, num=n)
j = np.linspace(f, w, num=n)

for x_1 in range(n):
    for y_1 in range(n):
        x = i[x_1]
        y = j[y_1]
		
		# create partioned sketch based on on size parameters
        mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                sheetSize=200.0)
        mdb.models['Model-1'].sketches['__profile__'
                ].rectangle(point1=(0.0, 0.0), point2=(x, -y))
        mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR,
                                   name='Part-1', type=DEFORMABLE_BODY)
        mdb.models['Model-1'].parts['Part-1'
                                    ].BaseShell(sketch=mdb.models['Model-1'
                ].sketches['__profile__'])
        del mdb.models['Model-1'].sketches['__profile__']
        mdb.models['Model-1'].ConstrainedSketch(gridSpacing=5.83,
                name='__profile__', sheetSize=233.23,
                transform=mdb.models['Model-1'].parts['Part-1'
                ].MakeSketchTransform(sketchPlane=mdb.models['Model-1'
                ].parts['Part-1'].faces[0], sketchPlaneSide=SIDE1,
                sketchOrientation=RIGHT, origin=(50.0, -30.0, 0.0)))
        mdb.models['Model-1'].parts['Part-1'
                                    ].projectReferencesOntoSketch(filter=COPLANAR_EDGES,
                sketch=mdb.models['Model-1'].sketches['__profile__'])
        mdb.models['Model-1'].sketches['__profile__'
                ].sketchOptions.setValues(gridOrigin=(-50.0, 30.0))
        mdb.models['Model-1'].sketches['__profile__'
                ].sketchOptions.setValues(gridAuto=OFF, gridSpacing=5.0)
        mdb.models['Model-1'].sketches['__profile__'
                ].Line(point1=(-50.0, 10.0), point2=(-40.0, 10.0))
        mdb.models['Model-1'].sketches['__profile__'
                ].HorizontalConstraint(addUndoState=False,
                entity=mdb.models['Model-1'].sketches['__profile__'
                ].geometry[6])
        mdb.models['Model-1'].sketches['__profile__'
                ].PerpendicularConstraint(addUndoState=False,
                entity1=mdb.models['Model-1'].sketches['__profile__'
                ].geometry[3], entity2=mdb.models['Model-1'
                ].sketches['__profile__'].geometry[6])
        mdb.models['Model-1'].sketches['__profile__'
                ].CoincidentConstraint(addUndoState=False,
                entity1=mdb.models['Model-1'].sketches['__profile__'
                ].vertices[4], entity2=mdb.models['Model-1'
                ].sketches['__profile__'].geometry[3])
        mdb.models['Model-1'].sketches['__profile__'
                ].Line(point1=(-40.0, 10.0), point2=(-40.0, -10.0))
        mdb.models['Model-1'].sketches['__profile__'
                ].VerticalConstraint(addUndoState=False,
                entity=mdb.models['Model-1'].sketches['__profile__'
                ].geometry[7])
        mdb.models['Model-1'].sketches['__profile__'
                ].PerpendicularConstraint(addUndoState=False,
                entity1=mdb.models['Model-1'].sketches['__profile__'
                ].geometry[6], entity2=mdb.models['Model-1'
                ].sketches['__profile__'].geometry[7])
        mdb.models['Model-1'].sketches['__profile__'
                ].Line(point1=(-40.0, -10.0), point2=(-50.0, -10.0))
        mdb.models['Model-1'].sketches['__profile__'
                ].HorizontalConstraint(addUndoState=False,
                entity=mdb.models['Model-1'].sketches['__profile__'
                ].geometry[8])
        mdb.models['Model-1'].sketches['__profile__'
                ].PerpendicularConstraint(addUndoState=False,
                entity1=mdb.models['Model-1'].sketches['__profile__'
                ].geometry[7], entity2=mdb.models['Model-1'
                ].sketches['__profile__'].geometry[8])
        mdb.models['Model-1'].sketches['__profile__'
                ].CoincidentConstraint(addUndoState=False,
                entity1=mdb.models['Model-1'].sketches['__profile__'
                ].vertices[7], entity2=mdb.models['Model-1'
                ].sketches['__profile__'].geometry[3])
        mdb.models['Model-1'].sketches['__profile__'
                ].Line(point1=(-40.0, 10.0), point2=(-20.0, 30.0))
        mdb.models['Model-1'].sketches['__profile__'
                ].CoincidentConstraint(addUndoState=False,
                entity1=mdb.models['Model-1'].sketches['__profile__'
                ].vertices[8], entity2=mdb.models['Model-1'
                ].sketches['__profile__'].geometry[2])
        mdb.models['Model-1'].sketches['__profile__'
                ].Line(point1=(-50.0, 0.0), point2=(0.0, 30.0))
        mdb.models['Model-1'].sketches['__profile__'].undo()
        mdb.models['Model-1'].sketches['__profile__'
                ].Line(point1=(-50.0, 0.0), point2=(-50.0 + x, 0.0))
        mdb.models['Model-1'].sketches['__profile__'
                ].HorizontalConstraint(addUndoState=False,
                entity=mdb.models['Model-1'].sketches['__profile__'
                ].geometry[10])
        mdb.models['Model-1'].sketches['__profile__'
                ].Line(point1=(-20.0, 30.0), point2=(-70.0, 0.0))
        mdb.models['Model-1'].sketches['__profile__'].undo()
        mdb.models['Model-1'].sketches['__profile__'
                ].Line(point1=(-20.0, 30.0), point2=(-20.0, -30.0 - y))
        mdb.models['Model-1'].sketches['__profile__'
                ].VerticalConstraint(addUndoState=False,
                entity=mdb.models['Model-1'].sketches['__profile__'
                ].geometry[11])
        mdb.models['Model-1'].sketches['__profile__'
                ].Line(point1=(-20.0, 30.0 - y), point2=(-40.0, -10.0))
        mdb.models['Model-1'].sketches['__profile__'
                ].CoincidentConstraint(entity1=mdb.models['Model-1'
                ].sketches['__profile__'].geometry[3],
                entity2=mdb.models['Model-1'].sketches['__profile__'
                ].vertices[9])
        mdb.models['Model-1'].sketches['__profile__'
                ].CoincidentConstraint(entity1=mdb.models['Model-1'
                ].sketches['__profile__'].geometry[5],
                entity2=mdb.models['Model-1'].sketches['__profile__'
                ].vertices[10])
        mdb.models['Model-1'].sketches['__profile__'
                ].CoincidentConstraint(entity1=mdb.models['Model-1'
                ].sketches['__profile__'].vertices[11],
                entity2=mdb.models['Model-1'].sketches['__profile__'
                ].geometry[4])
        mdb.models['Model-1'].parts['Part-1'
                                    ].PartitionFaceBySketch(faces=mdb.models['Model-1'
                ].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]',
                )), sketch=mdb.models['Model-1'].sketches['__profile__'
                ])
        del mdb.models['Model-1'].sketches['__profile__']

        # create material

        mdb.models['Model-1'].Material(name='Material-1')
        mdb.models['Model-1'].materials['Material-1'
                ].Elastic(table=((207000.0, 0.3), ))

        # JC material model for plastic behaviour

        mdb.models['Model-1'].materials['Material-1'
                ].Plastic(hardening=JOHNSON_COOK, table=((
            615.8,
            667.7,
            0.255,
            1.078,
            0.0,
            0.0,
            ), ))
        mdb.models['Model-1'
                   ].HomogeneousSolidSection(material='Material-1',
                name='Section-1', thickness=None)
        mdb.models['Model-1'].parts['Part-1'].SectionAssignment(
            offset=0.0,
            offsetField='',
            offsetType=MIDDLE_SURFACE,
            region=Region(faces=mdb.models['Model-1'].parts['Part-1'
                          ].faces.getSequenceFromMask(mask=('[#ff ]',
                          ))),
            sectionName='Section-1',
            thicknessAssignment=FROM_SECTION,
            )
        mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
        mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Part-1-1', part=mdb.models['Model-1'
                ].parts['Part-1'])
        mdb.models['Model-1'].StaticStep(initialInc=0.1, maxInc=0.1,
                name='Step-1', previous='Initial')
				
		# define crack and J-integral output
        mdb.models['Model-1'
                   ].rootAssembly.engineeringFeatures.ContourIntegral(
            collapsedElementAtTip=NONE,
            crackFront=Region(vertices=mdb.models['Model-1'
                              ].rootAssembly.instances['Part-1-1'
                              ].vertices.getSequenceFromMask(mask=('[#100 ]'
                              , ))),
            crackNormal=((0.0, 0.0, 0.0), (-1.0, 0.0, 0.0)),
            crackTip=Region(vertices=mdb.models['Model-1'
                            ].rootAssembly.instances['Part-1-1'
                            ].vertices.getSequenceFromMask(mask=('[#100 ]'
                            , ))),
            extensionDirectionMethod=CRACK_NORMAL,
            midNodePosition=0.5,
            name='Crack-1',
            symmetric=ON,
            )
		# boundary conditions
        mdb.models['Model-1'].XsymmBC(createStepName='Initial',
                localCsys=None, name='BC-1',
                region=Region(edges=mdb.models['Model-1'
                ].rootAssembly.instances['Part-1-1'
                ].edges.getSequenceFromMask(mask=('[#420 ]', ))))
        mdb.models['Model-1'].DisplacementBC(
            amplitude=UNSET,
            createStepName='Initial',
            distributionType=UNIFORM,
            fieldName='',
            localCsys=None,
            name='BC-2',
            region=Region(vertices=mdb.models['Model-1'
                          ].rootAssembly.instances['Part-1-1'
                          ].vertices.getSequenceFromMask(mask=('[#40 ]'
                          , ))),
            u1=UNSET,
            u2=SET,
            ur3=UNSET,
            )

        # displacement is defined from the rectangle width

        mdb.models['Model-1'].DisplacementBC(
            amplitude=UNSET,
            createStepName='Step-1',
            distributionType=UNIFORM,
            fieldName='',
            fixed=OFF,
            localCsys=None,
            name='BC-3',
            region=Region(edges=mdb.models['Model-1'
                          ].rootAssembly.instances['Part-1-1'
                          ].edges.getSequenceFromMask(mask=('[#808 ]',
                          ))),
            u1=0.1,
            u2=UNSET,
            ur3=UNSET,
            )
        mdb.models['Model-1'].HistoryOutputRequest(
            contourIntegral='Crack-1',
            createStepName='Step-1',
            name='jIntegral',
            numberOfContours=10,
            rebar=EXCLUDE,
            sectionPoints=DEFAULT,
            frequency=LAST_INCREMENT,
            )
        mdb.models['Model-1'
                   ].rootAssembly.makeIndependent(instances=(mdb.models['Model-1'
                ].rootAssembly.instances['Part-1-1'], ))
        mdb.models['Model-1'
                   ].rootAssembly.setMeshControls(elemShape=QUAD,
                regions=mdb.models['Model-1'
                ].rootAssembly.instances['Part-1-1'
                ].faces.getSequenceFromMask(('[#ef ]', )),
                technique=STRUCTURED)
        mdb.models['Model-1'
                   ].rootAssembly.setMeshControls(elemShape=QUAD,
                regions=mdb.models['Model-1'
                ].rootAssembly.instances['Part-1-1'
                ].faces.getSequenceFromMask(('[#10 ]', )),
                technique=STRUCTURED)
        mdb.models['Model-1'
                   ].rootAssembly.setElementType(elemTypes=(ElemType(elemCode=CPE4,
                elemLibrary=STANDARD, secondOrderAccuracy=OFF,
                hourglassControl=DEFAULT, distortionControl=DEFAULT),
                ElemType(elemCode=CPE3, elemLibrary=STANDARD)),
                regions=(mdb.models['Model-1'
                ].rootAssembly.instances['Part-1-1'
                ].faces.getSequenceFromMask(('[#ff ]', )), ))
				
		# mesh seeds
        mdb.models['Model-1'
                   ].rootAssembly.seedEdgeByNumber(constraint=FINER,
                edges=mdb.models['Model-1'
                ].rootAssembly.instances['Part-1-1'
                ].edges.getSequenceFromMask(('[#1feffa ]', )),
                number=10)
        mdb.models['Model-1'
                   ].rootAssembly.seedEdgeByNumber(constraint=FINER,
                edges=mdb.models['Model-1'
                ].rootAssembly.instances['Part-1-1'
                ].edges.getSequenceFromMask(('[#1005 ]', )), number=30)
        mdb.models['Model-1'
                   ].rootAssembly.generateMesh(regions=(mdb.models['Model-1'
                ].rootAssembly.instances['Part-1-1'], ))
        mdb.Job(
            atTime=None,
            contactPrint=OFF,
            description='',
            echoPrint=OFF,
            explicitPrecision=SINGLE,
            getMemoryFromAnalysis=True,
            historyPrint=OFF,
            memory=90,
            memoryUnits=PERCENTAGE,
            model='Model-1',
            modelPrint=OFF,
            multiprocessingMode=DEFAULT,
            name=str(x_1) + str(y_1),
            nodalOutputPrecision=SINGLE,
            numCpus=1,
            numGPUs=0,
            queue=None,
            resultsFormat=ODB,
            scratch='',
            type=ANALYSIS,
            userSubroutine='',
            waitHours=0,
            waitMinutes=0,
            )
        mdb.jobs[str(x_1) + str(y_1)].submit(consistencyChecking=OFF)
		# this is here to ensure your memory is still intact after the simulation batches
		# change this to the average simulation time
        time.sleep(60)


			
			