#include <iostream>
#include <boost/numpy.hpp>
#include "Trajectory.h"
#include "Path.h"

using namespace boost::python;
namespace np = boost::numpy;

void SetupEigenConverters();

boost::shared_ptr<Trajectory> CreateCubicSpline(Eigen::MatrixXd const & pts,
                                                Eigen::VectorXd const & max_vel,
                                                Eigen::VectorXd const & max_accel,
                                                double timestep=0.001) {
    // Create path.
    int n = pts.cols();
    std::list<Eigen::VectorXd> path_pts;
    for (int i = 0; i < n; i++) {
        path_pts.push_back(pts.col(i));
    }
    Path path = Path(path_pts, 0.1);

    // Create cubic spline.
    boost::shared_ptr<Trajectory> spline(new Trajectory(path, max_vel, max_accel, timestep));

    std::cout << "c++ pts: \n" << pts << std::endl;
    std::cout << "c++ max vel: \n" << max_vel << std::endl;
    std::cout << "c++ max accel: \n" << max_accel << std::endl;
    std::cout << "c++ duration: " << spline->getDuration() << std::endl;

    return spline;
}

BOOST_PYTHON_MODULE(_cubic)
{
    np::initialize();
    SetupEigenConverters();

    class_<Trajectory,boost::shared_ptr<Trajectory>,boost::noncopyable>
        ("CubicSpline", no_init)
        .def("GetPosition", &Trajectory::getPosition)
        .def("GetVelocity", &Trajectory::getVelocity)
        .def("GetDuration", &Trajectory::getDuration)
        .def("IsValid", &Trajectory::isValid)
        ;

    def("CreateCubicSpline", &CreateCubicSpline)
        ;
}
