Purpose
--

This repo contains the daily to-do lists and what actually done.
It is my notes about what I have learned, and the notes are not guarantee to be correct.
I use it to keep track of my activities as another form of dairy.

這個 repo 為個人的to-do list，以及實際上完成了那些todo。此處內容僅為個人的筆記並當作一種日誌在寫，並不保証正確性。

Logs
--
2017
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
