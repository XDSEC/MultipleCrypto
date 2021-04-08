# MultipleCrypto

### 这个项目是干嘛的？

这个项目目的是，翻译那些在『开/闭源通用cms』里出现过的加密、解密函数，翻译成各种语言，以便以后可以直接拿来用。  
举个例子，在discuz里他自己实现了一个加密/解密的函数，语言是php。这个翻译项目的目的就是把这个函数翻译成其他语言，比如python、javascript。  
包括一些通用的密码算法，比如AES、XXTEA、3DES这种，也需要翻译（收集公开的项目也可以）。   

### 利用场景？

1. 假设discuz以后出现了一个UC API相关的漏洞，需要传递过去的数据在解密以后才能触发。那么我就可以直接使用py写exp。
2. 假设的一句话是用discuz自带的解密函数解密传入的数据并执行，那么我用C#写的一句话主控端就可以直接调用C#版的加密函数对数据进行加密。

etc.

### Project Layout

```
|-- root
    |-- source_language
        |-- function_name1
            |-- tests
                |> test1.*
                |> test2.*
            |> impl1.*
            |> impl2.*
        |-- function_name2
            |-- tests
                |> test1.*
                |> test2.*
            |> impl1.*
            |> impl2.*
```
