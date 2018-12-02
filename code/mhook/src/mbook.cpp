#include <mbook.h>
#include <stdio.h>
#include <iostream>

MBook::MBook() {
    m_peak = 0;
    m_current_usage = 0;
    m_locked = false;
}

size_t MBook::get_peak(){
    return m_peak;
}

size_t MBook::get_current_usage() {
    return m_current_usage;
}

int MBook::add_record(size_t addr, size_t mem_size) {
    if (m_locked) {
        return 0;
    }
    std::cout << "add_record: addr " << std::hex  << addr << " mem_size: " <<std::dec << mem_size <<  std::endl;
    m_locked = true;
    //find_addr_and_delete_current_usage(addr);
    m_allocation[addr] = mem_size;
    m_current_usage += mem_size;
    update_peak();
    m_locked = false;

    return 0;
}

int MBook::delete_record(size_t addr){
    find_addr_and_delete_current_usage(addr);
    // since deletion does not increase memory usage, we don't update
    // m_peak here.
    return 0;
}

// private functions
int MBook::update_peak(){
    if (m_current_usage > m_peak){
        m_peak = m_current_usage;
    }
    return 0;
}

void MBook::find_addr_and_delete_current_usage(size_t addr){
    if (m_allocation.count(addr)){
        m_current_usage -= m_allocation[addr];
        m_allocation.erase(addr);
        std::cout << "delete record at " << std::hex  << addr << std::endl;
    }
    else {
        std::cout << "cannot find addr record at " << std::hex  << addr << std::endl;
    }
}

