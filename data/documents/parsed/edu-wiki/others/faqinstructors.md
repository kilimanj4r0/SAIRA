






FAQInstructors
==============






Contents
--------


* [1 Introduction to MediaWiki](#Introduction_to_MediaWiki)
	+ [1.1 The structure of the content](#The_structure_of_the_content)
		- [1.1.1 Structure of syllabi](#Structure_of_syllabi)
		- [1.1.2 Structure of Teaching Regulation Document](#Structure_of_Teaching_Regulation_Document)
		- [1.1.3 Individual instructors' pages](#Individual_instructors.27_pages)
* [2 Content editing](#Content_editing)
	+ [2.1 How to log in the system?](#How_to_log_in_the_system.3F)
	+ [2.2 How to create a page?](#How_to_create_a_page.3F)
	+ [2.3 How to edit a page?](#How_to_edit_a_page.3F)
	+ [2.4 How to work with text and its structuring?](#How_to_work_with_text_and_its_structuring.3F)
		- [2.4.1 How to structurize a text?](#How_to_structurize_a_text.3F)
		- [2.4.2 How to format text?](#How_to_format_text.3F)
		- [2.4.3 How to use HTML tags?](#How_to_use_HTML_tags.3F)
		- [2.4.4 How to work with lists?](#How_to_work_with_lists.3F)
		- [2.4.5 How to insert a link?](#How_to_insert_a_link.3F)
	+ [2.5 How to format tables?](#How_to_format_tables.3F)
	+ [2.6 How to work with math formulas?](#How_to_work_with_math_formulas.3F)
	+ [2.7 How to put a source code?](#How_to_put_a_source_code.3F)
	+ [2.8 How to add TikZ-flowchart?](#How_to_add_TikZ-flowchart.3F)
	+ [2.9 How to paste pictures?](#How_to_paste_pictures.3F)
	+ [2.10 How to embed a Google document into mediawiki page?](#How_to_embed_a_Google_document_into_mediawiki_page.3F)
* [3 Content import / export](#Content_import_.2F_export)
	+ [3.1 How to import content?](#How_to_import_content.3F)
	+ [3.2 How to export content?](#How_to_export_content.3F)
		- [3.2.1 To PDF-file](#To_PDF-file)



Introduction to MediaWiki
=========================


The MediaWiki software is used by tens of thousands of websites and thousands of companies and organizations. It powers Wikipedia and also this website. MediaWiki helps you collect and organize knowledge and make it available to people. It's powerful, multilingual, free and open, extensible, customizable, reliable, and free of charge.



The structure of the content
----------------------------


### Structure of syllabi


 **Core courses** 
The lists of the core courses are placed here:



* [Core courses](https://eduwiki.innopolis.university/index.php/List_of_core_courses)


 **Elective courses** 


The lists of the elective courses are placed here:



* [Electives](https://eduwiki.innopolis.university/index.php/List_of_Electives)


### Structure of Teaching Regulation Document


Overall teaching regulation can be found here:



* [Overall teaching regulations](https://eduwiki.innopolis.university/index.php/OverallRegulations)


### Individual instructors' pages


By the following link you can find your personal instructor's page, edit it or create, if necessary. It's highly recommended to preserve common structure of the page during editing.



* [The list of instructors](https://eduwiki.innopolis.university/index.php/Professors)


Content editing
===============


How to log in the system?
-------------------------


Use your regular credentials for this purpose: user@innopolis.ru and the password from your account.
If you cannot log in, please contact the IT-department [@iuithelp](https://t.me/iuithelp)



How to create a page?
---------------------


 **From the search box** 
If you search for a page that doesn't exist, then you will be provided with a link to create the new page.


 **Using the URL** 
You can use the wiki's URL for creating a new page.


The URL to an article of the wiki is usually something like this:



* <https://eduwiki.innopolis.university/index.php/ARTICLE>


If you replace ARTICLE with the name of the page you wish to create, you will be taken to a blank page which indicates that no article of that name exists yet.




> To get more detailed information you can refer to the user's manual: 
> [Help: Starting a new page](https://www.mediawiki.org/wiki/Help:Starting_a_new_page)
> 
> 


How to edit a page?
-------------------


Clicking the "Edit" page tab at the top of the page will take you to the edit page for that article, where you can create the new page by typing your text, and clicking submit. Moreover, if you need not edit the whole page but only its part, you can click on "Edit" link related to this certain part and work only with it. If the text is so long it helps to save a time.


Note that only the authorized users are able to edit the content.




> Here you can get more information about the editing process: [Help:Editing pages](https://www.mediawiki.org/wiki/Help:Editing_pages)
> 
> 


How to work with text and its structuring?
------------------------------------------



> Detailed user guide on text formatting: [MediaWiki: User guide](https://en.wikibooks.org/wiki/MediaWiki_User_Guide)
> 
> 


### How to structurize a text?


Headings are created using sequences of "=" characters, placed before the heading title and after the heading title, on the same line. The level of headings is determined by the number of "=" characters.


Examples:





| Level
 | Example
 |
| --- | --- |
| 2.
 | ==Plants==
 |
| 3.
 | ===Plants===
 |
| 4.
 | ====Plants====
 |


*Start level:* 2


Do not use headings of level 1, such as "=Title="; start with level 2 instead. The heading at level 1 is used for the title of the page.


*Maximum level:* 6


The maximum level of a heading is 6, rendered using ======Heading L6======. Entering a heading with 7 equals-signs such as =======Heading L7======= results in the creation of a heading of the level 6, with one equal-sign becoming part of the text of the heading: "=Heading L7=".




> See more details here: [MediaWiki user guide: sections and headings](https://en.wikibooks.org/wiki/MediaWiki_User_Guide/Sections_and_Headings)
> 
> 


### How to format text?


The following is an overview of text formatting available in Mediawiki:





Basic text formatting
| Formatting
 | Markup
 | Note
 |
| --- | --- | --- |
| **Boldface** | `'''text'''` |  |
| *Italics* | `''text''` |  |
| ***Boldface and italics*** | `'''''text'''''` |  |
| **[Boldface combined with wikilink](/index.php?title=Boldface_combined_with_wikilink&action=edit&redlink=1 "Boldface combined with wikilink (page does not exist)")** | `'''[[text]]'''` | The reverse order of ticks and brackets does not work: `[['''text''']]` |


Other text formatting such as underline or blockquote needs to be done using HTML tags, including U for underline, TT for typewriter text, S for strikethrough, SUB for lower index and SUP for upper index.



### How to use HTML tags?


Text formatting can also be done using HTML and CSS. Some of the most useful HTML elements are:





Most needed HTML markup
| Task
 | Markup
 | Note
 |
| --- | --- | --- |
| Preformatted text
 | 
```
<pre>
 preformatted
</pre>

```
 | The effect in wiki differs from the one in HTML; in wiki, the text within the PRE element is treated as within NOWIKI element, leaving all the HTML and wiki markup uninterpreted.
 |
| Blockquote
 | 
```
<blockquote>Longer passage.</blockquote>

```
 |
| Comments
 | 
```
<!-- comment -->

```
 | Avoid nesting, such as 
```
<!-- <!-- comment --> -->

```
 |
| Generic inline element
 | 
```
<span style="TODO"></span>

```
 | Can be styled arbitrarily using cascading style sheets - CSS.
 |
| Generic block element
 | 
```
<div style="TODO"></div>

```
 | Can be styled arbitrarily using cascading style sheets - CSS.
 |


Some HTML elements are not allowed, such as A and IMG.



### How to work with lists?


Bullet lists:





| Example Syntax
 | Example Output
 |
| --- | --- |
| 
```
* a
** b
** c
*** d

```
 | * a
	+ b
	+ c
		- d
 |


Numbered lists:





| Example Syntax
 | Example Output
 |
| --- | --- |
| 
```
# a
## b
## c
### d

```
 | 1. a
	1. b
	2. c
		1. d
 |


Definition lists:





| Example Syntax
 | Example Output
 |
| --- | --- |
| 
```
; defined term : definition
; defined term 2 : definition 2

```
 | defined term
definition
defined term 2
definition 2 |


Mixed lists:





| Example Syntax
 | Example Output
 |
| --- | --- |
| 
```
 * a
 *# b
 *# c

```
 | * a
	1. b
	2. c
 |


### How to insert a link?


There are five types of hypertext links in MediaWiki, but two of them are the mostly used:



* Internal links to other pages in the same wiki (commonly called "wikilinks")
* External links to pages at other websites


 **Internal hyperlinks** 





| Task
 | Markup
 |
| --- | --- |
| Internal hyperlink
 | [[keyword]]
 |
| Internal hyperlink to a section
 | [[keyword#section\_heading|link title]]
 |
| Internal hyperlink showing a different word
 | [[keyword|its appearance]]
 |
| Internal hyperlink with a tooltip
 | [[keyword|<span title="A tooltip">its appearance</span>]]
 |
| Internal hyperlink in bold
 | '''[[keyword]]'''
 |


 **External hyperlinks** 





| Task
 | Markup
 |
| --- | --- |
| External hyperlink
 | [URL\_containing\_no\_spaces title of the URL]
 |



> You can also fing some more details here: [Help: links](https://www.mediawiki.org/wiki/Help:Links)
> 
> 


How to format tables?
---------------------


The following code




```
{| class="wikitable" style="height:14em;"
|-
! Left !! Center !! Right
|-
| Top left cell || Top center cell || Top right cell
|- style=height:7em
| Middle left cell || Middle center cell || Middle right cell
|-
| Bottom left cell || Bottom center cell || Bottom right cell
|}

```

gives the following:





| Left | Center | Right
 |
| --- | --- | --- |
| Top left cell | Top center cell | Top right cell
 |
| Middle left cell | Middle center cell | Middle right cell
 |
| Bottom left cell | Bottom center cell | Bottom right cell
 |



> Basics: [MediaWiki User guide: Tables](https://en.wikibooks.org/wiki/MediaWiki_User_Guide/Tables)
> 
> 



> Advanced: [Wiki: Tables](https://en.wikipedia.org/wiki/Help:Table)
> 
> 


How to work with math formulas?
-------------------------------


You can enter mathematical formulas into a wiki, using a `math` tag, such as:




```
<math>\sqrt{2}</math>

```

The formulas are marked up in the TeX markup, the markup of a complex typesetting system specialized on mathematics.


  

To get started, follow the examples below.





Examples of mathematical markup
| No.
 | Desired Effect
 | Markup
 |
| --- | --- | --- |
| 1.
 | 



α


{\displaystyle \alpha }

{\displaystyle \alpha } | 
```
<math>\alpha</math>

```
 |
| 2.
 | 





2




{\displaystyle {\sqrt {2}}}

{\displaystyle {\sqrt {2}}} | 
```
<math>\sqrt{2}</math>

```
 |
| 3.
 | 





1
−

e

2






{\displaystyle {\sqrt {1-e^{2}}}}

{\displaystyle {\sqrt {1-e^{2}}}} | 
```
<math>\sqrt{1-e^2}</math>

```
 |
| 4.
 | 





2
4


=
0.5


{\displaystyle {\frac {2}{4}}=0.5}

{\displaystyle {\frac {2}{4}}=0.5} | 
```
<math>\frac{2}{4}=0.5</math>

```
 |
| 5.
 | 




∑

k
=
1


N



k

2




{\displaystyle \sum \_{k=1}^{N}k^{2}}

{\displaystyle \sum _{k=1}^{N}k^{2}} | 
```
<math>\sum\_{k=1}^N k^2</math>

```
 |
| 6.
 | 




∫

1


3






e

3



/

x


x

2





d
x


{\displaystyle \int \limits \_{1}^{3}{\frac {e^{3}/x}{x^{2}}}\,dx}

{\displaystyle \int \limits _{1}^{3}{\frac {e^{3}/x}{x^{2}}}\,dx} | 
```
<math>\int\limits\_{1}^{3}\frac{e^3/x}{x^2}\, dx</math>

```
 |
| 7.
 | 





[



0


⋯


0




⋮


⋱


⋮




0


⋯


0



]




{\displaystyle {\begin{bmatrix}0&\cdots &0\\\vdots &\ddots &\vdots \\0&\cdots &0\end{bmatrix}}}

{\displaystyle {\begin{bmatrix}0&\cdots &0\\\vdots &\ddots &\vdots \\0&\cdots &0\end{bmatrix}}} | 
```
<math>\begin{bmatrix}
  0      & \cdots & 0      \\
  \vdots & \ddots & \vdots \\ 
  0      & \cdots & 0
\end{bmatrix}</math>

```
 |
| 8.
 | 





(



x


y




z


v



)




{\displaystyle {\begin{pmatrix}x&y\\z&v\end{pmatrix}}}

{\displaystyle {\begin{pmatrix}x&y\\z&v\end{pmatrix}}} | 
```
<math>\begin{pmatrix}
  x & y \\
  z & v 
\end{pmatrix}</math>

```
 |


How to put a source code?
-------------------------


The following code:




```
‎<syntaxhighlight lang="python" line>
def quick_sort(arr):
	less = []
	pivot_list = []
	more = []
	if len(arr) <= 1:
		return arr
	else:
		pass
‎</syntaxhighlight>

```

gives:



‎


```
def quick\_sort(arr):
	less = []
	pivot\_list = []
	more = []
	if len(arr) <= 1:
		return arr
	else:
		pass‎

```


> See the documentation of the syntaxhighlight-extension here: [Syntax highlight](https://www.mediawiki.org/wiki/Extension:SyntaxHighlight)
> 
> 


How to add TikZ-flowchart?
--------------------------


With the use of the special extension you can embed the TikZ-flowchart written in LaTex directly to your page within the tag 


```
<PGTikZ>
```
.


For examle, the following code




```
<PGFTikZ>
[[File:My_image_1.png|400px|test image]]

<PGFTikZPreamble>

\usepackage{tikz}
\usetikzlibrary{arrows}
\usetikzlibrary{intersections}
\usetikzlibrary{calc}

</PGFTikZPreamble>
\begin{tikzpicture}[scale=.8,every node/.style={minimum size=1cm}]
%
   \begin{scope}[
           yshift=-83,every node/.append style={
           yslant=0.5,xslant=-1},yslant=0.5,xslant=-1
           ]
       \draw[step=4mm, black] (0,0) grid (5,5); 
       \draw[black,thick] (0,0) rectangle (5,5);%borders
       \fill[green] (2.05,2.05) rectangle (2.35,2.35); % center pixel
       \fill[green] (1.65,2.05) rectangle (1.95,2.35); %left
       \fill[green] (2.45,2.05) rectangle (2.75,2.35); %right
       \fill[green] (2.05,2.45) rectangle (2.35,2.75); %top
       \fill[green] (2.05,1.95) rectangle (2.35,1.65); %bottom

   \end{scope}
%
% draw annotations
%
   \draw[-latex,thick,green](-3,-2)node[left]{1 patch}
       to[out=0,in=200] (-1,-.9);
\end{tikzpicture}
</PGFTikZ>

```

[![test image](/img_auth.php/0/04/My_image_1.png)](/index.php/File:My_image_1.png "test image")




> See the instructions here: [PGTikZ](https://www.mediawiki.org/wiki/Extension:PGFTikZ)
> 
> 


How to paste pictures?
----------------------


Mediawiki supports the use of images in various formats. In order to be used in a wiki, image first needs to be uploaded. To upload the picture please use the link "Upload file" in the left menu column of the page and follow the certain instructions.


The following is an overview of placing images into pages, such images that have already been uploaded.





Placing of images
| Task
 | Markup
 | Default Frame
 | Note
 |
| --- | --- | --- | --- |
| Image
 | [[Image:image\_name.png]]
 | No
 | The image is shown in its full size as found in the file.
 |
| Image with thumb
 | [[Image:image\_name.png|thumb|A caption text of the image.]]
 | Yes
 | Thumbs are always scaled down so as not to exceed an upper limit on the size.
 |
| Image without thumb, with restricted size
 | [[Image:image\_name.png|150px]]
 | No
 |  |



> To know about other feature please refer to: [MediaWiki User Guide: images](https://en.wikibooks.org/wiki/MediaWiki_User_Guide/Images)
> 
> 


How to embed a Google document into mediawiki page?
---------------------------------------------------


Special extension allows to embed Google Docs' spreadsheets into the wiki page.


Supported parameters are:





| Name | Default
 |
| --- | --- |
| **width** | 500
 |
| **height** | 300
 |
| **style** | width:100%
 |


As an example using all of the parameters:




```
<googlespreadsheet width="600" height="200" style="width:50%">Google Docs' key goes here</googlespreadsheet>
```

To actually embed a spreadsheet, the spreadsheet needs to be published with Google's **File** > **Publish to Web...** option. It is not sufficient to just have a shareable link.



Content import / export
=======================


How to import content?
----------------------


 **From Latex file** 


To upload your syllabus from Latex to MediaWiki use the toolkit developed by our students:



* [Syllabus in Latex: import](https://dev.digitalprofile.innopolis.university/generator/eduwiki/upload)


How to export content?
----------------------


### To PDF-file


To get a printable version of the certain page use the link **Printable version** at the left column of the page. After the page is generated you may print it as usually.











