% Data = csvread('B_heat_z.csv',1,0);
% %reads csv file called "test results" and makes a 2D Matrix called Data
% 
% %use these points to get the B-field surface at each height
% %keep the -1 in the start and end arrays, for matlab's index
% %5.4385 - 2-2026
% %7.4385 - 2027-4051
% 
% x = Data(:,1);
% y = Data(:,2);
% B = Data(:,4);
% 
% heat = table(x,y,B);
% %makes column vectors for x, y and z
% 
% %heatmap(heat,'x','y', 'ColorVariable','B')
% 
% 
%  xv = linspace(min(x), max(x), size(x, 1));
%  yv = linspace(min(y), max(y), size(y, 1));
% % %makes smooth spaced array of the x and y values
% % %as to stop the surface from clipping
% % 
% % 
%  [X,Y] = meshgrid(xv, yv);
% % %makes a mesh grid of the smooth x and y vales
% % 
%  Z = griddata(x,y,B,X,Y);
% % %creates a Matrix of data that can be put into surface
% 
 s = contourf(X, Y, Z);
% %creates a surface of the data
% 
% hold on;
% 
% % surfc is a 2-element array of handles: the surface plot and the contours
% % sContour = s(2); % get the handle to the contour lines
% % sContour.ContourZLevel = min(B); % set the contour's Z position (default: hAxes.ZLim(1)=-10)
% 
% s.EdgeColor = 'none';
% %removes lines from surface plot
% 
% azHand = s.Parent;          %z axis ticks
% %azHand.XTick = -0.4 : 3 : 0.1;  %z axis ticks
% azHand.ZLim = [-0.6, 0.6];   %z axis limits
% 
% axHand = s.Parent;          %x axis ticks
% axHand.XTick = -10 : 10 : 10;  %x axis ticks
% axHand.XLim = [-11, 11];   %z axis limits
% 
% ayHand = s.Parent;          %y axis ticks
% ayHand.YTick = -10 : 10 : 10;  %y axis ticks
% ayHand.YLim = [-11, 11];   %y axis limits
% 
% xlabel('X (mm)'), ylabel('Y (mm)'), zlabel('B (T)');
% title('(a)');
% %grid off   %remove grid in background
% box on   % standard black box wireframe
% 
% 
% %point markers to show magnet position
% 
% mag_x_up_top = linspace(5,5,1);
% mag_x_up_bottom = linspace(-5,-5,1);
% mag_x_down_left = linspace(-5,-5,1);
% mag_x_down_right = linspace(5,5,1);
% % 
% mag_y_up_top = linspace(5,5,1);
% mag_y_up_bottom = linspace(-5,-5,1);
% mag_y_down_left = linspace(5,5,1);
% mag_y_down_right =  linspace(-5,-5,1);
% % 
% [mag_X_up_top,mag_Y_up_top,mag_Z_up_top] = meshgrid(mag_x_up_top, mag_y_up_top,-0.6);
% [mag_X_up_bottom,mag_Y_up_bottom,mag_Z_up_bottom] = meshgrid(mag_x_up_bottom, mag_y_up_bottom,-0.6);
% [mag_X_down_left,mag_Y_down_left,mag_Z_down_left] = meshgrid(mag_x_down_left, mag_y_down_left,-0.6);
% [mag_X_down_right,mag_Y_down_right,mag_Z_down_right] = meshgrid(mag_x_down_right, mag_y_down_right,-0.6);
% 
% % %w = [0.5 0.5 0.5];
% % 
% % %scatter3(mag_X,mag_V,'filled');
% %
% 
% scatter3(mag_X_up_top,mag_Y_up_top,mag_Z_up_top,200, 'ok', 'MarkerFaceColor', 'k')
% scatter3(mag_X_up_bottom,mag_Y_up_bottom,mag_Z_up_bottom,200,'ok', 'MarkerFaceColor', 'k')
% scatter3(mag_X_down_left,mag_Y_down_left,mag_Z_down_left,200,'xk')
% scatter3(mag_X_down_right,mag_Y_down_right,mag_Z_down_right,200,'xk')
% 
% 
% 
% hold off;
% 
% 
% 
% 
