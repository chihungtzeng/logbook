#include <vector>
#include <iostream>
#include <cstring>
#include <zstd.h>
#include <glog/logging.h>

// g++ -std=c++11 zstd_vector.cpp -lzstd -lglog

int main(int argc, char* argv[])
{
  std::vector<int> org;
  const size_t ub=1024*16;
  for(int i=0; i<ub; i++){
    org.push_back(i%64);
  }
  size_t const cmpr_ub = ZSTD_compressBound(org.size()*sizeof(int));
  LOG(INFO) << "org size: " << org.size()*sizeof(int) << " cmpr_ub: " << cmpr_ub;
  void * const cmpr_data = malloc(cmpr_ub);
  size_t cmpr_size = ZSTD_compress(cmpr_data, cmpr_ub, reinterpret_cast<void *>(org.data()), org.size()*sizeof(int), 1);
  LOG(INFO) << "cmpr_size: " << cmpr_size;

/* decmpr */
  size_t decmpr_size = ZSTD_getFrameContentSize(cmpr_data, cmpr_size);
  std::vector<int> decmpr_data;
  decmpr_data.reserve(decmpr_size/sizeof(int));

  size_t actual_decmpr_size = ZSTD_decompress(reinterpret_cast<void *>(decmpr_data.data()), decmpr_size, cmpr_data, cmpr_size);
  LOG(INFO)<< "decmpr_size: " << decmpr_size << " actual: " << actual_decmpr_size;


  for(int i=0; i<ub; i++){
    CHECK(org[i] == decmpr_data[i]);
  }
  LOG(INFO) << "match!";
  free(cmpr_data);
  return 0;
}
