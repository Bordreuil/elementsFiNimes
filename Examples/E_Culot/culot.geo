// Definition de la geometrie d un fond de verin
// Visualisation de l influence de la penetration et
// de la position du joint soude

lc      = 2.5;
lcf     = .1;
Rculot  = 136.5;
Hculot  = 100.;
Hcordon = 100.;
Lcordon = 20.;
Pcordon = 20.;
Htot    = 200.;
Rint    = 110.;
Rplat   = 90.;
Rdeg    = 60.;
Hdeg    = 82.;
Hplat   = 87.; 
jeu     = 0.1;


Point(1)  = {0.             ,                 0.,    0.,lc};
Point(2)  = {Rculot         ,                 0.,    0.,lc};
Point(3)  = {Rculot         ,Hcordon-Lcordon/2. ,    0.,lc};
Point(4)  = {Rculot         ,Hcordon+Lcordon/2. ,    0.,lc};
Point(5)  = {Rculot         ,Htot               ,    0.,lc};
Point(6)  = {Rint           ,Htot               ,    0.,lc};
Point(7)  = {Rint           ,Hcordon+jeu        ,    0.,lc};
Point(8)  = {Rculot-Pcordon ,Hcordon            ,    0.,lcf};
Point(9)  = {Rint           ,Hcordon-jeu        ,    0.,lc};
Point(10) = {Rint           ,Hculot             ,    0.,lc};
Point(11) = {Rplat          ,Hculot             ,    0.,lc};
Point(12) = {Rplat+Hplat-Hculot,Hplat           ,    0.,lc};
Point(13) = {Rdeg              ,Hdeg            ,    0.,lc};
Point(14) = {0.                ,Hdeg             ,    0., lc};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {6, 5};
Line(6) = {6, 7};
Line(7) = {7, 8};
Line(8) = {8, 9};
Line(9) = {9, 11};
Line(10) = {11, 12};
Line(11) = {12, 13};
Line(12) = {13, 14};
Line(13) = {14, 1};
Line Loop(14) = {12, 13, 1, 2, 3, 4, -5, 6, 7, 8, 9, 10, 11};
Plane Surface(15) = {14};
Physical Surface(16) = {15};
Physical Line("Haut") = {5};
Physical Line("Inter") = {6, 9, 10, 11, 12, 7, 8};
