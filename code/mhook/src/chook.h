
#ifndef __MHOOK_UTIL_H__
#define __MHOOK_UTIL_H__

#ifdef __cplusplus
extern C {
#endif

void *malloc_hooked(size_t size);
void free_hooked(void *ptr);

#ifdef __cplusplus
}
#endif

#endif // __MHOOK_UTIL_H__
