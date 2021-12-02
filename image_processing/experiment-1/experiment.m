% MATLAB中文官网：https://ww2.mathworks.cn/
% 在线版MATLAB（功能不全）：https://octave-online.net/

% 基本概念
% 低通滤波有:线性的均值滤波器、高斯滤波器,非线性的双边滤波器有中值滤波器
% 高通滤波有:巴特沃斯高通滤波器，基于Canny,Sobel等算子的各种边缘滤波器

% 清除没有用的输出
clear all;
close all;
clc;

% 1.平滑滤波器(PDF中的1、2两题)
% 先添加噪声
image = imread('peppers.png');
image_double = im2double(image);
image_gray = rgb2gray(image);
% 创建2*2个图像窗口，注意是窗口，不是图（plot）
figure;
% 创建子图
% 添加噪声
subplot(2, 2, 1), imshow(image_gray), title('Original image');
image_noise_guassian = imnoise(image_gray, 'gaussian', 0, 0.02);
subplot(2, 2, 2), imshow(image_noise_guassian), title('Gaussian');
image_noise_salt = imnoise(image_gray, 'salt & pepper', 0.02);
subplot(2, 2, 3), imshow(image_noise_salt), title('salt & pepper');
image_noise_poisson = imnoise(image_gray, 'poisson');
subplot(2, 2, 4), imshow(image_noise_poisson), title('poisson');

% 均值平滑滤器
% mean_filter=1/8*[[1,1,1],[1,0,1],[1,1,1]];
mean_filter = 1/9 * [[1, 1, 1], [1, 1, 1], [1, 1, 1]];
image_gray_mean = imfilter(image_gray, mean_filter);
figure;
subplot(4, 2, 1), imshow(image_gray), title('Original image');
subplot(4, 2, 2), imshow(image_gray_mean), title('Original image mean');
image_noise_guassian_mean = imfilter(image_noise_guassian, mean_filter);
subplot(4, 2, 3), imshow(image_noise_guassian), title('Gaussian');
subplot(4, 2, 4), imshow(image_noise_guassian_mean), title('Gaussian mean');
image_noise_salt_mean = imfilter(image_noise_salt, mean_filter);
subplot(4, 2, 5), imshow(image_noise_salt), title('salt & pepper');
subplot(4, 2, 6), imshow(image_noise_salt_mean), title('salt & pepper mean');
image_noise_poisson_mean = imfilter(image_noise_poisson, mean_filter);
subplot(4, 2, 7), imshow(image_noise_poisson), title('poisson');
subplot(4, 2, 8), imshow(image_noise_poisson_mean), title('poisson mean');

% 加权平滑滤波
weighting_filter = 1/16 * [[1, 2, 1], [2, 4, 2], [1, 2, 1]];
image_gray_weighting = imfilter(image_gray, weighting_filter);
figure;
subplot(4, 2, 1), imshow(image_gray), title('Original image');
subplot(4, 2, 2), imshow(image_gray_mean), title('Original image weighting');
image_noise_guassian_weighting = imfilter(image_noise_guassian, weighting_filter);
subplot(4, 2, 3), imshow(image_noise_guassian), title('Gaussian');
subplot(4, 2, 4), imshow(image_noise_guassian_mean), title('Gaussian weighting');
image_noise_salt_weighting = imfilter(image_noise_salt, weighting_filter);
subplot(4, 2, 5), imshow(image_noise_salt), title('salt & pepper');
subplot(4, 2, 6), imshow(image_noise_salt_mean), title('salt & pepper weighting');
image_noise_poisson_weighting = imfilter(image_noise_poisson, weighting_filter);
subplot(4, 2, 7), imshow(image_noise_poisson), title('poisson');
subplot(4, 2, 8), imshow(image_noise_poisson_mean), title('poisson weighting');

% 2.巴特沃斯
% 二维傅里叶变换
% 为什么要傅里叶变换建议参考《信号处理》这门课
image = imread('peppers.png');
image_double = im2double(image);
fourier = fft2(image_double);
% 转换为矩阵，通过将零频分量移动到数组中心,重新排列傅里叶变换
% 解释：经过fft变换后，数据的频率范围是从[0,fs]排列的，一般，我们在画图或者讨论的时候，是从[-fs/2,fs/2]的范围进行分析，因此，要将经过fft变换后的图像的[fs/2,fs]部分移动到[-fs/2,0]这个范围内，
% 参考：https://blog.csdn.net/lihe4151021/article/details/89675567
fourier_shifted = fftshift(fourier);
% 获得矩阵的行列数
[M, N] = size(fourier_shifted);
% 下面的代码可以达到同样的效果
% M=size(fourier_shifted,1);%返回矩阵的行数
% N=size(fourier_shifted,2);%返回矩阵的列数

