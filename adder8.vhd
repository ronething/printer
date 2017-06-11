library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity adder8 is
port(    A_in,B_in : in std_logic_vector(7 downto 0);
               F : out std_logic_vector(7 downto 0);
  	  		c_in : in std_logic;
		  	   C : out std_logic;    --最高位进位 C     
		       Z : out std_logic;    --结果为零 Z   
	           V : out std_logic;    --结果溢出 V    
	  	       N : out std_logic     --结果为负数 N
	);
end adder8;

architecture structure of adder8 is
component fa
	port(a,b,ci : in std_logic;
		  s,co : out std_logic);
end component;

signal s_temp, cv : std_logic_vector(7 downto 0);  --结果F  进位C  过程变量  
signal overflow_temp : std_logic;               --溢出V  过程变量  

begin
	----------------------------------------8个fa级联----------------------------------------
	f0:   fa port map( A_in(0),B_in(0),c_in,s_temp(0),cv(0) );    --最低位相加   	
	f1_7: for i in 1 to 7 generate                     --其他7位用循环体相加          
		    fm: fa port map(A_in(i),B_in(i),cv(i-1),s_temp(i),cv(i) ); 
		  end generate f1_7;
    
	F <=s_temp; 		--运算结果
	
----------------------------------------PSW判断--------------------------------------
	C<=cv(7);	                                   --进位 C 
	                                         
	Z <= '1' WHEN s_temp="00000000" ELSE '0';   --零 Z 
	        			
	overflow_temp <= cv(7) xor cv(6);
	V <= '1' WHEN overflow_temp = '1' ELSE '0';   --溢出 V 	            
	
	N <= '1' WHEN s_temp(7) = '1' ELSE '0';       --负数 N 	            	
end structure;
