#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import numpy as np
import pygimli as pg


class TestMeshGenerator(unittest.TestCase):

    def test_createGrid(self):
        mesh = pg.createGrid(3)
        self.assertEqual(mesh.xmax(), 2.0)
        mesh = pg.createGrid(3, 3)
        self.assertEqual(mesh.ymax(), 2.0)
        mesh = pg.createGrid(3, 3, 3)
        self.assertEqual(mesh.zmax(), 2.0)
        # mesh = pg.createMesh1D(10, 1)
        # print(mesh)
        # self.assertEqual(mesh.cellCount(), 10.0)

    def test_createMesh1D(self):

        mesh = pg.createMesh1D(10, 1)
        self.assertEqual(mesh.cellCount(), 10.0)
        self.assertEqual(mesh.xmax(), 10.0)

        mesh = pg.createMesh1D(nCells=10)
        self.assertEqual(mesh.cellCount(), 10.0)

        mesh = pg.createMesh1D(nCells=5, nProperties=2)
        self.assertEqual(mesh.cellCount(), 10.0)

        mesh = pg.createMesh1D(5, 2)
        self.assertEqual(mesh.cellCount(), 10.0)

        mesh = pg.createMesh1D(10)
        self.assertEqual(mesh.cellCount(), 10.0)

    def test_createMesh1DBlock(self):

        mesh = pg.createMesh1DBlock(nLayers=5)
        self.assertEqual(mesh.cellCount(), 9.0)

        mesh = pg.createMesh1DBlock(5)
        self.assertEqual(mesh.cellCount(), 9.0)

        mesh = pg.createMesh1DBlock(5, 1)
        self.assertEqual(mesh.cellCount(), 9.0)

        mesh = pg.createMesh1DBlock(nLayers=4, nProperties=2)
        self.assertEqual(mesh.cellCount(), 11.0)

        mesh = pg.createMesh1DBlock(4, 2)
        self.assertEqual(mesh.cellCount(), 11.0)

    def test_createMesh2D(self):

        mesh = pg.createMesh2D(xDim=5, yDim=2)
        self.assertEqual(mesh.cellCount(), 10.0)

        mesh = pg.createMesh2D(5, 2)
        self.assertEqual(mesh.cellCount(), 10.0)

        mesh = pg.createMesh2D(np.linspace(0, 1, 6),np.linspace(0, 1, 3))
        self.assertEqual(mesh.cellCount(), 10.0)

    def test_createMesh3D(self):

        mesh = pg.createMesh3D(xDim=5, yDim=3, zDim=2)
        self.assertEqual(mesh.cellCount(), 30.0)

    def test_createPartMesh(self):
        mesh = pg.createMesh1D(np.linspace(0, 1, 10))
        self.assertEqual(mesh.cellCount(), 9)

        mesh2 = mesh.createMeshByCellIdx(
            pg.find(pg.x(mesh.cellCenters()) < 0.5))
        self.assertEqual(mesh2.cellCount(), 4)
        self.assertEqual(mesh2.cellCenters()[-1][0] < 0.5, True)

    def test_MeshCreatePolyList(self):
        pos = [[0, 0], [1, 0], [1, -1], [0, -1]]
        poly = pg.meshtools.createPolygon(pos, isClosed=0)
        mesh = pg.meshtools.createMesh(poly, quality=20, area=0.001)
        self.assertEqual(mesh.nodeCount(), 4)
        self.assertEqual(mesh.cellCount(), 0)
        poly = pg.meshtools.createPolygon(pos, isClosed=1)
        mesh = pg.meshtools.createMesh(poly, quality=0, area=0.)
        self.assertEqual(mesh.nodeCount(), 4)
        self.assertEqual(mesh.cellCount(), 2)
        self.assertEqual(mesh.boundaryCount(), 5)


if __name__ == '__main__':

    pg.setDeepDebug(0)

    t = TestMeshGenerator()
    t.test_createGrid()
    exit()

    unittest.main()