% round：四舍五入
% fix：截尾取整（又称向零方向取整，其实就是直接去掉小数部分）
% floor：向下取整（如：-3.12为-4）
% ceil：向下取整（如：-3.12为-3）
u = round(M / 2);
v = round(N / 2);

% 巴特沃斯滤波过程
% 巴特沃斯滤波器的阶数
n = 6;
% 截止频率
d0 = 30;
% 执行滤波
for i = 1:M

    for j = 1:N
        d = sqrt((i - u)^2 + (j - v)^2);
        % 定义滤波函数
        butterworth_filter = (1 / (1 + (d0 / d)^(2 * n))) + 0.5;
        butterworth_filtered_fourier_shifted(i, j) = butterworth_filter * fourier_shifted(i, j);
    end

end

% i是反的意思，傅里叶变换后要反变换回来
butterworth_filtered_fourier = ifftshift(butterworth_filtered_fourier_shifted);
butterworth_filtered_image = ifft2(butterworth_filtered_fourier);
% 经过傅里叶导致图像变大了，因为有虚数（在图像中就是有1圈黑框），要截取图像，网上的方法是：real()
butterworth_filtered_image = butterworth_filtered_image(1:size(image_double, 1), 1:size(image_double, 2));
figure;
subplot(2, 1, 1), imshow(image_double), title('原图');
subplot(2, 1, 2), imshow(real(butterworth_filtered_image)), title('巴特沃斯滤波');

% 另一种写法，注意：带.的是矩阵操作，不是数操作（当然数操作也可以用，但是没区别，不报错
M = 2 * size(image_double, 1); %返回矩阵的行数
N = 2 * size(image_double, 2); %返回矩阵的列数
% m:n是指创建1个从m到n的行向量，可以进行和Python切片一样的间隔操作
u = -M / 2:(M / 2 - 1);
v = -N / 2:(N / 2 - 1);

% meshgrid函数参考：https://ww2.mathworks.cn/help/matlab/ref/meshgrid.html
[U, V] = meshgrid(u, v);
n = 6;
D0 = 30;
D = sqrt(U.^2 + V.^2);
butterworth_filter = 1 ./ (1 + (D0 ./ D).^(2 * n));
% 傅里叶变换
fourier_shifted = fftshift(fft2(image_double, size(butterworth_filter, 1), size(butterworth_filter, 2)));
% 滤波
butterworth_filtered_fourier_shifted = fourier_shifted .* butterworth_filter;
% 傅里叶反变换
butterworth_filtered_image = ifft2(ifftshift(butterworth_filtered_fourier_shifted));
butterworth_filtered_image = butterworth_filtered_image(1:size(image_double, 1), 1:size(image_double, 2));
figure;
subplot(2, 1, 1), imshow(image_double), title('原图');
subplot(2, 1, 2), imshow(real(butterworth_filtered_image)), title('巴特沃斯滤波2');

% 3.利用fspecial函数实现rice.png运动模糊的效果
image = imread('rice.png');
% 偏移像素
offset = 31;
% 角度
theta = 11;

% fspecial：二维滤波器，函数参考：https://ww2.mathworks.cn/help/images/ref/fspecial.html?lang=en
% imfilter：多维图像的N维滤波
% 运动模糊
motion_filter = fspecial('motion', offset, theta);
image_motion = imfilter(image, motion_filter, 'replicate');
% 老师用的参数不大一样
image_motion2 = imfilter(image, motion_filter, 'circular', 'conv');

% 以下为一些补充
% 普通模糊
radius = 10;
disk_filter = fspecial('motion', radius);
image_doubleisk = imfilter(image, disk_filter, 'replicate');
% 锐化图像
unsharp_filter = fspecial('unsharp');
image_sharpened = imfilter(image, unsharp_filter, 'replicate');
figure;
subplot(2, 2, 1), imshow(image), title('原图');
subplot(2, 2, 2), imshow(image_motion), title('运动模糊1');
subplot(2, 2, 3), imshow(image_motion2), title('运动模糊2');

