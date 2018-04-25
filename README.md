Purpose
--

This repo contains the daily to-do lists and what actually done.
It is my notes about what I have learned, and the notes are not guarantee to be correct.
I use it to keep track of my activities as another form of dairy.

這個 repo 為個人的to-do list，以及實際上完成了那些todo。此處內容僅為個人的筆記並當作一種日誌在寫，並不保証正確性。

Logs
--

2018
* 4/25 研究如何從Python call C的function (為了加快程式的速度)
* 3/12~4/25 小犬出生，放下手邊所有工作。
* 3/11 預計：研究buildbot以建出一個work flow.實際: Done. 原本的test environment寫得比較自由，沒有考慮到buildbot會把repository命名為build, 造成測試程式不會執行，把這個情況考慮進test plan裡才算整合完成。
* 3/10 預計：研究phabricator, git push, code review要如何整合。實際：Done. phabricator那邊主要是做code review, review完了之後，user還是要自己執行git commit and git push。
  * 為了控制那些commit可以push到remote repository, 在remote repository那邊要設好pre-receive hook, 只要hook return 1, 上code的人就無法把成功執行git push.
* 3/9 預計：研究unsupervised learning。實際：大略把unsupervised learning的研究成果掃過一遍，有些研究和NLP處理相關，但還不知道可以怎麼應用。
* 3/8 預計：檢查証據列表是否有其他的模式尚未被找出來。實際:Done.
  * 學到了mini-batch和epoch這兩個術語的差別。
* 3/7 預計：找出証據列表的句子。實際：Done.
* 3/6 預計：把類別名稱做正規化，現行不同的類別名稱其實對應到同一類別，應統一化他們。實際：Done.
  * 摘錄Misbehaving裡一段對behavioral economics的defense (Chapter 17): I tend to view to study of behavioral extensions of these efficient market models as leading in a sense to the enhancement of the efficient market models. I could teach the efficient market models to my students with much more relish if I could describe them as extreme special cases before moving to the more realistic models.
* 3/5 預計：把文字內容做正規化，把各別作者的寫作差異儘量消除掉。實際：Done.
* 3/4 預計：完成db的重組。實際：會造成程式當掉的case都已處理完成，但極少數的document太肥，超過了db對單一document的大小限制，於是重新layout。
  * 看了CNN(Convolutional Neural Network)的作法和程式，CNN是個很強的工具，但tensorflow包得很high level, 目前我對CNN的知識還不足以駕御使用它。
* 3/3 預計：為了方便管理，對db的layout做出大改動。實際：In progress, 要處理的document太多，而且原始的document多有誤失，讓程式當掉，整個過程就在修修補補中進行。
* 3/2 預計：開會討論未來的工作。實際：Done.
* 3/1 預計：實作對段落做摘要的程式。實際：Done. 成效上看起來還OK, 段落長度太短的跑不出結果，10句以上的段落較看得出成果，不過缺了benchmark, 無法驗証程式的優劣；另外試圖把中文的輸入改成可以讓內建的英文版程式執行，但常出現exception, 應是不了解原生程式內在邏輯造成的。
* 2/28 預計：把TextRank改成適合我們的樣子。實際：Done. 目前尚看不出來能拿來做什麼。
* 2/27 預計：對段落做分類。實際：用程式對一些基本屬性做了分類，未來在分析時，希望可以不用處理太多不相關的資料。
* 2/26 預計：研究PageRank的實作方式。實際：Done. 大致了解為什麼是用eigenvector算pagerank。
* 2/25 預計：研究自動摘要及TextRank的演算法。實際：已了解大致的流程，其最後都會回到PageRank的算法，目前還不清楚為什麼在實作中的PageRank是用eigenvector作為rank。
* 2/24 預計：研究自動摘要的演算法。實際：被段落屬性的判斷程式給佔住時間了，還沒讀完paper.
* 2/23 預計：研究page rank. 實際：原始的idea不難，容易理解。
  * 重新實作主刑條文的程式，執行速度變慢，但可找出更正確的條文。
* 2/22 預計：提高主刑條文的正確率。實際：正確率拉高到82%左右，有許多是簡易形式的判決，直接引用檢察官的資料，這種的找不出主刑條文的模式。
* 2/21 預計：把主刑的條文及其對應的法律名稱parse出來。實際：Done. 其中條文對應到的罪名並非一致，每個主筆人會用自己慣用的名稱。
  * 使用unicodedata的function企圖對全文部分做normalize.
