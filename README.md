Purpose
--

This repo contains the daily to-do lists and what actually done.
It is my notes about what I have learned, and the notes are not guarantee to be correct.
I use it to keep track of my activities as another form of dairy.

這個 repo 為個人的to-do list，以及實際上完成了那些todo。此處內容僅為個人的筆記並當作一種日誌在寫，並不保証正確性。

Logs
--
2017
* 12/18 預計：寫一個玩具性質的 tensorflow 程式。
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

