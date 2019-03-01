#include <pcl_visualization/cloud_viewer.h>
int main (int argc, char *argv[])
{
	pcl::PointCloud<pcl::PointXYZRGB> cloud;
	//... populate cloud
	pcl_visualization::CloudViewer viewer("Simple Cloud Viewer");
	viewer.showCloud(cloud);
	while (!viewer.wasStopped())
	{
	}
	return 0;
}
