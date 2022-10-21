rgb = imread("01.jpg");%读取原图像 
subplot(2,2,1);imshow(rgb); title("Image courtesy of Corel");%转化为灰度图像 
I = rgb2gray(rgb);
hy = fspecial("sobel");%sobel算子 
hx = hy';
Iy = imfilter(double(I), hy, "replicate");%滤波求y方向边缘 
Ix = imfilter(double(I), hx, "replicate");%滤波求x方向边缘 
gradmag = sqrt(Ix.^2 + Iy.^2);%求摸 
L = watershed(gradmag);%直接应用分水岭算法 
Lrgb = label2rgb(L);%转化为彩色图像 
subplot(2,2,2); imshow(Lrgb); title("直接使用梯度模值进行分水岭算法"); %显示分割后的图像 
%3.分别对前景和背景进行标记：本例中使用形态学重建技术对前景对象进行标记，首先使用开操作，开操作之后可以去掉一些很小的目标。 
se = strel("disk", 12);%圆形结构元素 
Io = imopen(I, se);%形态学开操作 
Ie = imerode(I, se);%对图像进行腐蚀 
Iobr = imreconstruct(Ie, I);%形态学重建 
Ioc = imclose(Io, se);%形态学关操作 
Iobrd = imdilate(Iobr, se);%对图像进行膨胀 
Iobrcbr = imreconstruct(imcomplement(Iobrd), imcomplement(Iobr));%形态学重建 
Iobrcbr = imcomplement(Iobrcbr);%图像求反 
fgm = imregionalmax(Iobrcbr);%局部极大值 
I2 = I; 
I2(fgm) = 255;%局部极大值处像素值设为255 
se2 = strel(ones(4,4));%结构元素 
fgm2 = imclose(fgm, se2);%关操作 
fgm3 = imerode(fgm2, se2);%腐蚀 
fgm4 = bwareaopen(fgm3, 15);%开操作 
I3 = I; 
I3(fgm4) = 255;%前景处设置为255 
bw = imbinarize(Iobrcbr, graythresh(Iobrcbr));%转化为二值图像 
%4. 进行分水岭变换并显示： 
D = bwdist(bw);%计算距离 
DL = watershed(D);%分水岭变换 
bgm = DL == 0;%求取分割边界 
gradmag2 = imimposemin(gradmag, bgm | fgm4);%置最小值 
L = watershed(gradmag2);%分水岭变换 
I4 = I; 
I4(imdilate(L == 0, ones(3, 3)) | bgm | fgm4) = 255;%前景及边界处置255 
subplot(2,2,3);imshow(I4); title("Markers and object boundaries"); %突出前景及边界
Lrgb = label2rgb(L, "jet", "w", "shuffle");%转化为伪彩色图像 
subplot(2,2,4); imshow(Lrgb);title("Colored watershed label matrix"); %显示伪彩色图像 
figure; 
imshow(I);
hold on
himage = imshow(Lrgb);set(himage, "AlphaData", 0.3); title("Lrgb superimposed transparently on original image");%在原图上显示伪彩色图像 