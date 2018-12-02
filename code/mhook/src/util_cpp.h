#ifndef __UTIL_CPP_H__
#define __UTIL_CPP_H__


#ifdef __cplusplus
#include <cstddef>
extern "C" {
#endif


size_t get_peak();
int add_record(size_t addr, size_t mem_size);
int delete_record(size_t addr);

#ifdef __cplusplus
}
#endif

#endif


