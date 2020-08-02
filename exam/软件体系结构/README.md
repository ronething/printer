<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [软件体系复习](#%E8%BD%AF%E4%BB%B6%E4%BD%93%E7%B3%BB%E5%A4%8D%E4%B9%A0)
  - [知识点？](#%E7%9F%A5%E8%AF%86%E7%82%B9)
  - [复习题](#%E5%A4%8D%E4%B9%A0%E9%A2%98)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 软件体系复习

---

更新于 `2018/06/23 21:57`

今晚考试 名词解释 考了软件体系结构、软件体系结构风格、开闭原则、设计模式。

选择题略坑。有考到软件设计模式的分类。创建型模式这些。（课本（P6））

`4+1` 视图 不会乱画。。

UMl 图写代码。考的是抽象工厂模式。

大概就这样。溜了。

---

## 知识点？

- 软件体系结构（课本P179）

  软件体系结构是系统的基本组织结构,包括系统构成要素、这些构成要素相互之间以及与运行环境之间的关系，还包括系统设计及演化时应遵循的原则。

- 软件体系结构风格（课本P181 课件第10讲）

  软件体系结构风格是对软件体系结构的分类，是描述某一特定应用领域中系统组织方式的惯用模式。

- 开闭原则（课本P6）

  开闭原则是java世界里最基础的设计原则，它指导我们如何建立一个稳定，灵活的系统。开闭原则定义如下：

  Software entities like classes,modules and functions should be open for extension but closed for modifications.

  一个软件实体如类，模块和函数应该对扩展开放（这意味着模块的行为是可以拓展的，即当需求改变时，软件开发者可以对模块进行拓展，增加新的功能），对修改关闭（在对模块行为进行拓展时，不允许改动模块中已经存在的类的源代码）。

- 设计模式（课本P4）

  （软件设计模式和设计模式不一样，软件设计模式分为三个层次：架构模式、设计模式和习惯用法）

  - 软件设计模式概念

    软件设计模式是对软件设计经验的总结，是对软件设计中反复出现的设计问题的成功解决方案的描述。

  设计模式是中层模式，是针对系统局部设计问题给出的解决方案。

- 物联网（？？百度）

  “物联网概念”是在“互联网概念”的基础上，将其用户端延伸和扩展到任何物品与物品之间，进行信息交换和通信的一种网络概念。

- 客户端服务器风格（课本P272）

  客户端-服务器软件体系结构是一个多样性的、基于消息的模块基础结构。其目的是改善可用性、灵活性、互操作性与可伸缩性。客户端被定义为是一个服务请求软件，服务器端被定义为一个服务提供软件，客户端与服务器互相通信。

- 4+1视图

  - 逻辑视图 主要支持系统的功能需求，即系统提供给最终用户的服务。
  - 开发视图 主要侧重于软件模块的组织和管理。
  - 进程视图 主要关注一些非功能性的需求。
  - 物理视图 主要考虑如何把软件映射到硬件上。
  - 场景 它使四个视图有机联系起来。

  - ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsfcc6xikyj20ua0m8469.jpg)

- 软件体系结构风格

  - 面向对象设计风格(软件体系群里)
    - 该架构风格是将应用或系统任务分割成单独、可重用、可自给的对象，每个对象包含数据，以及与对象相关的行为。

  - 结构化设计风格(软件体系群里)
    - 是一种特定的程序设计方法学。它是一种基于结构的编程方法，即采用顺序结构、判定结构以及重复结构进行编程，其中每一结构只允许一个入口和一个出口。

  - 管道过滤器风格（课本P211）
    - 管道-过滤器体系结构是数据流风格体系结构的一个子类型。 ~~该体系结构在形式上与顺序批处理结构相似，但是实际上他们却有本质的区别。~~ 在管道-过滤器软件体系结构中，每个组件都有一组输入和输出，组件读入输入数据流，经过数据处理，然后产生输出数据流。
  - 层次风格（课本P246）
    - 层次体系结构是指将软件设计成层次结构，每个层为其上层提供服务，同时又是其下层的客户。
  - CS风格
    - C/S软件体系结构是基于资源不对等，且为实现共享而提出来的，是20世纪90年代成熟起来的技术，C/S体系结构定义了工作站如何与服务器相连，以实现数据和应用分布到多个处理机上。
    - C/S体系结构有三个主要组成部分：数据库服务器、客户应用程序和网络。
  - BS风格
    - 浏览器/服务器（B/S）风格就是上述三层应用结构的一种实现方式，其具体结构为：浏览器/Web服务器/数据库服务器。
    - B/S体系结构主要是利用不断成熟的WWW浏览器技术，结合浏览器的多种脚本语言，用通用浏览器就实现了原来需要复杂的专用软件才能实现的强大功能，并节约了开发成本。从某种程度上来说，B/S结构是一种全新的软件体系结构。
  - [CS、BS风格](https://blog.csdn.net/hawksoft/article/details/8094567)
    - B/S与C/S混合软件体系结构是一种典型的异构体系结构。C/S与B/S混合软件体系结构的优点是外部用户不直接访问数据库服务器，能保证企业数据库的相对安全。企业内部用户的交互性较强，数据查询和修改的响应速度较快。
    - C/S与B/S混合软件体系结构的缺点是企业外部用户修改和维护数据时，速度较慢，较烦琐，数据的动态交互性不强。

  - 为什么要使用异构结构

    ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsge0kxb28j20vf0hrq8g.jpg)

  - [类之间的几种基本关系](https://blog.csdn.net/qq_31655965/article/details/54645220)

    ![](https://ws1.sinaimg.cn/large/ecb0a9c3gy1fsl4o44l2pj20vd0li755.jpg)


- 设计模式

  - 注：以下 UML 图为平时实验所画，不一定对（以课本为主）。

  - 更新于 `2018/06/23 15:33` 发现 UML 图有很多错误，建议别看。

  - 单例模式（课本P37）

    单例模式是指确保一个类仅有一个唯一的实例，并且提供一个全局的访问点。构造方法要声明为 `private` 类型。`getInstance`方法必须为静态方法，否则客户程序无法调用该方法。

    ![](https://ws1.sinaimg.cn/large/bdc70b0aly1fsjw6yh93sj208304oq2v.jpg)


    ```java
    // President.java

    package cn.edu.scau.cmi.zhengwanxing.singleton;

    public class President {
      
      private static President instance;
      
      private String name;
      
      private President(String name){
        this.name = name;
      }
      
      public static President getInstance(String name){
        if(instance==null && !name.equals(null)){
          instance = new President(name);
        }
        return instance;
      }

    }

    // client.java

    package cn.edu.scau.cmi.zhengwanxing.client;

    import cn.edu.scau.cmi.zhengwanxing.singleton.President;

    public class SingletonClient {
      
      public static void main(String[] args){
        System.out.println(President.getInstance("毛泽东"));
        System.out.println(President.getInstance("习近平"));
      }
    }

    ```
    ```
    // 输出

    cn.edu.scau.cmi.zhengwanxing.singleton.President@15db9742
    cn.edu.scau.cmi.zhengwanxing.singleton.President@15db9742
    //返回结果一样

    ```
  - 多例模式

    - 泰星提醒：增加检测对象是否重复。用 List

    使用单例模式的思想实现多例模式，确保系统中某个类的对象只能存在有限个。（添加计数器）

    ![](https://ws1.sinaimg.cn/large/bdc70b0agy1fsjwb1vj4zj206r03ea9x.jpg)

    ```java
    // Marshal.java

    package cn.edu.scau.cmi.zhengwanxing.multiton;

    import java.util.ArrayList;
    import java.util.List;

    public class Marshal {
      
      private static Marshal instance;
      private static int count = 0;
      private static List<Marshal> l = new ArrayList<Marshal>();
      private String name;
      
      private Marshal(String name){
        this.name = name;
      }
      
      public static Marshal getInstance(String name){
        for(Marshal m:l){
          if(m.name.equals(name)){
            return m;
          }
        }
        if(count<10){
          instance = new Marshal(name);
          l.add(instance);
          count++;
          return instance;
        }
        return null;
      }

    }


    // client.java

    package cn.edu.scau.cmi.zhengwanxing.client;

    import cn.edu.scau.cmi.zhengwanxing.multiton.Marshal;

    public class MultitonClient {

      public static void main(String[] args) {
        // TODO Auto-generated method stub
        System.out.println(Marshal.getInstance("1"));
        System.out.println(Marshal.getInstance("2"));
        System.out.println(Marshal.getInstance("3"));
        System.out.println(Marshal.getInstance("4"));
        System.out.println(Marshal.getInstance("5"));
        System.out.println(Marshal.getInstance("6"));
        System.out.println(Marshal.getInstance("7"));
        System.out.println(Marshal.getInstance("8"));
        System.out.println(Marshal.getInstance("9"));
        System.out.println(Marshal.getInstance("9"));
        System.out.println(Marshal.getInstance("10"));
        //上面已经达到10个上限
        System.out.println(Marshal.getInstance("11"));
      }

    }

    ```
    ```
    // 输出

    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@15db9742
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@6d06d69c
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@7852e922
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@4e25154f
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@70dea4e
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@5c647e05
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@33909752
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@55f96302
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@3d4eac69
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@3d4eac69
    cn.edu.scau.cmi.zhengwanxing.multiton.Marshal@42a57993
    null

    ```
  - 简单工厂方法模式（课本P10）

    ![](https://ws1.sinaimg.cn/large/bdc70b0agy1fsjbpzguzoj20er08kwel.jpg)

    ```java
    // SimpleFactory.java

    package cn.edu.scau.cmi.zhengwanxing.simplefactory;

    import cn.edu.scau.cmi.zhengwanxing.domain.CarDamage;
    import cn.edu.scau.cmi.zhengwanxing.domain.DriverDamage;
    import cn.edu.scau.cmi.zhengwanxing.domain.Insurance;
    import cn.edu.scau.cmi.zhengwanxing.domain.MultiAccident;
    import cn.edu.scau.cmi.zhengwanxing.domain.PersonDamage;

    public class SimpleFactory {

      public static Insurance getInsurance(String accident){
        switch(accident){
            case "汽车损坏": return new CarDamage();
            case "司机受伤": return new DriverDamage();
            case "多种事故": return new MultiAccident();
            case "人员伤亡": return new PersonDamage();
        }
        return null;
      }
    }

    // CarDamage.java

    package cn.edu.scau.cmi.zhengwanxing.domain;

    public class CarDamage extends Insurance{

      @Override
      public String getMessage() {
        // TODO Auto-generated method stub
        return "保险信息：汽车损坏";
      }

    }

    // Insurance.java

    package cn.edu.scau.cmi.zhengwanxing.domain;

    public abstract class Insurance {
      public abstract String getMessage();
      }

    // client.java

    package cn.edu.scau.cmi.zhengwanxing.client;

    import java.util.Scanner;

    import cn.edu.scau.cmi.zhengwanxing.domain.Insurance;
    import cn.edu.scau.cmi.zhengwanxing.simplefactory.SimpleFactory;

    public class FactoryClient {

      public static void main(String[] args) {
        // TODO Auto-generated method stub

        System.out.println("请选择保险：");
        String type;
        Scanner input=new Scanner(System.in);
        type=input.nextLine();
        Insurance ins=SimpleFactory.getInsurance(type);
        System.out.println(ins.getMessage());
        input.close();
      }

    }
    ```

    简单工厂方法模式的特点是仅仅有一个具体的创建者类，并且在此类中包含一个静态的工厂方法 factory() 。

    简单工厂方法模式不符合开闭原则。

  - 工厂模式（课本P12）

    ![](https://ws1.sinaimg.cn/large/bdc70b0agy1fsjc9kvk5zj20fe08v0t2.jpg)

    ```java
    // Factory.java

    package cn.edu.scau.cmi.zhengwanxing.factory;

    import cn.edu.scau.cmi.zhengwanxing.domain.Insurance;

    public interface Factory {
    public Insurance createInsurance();
    }

    // CarDamageFactory.java

    package cn.edu.scau.cmi.zhengwanxing.factory;

    import cn.edu.scau.cmi.zhengwanxing.domain.CarDamage;
    import cn.edu.scau.cmi.zhengwanxing.domain.Insurance;

    public  class CarDamageFactory implements Factory{

      public Insurance createInsurance(){
          return new CarDamage();
      }
    }

    // CarDamage.java 
    // Insurance.java
    // 均与上面简单工厂方法一样


    // client.java

    package cn.edu.scau.cmi.zhengwanxing.client;

    import java.util.Scanner;

    import cn.edu.scau.cmi.zhengwanxing.domain.Insurance;
    import cn.edu.scau.cmi.zhengwanxing.factory.CarDamageFactory;
    import cn.edu.scau.cmi.zhengwanxing.factory.DriverDamageFactory;
    import cn.edu.scau.cmi.zhengwanxing.factory.MultiAccidentFactory;
    import cn.edu.scau.cmi.zhengwanxing.factory.PersonDamageFactory;

    public class FactoryClient {

      public static void main(String[] args) {
          // TODO Auto-generated method stub

          System.out.println("请选择保险：");
          String type;
          Scanner input=new Scanner(System.in);
          type=input.nextLine();
          Factory ff = null;
          Insurance ins = null;
          switch(type){
            case "司机受伤":{ff=new DriverDamageFactory();ins=ff.createInsurance();break;}
            case "汽车损坏":{ff=new CarDamageFactory();ins=ff.createInsurance();break;}
            case "人员伤亡":{ff=new PersonDamageFactory();ins=ff.createInsurance();break;}
            case "多种事故":{ff=new MultiAccidentFactory();ins=ff.createInsurance();break;}
          }
          System.out.println(ins.getMessage());
          input.close();
      }

    }

    ```

    每个产品类对应与一个工厂类，工厂类只负责创建相应的产品类的对象。

  - 抽象工厂模式

    ![](https://ws1.sinaimg.cn/large/bdc70b0agy1fsjcnbyx5aj20fe0czq3n.jpg)

    ```java
    // AbstractFactory.java

    package cn.edu.scau.cmi.zhengwanxing.abstractFactory.factory;

    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.CarDamage;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.DriverBodyInjury;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.HumanInjury;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.MultiAccident;

    public abstract class AbstractFactory {
      public static AbstractFactory getFactory(String brand){
        switch(brand){
        case "PICC":
          return new PICCFactory();
        case "PingAn":
          return new PingAnFactory();
        }
        return null;
      }
      
      public abstract CarDamage createCarDamage();
      public abstract DriverBodyInjury createDriverBodyInjury();
      public abstract HumanInjury createHumanInjury();
      public abstract MultiAccident createMutiAccident();
    }

    // PICCFactory.java

    package cn.edu.scau.cmi.zhengwanxing.abstractFactory.factory;

    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domain.PICCCarDamage;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domain.PICCDriverBodyInjury;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domain.PICCHumanInjury;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domain.PICCMultiAccident;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.CarDamage;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.DriverBodyInjury;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.HumanInjury;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.MultiAccident;

    public class PICCFactory extends AbstractFactory{

      @Override
      public CarDamage createCarDamage() {
        // TODO Auto-generated method stub
        return new PICCCarDamage();
      }

      @Override
      public DriverBodyInjury createDriverBodyInjury() {
        // TODO Auto-generated method stub
        return new PICCDriverBodyInjury();
      }

      @Override
      public HumanInjury createHumanInjury() {
        // TODO Auto-generated method stub
        return new PICCHumanInjury();
      }

      @Override
      public MultiAccident createMutiAccident() {
        // TODO Auto-generated method stub
        return new PICCMultiAccident();
      }
      
    }


    // PICC.java

    package cn.edu.scau.cmi.zhengwanxing.abstractFactory.damainInterface;

    public interface PICC {
      String brand="中国人寿保险";
    }

    // CarDamage.java

    package cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass;

    public abstract class CarDamage extends Insurance{
      public final String name="汽车损坏";

    }

    // PICCCarDamage.java

    package cn.edu.scau.cmi.zhengwanxing.abstractFactory.domain;

    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.damainInterface.PICC;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.CarDamage;

    public class PICCCarDamage extends CarDamage implements PICC{

      @Override
      public void damn() {
        // TODO Auto-generated method stub
        System.out.println("这是中国人寿保险汽车损坏");
        System.out.println(super.name+PICC.brand);
      }
      

    }

    // client.java

    package cn.edu.scau.cmi.zhengwanxing.client;

    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.CarDamage;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.domainAbstractClass.DriverBodyInjury;
    import cn.edu.scau.cmi.zhengwanxing.abstractFactory.factory.AbstractFactory;

    public class AbstractFactoryClient {

      public static void main(String[] args) {
        // TODO Auto-generated method stub
        
        AbstractFactory brandProducer = AbstractFactory.getFactory("PICC");
        
        Insurance product = brandProducer.createCarDamage();
        Insurance product_1 = brandProducer.createDriverBodyInjury();
        product.damn();
        product_1.damn();
      }

    }

    ```
  - 安全组合模式（课本P61）

    ![](https://ws1.sinaimg.cn/large/bdc70b0aly1fsjwkmkjrzj20fp06wt8u.jpg)

    ```java
    // Component.java

    package cn.edu.scau.cmi.zhengwanxing.composite.safe;

    public interface Component {
      public String doSomething();
    }

    // Composite.java

    package cn.edu.scau.cmi.zhengwanxing.composite.safe;

    import java.util.ArrayList;

    public class Composite implements Component {
      
      private ArrayList<Component> leaflist;
      private String name;

      public Composite(String name) {
        this.name = name;
        leaflist = new ArrayList<Component>();
      }
      
      public void add(Component l){
        if(l!=null){
          leaflist.add(l);
        }
      }
      
      public void remove(Component l){
        leaflist.remove(l);
      }

      public ArrayList<Component> getLeaflist() {
        return leaflist;
      }
      
      @Override
      public String doSomething() {
        // TODO Auto-generated method stub
        String something="";
        for(Component com:leaflist){
          something+=com.doSomething()+"\n";
        }
        return something;
      }

    }

    // Leaf.java

    package cn.edu.scau.cmi.zhengwanxing.composite.safe;

    public class Leaf implements Component {
      
      private String name;
      
      public Leaf(String name) {
        this.name = name;
      }
      
      @Override
      public String doSomething() {
        // TODO Auto-generated method stub
        return name;
      }

    }

    // compositesafeClient.java

    package cn.edu.scau.cmi.zhengwanxing.client;

    import cn.edu.scau.cmi.zhengwanxing.composite.safe.Composite;
    import cn.edu.scau.cmi.zhengwanxing.composite.safe.Leaf;

    public class compositesafeClient {

      public static void main(String[] args) {
        // TODO Auto-generated method stub
        Leaf leaf = new Leaf("安全模式个人1");
        Composite com = new Composite("安全模式组织1");
        com.add(leaf);
        Leaf leaf1 = new Leaf("安全模式个人2");
        com.add(leaf1);
        System.out.println("com组织的人员：");
        System.out.println(com.doSomething());
        Composite com1 = new Composite("安全模式组织2");
        Leaf leaf2 = new Leaf("安全模式个人3");
        com1.add(leaf2);
        com.add(com1);
        System.out.println("com组织的人员：");
        System.out.println(com.doSomething());
        com.remove(leaf1);
        System.out.println("com组织的人员：");
        System.out.println(com.doSomething());
      }

    }

    ```

    ```
    //输出

    com组织的人员：
    安全模式个人1
    安全模式个人2

    com组织的人员：
    安全模式个人1
    安全模式个人2
    安全模式个人3


    com组织的人员：
    安全模式个人1
    安全模式个人3
    ```
  - 一致性组合模式（也称为透明组合模式 课本P61）

    好处：所有的构件类都有相同的接口。
    缺点：不够安全。

    ![](https://ws1.sinaimg.cn/large/bdc70b0agy1fsjxwt2zdtj20gk08ggm1.jpg)

    ```java
    // Component.java

    package cn.edu.scau.cmi.zhengwanxing.composite.transparent;

    public interface Component {
      String doSomething();
      void add(Component l);
      void remove(Component l);
    }

    // Composite.java
    package cn.edu.scau.cmi.zhengwanxing.composite.transparent;

    import java.util.ArrayList;

    public class Composite implements Component {
      
      private ArrayList<Component> leaflist;
      private String name;

      public Composite(String name) {
        this.name = name;
        leaflist = new ArrayList<Component>();
      }
      
      public void add(Component l){
        if(l!=null){
          leaflist.add(l);
        }
      }
      
      public void remove(Component l){
        leaflist.remove(l);
      }

      public ArrayList<Component> getLeaflist() {
        return leaflist;
      }
      
      @Override
      public String doSomething() {
        // TODO Auto-generated method stub
        int len = leaflist.size();
        String something="";
        for(int i=0;i<len;i++){
          Component com = leaflist.get(i);
          something+=com.doSomething()+"\n";
        }
        return something;
      }
      
    }

    // Leaf.java

    package cn.edu.scau.cmi.zhengwanxing.composite.transparent;

    public class Leaf implements Component {
      
      private String name;
      
      String ERRMSG1 = "The add operation in class Leaf is not supported";
      String ERRMSG2 = "The remove operation in class Leaf is not supported";
      
      public Leaf(String name) {
        this.name = name;
      }
      
      @Override
      public String doSomething() {
        // TODO Auto-generated method stub
        return name;
      }

      @Override
      public void add(Component l) {
        // TODO Auto-generated method stub
        System.out.println(ERRMSG1);
      }

      @Override
      public void remove(Component l) {
        // TODO Auto-generated method stub
        System.out.println(ERRMSG2);
      }

    }

    // compositetransparentClient.java

    package cn.edu.scau.cmi.zhengwanxing.client;

    import cn.edu.scau.cmi.zhengwanxing.composite.transparent.Composite;
    import cn.edu.scau.cmi.zhengwanxing.composite.transparent.Leaf;

    public class compositetransparentClient {
      
      public static void main(String[] args) {
        Leaf leaf = new Leaf("透明模式个人1");
        Composite com = new Composite("透明模式组织1");
        com.add(leaf);
        Leaf leaf1 = new Leaf("透明模式个人2");
        com.add(leaf1);
        System.out.println("com组织的人员：");
        System.out.println(com.doSomething());
        Composite com1 = new Composite("透明模式组织2");
        Leaf leaf2 = new Leaf("透明模式个人3");
        com1.add(leaf2);
        com.add(com1);
        System.out.println("com组织的人员：");
        System.out.println(com.doSomething());
        com.remove(leaf1);
        System.out.println("com组织的人员：");
        System.out.println(com.doSomething());
        //尝试个人加入个人
        leaf2.add(leaf1);
        //尝试个人移除个人
        leaf2.remove(leaf1);
      }
    }

    ```

    ```
    //输出

    com组织的人员：
    透明模式个人1
    透明模式个人2

    com组织的人员：
    透明模式个人1
    透明模式个人2
    透明模式个人3

    com组织的人员：
    透明模式个人1
    透明模式个人3

    The add operation in class Leaf is not supported
    The remove operation in class Leaf is not supported

    ```

  - 类适配器模式（课本P68）

    ![](https://ws1.sinaimg.cn/large/bdc70b0aly1fsjyev6mg2j20je0eat96.jpg)

    Target: 即所期望的 Java 接口

    Adaptee: 被继承的 Java 类

    Adapter: 将 Adaptee 类转化到增加了新功能的 Target 接口

    ![](https://ws1.sinaimg.cn/large/bdc70b0aly1fsjyhn4mwzj20fp08nmxe.jpg)

    ```java
    // Target.java

    package cn.edu.scau.cmi.zhengwanxing.adapter;

    /**
    * @author Administrator
    * 人可以扮演多个角色，学生，孩子，worker。
    */
    public interface Target {
      
      void kid();
      void student();
      void worker();
    }

    // Adaptee.java

    package cn.edu.scau.cmi.zhengwanxing.adapter;

    /**
    * @author Administrator
    * 人现在只能扮演孩子。
    */
    public class Adaptee {
      
      public void kid(){
        System.out.println("Now I can be a kid");
      }
    }

    // AdapterOfClass.java

    package cn.edu.scau.cmi.zhengwanxing.adapter;

    public class AdapterOfClass extends Adaptee implements Target{

      @Override
      public void student() {
        // TODO Auto-generated method stub
        System.out.println("Now I can be a student");
      }

      @Override
      public void worker() {
        // TODO Auto-generated method stub
        System.out.println("Now I can be a worker");
      }

    }

    // client.java

    package cn.edu.scau.cmi.zhengwanxing.client;

    import cn.edu.scau.cmi.zhengwanxing.adapter.AdapterOfClass;
    import cn.edu.scau.cmi.zhengwanxing.adapter.Target;

    public class AdapterClient {
      public static void main(String[] args){
        
        //以下为类适配器
        System.out.println("AdapterOfClass is Here");
        Target per = new AdapterOfClass();
        
        per.kid();
        per.student();
        per.worker();

      }

    }

    ```

    > `Target per = new AdapterOfClass();` 注意对象的类型为接口`Target`，这样做的好处是有利于动态绑定。

    ```
    //输出

    AdapterOfClass is Here
    Now I can be a kid
    Now I can be a student
    Now I can be a worker

    ```

  - 对象适配器模式

    ![](https://ws1.sinaimg.cn/large/bdc70b0aly1fsjz8m4warj20jc0dgdg9.jpg)

    > 注意对象适配器对被适配器对象采用的是调用。

    ![](https://ws1.sinaimg.cn/large/bdc70b0agy1fsjz6c0c84j20gf06ldfz.jpg)

    ```java
    // Target.java Adaptee.java
    // 与类适配器一样

    // AdapterOfObject.java

    package cn.edu.scau.cmi.zhengwanxing.adapter;

    public class AdapterOfObject implements Target{
      
      private Adaptee pre;
      
      public AdapterOfObject(Adaptee pre){
        this.pre = pre;
      }
      
      @Override
      public void kid() {
        // TODO Auto-generated method stub
        this.pre.kid();
      }

      @Override
      public void student() {
        // TODO Auto-generated method stub
        System.out.println("Now I can be a student(AdapterOfObejct)");
      }

      @Override
      public void worker() {
        // TODO Auto-generated method stub
        System.out.println("Now I can be a worker(AdapterOfObejct)");
      }

    }

    // AdapterClient.java

    package cn.edu.scau.cmi.zhengwanxing.client;

    import cn.edu.scau.cmi.zhengwanxing.adapter.Adaptee;
    import cn.edu.scau.cmi.zhengwanxing.adapter.AdapterOfObject;
    import cn.edu.scau.cmi.zhengwanxing.adapter.Target;

    public class AdapterClient {
      public static void main(String[] args){
        
        //以下为对象适配器
        System.out.println("AdapterOfObject is Here");
        Target pre = new AdapterOfObject(new Adaptee());
        pre.kid();
        pre.student();
        pre.worker();
      }

    }

    ```

    ```
    //输出

    AdapterOfObject is Here
    Now I can be a kid
    Now I can be a student(AdapterOfObejct)
    Now I can be a worker(AdapterOfObejct)

    ```

    
  - ORM模式
    
    Hibernate对象关系映射

  - IOC模式
  
    Spring的控制反转

  - Spring 框架基本原理和实验使用

    > applicationContext.xml

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <beans xmlns="http://www.springframework.org/schema/beans"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p"
      xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.1.xsd http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx.xsd"
      xmlns:tx="http://www.springframework.org/schema/tx">
      
      <bean id="liangzaoqing" class="cn.edu.scau.cmi.zhengwanxing.spring.domain.Teacher">
        <property name="name" value="梁早清"></property>
        <property name="gendar" value="男"></property>
      </bean>
      <bean id="zhengwanxing" class="cn.edu.scau.cmi.zhengwanxing.spring.domain.Student">
        <property name="name" value="郑玩星"></property>
        <property name="gendar" value="男"></property>
        <property name="tutor" ref="liangzaoqing"></property>
      </bean>
    </beans>
    ```

    > springclient.java

    ```java
    package cn.edu.scau.cmi.zhengwanxing.client;

    import org.springframework.context.ApplicationContext;
    import org.springframework.context.support.ClassPathXmlApplicationContext;

    import cn.edu.scau.cmi.zhengwanxing.spring.domain.Student;

    public class SpringClient {
      
      public SpringClient(){
        
      }
      
      public static void main(String[] args) {
        ApplicationContext ac=new ClassPathXmlApplicationContext("applicationContext.xml");
        Student student=(Student) ac.getBean("zhengwanxing");
        System.out.println(student.getTutor().getName());
        // 销毁ApplicationContext((ClassPathXmlApplicationContext) ac).close();
      }

    }

    ```
  - Hibernate 框架基本原理和使用

    > hibernate.cfg.xml

    ```xml
    <?xml version='1.0' encoding='UTF-8'?>
    <!DOCTYPE hibernate-configuration PUBLIC
              "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
              "http://www.hibernate.org/dtd/hibernate-configuration-3.0.dtd">
    <!-- Generated by MyEclipse Hibernate Tools.                   -->
    <hibernate-configuration>

      <session-factory>
        <property name="myeclipse.connection.profile">test</property>
        <property name="dialect">
          org.hibernate.dialect.MySQLDialect
        </property>
        <property name="connection.password">root</property>
        <property name="connection.username">root</property>
        <property name="connection.url">jdbc:mysql://127.0.0.1/homework?characterEncoding=utf8&amp;useSSL=true</property>
        <property name="connection.driver_class">
          com.mysql.jdbc.Driver
        </property>
        <mapping
          resource="cn/edu/scau/cmi/zhengwanxing/domain/Author.hbm.xml" />

      </session-factory>

    </hibernate-configuration>
    ```

    > example: 实体类`Author`映射文件
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE hibernate-mapping PUBLIC "-//Hibernate/Hibernate Mapping DTD 3.0//EN"
    "http://www.hibernate.org/dtd/hibernate-mapping-3.0.dtd">
    <!-- 
        Mapping file autogenerated by MyEclipse Persistence Tools
    -->
    <hibernate-mapping>
        <class name="cn.edu.scau.cmi.zhengwanxing.domain.Author" table="author" catalog="homework">
            <id name="name" type="java.lang.String">
                <column name="name" length="20" />
                <generator class="assigned" />
            </id>
            <property name="country" type="java.lang.String">
                <column name="country" length="20" />
            </property>
            <set name="books" inverse="true">
                <key>
                    <column name="author" length="20" />
                </key>
                <one-to-many class="cn.edu.scau.cmi.zhengwanxing.domain.Book" />
            </set>
        </class>
    </hibernate-mapping>

    ```



---

## 复习题

```
有一个显示类Monitor，这个类有一个方法show(Content content)，其中，Content的分辨率属性是1920P。如果视频源不是这个分辨率的话，视频不能正常地在显示器中显示。现有一视频源，因为拍摄的时间比较早，它的分辨率只有480P，怎样才能使得这个视频源也能在显示器里正常显示，请你用适配器模式设计。
```

```
有一个通知系统，通知者(Notifier)可以这样组织被通知者(Notified)，单个的被通知者(SingleNotified)是被通知者，可以把多个被通知者组合成被通知组(GroupNotified)，这个被通知组也是被通知者，被通知组又可以和其他的单个通知者以及被通知组组合成更大的被通知组。请你用组合设计模式设计这种思想。
```

```
项目中需要使用到多种服装对象(Clothing)，包含衬衣(Shirt)，裤子(Trousers)，夹克(Jacket)。请利用工厂模式设计。
```

```
项目中需要使用多种品牌(Brand)的服装对象，品牌包含雅戈尔(Younger)，金利来(Goldlion)，古奇(Gucci)，服装包含衬衣(Shirt)，裤子(Trousers)，夹克(Jacket)。请利用抽象工厂模式设计。
```





---

__老师说简答题不考__

__老师说简答题不考__

__老师说简答题不考__

- [简要说明接口编程的好处](https://blog.csdn.net/u012402177/article/details/70145507)
  
  - 高内聚低耦合

  - 设计模式之开闭原则

- 怎样保证在一个OO的系统中，只能创建指定数量的对象

  - 多例模式？类似这样。

  ```java
  package cn.edu.scau.cmi.zhengwanxing.multiton;
  
  public class Marshal {
  	
  	private static Marshal instance;
  	private static int count = 0;
  	
  	private Marshal(){
  		
  	}
  	
  	public static Marshal getInstance(){
  		if(count<10){
  			instance = new Marshal();
  			count++;
  		}
  		return instance;
  	}
  
  }
  
  ```

- Hibernate框架体现了哪一种设计模式？这个模式在软件开发中的好处是什么？（不会啊）

  https://zhidao.baidu.com/question/200165176.html
  
  https://baike.baidu.com/item/ORM/3583252

  ORM设计模式。

  对象关系映射（Object-Relational Mapping）提供了概念性的、易于理解的模型化数据的方法。

- 对象型适配器和类适配器的区别是什么？（课本P72）

  https://blog.csdn.net/scychina/article/details/12908355

  类适配器模式与对象适配器模式在形式上的区别是，类适配器模式对被适配器对象采用了继承，而对象适配器对被适配对象采用的则是调用。

- Spring框架是一个轻量级的应用框架，在实际的项目中有很重要的用途，请说明这个框架中最重要的思想是什么？这种思想在软件开发中有哪些好处？

  核心思想是控制反转（IOC），依赖注入和面向切面编程。
  最重要的思想是控制反转（IOC）。

  好处：http://www.cnblogs.com/sunada2005/p/3581391.html

  