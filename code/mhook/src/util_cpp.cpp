
#include <util_cpp.h>
#include <mbook.h>


extern "C" {
    MBook mbook;

    size_t get_peak() {
        return mbook.get_peak();
    }
    int add_record(size_t addr, size_t mem_size) {
        return mbook.add_record(addr, mem_size);
    }
    int delete_record(size_t addr){
        return mbook.delete_record(addr);
    }
}

