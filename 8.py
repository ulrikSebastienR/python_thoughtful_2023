ó
°Ëdc           @   sÁ  g  e  d  d d  D] Z e ^ q g  e  d  D] Z e d d k r/ e ^ q/ g  e  d d  D] Z e d d k r^ e ^ q^ g  e  d d	  D] Z e d d k r e ^ q g Z d  d
 d d d d d d d d d d d d d d d d d d d d d d d d d g Z d d d d d  d d! d d d d d d d
 d" d# d$ d% d& d' d! d d  d d d g Z d( d+ d)     YZ e   Z e g  e  d  d  D] Z e ^ qg  e  d  D] Z e ^ q¨ Z d* S(,   i   iX   i   i
   i   i    i!   i7   i   i   i   i#   i+   i3   i;   iC   iK   iS   i   i   i   i	   i$   i'   i*   i-   i0   i6   i   i   i   i   i   i   i@   i}   iØ   iW  i   iÙ  t   DSOperationsc           B   s  e  Z d  Z d d d d d d d d d	 d
 d d d	 d d d d d d d d d d d d d g g  e d  D] Z e ^ qj d d  Z d   Z d   Z d   Z d   Z	 d   Z
 d   Z d   Z d   Z d   Z d   Z d   Z d   Z d    Z d!   Z RS("   sK   common operations to lists, tuples and strings, enter your ds to operate oni    i   i   i   i   i   i   i   i   i	   i   i@   i}   iØ   iW  i   iÙ  s1   j dis oui madamoiselle cest arien neira madam ouic         C   s   | |  _  | |  _ | |  _ d  S(   N(   t   ds1t   ds2t   s(   t   selfR   R   R   (    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   __init__   s    		c         C   s   d S(   s5   make one string from another string, leetcode problemN(    (   R   (    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   distance_between_strings   t    c         C   s1   d d d d d g } d d d d	 d
 d g } d S(   s   sort l1 on basis of l2t   boyt   girlt   enfantt   jount   fillei   i   i3   i    i   i   N(    (   R   t   l1t   l2(    (    s/   /home/normal/python_thoughtful/ds_operations.pyt"   sort_list_on_basis_of_another_list   s    c         C   sV   d d l  m } g  } x9 t d t |  j   D] } | j | |  j |   q/ W| S(   s3   create sublists using permutations and combinationsiÿÿÿÿ(   t   combinationsi   (   t	   itertoolsR   t   ranget   lenR   t   extend(   R   R   t   sublistst   i(    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   all_sublists_using_combinations   s
    c         C   s   g  } x t  t |  j  d  D]e } x\ t  d t |  j  d  D]> } |  j | | !} | | k rC | g  k rC | j |  qC qC Wq  W| S(   Ni   (   R   R   R   t   append(   R   R   R   t   jt   add(    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   direct_all_sublists   s     #c         C   s¥   g  } d j  |  j j    } x t t |  d  D]h } x_ t d t |  d  D]D } | | | !} | | k rU | g  k rU | j d j  |   qU qU Wq5 W| S(   NR   i   (   t   joinR   t   splitR   R   R   (   R   t
   substringst   white_space_removedR   R   R   (    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   all_substrings_direct$   s     !c         C   s|   t  |  j  t  |  j  k r> t |  j  t |  j  @r> d St |  j  t |  j  @rt t |  j  t |  j  @Sd Sd S(   s)   using bitwise & operator to match two dsss   perfect Matchs   no matchN(   R   R   R   t   set(   R   (    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   bitwise_and_for_matching_two_ds-   s
    :c         C   s   g  |  j  D] } | |  j k r
 | ^ q
 } | r5 | St |  j  t |  j   k r| g  |  j D] } | |  j  k r] | ^ q] Sd Sd S(   s&   directly match two ds without inbuiltss   perfect matchN(   R   R   R   (   R   t   elementt   diff(    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   match_two_ds5   s    +)c         C   s´   g  g  } } x |  j    D] } x g  |  j    D] } | | k r0 | ^ q0 D]V } t |  t |  k r | | k r | j |  qL | | k rL | j |  qL qL Wq W| | f S(   s7   takes a string and groups anagrams but excludes repeats(   R    R!   R   (   R   t   anagramst   repeatedt	   substringt   itemt
   substring1(    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   group_anagrams_and_repeats>   s    2$c         C   sv   |  j  j   } g  g  } } xS | D]K } xB | D]: } t |  t |  k r0 | | k r0 | j |  q0 q0 Wq# W| S(   N(   R   R   R!   R   (   R   t   wordst
   duplicatesR&   t   wordt   word1(    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   anagrams_in_a_sentence_or_wordsH   s    $c         C   sA   |  j  j   } g  } x% | D] } d } x | D] } q/ Wq W| S(   Ni    (   R   R   (   R   R,   R-   R.   R   R/   (    (    s/   /home/normal/python_thoughtful/ds_operations.pyt!   duplicates_in_a_sentence_or_wordsP   s    c         C   s   |  j    i  } } xm |  j    D]_ } d } x- |  j    D] } | | k r9 | d 7} q9 q9 W| d k r  | j i | | 6 q  q  Wt | j    S(   s   find duplicatesi   (   R    t   updatet   listt   keys(   R   t   lt   dR(   R   R*   (    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   duplicates_in_allsubstringsY   s    c         C   s5   g  |  j    D] } | |  j   k r | ^ q } | S(   s$   find and remove duplicate substrings(   R    R-   (   R   R)   t   without_duplicates(    (    s/   /home/normal/python_thoughtful/ds_operations.pyt%   remove_duplicates_from_all_substringsd   s    1c         C   s   d j  |  j j    S(   s#   strips all white spaces of a stringR   (   R   R   R   (   R   (    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   whitespaces_without_stringh   s    c         C   s   d S(   s{   though set can remove duplicates but what if your ds has all sets to checked for duplicates error thrown is unhashable typeN(    (   R   (    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   set_inside_setk   s    (   t   __name__t
   __module__t   __doc__R   t   numberR   R   R   R   R   R    R"   R%   R+   R0   R1   R7   R9   R:   R;   (    (    (    s/   /home/normal/python_thoughtful/ds_operations.pyR       s    y										
						N(    (   R   R?   t   dot	   merged_dot   list_to_checkR    t   dsot   dso1(    (    (    s/   /home/normal/python_thoughtful/ds_operations.pyt   <module>   s
   ²WTj	