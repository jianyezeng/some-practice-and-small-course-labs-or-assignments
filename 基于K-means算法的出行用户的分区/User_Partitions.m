filename = 'data_customer.txt'; 
data = importdata(filename); 
location = [data(:,1:2);data(:,3:4)];
x = location(:,1);
y = location(:,2);
scatter(x,y,5,'filled','MarkerFaceColor',[0 .255 .5]);

K = 10;
[idx, C] = kmeans(location, K,'MaxIter', 1000);
gscatter(location(:,1), location(:,2), idx);
hold on;
plot(C(:,1), C(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 2,'DisplayName', '聚类中心');