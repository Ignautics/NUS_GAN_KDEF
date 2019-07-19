#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

void print_id(int i) {
  if ( i < 10) printf("0%d", i);
  else printf("%d", i);
}

int main(){
  freopen("get_image.bash", "w", stdout);

  for (int i = 1; i <= 35; i ++) {
    printf("cp ./AF");
    print_id(i);
    printf("/*.JPG ./ \n");
    printf("rm -rf AF");
    print_id(i);
    printf("\n");
  }
   for (int i = 1; i <= 35; i ++) {
    printf("cp ./AM");
    print_id(i);
    printf("/*.JPG ./\n");
    printf("rm -rf AM");
    print_id(i);
    printf("\n");
  }
  for (int i = 1; i <= 35; i ++) {
    printf("cp ./BF");
    print_id(i);
    printf("/*.JPG ./\n");
    printf("rm -rf BF");
    print_id(i);
    printf("\n");
  }
  for (int i = 1; i <= 35; i ++) {
    printf("cp ./BM");
    print_id(i);
    printf("/*.JPG ./\n");
    printf("rm -rf BM");
    print_id(i);
    printf("\n");
  }




  return 0;
}
