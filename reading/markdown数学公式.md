# markdown数学公式语法

markdown支持完整LaTex数学公式语法

#### 1.上标和下标
- 下标使用符号`Y_1`表达,公式表达结果为: $$$ y_1 $$$
- 上标使用 `X^{2m}`或者`X^2`, 其中较为复杂的表达式用`{}`包含, 公式表达结果为: $$$X^{2m}+X^2$$$

#### 2.常见运算符
符号|表达式|符号|表达式|符号|表达式
---|---|---|---|---|---
$$$\pm$$$|\pm|$$$\times$$$|\times|$$$\div$$$|\div
$$$\cdot$$$|\cdot|$$$\leq$$$|\leq|$$$\geq$$$|\geq
$$$\neq$$$|\neq|$$$\approx$$$|\approx|$$$\equiv$$$|\equiv
$$$\in$$$|\in|$$$\notin$$$|\notin|$$$\subset$$$|\subset
$$$\supset$$$|\supset|$$$\bigcap$$$|\bigcap|$$$\bigcup$$$|\bigcup

#### 3.特殊符号
- 求和符号: 使用`\sum` 转义表达求和符号,下限符号使用`_{m}`,上限符号使用`^\infty`, 如:  $$$ \sum_{m=0}^\infty  $$$
- 积分符号: `\int_0^1`转义表达积分符号, 如: $$$ \int_0^1$$$
- 极限符号: `\lim_{变量 \to 表达式} 表达式`, 如 $$$  \lim_{1 \to 5} 表达式 $$$
- 向量符号: `\vec{a}`转义表达向量, 如: $$$\vec{a}$$$
- 空格符号: markdown支持四种空格` \, 、\;、\quad 和 \qquad `

#### 4.希腊字母的大小写
希腊字母的大写使用首字母大写`\Gamma`转义,小写使用首字母小写`\gamma`转义, 公式表达结果为: $$$\Gamma$$$  和   $$$\gamma$$$
#### 5.关于注释
- 公式注释: 使用`\text{内容}`转义注释,公式表达结果为: $$$ \text {公式注释}$$$
- 文字颜色: 使用`\color{颜色}{文字}`转义表达带颜色的文字,公式表达结果为:  $$$\color{green}{文字} $$$

#### 6.分数
分数使用`\frac{part I}{part II}`转义表达,公式表达结果为: $$$ \frac{(-1)^m}{m!(m + 1)}$$$
#### 7.公式中的大括号或大分隔符
- 在配对符号中.如公式中的括号使用`\left(`表达左括号,使用`\right)`转义表达向右的括号;如: $$$ \left({\frac{x}{2} }\right) $$$
- 在非配对符号中以`\left. 其他 \right符号` 或 `\left符号 其他 \right.` 表非配对的较大符号.如: $$$\left.\frac{du}{dx}\right|_{x=0}$$$
- 注: 转义表达不需要`{ 和 }`

#### 8.上划线与下划线
上划线使用`\overline{}`转义表达,下划线使用`\underline{}`转义表达,公式表达结果为: $$$\overline{a+b+c+d}$$$和$$$\underline{a+b+c+d}$$$

#### 9.开根号
多次方根使用`\sqrt[n]{x}`,其中`n`表示根的次数,`x`表示被开方项,公式表达结果为: $$$\sqrt[n]{3}$$$

#### 10.方程组
1.表达方式一: 使用`\begin{array}{c}  表达式一\\表达式二... \end{array}`
$$
\left\{ 
\begin{array}
{a}
a_1x+b_1y+c_1z=d_1 \\ 
a_2x+b_2y+c_2z=d_2
\end{array}
\right. 
$$
2.表达方式二: 使用`\begin{cases}…\end{cases}`
$$
f(n) = 
\begin{cases}
\frac{n}{2},  & \text{if $n$ is even} \\[2ex]
3n+1, & \text{if $n$ is odd}
\end{cases}
$$

注: 关于`\\[2ex]`一个 [ex] 指一个 “X-Height”，即x字母高度。可以根据情况指定多个 [ex]，如 [3ex]、[4ex] 等。 其实可以在任何地方使用 \\[2ex] 语句，只要你觉得合适。

#### 12.使用HTML语法表达数学公式
- 上标与下标的表达: 使用标签`<sub>`和`<sup>`表达, 表达结果为: <sub>text</sub> 与<sup>text</sup>
- 上划线表达: 使用标签`<SPAN style="TEXT-DECORATION: overline">X</SPAN>`表达,表达结果为: <SPAN style="TEXT-DECORATION: overline">X</SPAN>



#### 13.补充
对于部分符号无法用 markdown 的公式表达,可以使用 `\符号` 转义表达,如 $$$ \%  $$$等



