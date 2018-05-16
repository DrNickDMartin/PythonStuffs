import pygmsh as pg
import meshio

if __name__ == "__main__":
    geom = pg.opencascade.Geometry(
        characteristic_length_min=0.1,
        characteristic_length_max=0.1)

    geom.add_box([0,0,0],[1,1,1])
    points, cells, point_data, cell_data, fd = pg.generate_mesh(geom)
    meshio.write('test.vtu', points, cells, cell_data=cell_data)