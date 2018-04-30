#include <iostream>
#include "lmdb.h"

int main() {
    std::cout << "LMDB version: " << mdb_version(NULL, NULL, NULL) << "\n";
}
