#include "leptjson.h"
#include <assert.h>
#include <stdlib.h>

#define EXPECT(c, ch) do{assert(*c->json == (ch)); c->json++;} while(0)
typedef struct{
    const char* json;
}lept_context;
