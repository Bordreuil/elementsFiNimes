lc       = 10.;
lp       = 100.;
Lp       = 400.;

Point(1) = {0.,0.,0.,lc};
Point(2) = {lp,0.,0.,lc};
Point(3) = {lp,Lp,0.,lc};
Point(4) = {0.,Lp,0.,lc};

Line(1) = {1,2};
Line(2) = {2,3};
Line(3) = {3,4};
Line(4) = {4,1};

Line Loop(6) = {2, 3, 4, 1};
Plane Surface(6) = {6};