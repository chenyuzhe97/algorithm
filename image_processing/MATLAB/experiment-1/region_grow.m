function [image_region_grow_result] = region_grow(image)
    I=image;

    if (~(size(I, 3) - 3))
        I = rgb2gray(I); %转化为单通道灰度图
    end

    I = im2double(I); %图像灰度值归一化到[0,1]之间
    Ireshape = imresize(I, [600, 800]);
    I = Ireshape(51:475, 200:699);
    gausFilter = fspecial('gaussian', [5 5], 0.5);
    I = imfilter(I, gausFilter, 'replicate');

    %种子点的交互式选择
    if (exist('x', 'var') == 0 && exist('y', 'var') == 0)
        subplot(2, 2, 1), imshow(I, []);
        hold on;
        [y, x] = getpts; %鼠标取点  回车确定
        x = round(x(1)); %选择种子点
        y = round(y(1));
    end

    if (nargin == 0)
        reg_maxdist = 0.1;
        %nargin是matlab代码编写中常用的一个技巧，主要用于计算当前主函数的输入参数个
        %数，一般可以根据nargin的返回值来确定主函数输入参数的缺省值。在实现中，如果
        %用户输入的参数个数为零，那么默认为0.2
    end

    J = zeros(size(I)); % 主函数的返回值，记录区域生长所得到的区域
    Isizes = size(I);
    reg_mean = I(x, y); %表示分割好的区域内的平均值，初始化为种子点的灰度值
    reg_size = 1; %分割的到的区域，初始化只有种子点一个
    neg_free = 10000; %动态分配内存的时候每次申请的连续空间大小
    neg_list = zeros(neg_free, 3);
    %定义邻域列表，并且预先分配用于储存待分析的像素点的坐标值和灰度值的空间，加速
    %如果图像比较大，需要结合neg_free来实现matlab内存的动态分配
    neg_pos = 0; %用于记录neg_list中的待分析的像素点的个数
    pixdist = 0;
    %记录最新像素点增加到分割区域后的距离测度
    %下一次待分析的四个邻域像素点和当前种子点的距离
    %如果当前坐标为（x,y）那么通过neigb我们可以得到其四个邻域像素的位置
    neigb = [-1 0;
        1 0;
        0 -1;
        0 1];
    %开始进行区域生长，当所有待分析的邻域像素点和已经分割好的区域像素点的灰度值距离
    %大于reg_maxdis,区域生长结束

    while (pixdist < 0.06 && reg_size < numel(I))
        %增加新的邻域像素到neg_list中
        for j = 1:4
            xn = x + neigb(j, 1);
            yn = y + neigb(j, 2);
            %检查邻域像素是否超过了图像的边界
            ins = (xn >= 1) && (yn >= 1) && (xn <= Isizes(1)) && (yn <= Isizes(1));
            %如果邻域像素在图像内部，并且尚未分割好；那么将它添加到邻域列表中
            if (ins && J(xn, yn) == 0)
                neg_pos = neg_pos + 1;
                neg_list(neg_pos, :) = [xn, yn, I(xn, yn)]; %存储对应点的灰度值
                J(xn, yn) = 1; %标注该邻域像素点已经被访问过 并不意味着，他在分割区域内
            end

        end

        %如果分配的内存空问不够，申请新的内存空间
        if (neg_pos + 10 > neg_free)
            neg_free = neg_free + 100000;
            neg_list((neg_pos +1):neg_free, :) = 0;
        end

        %从所有待分析的像素点中选择一个像素点，该点的灰度值和已经分割好区域灰度均值的
        %差的绝对值时所待分析像素中最小的
        dist = abs(neg_list(1:neg_pos, 3) - reg_mean);
        [pixdist, index] = min(dist);
        %计算区域的新的均值
        reg_mean = (reg_mean * reg_size +neg_list(index, 3)) / (reg_size + 1);
        reg_size = reg_size + 1;
        %将旧的种子点标记为已经分割好的区域像素点
        J(x, y) = 2; %标志该像素点已经是分割好的像素点
        x = neg_list(index, 1);
        y = neg_list(index, 2);
        %     pause(0.0005);%动态绘制
        %     if(J(x,y)==2)
        %     plot(x,y,'r.');
        %     end
        %将新的种子点从待分析的邻域像素列表中移除
        neg_list(index, :) = neg_list(neg_pos, :);
        neg_pos = neg_pos -1;
    end

    J = (J == 2); %我们之前将分割好的像素点标记为2
    hold off;
    subplot(2,2,1),imshow(I),title('原图');
    subplot(2, 2, 2), imshow(J);
    J = bwmorph(J, 'dilate'); %补充空洞
    subplot(2, 2, 3), imshow(J);
    subplot(2, 2, 4), imshow(I + J);
    image_region_grow_result = I + J;
end
