#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <clocale>

struct String {
    char* str;
    size_t len;
    bool isInit;

    String() {
        this->str = new char[1];
        if (this->str == NULL) {
            this->isInit = false;
            return;
        }
        this->str[0] = 0;
        this->len = 0;
        this->isInit = true;
    }

    String(const char* data) {
        if (data == NULL) {
            this->isInit = false;
            return;
        }
        size_t length = strlen(data);
        this->str = new char[length + 1];
        if (this->str == NULL) {
            this->isInit = false;
            return;
        }
        this->str[0] = 0;
        strcpy(this->str, data);
        this->len = length;
        this->isInit = true;
    }

    void Concat(const String& str) {
        if (!str.isInit || !this->isInit)
            return;

        char* newBuf = new char[this->len + str.len + 1];
        if (newBuf == NULL)
            return;
        std::copy_n(this->str, this->len + 1, newBuf);
        delete[] this->str;
        this->str = newBuf;
        strcat(this->str, str.str);
        this->len += str.len;
    }

    void ToUpperCase()
    {
        for (int i = 0; i < this->len; i++)
        {
            if (this->str[i] >= 97 && this->str[i] <= 122)
            {
                this->str[i] -= 32;
            }
            if (this->str[i] >= 224 && this->str[i] <= 255)
            {
                this->str[i] -= 32;
            }
            if (this->str[i] == 184) this->str[i] = 168;
        }
    }

    ~String() {
        if (this->isInit)
            delete[] this->str;
    }

};

int main() 
{
    setlocale(LC_ALL, "Rus");
    String s1("Hello, ");
    String s2("world!");
    s1.Concat(s2);
    s1.ToUpperCase();
    std::cout << s1.str << std::endl;

    if (s1.isInit)
        std::cout << s1.str << std::endl;
    if (s2.isInit)
        std::cout << s2.str << std::endl;
    return 0;
}