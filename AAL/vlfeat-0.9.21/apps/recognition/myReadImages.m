function final_im = myReadImages(intial_im)
% READIMAGE   Read and standardize image
%    [IM, SCALE] = READIMAGE(IMAGEPATH) reads the specified image file,
%    converts the result to SINGLE class, and rescales the image
%    to have a maximum height of 480 pixels, returing the corresponding
%    scaling factor SCALE.
%
%    READIMAGE(IM) where IM is already an image applies only the
%    standardization to it.

% Author: Andrea Vedaldi

% Copyright (C) 2013 Andrea Vedaldi
% All rights reserved.
%
% This file is part of the VLFeat library and is made available under
% the terms of the BSD license (see the COPYING file).

% if ischar(imagePath)
%   try
%     im = imread(imagePath) ;
%   catch
%     error('Corrupted image %s', imagePath) ;
%   end
% else
%   im = imagePath ;
% end

% intial_size = size(im);
% Convert image to single precision
intial_im = im2single(intial_im) ;


scale = 1 ;
if (size(intial_im,1) > 480)
  scale = 480 / size(intial_im,1) ;
  % �� A �ĳ�����С���� scale ��֮���ͼ��;��� A ����������ά�ȣ��� imresize ֻ����ǰ����ά�ȵĴ�С��
  temp_im = imresize(intial_im, scale) ;
  %����ʲô��˼���� --- ȷ��ͼ���е���������ֵ��0.0000~1.0000֮��
  final_im = min(max(temp_im,0),1) ;
else
    final_im = double(intial_im)/255;
end
