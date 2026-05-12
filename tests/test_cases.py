"""
test_cases.py
=============
Unit test suite for all 10 programming tasks (T01–T10).

Usage (from repo root):
    # Run all tests against a specific model's solutions:
    MODEL=claude pytest tests/test_cases.py -v

    # Run single task class:
    MODEL=chatgpt pytest tests/test_cases.py::TestT01_IsPrime -v

    # The MODEL env var selects solutions/<task>/<model>.py automatically.
    # Default: claude
"""

import csv
import importlib.util
import os
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
MODEL = os.environ.get("MODEL", "claude")  # chatgpt | claude | copilot


def load_solution(task_id: str):
    """Dynamically import the solution module for the active MODEL."""
    path = ROOT / "solutions" / task_id / f"{MODEL}.py"
    spec = importlib.util.spec_from_file_location(f"{task_id}_{MODEL}", path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ──────────────────────────────────────────────────────────────────────────────
# T01 – Prime Number Check
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def is_prime():
    return load_solution("T01").is_prime

class TestT01_IsPrime:
    def test_zero_not_prime(self, is_prime):         assert is_prime(0)    is False
    def test_one_not_prime(self, is_prime):          assert is_prime(1)    is False
    def test_two_is_prime(self, is_prime):           assert is_prime(2)    is True
    def test_three_is_prime(self, is_prime):         assert is_prime(3)    is True
    def test_four_not_prime(self, is_prime):         assert is_prime(4)    is False
    def test_seventeen_prime(self, is_prime):        assert is_prime(17)   is True
    def test_ninety_seven_prime(self, is_prime):     assert is_prime(97)   is True
    def test_hundred_not_prime(self, is_prime):      assert is_prime(100)  is False
    def test_large_prime_7919(self, is_prime):       assert is_prime(7919) is True
    def test_large_composite_7920(self, is_prime):   assert is_prime(7920) is False

# ──────────────────────────────────────────────────────────────────────────────
# T02 – String Reversal
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def reverse_string():
    return load_solution("T02").reverse_string

class TestT02_ReverseString:
    def test_empty(self, reverse_string):            assert reverse_string("")        == ""
    def test_single_char(self, reverse_string):      assert reverse_string("a")       == "a"
    def test_two_chars(self, reverse_string):        assert reverse_string("ab")      == "ba"
    def test_palindrome(self, reverse_string):       assert reverse_string("racecar") == "racecar"
    def test_word(self, reverse_string):             assert reverse_string("hello")   == "olleh"
    def test_with_spaces(self, reverse_string):      assert reverse_string("hi there")== "ereht ih"
    def test_digits(self, reverse_string):           assert reverse_string("12345")   == "54321"
    def test_mixed_case(self, reverse_string):       assert reverse_string("Python")  == "nohtyP"
    def test_special_chars(self, reverse_string):    assert reverse_string("!@#")     == "#@!"
    def test_unicode_ascii(self, reverse_string):    assert reverse_string("abc")     == "cba"

# ──────────────────────────────────────────────────────────────────────────────
# T03 – Temperature Converter
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def convert_temperature():
    return load_solution("T03").convert_temperature

class TestT03_ConvertTemperature:
    def test_c_to_f_freezing(self, convert_temperature):
        assert convert_temperature(0,   'C','F') == pytest.approx(32.0,   abs=0.01)
    def test_c_to_f_boiling(self, convert_temperature):
        assert convert_temperature(100, 'C','F') == pytest.approx(212.0,  abs=0.01)
    def test_f_to_c_freezing(self, convert_temperature):
        assert convert_temperature(32,  'F','C') == pytest.approx(0.0,    abs=0.01)
    def test_c_to_k(self, convert_temperature):
        assert convert_temperature(0,   'C','K') == pytest.approx(273.15, abs=0.01)
    def test_k_to_c(self, convert_temperature):
        assert convert_temperature(273.15,'K','C')== pytest.approx(0.0,   abs=0.01)
    def test_f_to_k(self, convert_temperature):
        assert convert_temperature(32,  'F','K') == pytest.approx(273.15, abs=0.01)
    def test_k_to_f(self, convert_temperature):
        assert convert_temperature(373.15,'K','F')== pytest.approx(212.0, abs=0.01)
    def test_same_unit(self, convert_temperature):
        assert convert_temperature(100, 'C','C') == pytest.approx(100.0,  abs=0.01)
    def test_negative_c_to_f(self, convert_temperature):
        assert convert_temperature(-40, 'C','F') == pytest.approx(-40.0,  abs=0.01)
    def test_body_temp(self, convert_temperature):
        assert convert_temperature(37,  'C','F') == pytest.approx(98.6,   abs=0.01)

# ──────────────────────────────────────────────────────────────────────────────
# T04 – Binary Search
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def binary_search():
    return load_solution("T04").binary_search

class TestT04_BinarySearch:
    def test_empty_list(self, binary_search):
        assert binary_search([], 5) == -1
    def test_single_found(self, binary_search):
        assert binary_search([7], 7) == 0
    def test_single_not_found(self, binary_search):
        assert binary_search([7], 3) == -1
    def test_target_start(self, binary_search):
        assert binary_search([1,3,5,7,9], 1) == 0
    def test_target_end(self, binary_search):
        assert binary_search([1,3,5,7,9], 9) == 4
    def test_target_middle(self, binary_search):
        assert binary_search([1,3,5,7,9], 5) == 2
    def test_not_found(self, binary_search):
        assert binary_search([1,3,5,7,9], 4) == -1
    def test_duplicates(self, binary_search):
        assert binary_search([1,2,2,2,3], 2) in [1,2,3]
    def test_large_list(self, binary_search):
        arr = list(range(0,1000,2))
        assert binary_search(arr, 500) == 250
    def test_negative_numbers(self, binary_search):
        assert binary_search([-10,-5,0,5,10], -5) == 1

# ──────────────────────────────────────────────────────────────────────────────
# T05 – CSV Aggregator
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def aggregate_csv():
    return load_solution("T05").aggregate_csv

@pytest.fixture
def sample_csv(tmp_path):
    content = "group,value\nA,10.5\nB,20.0\nA,5.5\nC,15.0\nB,10.0\n"
    p = tmp_path / "s.csv"; p.write_text(content); return str(p)

class TestT05_AggregateCSV:
    def test_multiple_groups(self, aggregate_csv, sample_csv):
        r = aggregate_csv(sample_csv)
        assert r["A"] == pytest.approx(16.0,  abs=0.01)
        assert r["B"] == pytest.approx(30.0,  abs=0.01)
        assert r["C"] == pytest.approx(15.0,  abs=0.01)
    def test_returns_dict(self, aggregate_csv, sample_csv):
        assert isinstance(aggregate_csv(sample_csv), dict)
    def test_empty_csv(self, aggregate_csv, tmp_path):
        p = tmp_path/"e.csv"; p.write_text("group,value\n"); assert aggregate_csv(str(p))=={}
    def test_single_group(self, aggregate_csv, tmp_path):
        p = tmp_path/"s.csv"; p.write_text("group,value\nX,100.0\nX,50.25\n")
        assert aggregate_csv(str(p))["X"] == pytest.approx(150.25, abs=0.01)
    def test_rounding(self, aggregate_csv, tmp_path):
        p = tmp_path/"r.csv"; p.write_text("group,value\nA,1.333\nA,1.334\n")
        assert aggregate_csv(str(p))["A"] == pytest.approx(2.67, abs=0.01)
    def test_group_count(self, aggregate_csv, sample_csv):
        assert len(aggregate_csv(sample_csv)) == 3
    def test_negative_values(self, aggregate_csv, tmp_path):
        p = tmp_path/"n.csv"; p.write_text("group,value\nN,-10.5\nN,5.5\n")
        assert aggregate_csv(str(p))["N"] == pytest.approx(-5.0, abs=0.01)
    def test_large_values(self, aggregate_csv, tmp_path):
        p = tmp_path/"l.csv"; p.write_text("group,value\nBIG,999999.99\nBIG,0.01\n")
        assert aggregate_csv(str(p))["BIG"] == pytest.approx(1000000.0, abs=0.01)
    def test_keys_are_strings(self, aggregate_csv, sample_csv):
        assert all(isinstance(k,str) for k in aggregate_csv(sample_csv))
    def test_single_row(self, aggregate_csv, tmp_path):
        p = tmp_path/"sr.csv"; p.write_text("group,value\nZ,99.99\n")
        assert aggregate_csv(str(p))["Z"] == pytest.approx(99.99, abs=0.01)

# ──────────────────────────────────────────────────────────────────────────────
# T06 – Linked List Stack
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def Stack():
    return load_solution("T06").Stack

class TestT06_Stack:
    def test_new_empty(self, Stack):           s=Stack(); assert s.is_empty() is True
    def test_size_zero(self, Stack):           s=Stack(); assert s.size()==0
    def test_push_size(self, Stack):           s=Stack(); s.push(1); assert s.size()==1
    def test_peek_top(self, Stack):            s=Stack(); s.push(42); assert s.peek()==42
    def test_peek_no_remove(self, Stack):      s=Stack(); s.push(42); s.peek(); assert s.size()==1
    def test_pop_returns(self, Stack):         s=Stack(); s.push(10); s.push(20); assert s.pop()==20
    def test_lifo_order(self, Stack):
        s=Stack()
        for v in [1,2,3]: s.push(v)
        assert [s.pop(),s.pop(),s.pop()] == [3,2,1]
    def test_pop_empty_error(self, Stack):
        with pytest.raises(IndexError): Stack().pop()
    def test_peek_empty_error(self, Stack):
        with pytest.raises(IndexError): Stack().peek()
    def test_empty_after_all_popped(self, Stack):
        s=Stack(); s.push(1); s.pop(); assert s.is_empty() is True

# ──────────────────────────────────────────────────────────────────────────────
# T07 – BFS
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def bfs():
    return load_solution("T07").bfs

class TestT07_BFS:
    def test_single_node(self, bfs):      assert bfs({"A":[]}, "A")==["A"]
    def test_linear(self, bfs):           assert bfs({"A":["B"],"B":["C"],"C":[]}, "A")==["A","B","C"]
    def test_returns_list(self, bfs):     assert isinstance(bfs({"A":[]}, "A"), list)
    def test_no_duplicates(self, bfs):
        r=bfs({"A":["B","C"],"B":["C"],"C":[]}, "A"); assert len(r)==len(set(r))
    def test_disconnected(self, bfs):
        assert "C" not in bfs({"A":["B"],"B":[],"C":[]}, "A")
    def test_cycle(self, bfs):
        r=bfs({"A":["B"],"B":["C"],"C":["A"]}, "A"); assert set(r)=={"A","B","C"}
    def test_star(self, bfs):
        g={"c":["a","b","d"],"a":[],"b":[],"d":[]}; r=bfs(g,"c")
        assert r[0]=="c" and set(r[1:])=={"a","b","d"}
    def test_numeric_keys(self, bfs):
        r=bfs({1:[2,3],2:[4],3:[4],4:[]}, 1); assert set(r)=={1,2,3,4}
    def test_missing_neighbor_keys(self, bfs):
        r=bfs({"A":["B"]}, "A"); assert "A" in r and "B" in r
    def test_branching_root_first(self, bfs):
        r=bfs({"A":["B","C"],"B":["D"],"C":["D"],"D":[]}, "A"); assert r[0]=="A"

# ──────────────────────────────────────────────────────────────────────────────
# T08 – Merge Sort
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def merge_sort():
    return load_solution("T08").merge_sort

class TestT08_MergeSort:
    def test_empty(self, merge_sort):            assert merge_sort([]) == []
    def test_single(self, merge_sort):           assert merge_sort([5]) == [5]
    def test_sorted(self, merge_sort):           assert merge_sort([1,2,3,4,5]) == [1,2,3,4,5]
    def test_reverse(self, merge_sort):          assert merge_sort([5,4,3,2,1]) == [1,2,3,4,5]
    def test_unsorted(self, merge_sort):         assert merge_sort([3,1,4,1,5,9,2,6]) == [1,1,2,3,4,5,6,9]
    def test_duplicates(self, merge_sort):       assert merge_sort([2,2,2,1]) == [1,2,2,2]
    def test_negatives(self, merge_sort):        assert merge_sort([-3,-1,-4,-2]) == [-4,-3,-2,-1]
    def test_mixed(self, merge_sort):            assert merge_sort([3,-1,0,-5,2]) == [-5,-1,0,2,3]
    def test_no_mutation(self, merge_sort):
        orig=[3,1,2]; merge_sort(orig); assert orig==[3,1,2]
    def test_large(self, merge_sort):
        assert merge_sort(list(range(100,0,-1))) == list(range(1,101))

# ──────────────────────────────────────────────────────────────────────────────
# T09 – Inventory Manager
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def InventoryManager():
    return load_solution("T09").InventoryManager

class TestT09_InventoryManager:
    def test_add_get(self, InventoryManager):
        inv=InventoryManager(); inv.add_item("a",10,1.5)
        item=inv.get_item("a"); assert item["quantity"]==10 and item["price"]==1.5
    def test_get_missing_none(self, InventoryManager):
        assert InventoryManager().get_item("x") is None
    def test_update_qty(self, InventoryManager):
        inv=InventoryManager(); inv.add_item("b",5,0.5); inv.update_item("b",quantity=20)
        assert inv.get_item("b")["quantity"]==20
    def test_update_price(self, InventoryManager):
        inv=InventoryManager(); inv.add_item("c",3,2.0); inv.update_item("c",price=3.5)
        assert inv.get_item("c")["price"]==3.5
    def test_update_missing_key_error(self, InventoryManager):
        with pytest.raises(KeyError): InventoryManager().update_item("x",quantity=1)
    def test_delete(self, InventoryManager):
        inv=InventoryManager(); inv.add_item("d",7,1.0); inv.delete_item("d")
        assert inv.get_item("d") is None
    def test_delete_missing_key_error(self, InventoryManager):
        with pytest.raises(KeyError): InventoryManager().delete_item("x")
    def test_list_empty(self, InventoryManager):   assert InventoryManager().list_items()==[]
    def test_list_multiple(self, InventoryManager):
        inv=InventoryManager(); inv.add_item("a",1,1.0); inv.add_item("b",2,2.0)
        assert len(inv.list_items())==2
    def test_add_overwrites(self, InventoryManager):
        inv=InventoryManager(); inv.add_item("g",10,5.0); inv.add_item("g",99,9.9)
        item=inv.get_item("g"); assert item["quantity"]==99 and item["price"]==9.9

# ──────────────────────────────────────────────────────────────────────────────
# T10 – LRU Cache
# ──────────────────────────────────────────────────────────────────────────────
@pytest.fixture(scope="module")
def LRUCache():
    return load_solution("T10").LRUCache

class TestT10_LRUCache:
    def test_get_missing(self, LRUCache):       assert LRUCache(2).get(1)==-1
    def test_put_get(self, LRUCache):           c=LRUCache(2); c.put(1,10); assert c.get(1)==10
    def test_evict_lru(self, LRUCache):
        c=LRUCache(2); c.put(1,1); c.put(2,2); c.put(3,3)
        assert c.get(1)==-1 and c.get(2)==2 and c.get(3)==3
    def test_get_refreshes(self, LRUCache):
        c=LRUCache(2); c.put(1,1); c.put(2,2); c.get(1); c.put(3,3)
        assert c.get(1)==1 and c.get(2)==-1
    def test_update_key(self, LRUCache):
        c=LRUCache(2); c.put(1,100); c.put(1,200); assert c.get(1)==200
    def test_capacity_one(self, LRUCache):
        c=LRUCache(1); c.put(1,1); c.put(2,2); assert c.get(1)==-1 and c.get(2)==2
    def test_no_evict_below_cap(self, LRUCache):
        c=LRUCache(3); c.put(1,1); c.put(2,2); assert c.get(1)==1 and c.get(2)==2
    def test_multi_evict(self, LRUCache):
        c=LRUCache(2)
        for i in range(1,6): c.put(i,i*10)
        assert c.get(4)==40 and c.get(5)==50 and c.get(3)==-1
    def test_update_no_grow(self, LRUCache):
        c=LRUCache(2); c.put(1,1); c.put(2,2); c.put(1,99); c.put(3,3)
        assert c.get(2)==-1 and c.get(1)==99
    def test_large_capacity(self, LRUCache):
        c=LRUCache(100)
        for i in range(100): c.put(i,i)
        assert all(c.get(i)==i for i in range(100))
