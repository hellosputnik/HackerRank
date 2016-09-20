try
{
    std::cout << Server::compute(A, B) << std::endl;
} catch(const std::bad_alloc &ba) {
    std::cout << "Not enough memory" << std::endl;
} catch(const std::exception &e) {
    std::cout << "Exception: " << e.what() << std::endl;
} catch(...) {
    std::cout << "Other Exception" << std::endl;
}