* 2/15~2/20 農曆新年，休息。
  * 家中電腦因硬體問題，常常在emerge時出現segmentation fault，解決方法:
  ```
  ebuild xxx.ebuild compile
  ebuild xxx.ebuild install
  ebuild xxx.ebuild qmerge
  ```
* 2/14 預計：把刑事案的主條文找出來。實際:進行中，目前方法可以找出75%的資料。
* 2/13 預計：研究非數值資料在logistic regression 中要如何處理。實際：pandas 裡有內建get_dummies和join的function call, 可以處理此問題，例如，如果變數sex有male和female兩個值，就建出sex_male 和 sex_femal兩個dummy variables, 其值為0或1，之後再交給logistic regression處理。
* 2/12 預計：研究Logistic Regression. 實際：sklearn裡有內建的function, 看起來是很有趣也實用的概念，要想一下可以應用在那裡。
* 2/11 預計：研究T149這個issue. 實際: Done. 非我程式之因也。
* 2/10 預計：研究一下doc2vec及其應用。實際：使用內線交易的段落去訓練doc2vec, 但相似性比對的結果沒有很好。
* 2/9 預計：畫出word2vec的high level diagram. 實際：Done.
  * neural network的inner layer weights和output layer weights更新動作及目的和我猜測的相去不遠，都是為了把output調到(1, 0, 0,...). 在更新的過程中用到了外積等運算，讓程式看來很難懂。
