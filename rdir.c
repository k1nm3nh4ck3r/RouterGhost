#include <unistd.h>
#include <sys/types.h>
#include <dirent.h>
#include <stdio.h>
#include <string.h>

void listdirint(const char *name, int indent);

void handle_dir(char* name, char* filename, int indent){
   char path[1024];
   int space = 0;
   snprintf(path, sizeof(path), "%s/%s", name, filename);
   space = 40 - indent -strlen(filename);
   if(space <= 0){
      space = 1;
   }
   printf("%*s[%s]%*s%s\n", indent, "", filename, space, "", path);
   listdirint(path, indent + 2);
}


void handle_file(char* name, char* filename, int indent){
   char path[1024];
   int space = 0;
   snprintf(path, sizeof(path), "%s/%s", name, filename);
   space = 40 - indent -strlen(filename);
   if(space <= 0){
      space = 1;
   }
   printf("%*s- %s%*s%s\n", indent, "", filename, space, "", path);
}

void listdirint(const char *name, int indent) {
   DIR *dir;
   struct dirent *entry;

   if (!(dir = opendir(name)))
      return;

   while ((entry = readdir(dir)) != NULL) {
      if (entry->d_type == DT_DIR) {
         if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;
         handle_dir(name, entry->d_name, indent);
      } else {
         handle_file(name, entry->d_name, indent);
      }
   }
   closedir(dir);
}

void listdir(const char* name){
   listdirint(name, 0);
}

void main(int argc, char* argv[]){
   char* path = ".";
   if(argc >= 2){
      path = argv[1];
   }
   listdir(path);
}