% 4.逆滤波(图像去模糊)和维纳滤波做复原的比较
% 建议参考：https://blog.csdn.net/krian_a/article/details/110822172
image = imread('cell.tif');
image_double = im2double(image);
[m, n] = size(image);
fourier_shifted = fftshift(fft2(image_double));

% 生成逆滤波滤波器
k = 0.0025;
inverse_filter = [];

for u = 1:m

    for v = 1:n
        q = ((u - m / 2)^2 + (v - n / 2)^2)^(5/6);
        inverse_filter(u, v) = exp((-k) * q);
    end

end

% 退化（模糊）
image_inverse_fourier_shifted = fourier_shifted .* inverse_filter;
image_inverse = ifft2(ifftshift(image_inverse_fourier_shifted));
figure;
subplot(3, 2, 1), imshow(image), title('原图');
subplot(3, 2, 2), imshow(image_inverse), title('退化');

% 退化的逆滤波复原
image_inverse_fourier_shifted = fftshift(fft2(image_inverse));
image_inverse_repaired_fourier_shifted = image_inverse_fourier_shifted ./ inverse_filter;
image_inverse_repaired = ifft2(ifftshift(image_inverse_repaired_fourier_shifted));
subplot(3, 2, 3), imshow(real(image_inverse_repaired)), title('退化的逆滤波修复');

% 添加高斯噪声
gaussian_noise_mean = 0;
gaussian_noise_var = 0.01;
image_inverse_gaussian_noise = imnoise(image_inverse, 'gaussian', gaussian_noise_mean, gaussian_noise_var);
subplot(3, 2, 4), imshow(image_inverse_gaussian_noise), title('退化并添加高斯噪声');

% 逆滤波复原
image_inverse_gaussian_noise_fourier_shifted = fftshift(fft2(image_inverse_gaussian_noise));
image_inverse_gaussian_noise_repaired_fourier_shifted = image_inverse_gaussian_noise_fourier_shifted ./ inverse_filter;
image_inverse_gaussian_noise_repaired = ifft2(ifftshift(image_inverse_gaussian_noise_repaired_fourier_shifted));
subplot(3, 2, 5), imshow(real(image_inverse_gaussian_noise_repaired)), title('退化并添加高斯噪声的逆滤波修复');

% 使用维纳滤波做复原
% 老师的手写维纳滤波器
K = 0.1;
H = [];
H0 = [];
H1 = [];
% 手写的inverse_filter过滤器
for u = 1:m

    for v = 1:n
        q = ((u - m / 2)^2 + (v - n / 2)^2)^(5/6);
        H(u, v) = exp((-k) * q);
        H0(u, v) = (abs(H(u, v)))^2;
        H1(u, v) = H0(u, v) / (H(u, v) * (H0(u, v) + K));
    end

end

image_inverse_gaussian_noise_fourier_shifted = fftshift(fft2(image_inverse_gaussian_noise));
image_inverse_gaussian_noise_wiener_repaired_fourier_shifted = H1 .* image_inverse_gaussian_noise_fourier_shifted;
image_inverse_gaussian_noise_wiener_repaired = ifft2(ifftshift(image_inverse_gaussian_noise_wiener_repaired_fourier_shifted));
subplot(3, 2, 6), imshow(real(image_inverse_gaussian_noise_wiener_repaired)), title('退化并添加高斯噪声的维纳滤波修复');

% 使用MATLAB自带维纳滤波器函数deconvwnr，需要知道原退化（模糊）函数，如果有噪声，还需要知道噪信比(NSR)
% 未添加噪声的时候，此处NSR=0
image_without_noise_repaired = deconvwnr(image_inverse, inverse_filter, 0);
figure;
subplot(1, 2, 1), imshow(image_without_noise_repaired), title('退化的维纳滤波修复');

% 当添加高斯噪声的时候，需要计算噪信比(NSR)
signal_var = var(image_double(:));
% 这里比较奇怪，用手写的inverse_filter没有用，但是使用自带的fspecial('motion', offset, theta)生成的过滤器就可以复原
image_with_gaussian_noise_repaired = deconvwnr(abs(image_inverse_gaussian_noise), inverse_filter, gaussian_noise_var / signal_var);
subplot(1, 2, 2), imshow(image_with_gaussian_noise_repaired), title('退化并添加高斯噪声的维纳滤波修复');

