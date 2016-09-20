std::cout << std::setw(0)
          << std::showbase
          << std::hex
          << std::nouppercase
          << static_cast<long>(A)
          << std::endl;

std::cout << std::setw(15)
          << std::right
          << std::setfill('_')
          << std::showpos
          << std::setprecision(2)
          << std::fixed
          << B
          << std::endl;

std::cout << std::noshowpos
          << std::setprecision(9)
          << std::fixed
          << std::scientific
          << std::uppercase
          << C
          << std::endl;

