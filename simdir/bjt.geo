/* we are using cm with um scale length*/
/*
  The top part of this file was written by hand.
  The bottom part was appended by the gmsh viewer to connect points,
  and create physical groups
*/
Mesh.CharacteristicLengthExtendFromBoundary=0; /* don't extend from boundary points */
Mesh.Algorithm=5; /*Delaunay*/
Mesh.RandomFactor=1e-7; /*perturbation*/
/*Mesh.Algorithm=6;*/ /*Frontal*/

sf = 1.0e-4;
Mesh.CharacteristicLengthMax = 2.5e-5; /*maximum characteristic length */
/* characterisitic lengths for meshing */
/* results in coarse mesh */
cl1 = 2.5e-5;
cl2 = 2.5e-5;


/* all in microns, final output in cm */
/* we are simulating the intrinsic device*/
device_depth = 5 * sf;
left_space = 5 * sf;
right_space = 5 * sf;
contact_space = 7.5 * sf;
base_contact_width = 5 * sf;
emitter_contact_width = 5 * sf;
device_width = (left_space + base_contact_width + contact_space + emitter_contact_width + right_space);
collector_contact_width = device_width;

xb1 = left_space;
xb2 = xb1 + base_contact_width;
xe1 = xb2 + contact_space;
xe2 = xe1 + emitter_contact_width;


/* positive y is in the depth direction */
/* base contact */
Point(1) = {0, 0, 0, cl1};
Point(2) = {xb1, 0, 0, cl2};
Point(3) = {xb2, 0, 0, cl2};
/* emitter contact */
Point(4) = {xe1, 0, 0, cl2};
Point(5) = {xe2, 0, 0, cl2};
Point(6) = {device_width, 0, 0, cl1};

/* collector/bottom */
Point(7) = {0, device_depth, 0, cl1};
Point(8) = {device_width, device_depth, 0, cl1};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {5, 6};
Line(6) = {6, 8};
Line(7) = {7, 8};
Line(8) = {7, 1};
Physical Line("base") = {2};
Physical Line("emitter") = {4};
Physical Line("collector") = {7};
Line Loop(12) = {7, -6, -5, -4, -3, -2, -1, -8};
Plane Surface(13) = {12};
Physical Surface("bjt") = {13};
