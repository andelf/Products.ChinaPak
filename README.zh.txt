介绍
====

Plone 中文支持包.

目前只在 Plone 4 下测试过.

重新校对翻译了 ploe.app.locales 4.0.0 的 .po 文件. 可以认为是完整翻译.

同时包含一个中文的 id normalizer, 告别奇怪的十六进制字符串.

例如:

- u"你好" => "ni-hao"
- u"你好 Python" => "ni-hao-python"

为什么?
-------

当前 Plone 的中文翻译有很多错误, 而且很久没人维护了.

如何?
-----

灵感来自 http://www.zope.org/Members/panjunyong/ZopeChinaPak .

同时, 翻译文件添加方法来自 http://plone-regional-forums.221720.n2.nabble.com/plone4-how-to-override-translations-in-plone-app-locales-tt5456430.html .

联系
----

**andelf**

- e-mail: andelf@gmail.com
- location: Northeastern University of China

