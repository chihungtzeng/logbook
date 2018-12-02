#ifndef __MBOOK_H__
#define __MBOOK_H__

#include <map>
#include <cstddef>

class MBook {
private:
    size_t m_peak;
    size_t m_current_usage;
    std::map<size_t, size_t> m_allocation;
    bool m_locked;

public:
    MBook();
    size_t get_peak();
    size_t get_current_usage();
    int add_record(size_t addr, size_t mem_size);
    int delete_record(size_t addr);
    

private:
    int update_peak();
    void find_addr_and_delete_current_usage(size_t addr);
};

#endif // __MBOOK_H__