* 2/8 預計：繼續trace word2vec. 實際：把程式做了一些註解，放在[code](code/20180208/word2vec.py).
  * [word2vec_commented](https://github.com/chrisjmccormick/word2vec_commented): A great reference to understanding word2vec.
* 2/7 預計：繼續trace word2vec的程式。實際：到google查word2vec的詳細流程圖，沒找到太具體的結果，就真的trace程式吧。
  * wv.vocab 長度為unique字詞的數量
  * wv.index2word[index] 可 return 對應的字串
  * syn1neg: type 為 numpy.ndarray, 大小為 (|words| * |vector dimension|), 初始值全為 0.
  * vectors_lockf: type 為 numpy.ndarray, 大小為 (|words| * 1), 初始值全為 1.
* 2/6 預計：trace word2vec的程式。實際：去外地拜訪親友，只驗証了是否word embedding是否長度為1.
* 2/5 預計：把原告主張的段落用點選的方式顯示。實際：Done. 用collapse做比dropdown menu來得簡潔。
* 2/4 預計：沿續前一天的事務，把前端的功能做出來。實際：Done.
* 2/3 預計：把同判決書的有關慰撫金的段落整合在一起。實際：Done.
* 2/2 預計：實作排除具有特定字詞的功能。實際: Done.
  * 和從事協調理賠的從業人員聊天，說到他們實務上是把紛爭交給內勤處理，內勤照章辦事，若有談不瓏的地方，就交給法院裁決，最後法院判多少就給多少。雖然看來把慰撫金的功能推銷給他們這件事沒門了，還是很感謝他們坦白相告。
* 2/1 預計：找出何謂故意。實際：Done.
* 1/31 預計：找何謂良善風俗。實際：Done. 不過效果看來沒有很好，許多只是引用法條。
* 1/30 預計：研究如何做fuzzy search. 實際：重新train word2vec的model, 這次使用iterator, 可訓練超過百億個字。
* 1/29 預計：把設定功能弄好。實際：把select element移出dropdown menu, 簡化設計並解決flicker問題。
* 1/28 預計：試玩angularjs的route功能。實際：抓到angularjs的bug -- stack exceeded size. 再加上route功能會增加網頁的複雜度，也許用簡單的tag及layout組合可以避免使用route.
  * 把法律的選項資料從後端移到前端。
* 1/27 預計：新增減刑的查詢功能。實際：初步的輪廓已完成，目前缺背景圖，以及需要修正選取法條時的閃退問題。
* 1/26 預計：寫程式找出各種慰撫金的表示方式。實際：Done.
* 1/25 預計：改進金額判斷的準度。實際：Done.
* 1/24 預計：改進金額判斷的準度。實際：Done.
  * 新增對不限年份及近三年資料的四分位圖。
* 1/23 預計：動態產生分佈狀況並顯示在網頁上。實際：Done.
* 1/22 預計：用程式計算慰撫金的分佈狀況。實際：學習如何使用elasticsearch的aggregation產生四分位數，並survey如何產生圖表。
* 1/21 預計：算死亡情況下的慰撫金統計數字。實際：Done.
* 1/20 預計：推估市場大小。實際：推估買家的可能人數及可能的月收入。
* 1/19 預計：混雜NLP的model試著對違約金做分類。實際：把近十年的資料都作拆字，以訓練model。
* 1/18 預計：試作違約金的相關查詢。實際：Done. 初步看來，效果似乎不錯。
  * 有關律師費請求的段落太雜，似乎沒有太大的發展性。
* 1/17 預計：在frontend新增請求金額的顯示。實際：Done.
* 1/16 預計：增加請求金額的搜尋功能（若請求金額高，表示請求方有足夠的底氣，這部分資訊可能對寫訴狀等等有用。）實際：backend done.
* 1/15 預計：加年份的slider. 實際：年份slider佔據版面位置太大，在版面配置找不到適合的位置，二來，若在設定區裡放slider，點擊之後會立刻關掉設定頁，故此功能先擱置，若有user提出請求再實作。
* 1/14 預計：把fb login的功能整合進來。實際：進行中。FB developers的設定頁面可以把網站設為http://localhost，方便開發用。
  * 因有多種認証方式，加上flask-login那邊不宜改變太多，故選用 session 的方式儲存auth type及expired date.
* 1/13 預計：把名字欄從搜尋頁面拿掉。實際：Done.
* 1/12 預計：面試、開會、看辦公室。實際: 如預計。
* 1/11 預計：弄年份slidebar的功能。實際: 回台北，沒動。
* 1/10 預計：實作過濾人名。實際：Done. 要取出10個不同的人名需要使用aggregation, 但es那邊要設定，故workaround成前100筆資料的人名集合。
    * FB 登入功能初試驗
* 1/9 預計：實作過濾審級及法院的功能。 實際：先作審級過濾，個別法院的過濾很佔版面且較敏感，需討論。
    * 加碼完成feedback的post功能。
* 1/8 預計：實作登入的機制。實際：做了簡單的介面並把大致的流程弄出來了，因為使用者資料需要討論放在那裡，這一部分跳過。Google 的登入功能要domain的owner才能申請，facebook登入則要認証過才能申請，兩者皆需討論才能動工。
    * 另完成年份排序的功能雛型。
* 1/7 預計：研究登入的機制. 實際：看過範例後，覺得沒想像中難。
* 1/6 預計：研究payment API. 實際：Done
    * payment API 有分成前端和後端，前者統一了使用者介面，後端則是串金流。Google pay看來是比較簡單的路徑，在台灣，用綠界的介面似較妥商，Stripe的話則...不知道要等到何年何月。
* 1/5 預計：對各單位的層級做分類、過濾、排序。實際: 把最高院濾掉。
* 1/4 預計：對各單位的層級做分類、過濾、排序。實際: 從高雄到台北，家中pc還沒跑完程式，沒進度。
* 1/3 預計：在網頁上標示段落內容是來自何方。實際: Done.
* 1/2 預計：區分不同角色的論述。實際：ongoing. 之前誤以為當事人的請求有被加到db, 所以輕乎了工作量。
* 1/1 預計：加不同顏色到不同的關鍵字。實際: Done.

2017

* 12/31 預計：加不同顏色到不同的關鍵字。實際：沒進度，因回高雄。
* 12/30 預計：加不同顏色到不同的關鍵字。實際：沒進度, 手邊沒有環境可供開發。
* 12/29 預計：看user回報的feedback，把問題修一修，以及著手分析關鍵字的程式。實際：進度不快，因為今天去探望親人，以及台北的PC正忙於重建db，沒有最佳化的環境。
* 12/28 預計：陪人去台中面試。實際：如預期。
* 12/27 預計：看一下 skip gram 是怎麼實作的。實際：程式碼和原始paper要對照著看，不然會看不懂。
    * 寫個小程式追縱mongodb的空間使用量。
    * LDA, HDP 可以online training,
* 12/26 預計：把 Baroni 的 paper 看完。實際：搭著Mikolov的paper一起看，從不同作者的角度看這些模型的設計。
    * mc 的功能放到server上，結果大家都注意超高的金額case,沒在關心事實, 囧。
* 12/25 預計：摧人把資料搬到公開server上。實際：Done.
    * gensim.parsing.preprocessing.STOPWORDS 包括not, him, she等字，也許表示在分析語意時，電腦並不是像人一樣理解句子的意義，而是在解析句子的結構及其統計上的特性。
    * 在已知敗訴時，把准許金額設成 0.
* 12/24 預計：今天星期日兼聖誕夜，Relax
* 12/23 預計：把NNLM的paper看過一遍。實際：很快掃過，看得不深，大致上知道目前的研究成果為何。
* 12/22 預計：開會討論看有什麼事情要進行。實際：如預期。
    * 把寫錯字的句子改正，使之能使程式産生正確的金額，此部分涉及把寫錯字的句子都找出來，以免發生改到不該改的情況。
    * 區分出金額為 0 及無法判斷這兩種情況，避免把他們混在一起談。
    * 把醫療的資料重新生出來。
* 12/21 預計：幫台北的pc昇級資料庫。實際: Ongoing, 太多資料要更新了。
* 12/20 預計：處理T122 金額判斷裡的tricky cases. 實際：新增幾個判斷金額的邏輯，並標記程式無法處理的case。
* 12/19 預計：試用tensorboard。實際：如預期，tensorboard很容易弄出來，約十分鐘內搞定([code](code/20171218/guess_radius.py))，但覺得要做到細緻還是需要study一下。今日雜記：
    * 修正金額判斷程式，並用程式對es的type作in-place的更新。
    * 寫程式判斷一段文字是否值得顯示出來，如一般人不會對程序類的段落感興趣，預設應隱藏起來，故用新增欄位記錄這樣的屬性，另考慮過直接把這樣的段落從es裡刪除，但此法可能會讓有意思的段落（出現機率很小）永遠不會被挖出來。
* 12/18 預計：寫一個玩具性質的 tensorflow 程式。實際：如預期，做一個預測圓半徑的文具問題，讓程式去逼進預期的答案，但建出來的model不夠好，原因在於目標函數設計的不好，另一方面在於對tensorflow的認識還遠遠不足([code](code/20171218/guess_radius.py))。
    * 本日另修正es的自動更新程式，原本在判斷doc是否已在es裡的邏輯有誤。
    * 印出 LSI 和 LDA 的原始論文，開始補足自身知識的不足。
    * 試用 angucomplete, 發現在 input tag 裡不起作用，要放在 div 裡才可以；另可以使用 GET 去取得 json 的，可以angucomplete裡找到 github 的 API 範例。目前看來，angucomplete 目前還沒有運用的地方。
* 12/17 預計：把elasticsearch的一個type弄到可以自動化更新內容。實際：如預計。
* 12/16 預計：接續 dependency injection 的工作。實際：如預計。另清除mongodb裡用來作文字搜尋的欄位，還在查一下基本的elasticsearch查詢功能。
    * 刪除es整個index:```curl -XDELETE http://localhost:9200/your_index_name```
    * 顯示es的硬碟使用情況: ```curl http://localhost:9200/_cat/shards?v```
    * 顯示不特定文件: ```curl http://localhost:9200/your_index/your_type/_search```
* 12/15 預計：接續 dependency injection 的工作。實際：先改金額判斷的bug.
* 12/14 預計：因應新db，client 的 wrapper 測試程式改成 dependency injection 的方式。實際：把一部分的 python code 改掉了，但 python 2.7 沒有 unittest.mock 的 patch decorator，為了維持簡單的開發環境又不想裝 mock pacakge，只好連 source code 也一起改動。
* 12/13 預計：研究LSI. 實際：看了Deerwester的paper， 學習SVD及LSI之間的關係。筆記如下：
    * 用SVD産生一個近似距陣([code](code/20171213/matrix_approx_svd.py))
    * Let M = u \* s \* VT， 其中 u 是大小為 m \* t 的距陣， 在應用上， t 是 LSI topics 的數量; 每個 u 的 column 對應到一個 topic， 要在計算 topic 的數值的話，先將該 topic 對應到的 column normalize 為一個單位向量，算出該topic的字詞權重，這些權重乘上相對應的字詞頻率並加總即為所求。
    * 仍不明白為何 u 的 column 可以對應成 topic.
    * LSI 對字詞在文件的出現順序並不在意，John Doe 和 Doe John 對LSI來講是等義的。
    * 同一個字在不同句子裡有不同意思（如 Apple makes iPods 裡的 Apple 是一家公司，不是水果)，LSI 無法做字詞意義上的區分。
* 12/12 預計：研究SVD的feature extraction. 實際：sklearn， numpy的SVD有些微差異，尚看不出如何運用SVD算相似性，另在過程中學到了如何使用pandas以及TFIDF運作方式，算額外收獲。
* 12/11 預計：JS UnitTest. 實際： 進度超前，因此外加研究SVD及fake news的code.
