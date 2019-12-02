# 队列
先进者先出。队列跟栈一样，是一种操作受限的线性表数据结构。

队列最基本的操作是两个：
1. 入队 enqueue(), 放入一个数据到队列尾部；
2. 出队 dequeue(), 从队列头部取一个元素。
   
![avatar](https://static001.geekbang.org/resource/image/9e/3e/9eca53f9b557b1213c5d94b94e9dce3e.jpg)

## 顺序队列和链式队列
顺序队列：用数组实现的队列

链式队列：用链表实现的队列

队列需要两个指针：
1. head指针指向队头；
2. tail指针指向队尾。

## 基于数组的队列实现

e.g. 当 a、b、c、d 依次入队之后，队列中的 head 指针指向下标为 0 的位置，tail 指针指向下标为 4 的位置：
![avatar](https://static001.geekbang.org/resource/image/5c/cb/5c0ec42eb797e8a7d48c9dbe89dc93cb.jpg)
当我们调用两次出队操作之后，队列中 head 指针指向下标为 2 的位置，tail 指针仍然指向下标为 4 的位置。
![avatar](https://static001.geekbang.org/resource/image/de/0d/dea27f2c505dd8d0b6b86e262d03430d.jpg)

在出队时可以不用数据搬移，如果没有空闲空间，只需在入队时在集中触发一次数据的搬移操作。
e.g.当队列的泰勒指针移动到数组的最右边后，如果有新的数据入队，我们可以将head到tail之间的数据，整体搬移到数组中 0 到 tail-head 的位置。
![avatar](https://static001.geekbang.org/resource/image/09/c7/094ba7722eeec46ead58b40c097353c7.jpg)

## 基于链表的队列实现方法：

队列需要两个指针：
1. head指针指向链表的第一个结点
2. tail指针指向链表的最后一个结点

入队：tail->next=new_node, tail = tail->next
出队：head = head->next

![avatar](https://static001.geekbang.org/resource/image/c9/93/c916fe2212f8f543ddf539296444d393.jpg)


## 循环队列

如图，图中这个队列的大小为8，当前head=4， tail=7。当有一个新的元素a入队时，我们放入下标为7的位置。但同时，tail移动到下标为0的位置。当再有一个元素b入队时，我们将b放入下标为0的位置，然后tail加1更新为1。
![avatar](https://static001.geekbang.org/resource/image/58/90/58ba37bb4102b87d66dffe7148b0f990.jpg)

在a,b依次入队之后， 循环队列中的元素就变成了下图所示：
![avatar](https://static001.geekbang.org/resource/image/71/80/71a41effb54ccea9dd463bde1b6abe80.jpg)

队满示意图：
![avatar](https://static001.geekbang.org/resource/image/3d/ec/3d81a44f8c42b3ceee55605f9aeedcec.jpg)

当队满时， (tail+1)%n=head。

## 阻塞队列
阻塞队列就是在队列基础上增加了阻塞操作：
就是在队列为空的时候，从堆头取数据会被阻塞。因为此时还没有数据可取，直到队列中有了数据才能返回；如果队列已经满了，那么插入数据的操作就会被阻塞，直到队列中有空闲位置后在插入数据，然后再返回。

![avatar](https://static001.geekbang.org/resource/image/5e/eb/5ef3326181907dea0964f612890185eb.jpg)

这种基于阻塞队列实现的“生产者 - 消费者模型”， 可以有效地协调生产和消费的速度。当“生产者”生产数据的速度过快， “消费者”来不及消费时， 存储数据的队列很快就会满了。此时，生产者就阻塞等待，直到“消费者”消费了数据， “生产者”才会被唤醒继续“生产”。

同时，基于阻塞队列，我们还可以通过协调“生产者”和“消费者”的个数， 来提高数据的处理效率。如下图：多个“消费者”对应一个“生产者”。

注意：阻塞队列在多线程情况下，会有多个线程同时操作队列，这是会存在安全问题。

## 并发队列


并发队列是线程安全的队列，最简单直接的方法是直接在enqueue()、dequeue()方法上加锁， 但是锁粒度大并发度会比较低，同一时刻仅允许一个存或取操作。