% 5.几种经典算法进行复原比较
image = imread('pout.tif');
% 偏移像素
offset = 30;
% 角度
theta = 45;
motion_filter = fspecial('motion', offset, theta);
image_motion = imfilter(image, motion_filter, 'circular', 'conv');
% 维纳滤波
image_wiener = deconvwnr(image_motion, motion_filter);
% 最小二乘法
min_least_square_filter = imfilter(image_motion, motion_filter, 'conv');
gaussian_noise_mean = 0;
gaussian_noise_var = 0.02;
image_gaussian_noise = imnoise(min_least_square_filter, 'gaussian', gaussian_noise_mean, gaussian_noise_var);
NP = gaussian_noise_var * prod(size(image));
image_min_least_square = deconvreg(image_gaussian_noise, motion_filter, NP);
% Lucy-Richardson
lucy_filter = imfilter(image_motion, motion_filter, 'symmetric', 'conv');
gaussian_noise_mean = 0;
gaussian_noise_var = 0.002;
image_gaussian_noise = imnoise(lucy_filter, 'gaussian', gaussian_noise_mean, gaussian_noise_var);
image_lucy = deconvlucy(image_gaussian_noise, motion_filter, 5);
% 盲去卷积
image_blind_conv = imfilter(image_motion, motion_filter, 'circ', 'conv');
init_motion_filter = ones(size(motion_filter));
[image_blind_conv_repaired, new_motion_filter] = deconvblind(image_blind_conv, init_motion_filter, 30);
figure;
subplot(2, 3, 1), imshow(image), title('原图');
subplot(2, 3, 2), imshow(image_motion), title('模糊');
subplot(2, 3, 3), imshow(image_wiener), title('维纳滤波');
subplot(2, 3, 4), imshow(image_min_least_square), title('最小二乘法');
subplot(2, 3, 5), imshow(image_lucy), title('Lucy');
subplot(2, 3, 6), imshow(image_blind_conv_repaired), title('盲去卷积');

% 6.中值滤波
% image = imread('cell.tif');
% 彩色图和灰度图都可以
image = imread('peppers.png');
image_gray = rgb2gray(image);
subplot(3, 2, 1), imshow(image), title('原图');
subplot(3, 2, 2), imshow(image_gray), title('灰度图');
% 加盐
image_salt = imnoise(image_gray, 'salt & pepper', 0.02);
% 默认为3*3的滤波窗口，如果要自定义滤波窗口，使用medfilt2(image,[m,n])
image_salt_median_filtered = medfilt2(image_salt);
subplot(3, 2, 3), imshow(image_salt), title('加盐');
subplot(3, 2, 4), imshow(image_salt_median_filtered), title('加盐中值滤波');
% 高斯噪声
image_gaussian = imnoise(image_gray, 'gaussian', 0.02);
image_gaussian_median_filtered = medfilt2(image_gaussian, [5, 5]);
subplot(3, 2, 5), imshow(image_gaussian), title('加高斯噪声');
subplot(3, 2, 6), imshow(image_gaussian_median_filtered), title('加高斯噪声中值滤波');

% 7.分水岭算法，某位大神调了更好的参数
% 见water_shed.m

% 8.区域增长算法
image = imread('rice.png');
% 网上找的，可以自己选择点(多选几个点，回车等一会儿即可)，参考：https://blog.csdn.net/shenziheng1/article/details/50878911
image_region_grow = region_grow(image);

% 宿舍另一位大神改造老师的代码，老师的x，y顺序有问题
image = imread('rice.png');

seed_x = [110, 255, 86];
seed_y = [128, 255, 73];

subplot(1, 2, 1), imshow(image), title('Original image');
hold on;
plot(seed_y, seed_x, 'gs', 'linewidth', 1);
markerim = image == image(seed_y(1), seed_x(1));
disp(markerim(seed_y(1), seed_x(1)));

image_d = double(image);
markerim = zeros(size(image_d));

for i = 1:length(seed_x)
    markerim = markerim | (image_d == image_d(seed_y(i), seed_x(i)));
end

thresh = [15, 10, 15];
maskim = zeros(size(image_d));

for i = 1:length(seed_x)
    g = abs(image_d - image_d(seed_y(1), seed_x(1))) <= thresh(i);
    maskim = markerim | g;
end

[g, nr] = bwlabel(imreconstruct(markerim, maskim), 8);
g = mat2gray(g);
subplot(1, 2, 2), imshow(g), title('结果');
